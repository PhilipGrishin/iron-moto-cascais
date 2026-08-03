#!/usr/bin/env python3
"""Validate all generated multilingual project pages and legacy redirects."""

from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from bs4 import BeautifulSoup
from PIL import Image

from build_output import html_semantically_equal
from build_project_pages import CACHE_BUST, project_main
from project_pages_data import (
    PROJECT_CONFIGS,
    REDIRECT_CONFIGS,
    load_project,
    project_modified_iso,
)


SITE_ROOT = Path(__file__).resolve().parents[2]
DOMAIN = "https://ironcustommotors.com"
LANGS = ["en", "ru", "uk", "pt"]
HREFLANGS = {"en", "pt-PT", "ru", "uk", "x-default"}
EXPECTED_SCHEMA_TYPES = {
    "Article",
    "BreadcrumbList",
    "ImageObject",
    "ListItem",
    "LocalBusiness",
    "PostalAddress",
    "WebPage",
}


def page_path(slug: str, lang: str) -> Path:
    prefix = Path() if lang == "en" else Path(lang)
    return SITE_ROOT / prefix / "projects" / slug / "index.html"


def page_url(slug: str, lang: str) -> str:
    prefix = "" if lang == "en" else f"{lang}/"
    return f"{DOMAIN}/{prefix}projects/{slug}/"


def normalized_text(markup) -> str:
    if hasattr(markup, "get_text"):
        value = markup.get_text(" ", strip=True)
    else:
        value = BeautifulSoup(str(markup), "html.parser").get_text(" ", strip=True)
    return " ".join(value.split())


def schema_entities(data):
    if isinstance(data, list):
        for value in data:
            yield from schema_entities(value)
    elif isinstance(data, dict):
        yield data
        for value in data.values():
            yield from schema_entities(value)


def meta_content(soup: BeautifulSoup, *, name: str | None = None, prop: str | None = None) -> str:
    attrs = {"name": name} if name else {"property": prop}
    tag = soup.head.find("meta", attrs=attrs)
    return tag.get("content", "") if tag else ""


def expected_meta(project: dict, lang: str) -> dict:
    content = project["content"][lang]
    if project["source_format"] == "localized_html":
        return content
    image_url = f"{DOMAIN}{project['hero_base']}-2400.webp"
    return {
        "title": content["title"],
        "description": content["description"],
        "og_title": content["title"],
        "og_description": content["description"],
        "og_image": image_url,
        "twitter_title": content["title"],
        "twitter_description": content["description"],
        "twitter_image": image_url,
        "h1": content["h1"],
    }


def expected_visible_hash(project: dict, lang: str) -> str:
    if project["source_format"] == "localized_html":
        return project["content"][lang]["visible_text_sha256"]
    return project["visible_text_sha256"][lang]


def valid_iso_with_timezone(value: str) -> bool:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return "T" in value and parsed.tzinfo is not None


def srcset_urls(value: str) -> list[str]:
    return [part.strip().split()[0] for part in value.split(",") if part.strip()]


def validate_local_asset(label: str, url: str, issues: list[str]) -> None:
    if not url.startswith("/"):
        issues.append(f"{label}: asset path is not absolute-local: {url}")
        return
    path = SITE_ROOT / url.split("?", 1)[0].lstrip("/")
    if not path.exists():
        issues.append(f"{label}: missing local asset {url}")


def validate_cache_bust(label: str, soup: BeautifulSoup) -> list[str]:
    issues = []
    for asset_path, expected in CACHE_BUST.items():
        refs = []
        for tag in soup.find_all(["link", "script"]):
            attr = "href" if tag.name == "link" else "src"
            ref = tag.get(attr, "")
            if ref.split("?", 1)[0] == asset_path:
                refs.append(ref)
        if not refs:
            issues.append(f"{label}: missing cache-busted asset {asset_path}")
            continue
        values = {ref.split("?v=", 1)[1] if "?v=" in ref else "" for ref in refs}
        if values != {expected}:
            issues.append(
                f"{label}: {asset_path} cache-bust values {sorted(values)} != {expected}"
            )
    return issues


