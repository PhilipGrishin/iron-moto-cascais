#!/usr/bin/env python3
"""Shared helpers for optimized hero background images."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Optional

HERO_IMAGE_WIDTHS = (768, 1280, 1920)
HERO_IMAGE_FORMATS = ("avif", "webp", "jpg")
HERO_OPTIMIZED_URL_PREFIX = "/photos/optimized"
HERO_PRELOAD_BREAKPOINTS = (
    (768, "(max-width: 767px)"),
    (1280, "(min-width: 768px) and (max-width: 1279px)"),
    (1920, "(min-width: 1280px)"),
)
OPTIMIZED_AVIF_RE = re.compile(
    rf"{re.escape(HERO_OPTIMIZED_URL_PREFIX)}/(?P<slug>[a-z0-9-]+)-"
    rf"(?P<width>{'|'.join(str(width) for width in HERO_IMAGE_WIDTHS)})\.avif"
)
CSS_RULE_RE = re.compile(r"(?P<selectors>[^{}]+)\{(?P<body>[^{}]*)\}")
CSS_CLASS_RE = re.compile(r"\.([a-zA-Z0-9_-]+)")
LEGACY_PROJECT_HERO_RE = re.compile(
    r"(?P<url>/photos/projects/(?P<project>[a-z0-9-]+)-800\.jpg)"
)


def hero_image_slug(source_url: str) -> str:
    """Return the stable optimized-image slug for a local hero source path."""
    path = source_url.split("?", 1)[0].lstrip("/")
    stem = Path(path).with_suffix("").as_posix()
    if stem.startswith("photos/"):
        stem = stem[len("photos/"):]
    stem = re.sub(r"-(?:800|1200|1600|1920|2400)$", "", stem)
    return re.sub(r"[^a-zA-Z0-9]+", "-", stem).strip("-").lower()


def optimized_hero_url(source_url: str, width: int, ext: str) -> str:
    if ext not in HERO_IMAGE_FORMATS:
        raise ValueError(f"Unsupported hero image format: {ext}")
    return f"{HERO_OPTIMIZED_URL_PREFIX}/{hero_image_slug(source_url)}-{width}.{ext}"


def hero_image_set(source_url: str, width: int = 1280) -> str:
    """Return a CSS image-set() value with AVIF, WebP and JPEG fallback."""
    avif = optimized_hero_url(source_url, width, "avif")
    webp = optimized_hero_url(source_url, width, "webp")
    jpg = optimized_hero_url(source_url, width, "jpg")
    return (
        "image-set("
        f"url('{avif}') type('image/avif'), "
        f"url('{webp}') type('image/webp'), "
        f"url('{jpg}') type('image/jpeg')"
        ")"
    )


def hero_background_css(source_url: str, width: int = 1280) -> str:
    """Return CSS declarations for an optimized background with JPEG fallback."""
    fallback = optimized_hero_url(source_url, width, "jpg")
    return f"background-image:url('{fallback}');background-image:{hero_image_set(source_url, width)}"


def hero_preload_links(source_url: str) -> str:
    """Return AVIF preload links for the standard hero breakpoints."""
    return hero_preload_links_for_slug(hero_image_slug(source_url))


def hero_preload_links_for_slug(slug: str) -> str:
    """Return responsive AVIF preload links for an optimized hero slug."""
    return "\n".join(
        f'<link rel="preload" as="image" href="{HERO_OPTIMIZED_URL_PREFIX}/{slug}-{width}.avif" '
        f'type="image/avif" media="{media}" fetchpriority="high"/>'
        for width, media in HERO_PRELOAD_BREAKPOINTS
    )


def hero_srcset_for_slug(slug: str, ext: str) -> str:
    """Return the standard responsive srcset for an optimized hero slug."""
    if ext not in HERO_IMAGE_FORMATS:
        raise ValueError(f"Unsupported hero image format: {ext}")
    return ", ".join(
        f"{HERO_OPTIMIZED_URL_PREFIX}/{slug}-{width}.{ext} {width}w"
        for width in HERO_IMAGE_WIDTHS
    )


def has_lcp_image_hint(soup) -> bool:
    """Return whether a document already declares its primary image early."""
    for link in soup.head.find_all("link", href=True) if soup.head else []:
        rel = {str(item).lower() for item in link.get("rel", [])}
        if "preload" in rel and str(link.get("as", "")).lower() == "image":
            return True
    return soup.find("img", attrs={"fetchpriority": "high"}) is not None


def _append_preload_links(soup, slug: str) -> None:
    """Insert preload links before stylesheets so discovery happens early."""
    anchor = soup.head.find("link", attrs={"rel": "stylesheet"})
    for width, media in HERO_PRELOAD_BREAKPOINTS:
        link = soup.new_tag("link")
        link["rel"] = "preload"
        link["as"] = "image"
        link["href"] = f"{HERO_OPTIMIZED_URL_PREFIX}/{slug}-{width}.avif"
        link["type"] = "image/avif"
        link["media"] = media
        link["fetchpriority"] = "high"
        if anchor is not None:
            anchor.insert_before(link)
        else:
            soup.head.append(link)


def _optimized_hero_slug(soup) -> Optional[str]:
    """Infer the rendered hero slug from the page's existing CSS delivery."""
    background = soup.select_one("main section .bg") or soup.select_one("main .bg")
    if background is None:
        return None

    if background.name == "picture":
        source = background.find("source", srcset=True)
        match = OPTIMIZED_AVIF_RE.search(source.get("srcset", "")) if source else None
        if match:
            return match.group("slug")

    if background.has_attr("style"):
        match = OPTIMIZED_AVIF_RE.search(background.get("style", ""))
        if match:
            return match.group("slug")

    own_classes = set(background.get("class", []))
    context_classes = set(own_classes)
    for parent in background.parents:
        context_classes.update(parent.get("class", []))
        if parent.name == "main":
            break

    candidates = []
    if soup.head:
        for style in soup.head.find_all("style"):
            for rule in CSS_RULE_RE.finditer(style.get_text()):
                match = OPTIMIZED_AVIF_RE.search(rule.group("body"))
                if not match:
                    continue
                for selector in rule.group("selectors").split(","):
                    selector_classes = set(CSS_CLASS_RE.findall(selector))
                    if not own_classes.intersection(selector_classes):
                        continue
                    if not selector_classes.issubset(context_classes):
                        continue
                    score = (
                        10 * len((selector_classes - own_classes) & context_classes)
                        + len(selector_classes & own_classes)
                    )
                    candidates.append((score, match.group("slug")))
    return max(candidates, default=(0, None), key=lambda item: item[0])[1]


