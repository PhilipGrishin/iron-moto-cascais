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
    BRAND_PRICING,
    BRAND_PREFIX,
    BRAND_RELATED_LINKS,
    LANGS,
    PAGE_I18N,
)
from brand_pages_w2_content import CONTENT_PATH, EXPECTED_SHA256
from hero_images import HERO_IMAGE_FORMATS, HERO_IMAGE_WIDTHS, hero_image_slug
from pricing_data import SEC_02, SEC_04, SECTIONS

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


def schema_objects(value: object, schema_type: str) -> list[dict]:
    found: list[dict] = []
    if isinstance(value, list):
        for item in value:
            found.extend(schema_objects(item, schema_type))
    elif isinstance(value, dict):
        current = value.get("@type")
        if current == schema_type or (isinstance(current, list) and schema_type in current):
            found.append(value)
        for item in value.values():
            found.extend(schema_objects(item, schema_type))
    return found


def canonical_amount(value: str) -> str:
    return re.sub(r"[\s.,]", "", value)


def source_amounts(value: str) -> set[str]:
    return {
        canonical_amount(number)
        for number in re.findall(r"\d[\d\s.,]*", value)
        if canonical_amount(number)
    }


def normalized_text(value: str) -> str:
    return " ".join(value.split())


def monetary_amounts(text: str) -> set[str]:
    text = text.replace("\xa0", " ")
    number = r"(?:\d{1,3}(?:[\s.,]\d{3})+|\d+)"
    matches: list[str] = []
    for match in re.finditer(rf"€\s*({number})(?:\s*[–-]\s*€?\s*({number}))?", text):
        matches.extend(group for group in match.groups() if group)
    for match in re.finditer(rf"({number})(?:\s*/\s*({number}))?(?:\s*[–-]\s*({number}))?\+?\s*€", text):
        matches.extend(group for group in match.groups() if group)
    return {
        canonical_amount(value)
        for value in matches
        if canonical_amount(value)
    }


def pricing_amounts() -> set[str]:
    values: list[str] = []

    def visit(value, key=""):
        if isinstance(value, dict):
            for child_key, child in value.items():
                if child_key in {"price", "schema_price"}:
                    visit(child, child_key)
                else:
                    visit(child, child_key)
        elif isinstance(value, list):
            for child in value:
                visit(child, key)
        elif isinstance(value, str) and key in {"price", "schema_price"}:
            values.append(value)

    visit(SECTIONS)
    for row in SEC_04["valve_table"]["rows"]:
        values.extend(row[1:])
    return {
        canonical_amount(number)
        for value in values
        for number in re.findall(r"\d[\d\s.,]*", value)
        if canonical_amount(number)
    }


ALLOWED_PRICING_AMOUNTS = pricing_amounts()


def extract_inline_i18n(soup: BeautifulSoup) -> dict:
    for script in soup.find_all("script"):
        raw = script.string or script.get_text()
        match = re.search(r"window\.ICM_I18N_PAGE\s*=\s*(\{.*?\});", raw, re.DOTALL)
        if match:
            return json.loads(match.group(1))
    return {}


def numbered_count(values: dict[str, str], prefix: str, item_prefix: str, suffixes: tuple[str, ...]) -> int:
    idx = 1
    while all(values.get(f"{prefix}.{item_prefix}{idx}{suffix}") for suffix in suffixes):
        idx += 1
    return idx - 1