def validate_schema(
    label: str,
    soup: BeautifulSoup,
    project: dict,
    lang: str,
    meta: dict,
) -> list[str]:
    issues = []
    schemas = []
    for script in soup.find_all("script", attrs={"type": "application/ld+json"}):
        try:
            schemas.append(json.loads(script.string or ""))
        except json.JSONDecodeError:
            issues.append(f"{label}: invalid JSON-LD")
    entities = [entity for schema in schemas for entity in schema_entities(schema)]
    typed = [entity for entity in entities if isinstance(entity.get("@type"), str)]
    types = {entity["@type"] for entity in typed}
    if types != EXPECTED_SCHEMA_TYPES:
        issues.append(f"{label}: schema types {sorted(types)} != {sorted(EXPECTED_SCHEMA_TYPES)}")
    if "CreativeWork" in types:
        issues.append(f"{label}: legacy CreativeWork schema remains")
    if "Organization" in types:
        issues.append(f"{label}: inline Organization entity remains")

    article = next((entity for entity in typed if entity.get("@type") == "Article"), None)
    business = next(
        (
            entity
            for entity in typed
            if entity.get("@type") == "LocalBusiness"
            and entity.get("@id") == f"{DOMAIN}/#business"
        ),
        None,
    )
    webpage = next(
        (
            entity
            for entity in typed
            if entity.get("@type") == "WebPage" and entity.get("@id") == page_url(project["slug"], lang)
        ),
        None,
    )
    breadcrumb = next(
        (entity for entity in typed if entity.get("@type") == "BreadcrumbList"),
        None,
    )

    if article is None:
        issues.append(f"{label}: Article entity missing")
    else:
        if article.get("headline") != meta["h1"]:
            issues.append(f"{label}: Article headline mismatch")
        if article.get("description") != meta["description"]:
            issues.append(f"{label}: Article description mismatch")
        if article.get("inLanguage") != lang:
            issues.append(f"{label}: Article language mismatch")
        if article.get("publisher") != {"@id": f"{DOMAIN}/#business"}:
            issues.append(f"{label}: publisher is not an @id-only reference")
        if article.get("author") != {"@id": f"{DOMAIN}/#business"}:
            issues.append(f"{label}: author is not an @id-only reference")
        if article.get("mainEntityOfPage") != {"@id": page_url(project["slug"], lang)}:
            issues.append(f"{label}: mainEntityOfPage reference mismatch")
        expected_dates = {
            "datePublished": project["published_iso"],
            "dateModified": project_modified_iso(project, lang),
        }
        for field, expected in expected_dates.items():
            value = article.get(field, "")
            if value != expected:
                issues.append(f"{label}: {field} {value!r} != {expected!r}")
            if not valid_iso_with_timezone(value):
                issues.append(f"{label}: {field} is not full ISO-8601 with timezone")

    if business is None:
        issues.append(f"{label}: referenced LocalBusiness entity missing")
    else:
        logo = business.get("logo")
        expected_business = {
            "name": "Iron Custom Motors",
            "url": f"{DOMAIN}/" if lang == "en" else f"{DOMAIN}/{lang}/",
            "image": f"{DOMAIN}/photos/og.jpg",
            "telephone": "+351917961230",
            "priceRange": "€€",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "R. António José da Silva 100 B",
                "addressLocality": "São Domingos de Rana",
                "addressRegion": "Lisbon",
                "postalCode": "2785-253",
                "addressCountry": "PT",
            },
        }
        for field, expected in expected_business.items():
            if business.get(field) != expected:
                issues.append(f"{label}: referenced publisher {field} mismatch")
        if not isinstance(logo, dict) or not logo.get("url") or not logo.get("width") or not logo.get("height"):
            issues.append(f"{label}: referenced publisher logo incomplete")
    if webpage is None:
        issues.append(f"{label}: referenced WebPage entity missing")
    if breadcrumb is None or len(breadcrumb.get("itemListElement", [])) != 3:
        issues.append(f"{label}: three-level BreadcrumbList missing")
    return issues


