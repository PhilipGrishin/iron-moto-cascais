#!/usr/bin/env python3
"""Validate generated multilingual project pages and their integrations."""

from __future__ import annotations

import argparse
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from bs4 import BeautifulSoup
from PIL import Image

from project_pages_data import PROJECT_CONFIGS, load_project


SITE_ROOT = Path(__file__).resolve().parents[2]
DOMAIN = "https://ironcustommotors.com"
LANGS = ["en", "pt", "ru", "uk"]
HREFLANGS = {"en", "pt-PT", "ru", "uk", "x-default"}


def page_path(slug: str, lang: str) -> Path:
    prefix = Path() if lang == "en" else Path(lang)
    return SITE_ROOT / prefix / "projects" / slug / "index.html"


def page_url(slug: str, lang: str) -> str:
    prefix = "" if lang == "en" else f"{lang}/"
    return f"{DOMAIN}/{prefix}projects/{slug}/"


def normalized_text(markup: str) -> str:
    return " ".join(BeautifulSoup(markup, "html.parser").get_text(" ", strip=True).split())


def schema_entities(data):
    if isinstance(data, list):
        for value in data:
            yield from schema_entities(value)
    elif isinstance(data, dict):
        yield data
        for value in data.values():
            yield from schema_entities(value)


def validate_page(slug: str, lang: str, project: dict) -> list[str]:
    issues = []
    path = page_path(slug, lang)
    if not path.exists():
        return [f"{path.relative_to(SITE_ROOT)}: missing page"]

    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    expected = project["content"][lang]
    expected_url = page_url(slug, lang)
    label = str(path.relative_to(SITE_ROOT))

    title = soup.title.get_text(strip=True) if soup.title else ""
    if title != expected["title"]:
        issues.append(f"{label}: title mismatch")
    description = soup.find("meta", attrs={"name": "description"})
    if not description or description.get("content") != expected["description"]:
        issues.append(f"{label}: meta description mismatch")
    canonical = soup.find("link", rel="canonical")
    if not canonical or canonical.get("href") != expected_url:
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
    if not h1 or normalized_text(str(h1)) != expected["h1"]:
        issues.append(f"{label}: H1 mismatch")
    subtitle = soup.select_one(".subpage .tagline")
    if not subtitle or normalized_text(str(subtitle)) != expected["subtitle"]:
        issues.append(f"{label}: subtitle mismatch")
    body = soup.select_one(".generated-project-story")
    if not body or normalized_text(str(body)) != normalized_text(expected["body_html"]):
        issues.append(f"{label}: body copy mismatch")
    closing = soup.select_one(".generated-project-closing .lead")
    if not closing or normalized_text(str(closing)) != normalized_text(expected["closing_html"]):
        issues.append(f"{label}: closing copy mismatch")

    hero = soup.select_one(".subpage picture.bg img")
    if not hero:
        issues.append(f"{label}: hero image missing")
    else:
        if hero.get("alt") != expected["hero_alt"]:
            issues.append(f"{label}: hero alt mismatch")
        if hero.get("fetchpriority") != "high" or hero.has_attr("loading"):
            issues.append(f"{label}: hero LCP attributes invalid")
        if not hero.get("width") or not hero.get("height"):
            issues.append(f"{label}: hero dimensions missing")
        picture = hero.find_parent("picture")
        source_types = {source.get("type") for source in picture.find_all("source")}
        if source_types != {"image/avif", "image/webp"}:
            issues.append(f"{label}: hero AVIF/WebP sources incomplete")
    preload = soup.find("link", attrs={"rel": "preload", "as": "image"})
    if not preload or preload.get("fetchpriority") != "high":
        issues.append(f"{label}: hero preload missing")

    gallery_images = soup.select(".proj-gallery img")
    if len(gallery_images) != len(project["gallery_sources"]):
        issues.append(f"{label}: expected {len(project['gallery_sources'])} gallery images")
    for index, image in enumerate(gallery_images):
        if image.get("alt") != project["gallery_alts"][lang][index]:
            issues.append(f"{label}: gallery alt {index + 1} mismatch")
        if image.get("loading") != "lazy":
            issues.append(f"{label}: gallery image {index + 1} is not lazy")
        if not image.get("width") or not image.get("height"):
            issues.append(f"{label}: gallery image {index + 1} dimensions missing")
        picture = image.find_parent("picture")
        source_types = {source.get("type") for source in picture.find_all("source")} if picture else set()
        if source_types != {"image/avif", "image/webp"}:
            issues.append(f"{label}: gallery image {index + 1} sources incomplete")
        local_image = SITE_ROOT / image["src"].lstrip("/")
        if not local_image.exists():
            issues.append(f"{label}: missing gallery asset {image['src']}")
        else:
            with Image.open(local_image) as disk_image:
                if (int(image["width"]), int(image["height"])) != disk_image.size:
                    issues.append(f"{label}: gallery image {index + 1} dimensions incorrect")

    internal_targets = {
        "en": ["/projects/", "/custom/", "/contact/"],
        "pt": ["/pt/projects/", "/pt/custom/", "/pt/contact/"],
        "ru": ["/ru/projects/", "/ru/custom/", "/ru/contact/"],
        "uk": ["/uk/projects/", "/uk/custom/", "/uk/contact/"],
    }
    closing_links = [anchor.get("href") for anchor in soup.select(".generated-project-closing a")]
    if closing_links != internal_targets[lang]:
        issues.append(f"{label}: closing internal links are not language-local")

    schemas = []
    for script in soup.find_all("script", attrs={"type": "application/ld+json"}):
        try:
            schemas.append(json.loads(script.string or ""))
        except json.JSONDecodeError:
            issues.append(f"{label}: invalid JSON-LD")
    entities = [entity for schema in schemas for entity in schema_entities(schema)]
    types = {entity.get("@type") for entity in entities}
    if "Article" not in types or "BreadcrumbList" not in types:
        issues.append(f"{label}: Article/BreadcrumbList schema missing")
    if "Product" in types or "Offer" in types:
        issues.append(f"{label}: Product/Offer schema must not be present")
    article = next((entity for entity in entities if entity.get("@type") == "Article"), None)
    if article:
        publisher = article.get("publisher", {})
        if not publisher.get("@id") or not publisher.get("name") or not publisher.get("logo"):
            issues.append(f"{label}: publisher @id/name/logo incomplete")
        author = article.get("author", {})
        if not author.get("name") or not author.get("url"):
            issues.append(f"{label}: author name/url incomplete")
        main_page = article.get("mainEntityOfPage", {})
        if not main_page.get("@id") or not main_page.get("name"):
            issues.append(f"{label}: mainEntityOfPage @id/name incomplete")
        for field in ("datePublished", "dateModified"):
            value = article.get(field, "")
            if "T" not in value or not (value.endswith("Z") or "+" in value[10:] or "-" in value[10:]):
                issues.append(f"{label}: {field} is not full ISO-8601")

    return issues


