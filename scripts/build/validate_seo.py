#!/usr/bin/env python3
"""Validate core static SEO invariants across sitemap URLs."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from bs4 import BeautifulSoup, FeatureNotFound

from brand_pages_data import BRAND_ORDER
from hero_images import css_hero_preload_alignment, picture_hero_preload_alignment
from seo_meta import robots_has_large_image_preview

SITE_ROOT = Path(__file__).resolve().parents[2]
DOMAIN = "https://ironcustommotors.com"
OWN_HOSTS = {"ironcustommotors.com", "www.ironcustommotors.com"}
LANGS = ["en", "ru", "uk", "pt"]
HREFLANG_CODES = {"en": "en", "ru": "ru", "uk": "uk", "pt": "pt-PT"}
TARGET_LANGS = ["ru", "uk", "pt"]
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
CHROME_TEXT_REGIONS = (
    "#cookieBanner",
    "#stickyCta",
    ".fab-wa",
    "header.site-header",
    "#mobileDrawer",
    "footer.site-footer",
)
REQUIRED_CHROME_I18N_KEYS = {
    "cookie.text",
    "cookie.reject",
    "cookie.accept",
    "cta.bookHeader",
    "cta.whatsapp",
    "footer.tagline",
    "footer.col1",
    "footer.col2",
}

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
    "/authorized-dealer/c-way/",
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
    "fighter",
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
        if link.get("imagesrcset"):
            for ref in srcset_refs(link["imagesrcset"]):
                issue = check_ref_exists(ref, html_path, "link[imagesrcset]")
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


def versioned_asset_refs(soup):
    tags = [
        (tag, "href")
        for tag in soup.find_all("link", href=True)
        if "stylesheet" in {str(item).lower() for item in tag.get("rel", [])}
    ]
    tags.extend((tag, "src") for tag in soup.find_all("script", src=True))

    for tag, attr in tags:
        ref = tag[attr]
        parsed = urlparse(ref)
        if parsed.scheme in {"http", "https"} and parsed.netloc not in OWN_HOSTS:
            continue
        if not parsed.path.startswith("/assets/") or not parsed.path.endswith((".css", ".js")):
            continue
        yield parsed.path, parse_qs(parsed.query, keep_blank_values=True).get("v", []), ref


def check_asset_cache_bust_presence(soup) -> list[str]:
    issues = []
    for _, versions, ref in versioned_asset_refs(soup):
        if len(versions) != 1 or not versions[0]:
            issues.append(f"asset is missing one non-empty cache-bust value: {ref}")
    return issues


def check_lcp_image_delivery(soup) -> list[str]:
    """Validate the browser hints and image attributes used for LCP delivery."""
    issues = []
    image_preloads = [
        link
        for link in soup.find_all("link", href=True)
        if "preload" in {str(item).lower() for item in link.get("rel", [])}
        and str(link.get("as", "")).lower() == "image"
    ]
    priority_images = soup.find_all("img", attrs={"fetchpriority": "high"})

    if not image_preloads and not priority_images:
        issues.append("missing LCP image preload or img fetchpriority=high")
    if len(priority_images) > 1:
        issues.append(f"multiple img fetchpriority=high candidates: {len(priority_images)}")
    for image in priority_images:
        if image.get("loading") == "lazy":
            issues.append("img fetchpriority=high must not use loading=lazy")
    for image in soup.find_all("img"):
        if not image.has_attr("alt"):
            issues.append(f"img is missing alt: {image.get('src', '<no src>')}")
    return issues


def check_css_hero_preload_alignment(soup) -> tuple[bool, list[str]]:
    """Validate that responsive preloads match the CSS-rendered hero resource."""
    hero, mismatches = css_hero_preload_alignment(soup, SITE_ROOT)
    if hero is None:
        return False, []
    return True, [f"CSS hero preload mismatch: {item}" for item in mismatches]


def check_picture_hero_preload_alignment(soup) -> tuple[bool, list[str]]:
    """Validate that a Blog picture hero and its preload share one selection."""
    hero, mismatches = picture_hero_preload_alignment(soup)
    if hero is None:
        return False, []
    return True, [f"picture hero preload mismatch: {item}" for item in mismatches]


def check_asset_cache_bust_consistency(urls: list[str]) -> list[str]:
    values_by_asset = {}
    for url in urls:
        html_path, _, _ = file_for_url(url)
        if not html_path.exists():
            continue
        soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), HTML_PARSER)
        for asset_path, versions, _ in versioned_asset_refs(soup):
            if len(versions) == 1 and versions[0]:
                values_by_asset.setdefault(asset_path, set()).add(versions[0])

    issues = []
    for asset_path, values in sorted(values_by_asset.items()):
        if len(values) > 1:
            issues.append(
                f"{asset_path}: multiple cache-bust values across sitemap pages: "
                f"{', '.join(sorted(values))}"
            )
    return issues


def sitemap_urls() -> list[str]:
    tree = ET.parse(SITE_ROOT / "sitemap.xml")
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return [loc.text.strip() for loc in tree.findall(".//sm:loc", ns) if loc.text]


def normalize_site_url(url: str) -> str | None:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or parsed.netloc not in OWN_HOSTS:
        return None
    path = parsed.path or "/"
    if path != "/" and not path.endswith("/"):
        path = f"{path}/"
    return f"{DOMAIN}{path}"


def llms_internal_urls() -> set[str]:
    llms_path = SITE_ROOT / "llms.txt"
    if not llms_path.exists():
        return set()
    targets = re.findall(
        r"\]\((https?://[^)\s]+)\)",
        llms_path.read_text(encoding="utf-8"),
    )
    return {
        normalized
        for target in targets
        if (normalized := normalize_site_url(target)) is not None
    }


def check_llms_sitemap_coverage(urls: list[str]) -> list[str]:
    english_urls = {
        normalized
        for url in urls
        if not re.match(r"^/(ru|uk|pt)(/|$)", urlparse(url).path)
        if (normalized := normalize_site_url(url)) is not None
    }
    missing = sorted(english_urls - llms_internal_urls())
    if not missing:
        return []
    return [
        "llms.txt is missing "
        f"{len(missing)} English sitemap URL(s): {', '.join(missing)}"
    ]


def check_codex_changelog() -> list[str]:
    changelog_path = SITE_ROOT / "docs" / "CODEX_CHANGELOG.md"
    if not changelog_path.exists():
        return ["docs/CODEX_CHANGELOG.md is missing"]

    text = changelog_path.read_text(encoding="utf-8")
    issues = []
    if re.search(r"\bthis commit\b", text, flags=re.IGNORECASE):
        issues.append("docs/CODEX_CHANGELOG.md contains a 'this commit' placeholder")

    entries = list(
        re.finditer(
            r"^## (\d{4}-\d{2}-\d{2} - .+)$",
            text,
            flags=re.MULTILINE,
        )
    )
    for index, entry in enumerate(entries):
        block_end = entries[index + 1].start() if index + 1 < len(entries) else len(text)
        block = text[entry.end():block_end]
        commit_match = re.search(
            r"^- Commit: `([0-9a-f]{7,40})`$",
            block,
            flags=re.MULTILINE,
        )
        if commit_match is None:
            issues.append(f"changelog entry {entry.group(1)!r} has no commit hash")
            continue
        commit_hash = commit_match.group(1)
        result = subprocess.run(
            ["git", "cat-file", "-e", f"{commit_hash}^{{commit}}"],
            cwd=SITE_ROOT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        if result.returncode != 0:
            issues.append(
                f"changelog entry {entry.group(1)!r} references unknown commit {commit_hash}"
            )
    return issues


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


def schema_has_entity_type(blocks: list[object], schema_type: str) -> bool:
    for block in blocks:
        if not isinstance(block, dict):
            continue
        current = block.get("@type")
        if current == schema_type or (isinstance(current, list) and schema_type in current):
            return True
        graph = block.get("@graph")
        if not isinstance(graph, list):
            continue
        for node in graph:
            if not isinstance(node, dict):
                continue
            current = node.get("@type")
            if current == schema_type or (isinstance(current, list) and schema_type in current):
                return True
    return False


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
        if a.get("hreflang") in LANG_HREFLANGS:
            continue
        if href.startswith(("http://", "https://", "mailto:", "tel:", "#", "javascript:")):
            continue
        if href.startswith(("/assets/", "/photos/", "/pricing/files/", "/worker/")):
            continue
        if re.match(r"^/(ru|uk|pt)(/|$)", href):
            continue
        base = re.split(r"[?#]", href, maxsplit=1)[0]
        if base in LOCALIZED_PATHS:
            issues.append(f"localized page links to EN path {href}")
    return issues


def nav_item_identity(anchor) -> str:
    key = anchor.get("data-i18n")
    if key:
        return f"i18n:{key}"
    return f"text:{clean_text(anchor.get_text(' ', strip=True))}"


def footer_column(soup, key: str):
    heading = soup.find(attrs={"data-i18n": key})
    return heading.find_parent("div", class_="footer-col") if heading else None


def navigation_signature(soup) -> dict[str, object]:
    primary = soup.find("nav", attrs={"aria-label": "Primary"})
    mobile = soup.find("nav", class_="nav-mobile")
    footer_services = footer_column(soup, "footer.col1")
    footer_company = footer_column(soup, "footer.col2")
    return {
        "desktop": tuple(
            nav_item_identity(anchor)
            for anchor in primary.find_all("a", href=True)
        ) if primary else (),
        "mobile": tuple(
            nav_item_identity(anchor)
            for anchor in mobile.find_all("a", href=True)
        ) if mobile else (),
        "mobile_groups": len(mobile.select(".mobile-nav-group")) if mobile else 0,
        "footer_services": tuple(
            nav_item_identity(anchor)
            for anchor in footer_services.find_all("a", href=True)
        ) if footer_services else (),
        "footer_company": tuple(
            nav_item_identity(anchor)
            for anchor in footer_company.find_all("a", href=True)
        ) if footer_company else (),
    }


def chrome_text_signature(soup) -> tuple[tuple[str, str, str], ...]:
    """Return every translated chrome string in canonical region order."""
    signature = []
    for selector in CHROME_TEXT_REGIONS:
        region = soup.select_one(selector)
        if region is None:
            signature.append((selector, "<missing-region>", ""))
            continue
        elements = [region] if region.has_attr("data-i18n") else []
        elements.extend(region.select("[data-i18n]"))
        signature.extend(
            (
                selector,
                element["data-i18n"],
                clean_text(element.get_text(" ", strip=True)),
            )
            for element in elements
        )
    return tuple(signature)


def check_chrome_text_parity(urls: list[str]) -> list[str]:
    """Compare indexable chrome copy with the same-language homepage."""
    soups = {}
    baselines = {}
    for url in urls:
        html_path, lang, canonical_path = file_for_url(url)
        if not html_path.exists():
            continue
        soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), HTML_PARSER)
        soups[url] = (lang, soup)
        if canonical_path == "/":
            baselines[lang] = chrome_text_signature(soup)

    issues = []
    for lang, baseline in baselines.items():
        keys = {key for _, key, _ in baseline}
        missing = sorted(REQUIRED_CHROME_I18N_KEYS - keys)
        if missing:
            issues.append(
                f"{lang} homepage chrome baseline is missing keys: {', '.join(missing)}"
            )

    for url, (lang, soup) in soups.items():
        expected = baselines.get(lang)
        if expected is None:
            issues.append(f"{url}: missing {lang} homepage chrome baseline")
            continue
        actual = chrome_text_signature(soup)
        if actual == expected:
            continue
        mismatch_labels = []
        for index in range(max(len(actual), len(expected))):
            actual_item = actual[index] if index < len(actual) else None
            expected_item = expected[index] if index < len(expected) else None
            if actual_item == expected_item:
                continue
            item = actual_item or expected_item
            label = f"{item[0]}:{item[1]}"
            if label not in mismatch_labels:
                mismatch_labels.append(label)
        issues.append(
            f"{url}: chrome text parity mismatch against {lang} homepage: "
            f"{', '.join(mismatch_labels)}"
        )
    return issues


def navigation_anchors(soup):
    primary = soup.find("nav", attrs={"aria-label": "Primary"})
    mobile = soup.find("nav", class_="nav-mobile")
    footer_services = footer_column(soup, "footer.col1")
    footer_company = footer_column(soup, "footer.col2")
    for region in (primary, mobile, footer_services, footer_company):
        if region:
            yield from region.find_all("a", href=True)


def check_navigation_link_locality(soup, lang: str) -> list[str]:
    issues = []
    for anchor in navigation_anchors(soup):
        href = anchor["href"]
        parsed = urlparse(href)
        if (
            parsed.scheme
            or parsed.netloc
            or not parsed.path.startswith("/")
            or parsed.path.startswith(LOCALIZED_URL_SKIP_PATH_PREFIXES)
        ):
            continue
        if lang == "en":
            if re.match(r"^/(ru|uk|pt)(/|$)", parsed.path):
                issues.append(f"English navigation points to localized URL {href}")
            continue
        if parsed.path == f"/{lang}/" or parsed.path.startswith(f"/{lang}/"):
            continue
        issues.append(f"navigation points outside /{lang}/: {href}")
    return issues


def check_navigation_parity(urls: list[str]) -> list[str]:
    soups = {}
    signatures = {}
    for url in urls:
        html_path, lang, canonical_path = file_for_url(url)
        if not html_path.exists():
            continue
        soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), HTML_PARSER)
        soups[url] = soup
        if canonical_path == "/":
            signatures[lang] = navigation_signature(soup)

    issues = []
    for url, soup in soups.items():
        _, lang, _ = file_for_url(url)
        expected = signatures.get(lang)
        actual = navigation_signature(soup)
        if expected is None:
            issues.append(f"{url}: missing {lang} home navigation baseline")
            continue
        mismatches = [
            component
            for component in (
                "desktop",
                "mobile",
                "mobile_groups",
                "footer_services",
                "footer_company",
            )
            if actual[component] != expected[component]
        ]
        if mismatches:
            issues.append(
                f"{url}: navigation parity mismatch in {', '.join(mismatches)}"
            )
        for issue in check_navigation_link_locality(soup, lang):
            issues.append(f"{url}: {issue}")
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
    elif not schema_has_entity_type(jsonld_blocks, "BreadcrumbList"):
        issues.append("missing BreadcrumbList JSON-LD entity")
    issues.extend(check_jsonld_localized_urls(jsonld_blocks, lang))
    issues.extend(check_jsonld_assets(jsonld_blocks, html_path))

    issues.extend(check_i18n_html_prerender(soup, lang))
    issues.extend(check_internal_links(soup, lang))
    issues.extend(check_local_assets(soup, html_path))
    issues.extend(check_asset_cache_bust_presence(soup))
    issues.extend(check_lcp_image_delivery(soup))
    _, css_hero_issues = check_css_hero_preload_alignment(soup)
    issues.extend(css_hero_issues)
    _, picture_hero_issues = check_picture_hero_preload_alignment(soup)
    issues.extend(picture_hero_issues)
    return [f"{url}: {issue}" for issue in issues]


def validate_css_hero_preloads(urls: list[str]) -> tuple[int, list[str]]:
    checked = 0
    issues = []
    for url in urls:
        html_path, _, _ = file_for_url(url)
        if not html_path.exists():
            continue
        soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), HTML_PARSER)
        is_css_hero, page_issues = check_css_hero_preload_alignment(soup)
        if is_css_hero:
            checked += 1
        issues.extend(f"{url}: {issue}" for issue in page_issues)
    return checked, issues


def validate_picture_hero_preloads(urls: list[str]) -> tuple[int, list[str]]:
    checked = 0
    issues = []
    for url in urls:
        html_path, _, _ = file_for_url(url)
        if not html_path.exists():
            continue
        soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), HTML_PARSER)
        is_picture_hero, page_issues = check_picture_hero_preload_alignment(soup)
        if is_picture_hero:
            checked += 1
        issues.extend(f"{url}: {issue}" for issue in page_issues)
    return checked, issues


def main() -> int:
    urls = sitemap_urls()
    if "--check-css-hero-preloads" in sys.argv[1:]:
        checked, issues = validate_css_hero_preloads(urls)
        if issues:
            print(
                "CSS hero preload validation failed: "
                f"{len(issues)} mismatch(es) across {checked} CSS hero page(s)"
            )
            for issue in issues:
                print(f"  - {issue}")
            return 1
        print(f"CSS hero preload validation passed: {checked} CSS hero page(s)")
        return 0
    if "--check-picture-hero-preloads" in sys.argv[1:]:
        checked, issues = validate_picture_hero_preloads(urls)
        if issues:
            print(
                "Picture hero preload validation failed: "
                f"{len(issues)} mismatch(es) across {checked} picture hero page(s)"
            )
            for issue in issues:
                print(f"  - {issue}")
            return 1
        print(
            "Picture hero preload validation passed: "
            f"{checked} picture hero page(s); "
            "390px/DPR3, 390px/DPR2, 768px/DPR2, "
            "1280px/DPR1, 1440px/DPR1"
        )
        return 0
    issues = []
    for url in urls:
        issues.extend(validate_page(url))
    issues.extend(check_llms_sitemap_coverage(urls))
    issues.extend(check_codex_changelog())
    issues.extend(check_navigation_parity(urls))
    issues.extend(check_chrome_text_parity(urls))
    issues.extend(check_asset_cache_bust_consistency(urls))
    if issues:
        print(f"SEO validation failed: {len(issues)} issue(s)")
        for issue in issues:
            print(f"  - {issue}")
        return 1
    print(f"SEO validation passed: {len(urls)} sitemap URL(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
