#!/usr/bin/env python3
"""Validate generated brand service pages and their build wiring."""

from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from bs4 import BeautifulSoup, FeatureNotFound

from brand_pages_data import (
    BRAND_CONFIG,
    BRAND_HEAD,
    BRAND_NAME,
    BRAND_NAV_KEYS,
    BRAND_ORDER,
    BRAND_PREFIX,
    BRAND_RELATED_LINKS,
    LANGS,
    PAGE_I18N,
)
from hero_images import HERO_IMAGE_FORMATS, HERO_IMAGE_WIDTHS, hero_image_slug

SITE_ROOT = Path(__file__).resolve().parents[2]
DOMAIN = "https://ironcustommotors.com"

try:
    BeautifulSoup("", "lxml")
    HTML_PARSER = "lxml"
except FeatureNotFound:
    HTML_PARSER = "html.parser"


def expected_path(slug: str, lang: str) -> str:
    if lang == "en":
        return f"/{slug}/"
    return f"/{lang}/{slug}/"


def expected_file(slug: str, lang: str) -> Path:
    if lang == "en":
        return SITE_ROOT / slug / "index.html"
    return SITE_ROOT / lang / slug / "index.html"


def expected_url(slug: str, lang: str) -> str:
    return f"{DOMAIN}{expected_path(slug, lang)}"


def parse_jsonld(soup: BeautifulSoup) -> list[object]:
    blocks: list[object] = []
    for idx, script in enumerate(soup.find_all("script", attrs={"type": "application/ld+json"}), start=1):
        raw = script.string or script.get_text()
        if not raw.strip():
            continue
        try:
            blocks.append(json.loads(raw))
        except json.JSONDecodeError as exc:
            raise ValueError(f"JSON-LD block {idx} is invalid: {exc}") from exc
    return blocks


def schema_contains_type(value: object, schema_type: str) -> bool:
    if isinstance(value, list):
        return any(schema_contains_type(item, schema_type) for item in value)
    if not isinstance(value, dict):
        return False
    current = value.get("@type")
    if current == schema_type or (isinstance(current, list) and schema_type in current):
        return True
    if "@graph" in value:
        return schema_contains_type(value["@graph"], schema_type)
    return any(schema_contains_type(item, schema_type) for item in value.values())


def extract_inline_i18n(soup: BeautifulSoup) -> dict:
    for script in soup.find_all("script"):
        raw = script.string or script.get_text()
        match = re.search(r"window\.ICM_I18N_PAGE\s*=\s*(\{.*?\});", raw, re.DOTALL)
        if match:
            return json.loads(match.group(1))
    return {}


def required_content_keys(prefix: str) -> list[str]:
    keys = [
        "eyebrow", "h1", "sub", "breadHome", "h1Crumb", "btnWA", "btnSend",
        "heroAlt",
        "introEyebrow", "introTitle", "introP1", "introP2", "introP3",
        "toolsEyebrow", "toolsTitle", "toolsLead",
        "servicesEyebrow", "servicesTitle", "servicesLead",
        "issuesEyebrow", "issuesTitle", "issuesLead",
        "modelsEyebrow", "modelsTitle", "modelsLead",
        "partsEyebrow", "partsTitle", "partsLead",
        "faqEyebrow", "faqTitle",
        "ctaEyebrow", "ctaTitle", "ctaText", "btnBack",
    ]
    keys.extend(f"t{i}{suffix}" for i in range(1, 5) for suffix in ("t", "d"))
    keys.extend(f"s{i}{suffix}" for i in range(1, 9) for suffix in ("t", "d"))
    keys.extend(f"i{i}{suffix}" for i in range(1, 6) for suffix in ("t", "d"))
    keys.extend(f"m{i}{suffix}" for i in range(1, 7) for suffix in ("t", "d"))
    keys.extend(f"q{i}" for i in range(1, 6))
    keys.extend(f"a{i}" for i in range(1, 6))
    return [f"{prefix}.{key}" for key in keys]


def sitemap_urls() -> set[str]:
    sitemap = SITE_ROOT / "sitemap.xml"
    if not sitemap.exists():
        return set()
    tree = ET.parse(sitemap)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return {loc.text.strip() for loc in tree.findall(".//sm:loc", ns) if loc.text}


def check_registry(slug: str) -> list[str]:
    issues: list[str] = []
    if slug not in BRAND_CONFIG:
        return [f"{slug}: missing BRAND_CONFIG entry"]
    if slug not in BRAND_HEAD:
        issues.append("missing BRAND_HEAD entry")
    if slug not in PAGE_I18N:
        issues.append("missing PAGE_I18N entry")
    if slug not in BRAND_PREFIX:
        issues.append("missing prefix entry")
    if slug not in BRAND_RELATED_LINKS:
        issues.append("missing related links")

    nav_key = BRAND_NAV_KEYS.get(slug)
    i18n_path = SITE_ROOT / "scripts" / "build" / "i18n.json"
    if nav_key and i18n_path.exists():
        main_i18n = json.loads(i18n_path.read_text(encoding="utf-8"))
        for lang in LANGS:
            if nav_key not in main_i18n.get(lang, {}):
                issues.append(f"missing global i18n nav key {nav_key} in {lang}")

    for lang in LANGS:
        if lang not in BRAND_HEAD.get(slug, {}):
            issues.append(f"missing head meta for {lang}")
        if lang not in PAGE_I18N.get(slug, {}):
            issues.append(f"missing page i18n for {lang}")
            continue
        prefix = BRAND_PREFIX.get(slug)
        if prefix:
            missing = [key for key in required_content_keys(prefix) if key not in PAGE_I18N[slug][lang]]
            for key in missing[:20]:
                issues.append(f"missing content key {key} in {lang}")
            if len(missing) > 20:
                issues.append(f"{len(missing) - 20} more content keys missing in {lang}")
    return issues


