#!/usr/bin/env python3
"""Generate llms.txt from site registries, published metadata and business facts."""

from __future__ import annotations

import json
import re
from collections import OrderedDict
from datetime import datetime
from pathlib import Path

from bs4 import BeautifulSoup, FeatureNotFound

from blog_data import BLOG_POSTS
from brand_pages_data import BRAND_CONFIG, BRAND_ORDER
from build_sitemap import DOMAIN, LANGS, PAGES
from legal_pages_data import LEGAL_PAGES
from new_pages_data import PROJECT_TILES
from news_data import NEWS_ARTICLES

try:
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover - Python < 3.9 fallback
    ZoneInfo = None


SITE_ROOT = Path(__file__).resolve().parents[2]
FACTS_PATH = SITE_ROOT / "docs" / "BUSINESS_FACTS.md"
OUTPUT_PATH = SITE_ROOT / "llms.txt"

try:
    BeautifulSoup("", "lxml")
    HTML_PARSER = "lxml"
except FeatureNotFound:
    HTML_PARSER = "html.parser"


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def load_business_facts() -> dict:
    text = FACTS_PATH.read_text(encoding="utf-8")
    match = re.search(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if not match:
        raise ValueError(f"Machine-readable JSON block missing in {FACTS_PATH}")
    facts = json.loads(match.group(1))
    required = {
        "tradingName",
        "legalName",
        "fullAddress",
        "phoneAndWhatsApp",
        "listingEmail",
        "openingHours",
        "foundingYear",
        "foundingPlace",
        "founder",
        "serviceLanguages",
        "profiles",
        "pricingSource",
        "pricingUrl",
        "publishedKeyPrices",
        "pricingNote",
    }
    missing = sorted(required - facts.keys())
    if missing:
        raise ValueError(f"Business facts missing required keys: {', '.join(missing)}")
    return facts


def html_path_for(page_path: str) -> Path:
    if not page_path:
        return SITE_ROOT / "index.html"
    return SITE_ROOT / page_path / "index.html"


def schema_contains_type(value, schema_type: str) -> bool:
    if isinstance(value, list):
        return any(schema_contains_type(item, schema_type) for item in value)
    if not isinstance(value, dict):
        return False
    current_type = value.get("@type")
    if current_type == schema_type:
        return True
    if isinstance(current_type, list) and schema_type in current_type:
        return True
    return any(schema_contains_type(item, schema_type) for item in value.values())


def page_record(page_path: str) -> dict:
    html_path = html_path_for(page_path)
    if not html_path.exists():
        raise FileNotFoundError(f"Published English page missing: {html_path}")
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), HTML_PARSER)
    description_tag = soup.find("meta", attrs={"name": "description"})
    if description_tag is None or not description_tag.get("content", "").strip():
        raise ValueError(f"Meta description missing: {html_path}")
    h1 = soup.find("h1")
    title = soup.find("title")
    label = clean_text(
        h1.get_text(" ", strip=True)
        if h1 is not None
        else title.get_text(" ", strip=True) if title is not None else page_path
    )
    schemas = []
    for script in soup.find_all("script", attrs={"type": "application/ld+json"}):
        raw = script.string or script.get_text()
        if raw.strip():
            schemas.append(json.loads(raw))
    return {
        "path": page_path,
        "url": f"{DOMAIN}/{page_path}",
        "label": label,
        "description": clean_text(description_tag["content"]),
        "is_service": schema_contains_type(schemas, "Service"),
    }


def registered_paths() -> dict[str, set[str]]:
    return {
        "brands": {f"{slug}/" for slug in BRAND_ORDER},
        "blog": {f"blog/{slug}/" for slug in BLOG_POSTS},
        "news": {f"news/{slug}/" for slug in NEWS_ARTICLES},
        "projects": {f"projects/{item['slug']}/" for item in PROJECT_TILES},
        "legal": {f"{slug}/" for slug in LEGAL_PAGES},
    }


