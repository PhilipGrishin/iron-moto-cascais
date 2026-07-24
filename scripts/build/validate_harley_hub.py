#!/usr/bin/env python3
"""Validate Harley Hub pages and their required site integrations."""

from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from bs4 import BeautifulSoup

from build_harley_hub import LANGS, load_copy, plain_text
from harley_hub_data import (
    HREFLANG_CODES,
    PAGE_CONFIG,
    PORTFOLIO,
    PORTFOLIO_ORDER,
)


SITE_ROOT = Path(__file__).resolve().parents[2]
DOMAIN = "https://ironcustommotors.com"
ARTICLE_SLUG = "harley-davidson-full-service-done-right"


def page_path(slug: str, lang: str) -> Path:
    if lang == "en":
        return SITE_ROOT / slug / "index.html"
    return SITE_ROOT / lang / slug / "index.html"


def url_path(slug: str, lang: str) -> str:
    if lang == "en":
        return f"/{slug}/"
    return f"/{lang}/{slug}/"


def expected_url(slug: str, lang: str) -> str:
    return DOMAIN + url_path(slug, lang)


def schema_types(value) -> list[str]:
    found = []
    if isinstance(value, dict):
        item_type = value.get("@type")
        if isinstance(item_type, list):
            found.extend(str(item) for item in item_type)
        elif item_type:
            found.append(str(item_type))
        for child in value.values():
            found.extend(schema_types(child))
    elif isinstance(value, list):
        for child in value:
            found.extend(schema_types(child))
    return found


def load_schema(soup: BeautifulSoup) -> list[dict]:
    schemas = []
    for script in soup.find_all("script", attrs={"type": "application/ld+json"}):
        schemas.append(json.loads(script.string or script.get_text()))
    return schemas


