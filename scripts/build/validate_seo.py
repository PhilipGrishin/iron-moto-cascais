#!/usr/bin/env python3
"""Validate core static SEO invariants across sitemap URLs."""

from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup, FeatureNotFound

SITE_ROOT = Path(__file__).resolve().parents[2]
DOMAIN = "https://ironcustommotors.com"
LANGS = ["en", "ru", "uk", "pt"]
TARGET_LANGS = ["ru", "uk", "pt"]
LEGAL_PATHS = {"/privacy/", "/cookies/", "/terms/"}

try:
    BeautifulSoup("", "lxml")
    HTML_PARSER = "lxml"
except FeatureNotFound:
    HTML_PARSER = "html.parser"

LOCALIZED_PATHS = {
    "/",
    "/motorcycle-service/",
    "/parts/",
    "/upgrades-tuning/",
    "/custom/",
    "/pre-purchase-inspection/",
    "/pricing/",
    "/services/",
    "/projects/",
    "/about/",
    "/community/",
    "/contact/",
    "/faq/",
    "/privacy/",
    "/cookies/",
    "/terms/",
    "/bmw-service/",
    "/harley-service/",
    "/ducati-service/",
    "/blog/",
    "/blog/revtech-110-oil-service-engine-gearbox-drive/",
    "/news/",
    "/news/ericeira-kustom-fest-2026/",
    "/news/opens-new-workshop-in-cascais/",
    "/news/lisbon-motorcycle-film-fest-2026-beckman/",
}
for slug in [
    "inspirium",
    "beckman",
    "unbreakable",
    "quanta-r",
    "burly",
    "sturmvogel",
    "geometric",
    "joker",
    "hellboy",
    "true-religion",
]:
    LOCALIZED_PATHS.add(f"/projects/{slug}/")


def srcset_refs(value: str) -> list[str]:
    refs = []
    for item in value.split(","):
        ref = item.strip().split(" ", 1)[0]
        if ref:
            refs.append(ref)
    return refs


def local_ref_path(ref: str, html_path: Path) -> Path | None:
    ref = ref.strip()
    if not ref or ref.startswith(("#", "data:", "mailto:", "tel:", "javascript:", "http://", "https://", "//")):
        return None
    parsed = urlparse(ref)
    if not parsed.path:
        return None
    if parsed.path.startswith("/"):
        return SITE_ROOT / parsed.path.lstrip("/")
    return (html_path.parent / parsed.path).resolve()


def check_ref_exists(ref: str, html_path: Path, label: str) -> str | None:
    local_path = local_ref_path(ref, html_path)
    if local_path is None:
        return None
    if not local_path.exists():
        return f"missing local asset {label}: {ref}"
    return None


def check_local_assets(soup, html_path: Path) -> list[str]:
    issues = []
    attr_checks = {
        "img": ["src"],
        "source": ["src"],
        "video": ["src", "poster"],
        "script": ["src"],
    }
    for tag_name, attrs in attr_checks.items():
        for tag in soup.find_all(tag_name):
            for attr in attrs:
                if tag.get(attr):
                    issue = check_ref_exists(tag[attr], html_path, f"{tag_name}[{attr}]")
                    if issue:
                        issues.append(issue)
            if tag.get("srcset"):
                for ref in srcset_refs(tag["srcset"]):
                    issue = check_ref_exists(ref, html_path, f"{tag_name}[srcset]")
                    if issue:
                        issues.append(issue)

    for link in soup.find_all("link", href=True):
        rel = {str(item).lower() for item in link.get("rel", [])}
        if rel & {"stylesheet", "preload", "modulepreload", "icon", "apple-touch-icon", "manifest"}:
            issue = check_ref_exists(link["href"], html_path, "link[href]")
            if issue:
                issues.append(issue)

    style_texts = [style.get_text() for style in soup.find_all("style")]
    style_texts.extend(tag.get("style", "") for tag in soup.find_all(style=True))
    for text in style_texts:
        for ref in re.findall(r"url\\(([^)]+)\\)", text):
            ref = ref.strip().strip("\"'")
            issue = check_ref_exists(ref, html_path, "css url()")
            if issue:
                issues.append(issue)
    return issues


def sitemap_urls() -> list[str]:
    tree = ET.parse(SITE_ROOT / "sitemap.xml")
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return [loc.text.strip() for loc in tree.findall(".//sm:loc", ns) if loc.text]