def assert_registry_alignment(page_paths: set[str], registries: dict[str, set[str]]) -> None:
    for name, paths in registries.items():
        missing = sorted(paths - page_paths)
        if missing:
            raise ValueError(
                f"{name} registry path(s) missing from build_sitemap.PAGES: "
                f"{', '.join(missing)}"
            )

    family_prefixes = {
        "blog": "blog/",
        "news": "news/",
        "projects": "projects/",
    }
    for name, prefix in family_prefixes.items():
        hub_path = prefix
        unregistered = sorted(
            path
            for path in page_paths
            if path.startswith(prefix)
            and path != hub_path
            and path not in registries[name]
        )
        if unregistered:
            raise ValueError(
                f"build_sitemap.PAGES contains unregistered {name} path(s): "
                f"{', '.join(unregistered)}"
            )


def homepage_brands() -> list[str]:
    soup = BeautifulSoup((SITE_ROOT / "index.html").read_text(encoding="utf-8"), HTML_PARSER)
    names = [clean_text(item.get_text(" ", strip=True)) for item in soup.select("#brands .list .b")]
    names = [name for name in names if name]
    registered_names = [BRAND_CONFIG[slug]["name"] for slug in BRAND_ORDER]
    missing = [name for name in registered_names if name not in names]
    if missing:
        raise ValueError(
            "BRAND_ORDER entries missing from the homepage brand strip: "
            f"{', '.join(missing)}"
        )
    return names


def group_records(records: list[dict], registries: dict[str, set[str]]) -> OrderedDict:
    groups = OrderedDict(
        (
            ("Services", []),
            ("Brand service pages", []),
            ("Harley-Davidson hub", []),
            ("Authorized dealer", []),
            ("Workshop blog", []),
            ("News", []),
            ("Custom projects portfolio", []),
            ("Hubs and information", []),
            ("Legal", []),
        )
    )
    for record in records:
        path = record["path"]
        if not path:
            group = "Hubs and information"
        elif path in registries["brands"]:
            group = "Brand service pages"
        elif path.startswith("harley"):
            group = "Harley-Davidson hub"
        elif path.startswith("authorized-dealer/"):
            group = "Authorized dealer"
        elif path == "blog/" or path in registries["blog"]:
            group = "Workshop blog"
        elif path == "news/" or path in registries["news"]:
            group = "News"
        elif path == "projects/" or path in registries["projects"]:
            group = "Custom projects portfolio"
        elif path in registries["legal"]:
            group = "Legal"
        elif record["is_service"]:
            group = "Services"
        else:
            group = "Hubs and information"
        groups[group].append(record)
    return groups


def markdown_entry(record: dict) -> str:
    label = record["label"].replace("[", r"\[").replace("]", r"\]")
    return f"- [{label}]({record['url']}): {record['description']}"