def validate_media(label: str, soup: BeautifulSoup, project: dict, lang: str) -> list[str]:
    issues = []
    hero = soup.select_one(".subpage picture.bg img")
    if hero is None:
        return [f"{label}: hero image missing"]
    picture = hero.find_parent("picture")
    sources = {source.get("type"): source for source in picture.find_all("source")}
    if set(sources) != {"image/avif", "image/webp"}:
        issues.append(f"{label}: hero AVIF/WebP sources incomplete")
    if hero.get("fetchpriority") != "high" or hero.has_attr("loading"):
        issues.append(f"{label}: hero LCP attributes invalid")
    if not hero.get("width") or not hero.get("height"):
        issues.append(f"{label}: hero dimensions missing")
    if project["source_format"] == "localized_html" and not hero.get("src", "").lower().endswith((".jpg", ".jpeg")):
        issues.append(f"{label}: legacy JPEG hero fallback regressed")
    if project.get("jpeg_fallback") and not hero.get("src", "").lower().endswith((".jpg", ".jpeg")):
        issues.append(f"{label}: registered JPEG hero fallback missing")

    high = soup.select('[fetchpriority="high"]')
    if len(high) != 1:
        issues.append(f"{label}: expected exactly one high-priority element, found {len(high)}")
    if soup.select('[fetchpriority="high"][loading="lazy"]'):
        issues.append(f"{label}: high-priority lazy image conflict")

    avif = sources.get("image/avif")
    preload = soup.find("link", attrs={"rel": "preload", "as": "image"})
    if preload is None or avif is None:
        issues.append(f"{label}: responsive AVIF preload missing")
    else:
        if preload.get("imagesrcset") != avif.get("srcset"):
            issues.append(f"{label}: preload/AVIF srcset mismatch")
        if preload.get("imagesizes") != avif.get("sizes"):
            issues.append(f"{label}: preload/AVIF sizes mismatch")
        if preload.get("fetchpriority") == "high":
            issues.append(f"{label}: preload duplicates high priority")
        if preload.get("href") not in srcset_urls(avif.get("srcset", "")):
            issues.append(f"{label}: preload href is not an AVIF candidate")

    for source in picture.find_all("source"):
        for url in srcset_urls(source.get("srcset", "")):
            validate_local_asset(label, url, issues)
    validate_local_asset(label, hero.get("src", ""), issues)
    for url in srcset_urls(hero.get("srcset", "")):
        validate_local_asset(label, url, issues)

    gallery_images = soup.select(".proj-gallery img")
    expected_count = (
        project["content"][lang]["gallery_count"]
        if project["source_format"] == "localized_html"
        else len(project["gallery_sources"])
    )
    if len(gallery_images) != expected_count:
        issues.append(f"{label}: expected {expected_count} gallery images")
    for index, image in enumerate(gallery_images, start=1):
        if image.get("loading") != "lazy":
            issues.append(f"{label}: gallery image {index} is not lazy")
        if not image.get("width") or not image.get("height"):
            issues.append(f"{label}: gallery image {index} dimensions missing")
        validate_local_asset(label, image.get("src", ""), issues)
        local_image = SITE_ROOT / image.get("src", "").lstrip("/")
        if local_image.exists() and image.get("width") and image.get("height"):
            with Image.open(local_image) as disk_image:
                if (int(image["width"]), int(image["height"])) != disk_image.size:
                    issues.append(f"{label}: gallery image {index} dimensions incorrect")
        gallery_picture = image.find_parent("picture")
        if gallery_picture:
            source_types = {source.get("type") for source in gallery_picture.find_all("source")}
            if source_types != {"image/avif", "image/webp"}:
                issues.append(f"{label}: gallery image {index} responsive sources incomplete")
        if project.get("jpeg_fallback") and not image.get("src", "").lower().endswith((".jpg", ".jpeg")):
            issues.append(f"{label}: gallery image {index} JPEG fallback missing")

    exhibition = project.get("exhibition_media")
    exhibition_sections = soup.select('[data-project-exhibition="true"]')
    if exhibition is None:
        if exhibition_sections:
            issues.append(f"{label}: unregistered project exhibition section")
        return issues
    if len(exhibition_sections) != 1:
        issues.append(
            f"{label}: expected one project exhibition section, found {len(exhibition_sections)}"
        )
        return issues

    section = exhibition_sections[0]
    split = section.select_one(".project-exhibition-split")
    image = section.select_one(".project-exhibition-media picture img")
    if split is None or image is None:
        issues.append(f"{label}: exhibition split media is incomplete")
        return issues
    if image.get("alt") != exhibition["alts"][lang]:
        issues.append(f"{label}: exhibition image alt mismatch")
    if image.get("loading") != "lazy" or image.has_attr("fetchpriority"):
        issues.append(f"{label}: exhibition image priority attributes invalid")
    if not image.get("width") or not image.get("height"):
        issues.append(f"{label}: exhibition image dimensions missing")
    if not image.get("src", "").endswith(".jpg"):
        issues.append(f"{label}: exhibition JPEG fallback missing")

    exhibition_picture = image.find_parent("picture")
    sources = {
        source.get("type"): source for source in exhibition_picture.find_all("source")
    }
    if set(sources) != {"image/avif", "image/webp"}:
        issues.append(f"{label}: exhibition AVIF/WebP sources incomplete")
    expected_sizes = "(max-width: 900px) calc(100vw - 40px), 42vw"
    if image.get("sizes") != expected_sizes:
        issues.append(f"{label}: exhibition image sizes mismatch")
    expected_urls = {
        extension: [
            f"{exhibition['base']}-{width}.{extension}"
            for width in exhibition["widths"]
        ]
        for extension in ("avif", "webp", "jpg")
    }
    for extension, source_type in (("avif", "image/avif"), ("webp", "image/webp")):
        source = sources.get(source_type)
        if source is None:
            continue
        if srcset_urls(source.get("srcset", "")) != expected_urls[extension]:
            issues.append(f"{label}: exhibition {extension.upper()} srcset mismatch")
        if source.get("sizes") != expected_sizes:
            issues.append(f"{label}: exhibition {extension.upper()} sizes mismatch")
    if srcset_urls(image.get("srcset", "")) != expected_urls["jpg"]:
        issues.append(f"{label}: exhibition JPEG srcset mismatch")
    for urls in expected_urls.values():
        for url in urls:
            validate_local_asset(label, url, issues)
    local_image = SITE_ROOT / image.get("src", "").lstrip("/")
    if local_image.exists() and image.get("width") and image.get("height"):
        with Image.open(local_image) as disk_image:
            if (int(image["width"]), int(image["height"])) != disk_image.size:
                issues.append(f"{label}: exhibition image dimensions incorrect")
    return issues