def required_content_keys(prefix: str, values: dict[str, str]) -> tuple[list[str], list[str]]:
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
    group_requirements = [
        ("t", ("t", "d"), 4, "tools"),
        ("s", ("t", "d"), 8, "services"),
        ("i", ("t", "d"), 5, "issues"),
        ("m", ("t", "d"), 5, "models"),
        ("q", ("",), 5, "FAQ questions"),
        ("a", ("",), 5, "FAQ answers"),
    ]
    group_issues: list[str] = []
    for item_prefix, suffixes, minimum, label in group_requirements:
        count = numbered_count(values, prefix, item_prefix, suffixes)
        if count < minimum:
            group_issues.append(f"{label} has {count}, expected at least {minimum}")
        for i in range(1, count + 1):
            if suffixes == ("",):
                keys.append(f"{item_prefix}{i}")
            else:
                keys.extend(f"{item_prefix}{i}{suffix}" for suffix in suffixes)
    return [f"{prefix}.{key}" for key in keys], group_issues


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
        meta = BRAND_HEAD[slug][lang]
        if len(meta["title"]) > 60:
            issues.append(f"title is {len(meta['title'])} characters in {lang}; maximum is 60")
        if not 140 <= len(meta["description"]) <= 155:
            issues.append(f"meta description is {len(meta['description'])} characters in {lang}; expected 140–155")
        for key, value in {**PAGE_I18N[slug][lang], **meta}.items():
            unexpected = monetary_amounts(value) - ALLOWED_PRICING_AMOUNTS
            if unexpected:
                issues.append(f"{lang} {key} contains price amount(s) absent from pricing_data.py: {sorted(unexpected)}")
        prefix = BRAND_PREFIX.get(slug)
        if prefix:
            required_keys, group_issues = required_content_keys(prefix, PAGE_I18N[slug][lang])
            for group_issue in group_issues:
                issues.append(f"{group_issue} in {lang}")
            missing = [key for key in required_keys if key not in PAGE_I18N[slug][lang]]
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


def check_home_brand_strip() -> list[str]:
    issues: list[str] = []
    home_files = {
        "en": SITE_ROOT / "index.html",
        "ru": SITE_ROOT / "ru" / "index.html",
        "uk": SITE_ROOT / "uk" / "index.html",
        "pt": SITE_ROOT / "pt" / "index.html",
    }
    for lang, html_path in home_files.items():
        if not html_path.exists():
            issues.append(f"{lang}: missing homepage {html_path.relative_to(SITE_ROOT)}")
            continue
        soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), HTML_PARSER)
        brand_strip = soup.find("section", id="brands")
        if brand_strip is None:
            issues.append(f"{lang}: missing homepage brand strip")
            continue
        for slug in BRAND_ORDER:
            href = expected_path(slug, lang)
            if brand_strip.find("a", href=href) is None:
                issues.append(f"{lang}: homepage brand strip missing active link to {href}")
    return issues