def _sync_responsive_preloads(soup, slug: str) -> bool:
    """Keep shared responsive preloads aligned with the rendered hero."""
    changed = False
    expected_media = {media for _, media in HERO_PRELOAD_BREAKPOINTS}
    links = []
    for link in soup.head.find_all("link", href=True) if soup.head else []:
        rel = {str(item).lower() for item in link.get("rel", [])}
        match = OPTIMIZED_AVIF_RE.fullmatch(link.get("href", ""))
        if (
            "preload" in rel
            and str(link.get("as", "")).lower() == "image"
            and link.get("media") in expected_media
            and match
        ):
            links.append((link, match))
    if len(links) != len(HERO_PRELOAD_BREAKPOINTS):
        return False
    for link, match in links:
        expected = f"{HERO_OPTIMIZED_URL_PREFIX}/{slug}-{match.group('width')}.avif"
        if link.get("href") != expected:
            link["href"] = expected
            changed = True
    return changed


def _upgrade_legacy_project_hero(soup, site_root: Path) -> Optional[str]:
    """Replace a legacy project JPEG background with the shared picture pattern."""
    background = soup.select_one("main section.subpage > .bg[style]")
    if background is None:
        return None
    match = LEGACY_PROJECT_HERO_RE.search(background.get("style", ""))
    if not match:
        return None

    slug = hero_image_slug(f"/photos/projects/{match.group('project')}.jpg")
    fallback_url = f"{HERO_OPTIMIZED_URL_PREFIX}/{slug}-1920.jpg"
    fallback_path = site_root / fallback_url.lstrip("/")
    if not fallback_path.exists():
        raise FileNotFoundError(
            f"Missing optimized legacy project hero {fallback_url}; "
            "run optimize_hero_images.py for its source image"
        )

    from PIL import Image

    with Image.open(fallback_path) as image:
        width, height = image.size

    picture = soup.new_tag("picture")
    picture["class"] = background.get("class", ["bg"])
    picture["aria-hidden"] = "true"
    for ext, mime in (("avif", "image/avif"), ("webp", "image/webp")):
        source = soup.new_tag("source")
        source["type"] = mime
        source["sizes"] = "100vw"
        source["srcset"] = hero_srcset_for_slug(slug, ext)
        picture.append(source)
    image = soup.new_tag("img")
    image["alt"] = ""
    image["decoding"] = "async"
    image["fetchpriority"] = "high"
    image["sizes"] = "100vw"
    image["src"] = fallback_url
    image["srcset"] = hero_srcset_for_slug(slug, "jpg")
    image["width"] = str(width)
    image["height"] = str(height)
    picture.append(image)
    background.replace_with(picture)

    style = soup.new_tag("style")
    style.string = (
        ".subpage picture.bg{display:block}\n"
        ".subpage picture.bg img{width:100%;height:100%;object-fit:cover;"
        "object-position:center;display:block}"
    )
    soup.head.append(style)
    return slug


def ensure_lcp_image_delivery(soup, site_root: Path) -> bool:
    """Apply the established LCP image pattern to an indexable page."""
    legacy_project_slug = _upgrade_legacy_project_hero(soup, site_root)
    optimized_slug = legacy_project_slug or _optimized_hero_slug(soup)
    changed = bool(legacy_project_slug)
    if optimized_slug:
        changed = _sync_responsive_preloads(soup, optimized_slug) or changed
    if has_lcp_image_hint(soup):
        return changed

    if optimized_slug:
        _append_preload_links(soup, optimized_slug)
        return True

    social_image = soup.head.find("meta", attrs={"property": "og:image"}) if soup.head else None
    social_url = social_image.get("content", "") if social_image else ""
    site_origin = "https://ironcustommotors.com"
    if social_url.startswith(f"{site_origin}/"):
        social_url = social_url[len(site_origin):]
    if social_url.startswith("/photos/"):
        link = soup.new_tag("link")
        link["rel"] = "preload"
        link["as"] = "image"
        link["href"] = social_url
        link["fetchpriority"] = "high"
        anchor = soup.head.find("link", attrs={"rel": "stylesheet"})
        anchor.insert_before(link) if anchor else soup.head.append(link)
        return True

    raise ValueError("Indexable page has no image source for its required LCP hint")