def check_hero_assets(slug: str) -> list[str]:
    issues: list[str] = []
    source = BRAND_CONFIG[slug]["hero"].lstrip("/")
    source_path = SITE_ROOT / source
    if not source_path.exists():
        return [f"missing hero source {source}"]
    image_slug = hero_image_slug(source)
    for width in HERO_IMAGE_WIDTHS:
        for ext in HERO_IMAGE_FORMATS:
            variant = SITE_ROOT / "photos" / "optimized" / f"{image_slug}-{width}.{ext}"
            if not variant.exists():
                issues.append(f"missing optimized hero variant {variant.relative_to(SITE_ROOT)}")
    return issues


def check_workflow(slug: str) -> list[str]:
    workflow = SITE_ROOT / ".github" / "workflows" / "pages.yml"
    if not workflow.exists():
        return ["missing GitHub Pages workflow"]
    text = workflow.read_text(encoding="utf-8")
    if re.search(rf"^\s*{re.escape(slug)}\s*\\?$", text, re.MULTILINE):
        return []
    return [f"{slug} is not copied into the GitHub Pages artifact"]


def check_generated_page(slug: str, lang: str, sitemap: set[str]) -> list[str]:
    issues: list[str] = []
    html_path = expected_file(slug, lang)
    if not html_path.exists():
        return [f"missing generated file {html_path.relative_to(SITE_ROOT)}"]

    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), HTML_PARSER)
    url = expected_url(slug, lang)

    canonical = soup.find("link", rel="canonical")
    if not canonical or canonical.get("href") != url:
        issues.append(f"bad canonical: {canonical.get('href') if canonical else 'missing'}")

    alternates = {
        link.get("hreflang"): link.get("href")
        for link in soup.find_all("link")
        if "alternate" in (link.get("rel") or [])
    }
    expected_hreflang = {
        "en": expected_url(slug, "en"),
        "ru": expected_url(slug, "ru"),
        "uk": expected_url(slug, "uk"),
        "pt-PT": expected_url(slug, "pt"),
        "x-default": expected_url(slug, "en"),
    }
    for code, href in expected_hreflang.items():
        if alternates.get(code) != href:
            issues.append(f"bad hreflang {code}: {alternates.get(code)}")

    try:
        blocks = parse_jsonld(soup)
    except ValueError as exc:
        issues.append(str(exc))
        blocks = []
    for schema_type in ("Service", "FAQPage", "BreadcrumbList"):
        if not schema_contains_type(blocks, schema_type):
            issues.append(f"missing JSON-LD {schema_type}")

    inline_i18n = extract_inline_i18n(soup)
    for required_lang in LANGS:
        if required_lang not in inline_i18n:
            issues.append(f"inline ICM_I18N_PAGE missing {required_lang}")

    if url not in sitemap:
        issues.append(f"missing from sitemap: {url}")

    text = soup.get_text(" ", strip=True).lower()
    banned_terms = ("scooter", "скутер", "самокат")
    for term in banned_terms:
        if term in text:
            issues.append(f"banned term present: {term}")

    related_section = soup.find(attrs={"data-enhancement": "money-related"})
    if related_section is None:
        issues.append("missing money-related section")

    for other_slug in BRAND_ORDER:
        if other_slug == slug:
            continue
        href = expected_path(other_slug, lang)
        if related_section is None or related_section.find("a", href=href) is None:
            issues.append(f"missing reciprocal brand link in related section to {href}")

    return issues


def validate_slug(slug: str, sitemap: set[str]) -> list[str]:
    issues: list[str] = []
    issues.extend(check_registry(slug))
    if slug in BRAND_CONFIG:
        issues.extend(check_hero_assets(slug))
        issues.extend(check_workflow(slug))
    for lang in LANGS:
        issues.extend(f"{lang}: {issue}" for issue in check_generated_page(slug, lang, sitemap))
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate generated brand service pages.")
    parser.add_argument("slugs", nargs="*", help="Brand slugs to validate. Defaults to all registered brands.")
    args = parser.parse_args()

    slugs = args.slugs or list(BRAND_ORDER)
    sitemap = sitemap_urls()
    all_issues: list[str] = []
    for slug in slugs:
        if slug not in BRAND_ORDER and slug not in BRAND_CONFIG:
            all_issues.append(f"{slug}: unknown brand slug")
            continue
        for issue in validate_slug(slug, sitemap):
            all_issues.append(f"{slug}: {issue}")

    if all_issues:
        print("Brand page validation failed:")
        for issue in all_issues:
            print(f" - {issue}")
        return 1

    print(f"Brand page validation passed: {len(slugs)} brand page set(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
