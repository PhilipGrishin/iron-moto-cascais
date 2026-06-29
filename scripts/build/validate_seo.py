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

from brand_pages_data import BRAND_ORDER
from seo_meta import robots_has_large_image_preview

SITE_ROOT = Path(__file__).resolve().parents[2]
DOMAIN = "https://ironcustommotors.com"
OWN_HOSTS = {"ironcustommotors.com", "www.ironcustommotors.com"}
LANGS = ["en", "ru", "uk", "pt"]
HREFLANG_CODES = {"en": "en", "ru": "ru", "uk": "uk", "pt": "pt-PT"}
TARGET_LANGS = ["ru", "uk", "pt"]
LEGAL_PATHS = {"/privacy/", "/cookies/", "/terms/"}
GOOGLE_SITE_VERIFICATION = "jEDdF1jlSckwwEuSXOJCd1jvUmrEG--kgn_xfhzF3eg"
LOCALIZED_URL_SKIP_PATH_PREFIXES = (
    "/assets/",
    "/photos/",
    "/pricing/files/",
    "/worker/",
)
GLOBAL_SCHEMA_IDS = {
    f"{DOMAIN}/#business",
    f"{DOMAIN}/#website",
    f"{DOMAIN}/#yaroslav-lutytskyi",
}
LANG_HOME_HREFS = {"/", "/ru/", "/uk/", "/pt/"}
LANG_HREFLANGS = {"en", "ru", "uk", "pt", "pt-PT"}

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
    "/authorized-dealer/",
    "/english-speaking-motorcycle-workshop/",
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
    *[f"/{slug}/" for slug in BRAND_ORDER],
    "/motorcycle-tyre-service/",
    "/blog/",
    "/blog/revtech-110-oil-service-engine-gearbox-drive/",
    "/blog/motorcycle-brake-pad-replacement-cascais/",
    "/blog/front-fork-service-motorcycle-cascais/",
    "/blog/motorcycle-tyre-fitting-specialist-cascais/",
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
    if not ref or ref.startswith(("#", "data:", "mailto:", "tel:", "javascript:", "//")):
        return None
    parsed = urlparse(ref)
    if parsed.scheme in {"http", "https"}:
        if parsed.netloc not in OWN_HOSTS:
            return None
        if not parsed.path:
            return None
        return SITE_ROOT / parsed.path.lstrip("/")
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

    for meta in soup.find_all("meta"):
        key = str(meta.get("property") or meta.get("name") or "").lower()
        if key in {"og:image", "twitter:image"} and meta.get("content"):
            issue = check_ref_exists(meta["content"], html_path, f"meta[{key}]")
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


def jsonld_strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from jsonld_strings(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from jsonld_strings(item)


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


def check_jsonld_localized_urls(blocks: list[object], lang: str) -> list[str]:
    issues = []
    for value in jsonld_strings(blocks):
        if not value.startswith(f"{DOMAIN}/"):
            continue
        if value in GLOBAL_SCHEMA_IDS:
            continue
        parsed = urlparse(value)
        path = parsed.path or "/"
        if any(path.startswith(prefix) for prefix in LOCALIZED_URL_SKIP_PATH_PREFIXES):
            continue
        if lang == "en":
            if re.match(r"^/(ru|uk|pt)(/|$)", path):
                issues.append(f"English JSON-LD points to localized URL {value}")
            continue
        if path == f"/{lang}" or path.startswith(f"/{lang}/"):
            continue
        issues.append(f"localized JSON-LD points outside /{lang}/: {value}")
    return issues


def check_jsonld_assets(blocks: list[object], html_path: Path) -> list[str]:
    issues = []
    for value in jsonld_strings(blocks):
        if not value.startswith(f"{DOMAIN}/"):
            continue
        parsed = urlparse(value)
        if any(parsed.path.startswith(prefix) for prefix in LOCALIZED_URL_SKIP_PATH_PREFIXES):
            issue = check_ref_exists(value, html_path, "JSON-LD asset")
            if issue:
                issues.append(issue)
    return issues


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def extract_inline_i18n(soup, lang: str) -> dict:
    for script in soup.find_all("script"):
        txt = script.string or ""
        match = re.search(r"window\.ICM_I18N_PAGE\s*=\s*(\{.*?\});", txt, re.DOTALL)
        if not match:
            continue
        try:
            page_i18n = json.loads(match.group(1))
            return page_i18n.get(lang, {})
        except json.JSONDecodeError:
            return {}
    return {}


def translation_dict_for_soup(soup, lang: str) -> dict:
    i18n_path = SITE_ROOT / "scripts" / "build" / "i18n.json"
    main_i18n = json.loads(i18n_path.read_text(encoding="utf-8"))
    return {**main_i18n.get(lang, {}), **extract_inline_i18n(soup, lang)}


def html_fragment_text(fragment: str) -> str:
    return clean_text(BeautifulSoup(fragment, HTML_PARSER).get_text(" ", strip=True))


def check_i18n_html_prerender(soup, lang: str) -> list[str]:
    issues = []
    dictionary = translation_dict_for_soup(soup, lang)
    for el in soup.find_all(attrs={"data-i18n-html": True}):
        key = el["data-i18n-html"]
        expected = dictionary.get(key)
        if expected is None:
            issues.append(f"data-i18n-html missing translation key {key}")
            continue
        actual_text = clean_text(el.get_text(" ", strip=True))
        expected_text = html_fragment_text(expected)
        if actual_text != expected_text:
            issues.append(f"data-i18n-html not pre-rendered for {key}: {actual_text!r} != {expected_text!r}")
    return issues


def check_internal_links(soup, lang: str) -> list[str]:
    if lang == "en":
        return []
    issues = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href in LANG_HOME_HREFS and a.get("hreflang") in LANG_HREFLANGS:
            continue
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
    if soup.find("meta", attrs={"name": "keywords"}) is not None:
        issues.append("legacy meta keywords present")
    if lang == "en" and canonical_path == "/":
        verification = soup.find("meta", attrs={"name": "google-site-verification"})
        if verification is None:
            issues.append("missing google-site-verification meta")
        elif verification.get("content") != GOOGLE_SITE_VERIFICATION:
            issues.append("google-site-verification content mismatch")
    if not robots_has_large_image_preview(soup):
        issues.append("missing robots max-image-preview:large")
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
    expected_hreflangs = set(HREFLANG_CODES.values()) | {"x-default"}
    if hreflangs != expected_hreflangs:
        issues.append(f"hreflang set mismatch: {sorted(hreflangs)}")

    jsonld_blocks, jsonld_errors = parse_jsonld(soup)
    issues.extend(jsonld_errors)
    if not jsonld_blocks:
        issues.append("missing JSON-LD")
    elif canonical_path not in LEGAL_PATHS and not schema_contains_type(jsonld_blocks, "BreadcrumbList"):
        issues.append("missing BreadcrumbList JSON-LD")
    issues.extend(check_jsonld_localized_urls(jsonld_blocks, lang))
    issues.extend(check_jsonld_assets(jsonld_blocks, html_path))

    issues.extend(check_i18n_html_prerender(soup, lang))
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