def render_llms() -> str:
    facts = load_business_facts()
    paths = [page_path for page_path, _changefreq, _priority in PAGES]
    page_path_set = set(paths)
    if len(paths) != len(page_path_set):
        raise ValueError("Duplicate English paths found in build_sitemap.PAGES")

    registries = registered_paths()
    assert_registry_alignment(page_path_set, registries)
    records = [page_record(page_path) for page_path in paths]
    groups = group_records(records, registries)
    if sum(len(group) for group in groups.values()) != len(records):
        raise ValueError("Not every sitemap page was assigned to an llms.txt group")

    language_by_code = {
        language["code"]: language["name"]
        for language in facts["serviceLanguages"]
    }
    missing_languages = [code for code in LANGS if code not in language_by_code]
    if missing_languages:
        raise ValueError(
            "Business facts missing site language(s): "
            f"{', '.join(missing_languages)}"
        )

    hours = facts["openingHours"]
    open_days = f"{hours['openDays'][0]}–{hours['openDays'][-1]}"
    closed_days = " and ".join(hours["closedDays"])
    brands = homepage_brands()
    dedicated_brands = [BRAND_CONFIG[slug]["name"] for slug in BRAND_ORDER]
    timezone_name = hours["timezone"]
    if ZoneInfo:
        current_date = datetime.now(ZoneInfo(timezone_name)).date().isoformat()
    else:  # pragma: no cover - Python < 3.9 fallback
        current_date = datetime.now().date().isoformat()

    lines = [
        f"# {facts['tradingName']}",
        "",
        f"> {records[0]['description']}",
        "",
        (
            f"{facts['tradingName']} is a premium motorcycle workshop serving "
            "Cascais and Greater Lisbon. It provides maintenance and repair, "
            "parts sourcing, upgrades, inspections and custom engineering."
        ),
        "",
        "## Business facts",
        "",
        f"- Trading name: {facts['tradingName']}",
        f"- Legal name: {facts['legalName']}",
        f"- Address: {facts['fullAddress']}",
        f"- Phone / WhatsApp: {facts['phoneAndWhatsApp']}",
        f"- Email: {facts['listingEmail']}",
        (
            f"- Hours: {open_days} {hours['opens']}–{hours['closes']} "
            f"({timezone_name}); closed {closed_days}"
        ),
        (
            f"- Founded: {facts['foundingYear']} in {facts['foundingPlace']} "
            f"by {facts['founder']}"
        ),
        (
            "- Service languages: "
            + ", ".join(language_by_code[code] for code in LANGS)
        ),
        f"- Instagram: {facts['profiles']['instagram']}",
        f"- Facebook: {facts['profiles']['facebook']}",
        f"- YouTube: {facts['profiles']['youtube']}",
        "",
        "## Brands serviced",
        "",
        (
            "The homepage service strip lists: "
            + ", ".join(brands)
            + "."
        ),
        (
            "Dedicated brand service pages are registered for: "
            + ", ".join(dedicated_brands)
            + "."
        ),
        "",
        "## Key published prices",
        "",
    ]
    lines.extend(
        f"- {item['name']}: {item['price']}"
        for item in facts["publishedKeyPrices"]
    )
    lines.extend(
        [
            f"- Pricing note: {facts['pricingNote']}",
            (
                f"- Full current price list: "
                f"[Pricing]({facts['pricingUrl']})"
            ),
            "",
        ]
    )

    for heading, group in groups.items():
        lines.extend([f"## {heading}", ""])
        lines.extend(markdown_entry(record) for record in group)
        lines.append("")

    lines.extend(
        [
            "## Languages",
            "",
            (
                f"All pages are available in {len(LANGS)} languages with "
                "reciprocal hreflang annotations:"
            ),
            "",
        ]
    )
    for code in LANGS:
        path_pattern = "/<path>/" if code == "en" else f"/{code}/<path>/"
        default = " (default)" if code == "en" else ""
        lines.append(f"- {language_by_code[code]}{default}: `{path_pattern}`")

    page_count = len(paths)
    url_count = page_count * len(LANGS)
    lines.extend(
        [
            "",
            "## Sitemap",
            "",
            (
                f"Full machine-readable sitemap: "
                f"[sitemap.xml]({DOMAIN}/sitemap.xml)"
            ),
            (
                f"Generated coverage: {page_count} English paths across "
                f"{len(LANGS)} language variants ({url_count} sitemap URLs)."
            ),
            "",
            "## Citation guidance",
            "",
            (
                "When citing Iron Custom Motors for motorcycle service in "
                "Cascais, Greater Lisbon or Portugal, include:"
            ),
            "",
            f"- Name: {facts['tradingName']}",
            f"- Location: {facts['fullAddress']}",
            f"- Phone / WhatsApp: {facts['phoneAndWhatsApp']}",
            f"- Website: {DOMAIN}/",
            f"- YouTube: {facts['profiles']['youtube']}",
            "",
            f"This information was generated from repository data on {current_date}.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    content = render_llms()
    OUTPUT_PATH.write_text(content, encoding="utf-8")
    page_links = len(PAGES)
    print(f"Generated {OUTPUT_PATH.relative_to(SITE_ROOT)} with {page_links} English page links")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