def validate_page(slug: str, lang: str, project: dict) -> list[str]:
    issues = []
    path = page_path(slug, lang)
    if not path.exists():
        return [f"{path.relative_to(SITE_ROOT)}: missing page"]
    label = path.relative_to(SITE_ROOT).as_posix()
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    meta = expected_meta(project, lang)

    if soup.title is None or soup.title.get_text(strip=True) != meta["title"]:
        issues.append(f"{label}: title mismatch")
    expected_meta_values = {
        ("name", "description"): meta["description"],
        ("prop", "og:title"): meta["og_title"],
        ("prop", "og:description"): meta["og_description"],
        ("prop", "og:image"): meta["og_image"],
        ("name", "twitter:title"): meta["twitter_title"],
        ("name", "twitter:description"): meta["twitter_description"],
        ("name", "twitter:image"): meta["twitter_image"],
    }
    for (kind, key), expected in expected_meta_values.items():
        actual = meta_content(soup, **{kind: key})
        if actual != expected:
            issues.append(f"{label}: {key} mismatch")

    canonical = soup.find("link", rel="canonical")
    if canonical is None or canonical.get("href") != page_url(slug, lang):
        issues.append(f"{label}: canonical mismatch")
    hreflangs = {
        link.get("hreflang"): link.get("href")
        for link in soup.find_all("link", rel="alternate")
        if link.get("hreflang")
    }
    if set(hreflangs) != HREFLANGS:
        issues.append(f"{label}: incomplete hreflang set")
    if hreflangs.get("x-default") != page_url(slug, "en"):
        issues.append(f"{label}: x-default does not point to EN")

    h1 = soup.find("h1")
    if h1 is None or normalized_text(h1) != meta["h1"]:
        issues.append(f"{label}: H1 mismatch")
    visible = normalized_text(soup.main)
    visible_hash = hashlib.sha256(visible.encode()).hexdigest()
    if visible_hash != expected_visible_hash(project, lang):
        issues.append(f"{label}: visible project text changed")
    if project["source_format"] == "localized_html" and not html_semantically_equal(
        str(soup.main), str(project_main(project, lang))
    ):
        issues.append(f"{label}: legacy main structure or media differs from source data")
    if any("window.ICM_I18N_PAGE" in (script.string or "") for script in soup.find_all("script")):
        issues.append(f"{label}: inline ICM_I18N_PAGE remains")

    issues.extend(validate_media(label, soup, project, lang))
    issues.extend(validate_cache_bust(label, soup))
    issues.extend(validate_schema(label, soup, project, lang, meta))
    return issues


