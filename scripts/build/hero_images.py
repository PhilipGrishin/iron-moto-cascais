#!/usr/bin/env python3
"""Shared helpers for optimized hero background images."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

import soupsieve

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
OPTIMIZED_IMAGE_RE = re.compile(
    rf"{re.escape(HERO_OPTIMIZED_URL_PREFIX)}/(?P<slug>[a-z0-9-]+)-"
    rf"(?P<width>{'|'.join(str(width) for width in HERO_IMAGE_WIDTHS)})\."
    rf"(?P<ext>{'|'.join(HERO_IMAGE_FORMATS)})"
)
CSS_RULE_RE = re.compile(r"(?P<selectors>[^{}]+)\{(?P<body>[^{}]*)\}")
CSS_CLASS_RE = re.compile(r"\.([a-zA-Z0-9_-]+)")
BACKGROUND_IMAGE_DECL_RE = re.compile(
    r"(?:^|;)\s*background-image\s*:\s*(?P<value>[^;{}]+)",
    re.IGNORECASE,
)
LEGACY_PROJECT_HERO_RE = re.compile(
    r"(?P<url>/photos/projects/(?P<project>[a-z0-9-]+)-800\.jpg)"
)
RESPONSIVE_HERO_ATTR = "data-lcp-responsive-background"
RESPONSIVE_HERO_STYLE_ATTR = "data-lcp-responsive-background-style"
STANDARD_VIEWPORT_SAMPLES = (390, 900, 1440)


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


def hero_image_set_for_slug(slug: str, width: int = 1280) -> str:
    """Return an image-set() value for an existing optimized hero slug."""
    return (
        "image-set("
        f"url('{HERO_OPTIMIZED_URL_PREFIX}/{slug}-{width}.avif') type('image/avif'), "
        f"url('{HERO_OPTIMIZED_URL_PREFIX}/{slug}-{width}.webp') type('image/webp'), "
        f"url('{HERO_OPTIMIZED_URL_PREFIX}/{slug}-{width}.jpg') type('image/jpeg')"
        ")"
    )


def hero_background_css(source_url: str, width: int = 1280) -> str:
    """Return CSS declarations for an optimized background with JPEG fallback."""
    fallback = optimized_hero_url(source_url, width, "jpg")
    return f"background-image:url('{fallback}');background-image:{hero_image_set(source_url, width)}"


def hero_background_css_for_slug(slug: str, width: int = 1280, *, important: bool = False) -> str:
    """Return optimized background declarations for a stable hero slug."""
    suffix = "!important" if important else ""
    fallback = f"{HERO_OPTIMIZED_URL_PREFIX}/{slug}-{width}.jpg"
    return (
        f"background-image:url('{fallback}'){suffix};"
        f"background-image:{hero_image_set_for_slug(slug, width)}{suffix}"
    )


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


def responsive_hero_background_style(slug: str) -> str:
    """Return viewport-aligned CSS for a marked background hero."""
    selector = f"[{RESPONSIVE_HERO_ATTR}]"
    return "\n".join(
        f"@media {media}{{{selector}{{{hero_background_css_for_slug(slug, width, important=True)}}}}}"
        for width, media in HERO_PRELOAD_BREAKPOINTS
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


def _media_width_range(header: str) -> tuple[int, int]:
    """Return the inclusive pixel range described by a width media query."""
    minimum = 0
    maximum = 100_000
    min_match = re.search(r"min-width\s*:\s*(\d+)px", header, re.IGNORECASE)
    max_match = re.search(r"max-width\s*:\s*(\d+)px", header, re.IGNORECASE)
    if min_match:
        minimum = int(min_match.group(1))
    if max_match:
        maximum = int(max_match.group(1))
    return minimum, maximum


def _iter_css_blocks(
    css_text: str,
    inherited_range: tuple[int, int] = (0, 100_000),
):
    """Yield ordinary CSS rules with their effective viewport range."""
    css_text = re.sub(r"/\*.*?\*/", "", css_text, flags=re.DOTALL)
    position = 0
    length = len(css_text)
    while position < length:
        brace = css_text.find("{", position)
        if brace < 0:
            break
        header = css_text[position:brace].strip()
        if ";" in header:
            header = header.rsplit(";", 1)[-1].strip()

        depth = 1
        cursor = brace + 1
        while cursor < length and depth:
            if css_text[cursor] == "{":
                depth += 1
            elif css_text[cursor] == "}":
                depth -= 1
            cursor += 1
        if depth:
            break

        body = css_text[brace + 1:cursor - 1]
        if header.lower().startswith("@media"):
            current_min, current_max = _media_width_range(header)
            parent_min, parent_max = inherited_range
            yield from _iter_css_blocks(
                body,
                (max(parent_min, current_min), min(parent_max, current_max)),
            )
        elif header.lower().startswith(("@supports", "@layer")):
            yield from _iter_css_blocks(body, inherited_range)
        elif header and not header.startswith("@"):
            yield header, body, inherited_range
        position = cursor


def _css_rule_records(soup, site_root: Path):
    """Return matched-style candidates in document source order."""
    records = []
    source_order = 0
    if soup.head is None:
        return records
    for node in soup.head.find_all(["link", "style"]):
        css_text = None
        if node.name == "style":
            css_text = node.get_text()
        else:
            rel = {str(item).lower() for item in node.get("rel", [])}
            if "stylesheet" not in rel or not node.get("href"):
                continue
            parsed = urlparse(node["href"])
            if parsed.scheme or parsed.netloc or not parsed.path.startswith("/"):
                continue
            stylesheet_path = site_root / parsed.path.lstrip("/")
            if stylesheet_path.exists():
                css_text = stylesheet_path.read_text(encoding="utf-8")
        if css_text is None:
            continue
        for selectors, body, width_range in _iter_css_blocks(css_text):
            source_order += 1
            records.append((selectors, body, width_range, source_order))
    return records


def _selector_specificity(selector: str) -> tuple[int, int, int]:
    ids = len(re.findall(r"#[a-zA-Z0-9_-]+", selector))
    classes = len(re.findall(r"\.[a-zA-Z0-9_-]+|\[[^\]]+\]|:(?!:)[a-zA-Z0-9_-]+", selector))
    elements = len(
        re.findall(
            r"(?:^|[\s>+~])([a-zA-Z][a-zA-Z0-9_-]*)",
            re.sub(r"::?[a-zA-Z0-9_-]+(?:\([^)]*\))?", "", selector),
        )
    )
    return ids, classes, elements


def _selector_matches(element, selector: str) -> bool:
    try:
        return soupsieve.match(selector, element)
    except Exception:
        return False


def _background_declarations(body: str):
    for declaration_order, match in enumerate(BACKGROUND_IMAGE_DECL_RE.finditer(body)):
        raw_value = match.group("value").strip()
        important = bool(re.search(r"!important\s*$", raw_value, re.IGNORECASE))
        value = re.sub(r"\s*!important\s*$", "", raw_value, flags=re.IGNORECASE)
        yield value, important, declaration_order


def _background_cascade(element, records):
    cascade = []
    for selectors, body, (minimum, maximum), source_order in records:
        for selector in selectors.split(","):
            selector = selector.strip()
            if not selector or not _selector_matches(element, selector):
                continue
            specificity = _selector_specificity(selector)
            for value, important, declaration_order in _background_declarations(body):
                rank = (
                    int(important),
                    0,
                    *specificity,
                    source_order,
                    declaration_order,
                )
                cascade.append((minimum, maximum, rank, value))

    if element.has_attr("style"):
        for value, important, declaration_order in _background_declarations(element["style"]):
            rank = (int(important), 1, 0, 0, 0, 1_000_000, declaration_order)
            cascade.append((0, 100_000, rank, value))
    return cascade


def _computed_background_value(element, viewport: int, cascade) -> Optional[str]:
    matching = [
        (rank, value)
        for minimum, maximum, rank, value in cascade
        if minimum <= viewport <= maximum
    ]
    return max(matching, default=(None, None), key=lambda item: item[0])[1]


def _viewport_samples(records) -> list[int]:
    samples = {1, 390, 767, 768, 900, 1279, 1280, 1440, 1920}
    for _, _, (minimum, maximum), _ in records:
        for boundary in (minimum, maximum):
            if 1 <= boundary <= 1920:
                samples.update({max(1, boundary - 1), boundary, min(1920, boundary + 1)})
    return sorted(samples)


def _first_section_has_priority_image(section) -> bool:
    return section.find("img", attrs={"fetchpriority": "high"}) is not None


def css_hero_element(soup, site_root: Path, records=None):
    """Return the real first-section CSS background hero, if the page has one."""
    marked = soup.find(attrs={RESPONSIVE_HERO_ATTR: True})
    if marked is not None:
        return marked

    main = soup.find("main")
    section = main.find("section") if main else None
    if section is None or _first_section_has_priority_image(section):
        return None

    records = records if records is not None else _css_rule_records(soup, site_root)
    candidates = []
    elements = [section, *section.find_all(True)]
    for dom_order, element in enumerate(elements):
        identity = " ".join([str(element.get("id", "")), *element.get("class", [])]).lower()
        inline_style = element.get("style", "")
        if "bg" not in identity and not OPTIMIZED_IMAGE_RE.search(inline_style):
            continue
        cascade = _background_cascade(element, records)
        values = [
            _computed_background_value(element, viewport, cascade)
            for viewport in STANDARD_VIEWPORT_SAMPLES
        ]
        if not any(value and OPTIMIZED_IMAGE_RE.search(value) for value in values):
            continue
        score = (2 if "bg" in identity else 0) + (1 if "hero" in identity else 0)
        candidates.append((score, -dom_order, element))
    if not candidates:
        return None
    return max(candidates, key=lambda item: (item[0], item[1]))[2]


def _preload_url_for_viewport(soup, viewport: int) -> Optional[str]:
    if viewport <= 767:
        expected_media = HERO_PRELOAD_BREAKPOINTS[0][1]
    elif viewport <= 1279:
        expected_media = HERO_PRELOAD_BREAKPOINTS[1][1]
    else:
        expected_media = HERO_PRELOAD_BREAKPOINTS[2][1]
    for link in soup.head.find_all("link", href=True) if soup.head else []:
        rel = {str(item).lower() for item in link.get("rel", [])}
        if (
            "preload" in rel
            and str(link.get("as", "")).lower() == "image"
            and link.get("media") == expected_media
        ):
            return link.get("href")
    return None


def css_hero_preload_alignment(soup, site_root: Path):
    """Compare the responsive preload and CSS-selected hero at every boundary."""
    records = _css_rule_records(soup, site_root)
    hero = css_hero_element(soup, site_root, records)
    if hero is None:
        return None, []

    cascade = _background_cascade(hero, records)
    mismatches = []
    seen = set()
    for viewport in _viewport_samples(records):
        preload_url = _preload_url_for_viewport(soup, viewport)
        background_value = _computed_background_value(hero, viewport, cascade)
        match = OPTIMIZED_AVIF_RE.search(background_value or "")
        rendered_url = match.group(0) if match else None
        mismatch = (preload_url, rendered_url)
        if preload_url == rendered_url or mismatch in seen:
            continue
        seen.add(mismatch)
        mismatches.append(
            f"{viewport}px preload {preload_url or '<missing>'} != "
            f"CSS {rendered_url or '<missing>'}"
        )
    return hero, mismatches


def _hero_slug_from_css(soup, hero, site_root: Path) -> Optional[str]:
    records = _css_rule_records(soup, site_root)
    cascade = _background_cascade(hero, records)
    for viewport in STANDARD_VIEWPORT_SAMPLES:
        value = _computed_background_value(hero, viewport, cascade)
        match = OPTIMIZED_IMAGE_RE.search(value or "")
        if match:
            return match.group("slug")
    return None


def _ensure_responsive_css_hero(soup, site_root: Path, slug: str) -> bool:
    hero, mismatches = css_hero_preload_alignment(soup, site_root)
    if hero is None:
        return False
    existing_style = soup.head.find("style", attrs={RESPONSIVE_HERO_STYLE_ATTR: True})
    if not mismatches and existing_style is None:
        return False

    changed = False
    if not hero.has_attr(RESPONSIVE_HERO_ATTR):
        hero[RESPONSIVE_HERO_ATTR] = ""
        changed = True
    expected_css = responsive_hero_background_style(slug)
    if existing_style is None:
        existing_style = soup.new_tag("style")
        existing_style[RESPONSIVE_HERO_STYLE_ATTR] = ""
        soup.head.append(existing_style)
        changed = True
    if existing_style.get_text() != expected_css:
        existing_style.string = expected_css
        changed = True
    return changed


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
    css_hero = None if legacy_project_slug else css_hero_element(soup, site_root)
    css_hero_slug = _hero_slug_from_css(soup, css_hero, site_root) if css_hero else None
    optimized_slug = legacy_project_slug or css_hero_slug or _optimized_hero_slug(soup)
    changed = bool(legacy_project_slug)
    if optimized_slug:
        changed = _sync_responsive_preloads(soup, optimized_slug) or changed
    if css_hero_slug:
        changed = _ensure_responsive_css_hero(soup, site_root, css_hero_slug) or changed
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