def check_generated_page(slug: str, lang: str, sitemap: set[str]) -> list[str]:
    issues: list[str] = []
    html_path = expected_file(slug, lang)
    if not html_path.exists():
        return [f"missing generated file {html_path.relative_to(SITE_ROOT)}"]

    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), HTML_PARSER)
    url = expected_url(slug, lang)

    expected_head = BRAND_HEAD[slug][lang]
    actual_title = soup.title.get_text(strip=True) if soup.title else ""
    if actual_title != expected_head["title"]:
        issues.append(f"title does not match BRAND_HEAD: {actual_title!r}")
    description = soup.find("meta", attrs={"name": "description"})
    actual_description = description.get("content", "") if description else ""
    if actual_description != expected_head["description"]:
        issues.append("meta description does not match BRAND_HEAD")

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

    faq = soup.select(".brand-faq details")
    faq_schemas = [item for block in blocks for item in schema_objects(block, "FAQPage")]
    schema_faq_count = len(faq_schemas[0].get("mainEntity", [])) if faq_schemas else 0
    if len(faq) != schema_faq_count:
        issues.append(f"visible FAQ count {len(faq)} != FAQPage count {schema_faq_count}")

    pricing_section = soup.find("section", attrs={"data-brand-pricing": True})
    if pricing_section is None:
        issues.append("missing generated brand pricing section")
    else:
        config = BRAND_PRICING[slug]
        group_id = config["group"]
        if pricing_section.get("data-source-group") != group_id:
            issues.append(f"brand pricing source group is {pricing_section.get('data-source-group')}, expected {group_id}")
        group = next((item for item in SEC_02["groups"] if item.get("id") == group_id), None)
        if group is None:
            issues.append(f"missing pricing source group {group_id}")
            return issues
        checklist = pricing_section.select(".brand-price-checklist li")
        actual_checklist = [normalized_text(item.get_text(" ", strip=True)) for item in checklist]
        expected_checklist = [normalized_text(item) for item in group["checklist"][lang]]
        if actual_checklist != expected_checklist:
            issues.append("pricing checklist does not match pricing_data.py")
        scheduled = pricing_section.find(attrs={"data-price-id": "scheduled-service"})
        if scheduled is None or scheduled.find(class_="amount") is None:
            issues.append("missing scheduled-service group price line")
        else:
            actual_group_amounts = monetary_amounts(scheduled.get_text(" ", strip=True))
            expected_group_amounts = source_amounts(group["price"])
            if actual_group_amounts != expected_group_amounts:
                issues.append(
                    f"scheduled-service amount(s) {sorted(actual_group_amounts)} != pricing source {sorted(expected_group_amounts)}"
                )
            has_from = scheduled.find(class_="from") is not None
            if has_from != bool(group.get("price_from")):
                issues.append(f"scheduled-service from marker is {has_from}, expected {bool(group.get('price_from'))}")

        expected_extra_ids = list(config["extras"])
        actual_extra_ids = [
            item.get("data-price-id")
            for item in pricing_section.select(".brand-price-card")
            if item.get("data-price-id") in expected_extra_ids
        ]
        if actual_extra_ids != expected_extra_ids:
            issues.append(f"brand-specific price cards {actual_extra_ids} != source {expected_extra_ids}")
        extra_sources = {
            item["id"]: item
            for item in SEC_02["brand_specific_cards"]
            if item.get("id") in expected_extra_ids
        }
        for item_id in expected_extra_ids:
            item = extra_sources.get(item_id)
            if item is None:
                issues.append(f"missing brand-specific pricing source {item_id}")
                continue
            card = pricing_section.find(attrs={"data-price-id": item["id"]})
            actual_amounts = monetary_amounts(card.get_text(" ", strip=True)) if card else set()
            if actual_amounts != source_amounts(item["price"]):
                issues.append(f"{item['id']} amount(s) {sorted(actual_amounts)} != pricing source {sorted(source_amounts(item['price']))}")

        pricing_href = "/pricing/" if lang == "en" else f"/{lang}/pricing/"
        if pricing_section.find("a", href=pricing_href) is None:
            issues.append(f"missing same-language price-list link to {pricing_href}")

        prefix = BRAND_PREFIX[slug]
        intro = pricing_section.find(attrs={"data-i18n": f"{prefix}.pricingIntro"})
        expected_intro = PAGE_I18N[slug][lang][f"{prefix}.pricingIntro"]
        if intro is None or normalized_text(intro.get_text(" ", strip=True)) != normalized_text(expected_intro):
            issues.append("pricing section intro does not match approved W2 copy")

    main = soup.find("main")
    direct_sections = main.find_all("section", recursive=False) if main else []
    pricing_index = direct_sections.index(pricing_section) if pricing_section in direct_sections else -1
    if pricing_index <= 0 or pricing_index + 1 >= len(direct_sections):
        issues.append("brand pricing section is not between page sections")
    elif not direct_sections[pricing_index - 1].find(attrs={"data-i18n": re.compile(r"\.servicesTitle$")}) or not direct_sections[pricing_index + 1].find(attrs={"data-i18n": re.compile(r"\.issuesTitle$")}):
        issues.append("brand pricing section is not directly between services and failure patterns")

    main_visible = main.get_text(" ", strip=True) if main else ""
    unexpected_visible = monetary_amounts(main_visible) - ALLOWED_PRICING_AMOUNTS
    if unexpected_visible:
        issues.append(f"visible price amount(s) absent from pricing_data.py: {sorted(unexpected_visible)}")

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
    import hashlib
    actual_copy_sha = hashlib.sha256(CONTENT_PATH.read_bytes()).hexdigest() if CONTENT_PATH.exists() else "missing"
    if actual_copy_sha != EXPECTED_SHA256:
        all_issues.append(f"W2 copy SHA-256 is {actual_copy_sha}; expected {EXPECTED_SHA256}")
    all_issues.extend(check_home_brand_strip())
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