def main() -> int:
    errors = []
    copy = load_copy()

    for config in PAGE_CONFIG.values():
        slug = config["slug"]
        for lang in LANGS:
            path = page_path(slug, lang)
            label = path.relative_to(SITE_ROOT).as_posix()
            if not path.exists():
                errors.append(f"{label}: missing page")
                continue
            soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
            source = copy[config["key"]][lang]

            if not soup.title or soup.title.get_text(strip=True) != source["title"]:
                errors.append(f"{label}: title differs from source")
            meta = soup.find("meta", attrs={"name": "description"})
            if not meta or meta.get("content") != source["description"]:
                errors.append(f"{label}: meta description differs from source")
            h1 = soup.find("h1")
            if not h1 or h1.get_text(" ", strip=True) != source["h1"]:
                errors.append(f"{label}: H1 differs from source")

            main_node = soup.find("main")
            main_text = " ".join(main_node.get_text(" ", strip=True).split())
            expected_section_titles = [
                section["title"] for section in source["sections"]
            ]
            visible_section_titles = [
                heading.get_text(" ", strip=True)
                for heading in soup.select(".harley-section h2")
            ]
            if visible_section_titles != expected_section_titles:
                errors.append(f"{label}: section order differs from source")
            source_blocks = list(source["preamble"])
            for section in source["sections"]:
                if section.get("faq"):
                    continue
                source_blocks.extend(section["blocks"])
            for block in source_blocks:
                if not block.get("html"):
                    continue
                expected_text = plain_text(block["html"])
                if expected_text and expected_text not in main_text:
                    errors.append(
                        f"{label}: source paragraph missing: {expected_text[:80]}"
                    )

            canonical = soup.find("link", attrs={"rel": "canonical"})
            if not canonical or canonical.get("href") != expected_url(slug, lang):
                errors.append(f"{label}: invalid canonical")
            alternates = {
                link.get("hreflang"): link.get("href")
                for link in soup.find_all("link", attrs={"rel": "alternate"})
            }
            for alternate_lang in LANGS:
                hreflang = HREFLANG_CODES[alternate_lang]
                if alternates.get(hreflang) != expected_url(slug, alternate_lang):
                    errors.append(f"{label}: invalid hreflang {hreflang}")
            if alternates.get("x-default") != expected_url(slug, "en"):
                errors.append(f"{label}: invalid x-default")

            hero = soup.select_one(".harley-hero-media img")
            if not hero:
                errors.append(f"{label}: missing hero image")
            else:
                if hero.get("fetchpriority") != "high":
                    errors.append(f"{label}: hero is not fetchpriority=high")
                if hero.get("loading") == "lazy":
                    errors.append(f"{label}: hero is lazy-loaded")
                if not hero.get("width") or not hero.get("height"):
                    errors.append(f"{label}: hero dimensions missing")
                if hero.get("alt") != source["hero_alt"]:
                    errors.append(f"{label}: hero ALT differs from source")
            hero_picture = soup.select_one("picture.harley-hero-media")
            source_types = {
                node.get("type")
                for node in hero_picture.find_all("source")
            } if hero_picture else set()
            if source_types != {"image/avif", "image/webp"}:
                errors.append(f"{label}: hero AVIF/WebP sources missing")
            if len(soup.find_all("link", attrs={"rel": "preload", "as": "image"})) != 3:
                errors.append(f"{label}: expected 3 responsive hero preloads")

            schemas = load_schema(soup)
            types = schema_types(schemas)
            required = {"FAQPage", "BreadcrumbList"}
            required.add("CollectionPage" if config["key"] == "hub" else "Service")
            missing_types = required - set(types)
            if missing_types:
                errors.append(f"{label}: missing schema types {sorted(missing_types)}")
            if {"Product", "Offer"} & set(types):
                errors.append(f"{label}: Product/Offer schema is forbidden")

            graph = next(
                (
                    schema.get("@graph", [])
                    for schema in schemas
                    if isinstance(schema, dict) and schema.get("@graph")
                ),
                [],
            )
            for entity in graph:
                if entity.get("@type") == "Service":
                    provider = entity.get("provider", {})
                    if provider.get("@id") and not provider.get("name"):
                        errors.append(f"{label}: Service provider @id has no name")
            visible_faq = soup.select(".harley-faq details")
            faq_schema = next(
                (
                    entity
                    for entity in graph
                    if entity.get("@type") == "FAQPage"
                ),
                None,
            )
            schema_faq = faq_schema.get("mainEntity", []) if faq_schema else []
            if len(visible_faq) != len(schema_faq):
                errors.append(f"{label}: visible/schema FAQ counts differ")
            for visible, structured in zip(visible_faq, schema_faq):
                visible_q = visible.find("summary").get_text(" ", strip=True)
                visible_a = " ".join(visible.select_one(".answer").get_text(" ", strip=True).split())
                schema_a = " ".join(structured["acceptedAnswer"]["text"].split())
                if visible_q != structured.get("name") or visible_a != schema_a:
                    errors.append(f"{label}: visible/schema FAQ content differs")

            forbidden = re.compile(
                r"dyno|диностенд|дино-тюн|діно-тюн|banco de ensaio|c-way|gold wing",
                re.IGNORECASE,
            )
            if forbidden.search(main_node.get_text(" ", strip=True)):
                errors.append(f"{label}: forbidden term in page content")

            if lang != "en":
                for anchor in main_node.find_all("a", href=True):
                    href = anchor["href"]
                    if (
                        href.startswith("/")
                        and not href.startswith((f"/{lang}/", "/photos/", "/assets/"))
                    ):
                        errors.append(f"{label}: cross-language main link {href}")

            desktop_group = soup.select_one(
                'nav[aria-label="Primary"] .nav-dropdown:has([data-i18n="nav.harleyHub"])'
            )
            desktop_links = [
                anchor.get("href")
                for anchor in desktop_group.select(".nav-dropdown-menu a")
            ] if desktop_group else []
            expected_nav = [
                url_path("harley", lang),
                url_path("harley-service", lang),
                url_path("harley-tuning", lang),
                url_path("harley-custom", lang),
            ]
            if desktop_links != expected_nav:
                errors.append(f"{label}: Harley desktop dropdown is invalid")

            if config["key"] == "hub":
                feed = soup.select(".harley-feed-card")
                if not feed:
                    errors.append(f"{label}: Harley blog feed is empty")
                expected_article = url_path(f"blog/{ARTICLE_SLUG}", lang)
                if expected_article not in [card.get("href") for card in feed]:
                    errors.append(f"{label}: Harley service article missing from feed")
            if config["key"] == "custom":
                names = [
                    item.get_text(" ", strip=True)
                    for item in soup.select(".portfolio-row h3")
                ]
                expected_names = [
                    PORTFOLIO[project_slug]["name"]
                    for project_slug in PORTFOLIO_ORDER
                ]
                if names != expected_names:
                    errors.append(f"{label}: portfolio order is invalid")
                project_links = [
                    item.get("href")
                    for item in soup.select(".portfolio-row .btn")
                ]
                expected_projects = [
                    url_path(f"projects/{project_slug}", lang)
                    for project_slug in PORTFOLIO_ORDER
                ]
                if project_links != expected_projects:
                    errors.append(f"{label}: portfolio links are invalid")

    integration_targets = []
    for lang in LANGS:
        prefix = "" if lang == "en" else f"{lang}/"
        integration_targets.extend(
            [
                (
                    SITE_ROOT / prefix / "index.html",
                    ".home-harley-hub",
                    url_path("harley", lang),
                    "homepage Harley block",
                ),
                (
                    SITE_ROOT / prefix / "custom" / "index.html",
                    ".custom-harley-link",
                    url_path("harley-custom", lang),
                    "custom Harley link",
                ),
                (
                    SITE_ROOT / prefix / "harley-service" / "index.html",
                    ".brand-pill-grid",
                    url_path("harley", lang),
                    "Harley service explore block",
                ),
                (
                    SITE_ROOT / prefix / "blog" / ARTICLE_SLUG / "index.html",
                    "main",
                    url_path("harley", lang),
                    "Harley article backlink",
                ),
            ]
        )
    for path, selector, href, description in integration_targets:
        soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
        scope = soup.select_one(selector)
        if not scope or not scope.find("a", href=href):
            errors.append(f"{path.relative_to(SITE_ROOT)}: missing {description}")

    sitemap = ET.parse(SITE_ROOT / "sitemap.xml")
    sitemap_urls = {
        node.text
        for node in sitemap.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
    }
    for config in PAGE_CONFIG.values():
        for lang in LANGS:
            url = expected_url(config["slug"], lang)
            if url not in sitemap_urls:
                errors.append(f"sitemap: missing {url}")

    if errors:
        print("Harley Hub validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("Harley Hub validation passed: 12 pages and all required integrations")
    return 0


if __name__ == "__main__":
    sys.exit(main())