def validate_integration(slug: str) -> list[str]:
    issues = []
    for lang in LANGS:
        prefix = "" if lang == "en" else f"{lang}/"
        listing_path = SITE_ROOT / prefix / "projects" / "index.html"
        soup = BeautifulSoup(listing_path.read_text(encoding="utf-8"), "html.parser")
        target = f"/{prefix}projects/{slug}/"
        card = soup.select_one(f'.prj-tile[href="{target}"]')
        if card is None:
            issues.append(f"{listing_path.relative_to(SITE_ROOT)}: Fighter card missing")
        elif not card.select_one('source[type="image/avif"]') or not card.select_one('source[type="image/webp"]'):
            issues.append(f"{listing_path.relative_to(SITE_ROOT)}: Fighter card AVIF/WebP missing")

    sitemap_ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    sitemap_urls = {
        node.find("s:loc", sitemap_ns).text
        for node in ET.parse(SITE_ROOT / "sitemap.xml").findall("s:url", sitemap_ns)
    }
    for lang in LANGS:
        expected = page_url(slug, lang)
        if expected not in sitemap_urls:
            issues.append(f"sitemap.xml: missing {expected}")

    sitemap_lastmods = {
        node.find("s:loc", sitemap_ns).text: node.find("s:lastmod", sitemap_ns).text
        for node in ET.parse(SITE_ROOT / "sitemap.xml").findall("s:url", sitemap_ns)
    }
    expected_lastmod = PROJECT_CONFIGS[slug]["published_iso"]
    for lang in LANGS:
        expected = page_url(slug, lang)
        if sitemap_lastmods.get(expected) != expected_lastmod:
            issues.append(f"sitemap.xml: incorrect lastmod for {expected}")
        listing_url = f"{DOMAIN}/{'projects/' if lang == 'en' else f'{lang}/projects/'}"
        if sitemap_lastmods.get(listing_url) != expected_lastmod:
            issues.append(f"sitemap.xml: incorrect projects listing lastmod for {listing_url}")

    for hub_slug in ("harley", "harley-custom", "harley-tuning"):
        for lang in LANGS:
            prefix = "" if lang == "en" else f"{lang}/"
            path = SITE_ROOT / prefix / hub_slug / "index.html"
            soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
            main = soup.find("main")
            if main and main.find("a", href=lambda href: href and f"/projects/{slug}/" in href):
                issues.append(f"{path.relative_to(SITE_ROOT)}: Fighter leaked into Harley content")

    return issues


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("slug", choices=sorted(PROJECT_CONFIGS))
    args = parser.parse_args()
    project = load_project(args.slug)

    issues = []
    for lang in LANGS:
        issues.extend(validate_page(args.slug, lang, project))
    issues.extend(validate_integration(args.slug))

    if issues:
        print("\n".join(f"ERROR: {issue}" for issue in issues))
        sys.exit(1)
    print(f"OK: {args.slug} project page passed multilingual, media, schema and integration checks")


if __name__ == "__main__":
    main()