def sitemap_data() -> tuple[set[str], dict[str, str]]:
    namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    nodes = ET.parse(SITE_ROOT / "sitemap.xml").findall("s:url", namespace)
    urls = {node.find("s:loc", namespace).text for node in nodes}
    lastmods = {
        node.find("s:loc", namespace).text: node.find("s:lastmod", namespace).text
        for node in nodes
    }
    return urls, lastmods


def validate_integration(slug: str) -> list[str]:
    issues = []
    project = PROJECT_CONFIGS[slug]
    for lang in LANGS:
        prefix = "" if lang == "en" else f"{lang}/"
        listing_path = SITE_ROOT / prefix / "projects" / "index.html"
        soup = BeautifulSoup(listing_path.read_text(encoding="utf-8"), "html.parser")
        target = f"/{prefix}projects/{slug}/"
        card = soup.select_one(f'.prj-tile[href="{target}"]')
        if card is None:
            issues.append(f"{listing_path.relative_to(SITE_ROOT)}: {slug} card missing")
        elif project["source_format"] == "markdown" and (
            not card.select_one('source[type="image/avif"]')
            or not card.select_one('source[type="image/webp"]')
        ):
            issues.append(f"{listing_path.relative_to(SITE_ROOT)}: {slug} card AVIF/WebP missing")

        integrations = project.get("integrations", {})
        if integrations.get("custom"):
            custom_path = SITE_ROOT / prefix / "custom" / "index.html"
            custom_soup = BeautifulSoup(
                custom_path.read_text(encoding="utf-8"), "html.parser"
            )
            custom_main = custom_soup.find("main")
            if custom_main is None or custom_main.find("a", href=target) is None:
                issues.append(
                    f"{custom_path.relative_to(SITE_ROOT)}: {slug} contextual link missing"
                )

        if integrations.get("harley_custom"):
            harley_path = SITE_ROOT / prefix / "harley-custom" / "index.html"
            harley_soup = BeautifulSoup(
                harley_path.read_text(encoding="utf-8"), "html.parser"
            )
            portfolio_link = harley_soup.select_one(
                f'.portfolio-row .btn[href="{target}"]'
            )
            if portfolio_link is None:
                issues.append(
                    f"{harley_path.relative_to(SITE_ROOT)}: {slug} portfolio link missing"
                )

            project_path = page_path(slug, lang)
            project_soup = BeautifulSoup(
                project_path.read_text(encoding="utf-8"), "html.parser"
            )
            project_main = project_soup.find("main")
            for related_slug in ("harley-service", "harley-custom"):
                related_target = f"/{prefix}{related_slug}/"
                if project_main is None or project_main.find(
                    "a", href=related_target
                ) is None:
                    issues.append(
                        f"{project_path.relative_to(SITE_ROOT)}: "
                        f"outgoing {related_slug} link missing"
                    )

        for related_slug in integrations.get("reciprocal_projects", []):
            project_path = page_path(slug, lang)
            related_path = page_path(related_slug, lang)
            project_main = BeautifulSoup(
                project_path.read_text(encoding="utf-8"), "html.parser"
            ).find("main")
            related_main = BeautifulSoup(
                related_path.read_text(encoding="utf-8"), "html.parser"
            ).find("main")
            related_target = f"/{prefix}projects/{related_slug}/"
            project_target = f"/{prefix}projects/{slug}/"
            if project_main is None or project_main.find("a", href=related_target) is None:
                issues.append(
                    f"{project_path.relative_to(SITE_ROOT)}: "
                    f"outgoing {related_slug} project link missing"
                )
            if related_main is None or related_main.find("a", href=project_target) is None:
                issues.append(
                    f"{related_path.relative_to(SITE_ROOT)}: "
                    f"reciprocal {slug} project link missing"
                )

    urls, lastmods = sitemap_data()
    for lang in LANGS:
        expected = page_url(slug, lang)
        if expected not in urls:
            issues.append(f"sitemap.xml: missing {expected}")
        if lastmods.get(expected) != project_modified_iso(project, lang):
            issues.append(f"sitemap.xml: incorrect lastmod for {expected}")

    if slug == "fighter":
        for hub_slug in ("harley", "harley-custom", "harley-tuning"):
            for lang in LANGS:
                prefix = "" if lang == "en" else f"{lang}/"
                path = SITE_ROOT / prefix / hub_slug / "index.html"
                soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
                main = soup.find("main")
                if main and main.find("a", href=lambda href: href and "/projects/fighter/" in href):
                    issues.append(f"{path.relative_to(SITE_ROOT)}: Fighter leaked into Harley content")
    return issues