def file_for_url(url: str) -> tuple[Path, str, str]:
    parsed = urlparse(url)
    path = parsed.path
    lang = "en"
    canonical_path = path
    for candidate in TARGET_LANGS:
        prefix = f"/{candidate}/"
        if path == f"/{candidate}/":
            lang = candidate
            canonical_path = "/"
            break
        if path.startswith(prefix):
            lang = candidate
            canonical_path = "/" + path[len(prefix):]
            break
    rel = path.strip("/")
    html_path = SITE_ROOT / rel / "index.html" if rel else SITE_ROOT / "index.html"
    return html_path, lang, canonical_path


def parse_jsonld(soup) -> tuple[list[object], list[str]]:
    blocks = []
    errors = []
    for idx, script in enumerate(soup.find_all("script", attrs={"type": "application/ld+json"}), start=1):
        raw = script.string or script.get_text()
        if not raw.strip():
            continue
        try:
            blocks.append(json.loads(raw))
        except json.JSONDecodeError as exc:
            errors.append(f"JSON-LD block {idx} is invalid: {exc}")
    return blocks, errors


def schema_contains_type(value, schema_type: str) -> bool:
    if isinstance(value, list):
        return any(schema_contains_type(item, schema_type) for item in value)
    if not isinstance(value, dict):
        return False
    current = value.get("@type")
    if current == schema_type or (isinstance(current, list) and schema_type in current):
        return True
    if "@graph" in value:
        return schema_contains_type(value["@graph"], schema_type)
    return any(schema_contains_type(child, schema_type) for child in value.values())


def expected_url(lang: str, canonical_path: str) -> str:
    suffix = canonical_path.lstrip("/")
    if lang == "en":
        return f"{DOMAIN}/{suffix}"
    return f"{DOMAIN}/{lang}/{suffix}"


def check_internal_links(soup, lang: str) -> list[str]:
    if lang == "en":
        return []
    issues = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith(("http://", "https://", "mailto:", "tel:", "#", "javascript:")):
            continue
        if href.startswith(("/assets/", "/photos/", "/pricing/files/", "/worker/")):
            continue
        if re.match(r"^/(ru|uk|pt)(/|$)", href):
            continue
        base = re.split(r"[?#]", href, 1)[0]
        if base in LOCALIZED_PATHS:
            issues.append(f"localized page links to EN path {href}")
    return issues


def validate_page(url: str) -> list[str]:
    html_path, lang, canonical_path = file_for_url(url)
    label = html_path.relative_to(SITE_ROOT) if html_path.exists() else html_path
    issues = []
    if not html_path.exists():
        return [f"{url}: missing file {label}"]

    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), HTML_PARSER)
    expected = expected_url(lang, canonical_path)

    title = soup.find("title")
    if title is None or not title.get_text(strip=True):
        issues.append("missing <title>")
    meta_desc = soup.find("meta", attrs={"name": "description"})
    if meta_desc is None or not meta_desc.get("content", "").strip():
        issues.append("missing meta description")
    canonical = soup.find("link", attrs={"rel": "canonical"})
    if canonical is None:
        issues.append("missing canonical")
    elif canonical.get("href") != expected:
        issues.append(f"canonical mismatch: {canonical.get('href')} != {expected}")

    h1_count = len(soup.find_all("h1"))
    if h1_count != 1:
        issues.append(f"expected one h1, found {h1_count}")

    alternates = soup.find_all("link", attrs={"rel": "alternate", "hreflang": True})
    hreflangs = {tag.get("hreflang") for tag in alternates}
    expected_hreflangs = set(LANGS + ["x-default"])
    if hreflangs != expected_hreflangs:
        issues.append(f"hreflang set mismatch: {sorted(hreflangs)}")

    jsonld_blocks, jsonld_errors = parse_jsonld(soup)
    issues.extend(jsonld_errors)
    if not jsonld_blocks:
        issues.append("missing JSON-LD")
    elif canonical_path not in LEGAL_PATHS and not schema_contains_type(jsonld_blocks, "BreadcrumbList"):
        issues.append("missing BreadcrumbList JSON-LD")

    issues.extend(check_internal_links(soup, lang))
    issues.extend(check_local_assets(soup, html_path))
    return [f"{url}: {issue}" for issue in issues]


def main() -> int:
    urls = sitemap_urls()
    issues = []
    for url in urls:
        issues.extend(validate_page(url))
    if issues:
        print(f"SEO validation failed: {len(issues)} issue(s)")
        for issue in issues:
            print(f"  - {issue}")
        return 1
    print(f"SEO validation passed: {len(urls)} sitemap URL(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