def validate_redirects() -> list[str]:
    issues = []
    sitemap_urls, _ = sitemap_data()
    for old_slug, config in REDIRECT_CONFIGS.items():
        for lang in LANGS:
            prefix = "" if lang == "en" else f"{lang}/"
            path = SITE_ROOT / prefix / "projects" / old_slug / "index.html"
            label = path.relative_to(SITE_ROOT).as_posix()
            if not path.exists():
                issues.append(f"{label}: redirect missing")
                continue
            soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
            target_path = f"/{prefix}projects/{config['target']}/"
            target_url = f"{DOMAIN}{target_path}"
            canonical = soup.find("link", rel="canonical")
            refresh = soup.find("meta", attrs={"http-equiv": "refresh"})
            robots = soup.find("meta", attrs={"name": "robots"})
            anchor = soup.find("a")
            script = soup.find("script")
            if canonical is None or canonical.get("href") != target_url:
                issues.append(f"{label}: redirect canonical mismatch")
            if refresh is None or refresh.get("content") != f"0; url={target_path}":
                issues.append(f"{label}: meta refresh mismatch")
            if robots is None or "noindex" not in robots.get("content", ""):
                issues.append(f"{label}: noindex missing")
            if anchor is None or anchor.get("href") != target_path:
                issues.append(f"{label}: redirect anchor mismatch")
            if script is None or f'window.location.replace("{target_path}")' not in (script.string or ""):
                issues.append(f"{label}: JavaScript redirect mismatch")
            if target_url.replace(f"projects/{config['target']}", f"projects/{old_slug}") in sitemap_urls:
                issues.append(f"{label}: noindex redirect leaked into sitemap")
    return issues


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("slug", choices=sorted(PROJECT_CONFIGS))
    args = parser.parse_args()
    project = load_project(args.slug)

    issues = []
    for lang in LANGS:
        issues.extend(validate_page(args.slug, lang, project))
    issues.extend(validate_integration(args.slug))
    issues.extend(validate_redirects())

    if issues:
        print("\n".join(f"ERROR: {issue}" for issue in issues))
        sys.exit(1)
    print(
        f"OK: {args.slug} project page passed multilingual copy, media, schema, "
        "cache-bust, redirect and integration checks"
    )


if __name__ == "__main__":
    main()
