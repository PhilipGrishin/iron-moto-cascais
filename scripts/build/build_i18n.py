#!/usr/bin/env python3
"""
Generate language variants of HTML pages for Iron Custom Motors.

Produces /ru/<path>/, /uk/<path>/, /pt/<path>/ for every English page,
each fully pre-rendered (Google + AI engines see correct content per URL).

Also adds proper hreflang block to every page.
"""

import json
import re
import shutil
from pathlib import Path
from copy import deepcopy

from bs4 import BeautifulSoup, FeatureNotFound, NavigableString

from page_meta import PAGE_META, PROJECT_NAMES, OG_LOCALES

# --------- Paths ---------
SITE_ROOT = Path(__file__).resolve().parents[2]
BUILD_DIR = Path(__file__).resolve().parent
DOMAIN = "https://ironcustommotors.com"
LANGS = ["en", "ru", "uk", "pt"]
TARGET_LANGS = ["ru", "uk", "pt"]  # generate these from EN source
LOCALIZED_URL_SKIP_PREFIXES = (
    f"{DOMAIN}/assets/",
    f"{DOMAIN}/photos/",
    f"{DOMAIN}/pricing/files/",
    f"{DOMAIN}/worker/",
)
GLOBAL_SCHEMA_IDS = {
    f"{DOMAIN}/#business",
    f"{DOMAIN}/#website",
}

try:
    BeautifulSoup("", "lxml")
    HTML_PARSER = "lxml"
except FeatureNotFound:
    HTML_PARSER = "html.parser"

# Pages to translate: (source_path_relative_to_site_root, page_id)
MAIN_PAGES = [
    ("index.html", ""),
    ("motorcycle-service/index.html", "motorcycle-service"),
    ("parts/index.html", "parts"),
    ("upgrades-tuning/index.html", "upgrades-tuning"),
    ("custom/index.html", "custom"),
    ("pre-purchase-inspection/index.html", "pre-purchase-inspection"),
    # pricing is handled by build_pricing.py (it has its own per-language generator)
    ("services/index.html", "services"),
    ("projects/index.html", "projects"),
    ("about/index.html", "about"),
    ("contact/index.html", "contact"),
    ("faq/index.html", "faq"),
    ("bmw-service/index.html", "bmw-service"),
    ("harley-service/index.html", "harley-service"),
    ("ducati-service/index.html", "ducati-service"),
    ("news/index.html", "news"),
    ("news/opens-new-workshop-in-cascais/index.html", "news/opens-new-workshop-in-cascais"),
    ("news/lisbon-motorcycle-film-fest-2026-beckman/index.html", "news/lisbon-motorcycle-film-fest-2026-beckman"),
]

# Project pages — handled separately because they have inline ICM_I18N_PAGE
PROJECT_PAGES = [(f"projects/{name}/index.html", name) for name in PROJECT_NAMES]


# --------- Load main I18N ---------
I18N = json.loads((BUILD_DIR / "i18n.json").read_text(encoding="utf-8"))


# --------- Helpers ---------

def make_hreflang_block(soup, page_id, project_name=None):
    """Build hreflang link tags pointing to all 4 language versions of this page."""
    # Path part after lang prefix (no leading slash, trailing slash)
    if project_name:
        path = f"projects/{project_name}/"
    elif page_id == "":
        path = ""
    else:
        path = f"{page_id}/"

    def url_for(lang):
        if lang == "en":
            return f"{DOMAIN}/{path}"
        return f"{DOMAIN}/{lang}/{path}"

    tags = []
    for lang in LANGS:
        tag = soup.new_tag("link")
        tag.attrs["rel"] = "alternate"
        tag.attrs["hreflang"] = lang
        tag.attrs["href"] = url_for(lang)
        tags.append(tag)
    # x-default points to English (default)
    xd = soup.new_tag("link")
    xd.attrs["rel"] = "alternate"
    xd.attrs["hreflang"] = "x-default"
    xd.attrs["href"] = url_for("en")
    tags.append(xd)
    return tags


def parse_html(markup: str) -> BeautifulSoup:
    return BeautifulSoup(markup, HTML_PARSER)


def replace_element_html(el, html_fragment: str):
    """Replace element contents with a translated HTML fragment."""
    fragment_soup = parse_html(html_fragment)
    container = fragment_soup.body or fragment_soup
    el.clear()
    for child in list(container.children):
        el.append(child)


def normalize_h1_break_spacing(soup):
    """Keep h1 textContent readable when visual line breaks split words."""
    for h1 in soup.find_all("h1"):
        for br in h1.find_all("br"):
            prev = br.previous_sibling
            if prev is None:
                continue
            prev_text = prev.get_text() if hasattr(prev, "get_text") else str(prev)
            if prev_text and not prev_text[-1].isspace():
                br.insert_before(NavigableString(" "))


def localize_schema_url(value: str, lang: str) -> str:
    """Localize site URLs inside JSON-LD while preserving global IDs and assets."""
    if lang == "en" or not isinstance(value, str):
        return value
    if value in GLOBAL_SCHEMA_IDS:
        return value
    if value == f"{DOMAIN}/#projects":
        return f"{DOMAIN}/{lang}/projects/"
    if value == f"{DOMAIN}/#reviews":
        return f"{DOMAIN}/{lang}/#reviews"
    if value == f"{DOMAIN}/":
        return f"{DOMAIN}/{lang}/"
    if any(value.startswith(prefix) for prefix in LOCALIZED_URL_SKIP_PREFIXES):
        return value
    if value.startswith(f"{DOMAIN}/{lang}/"):
        return value
    if any(value.startswith(f"{DOMAIN}/{other}/") for other in TARGET_LANGS):
        return value
    if value.startswith(f"{DOMAIN}/"):
        return value.replace(f"{DOMAIN}/", f"{DOMAIN}/{lang}/", 1)
    return value


def localize_jsonld_value(value, lang: str):
    if isinstance(value, dict):
        return {key: localize_jsonld_value(val, lang) for key, val in value.items()}
    if isinstance(value, list):
        return [localize_jsonld_value(item, lang) for item in value]
    if isinstance(value, str):
        return localize_schema_url(value, lang)
    return value


def localize_jsonld_blocks(soup, lang: str):
    """Update URL-like strings in JSON-LD blocks for localized pages."""
    for script in soup.find_all("script", attrs={"type": "application/ld+json"}):
        raw = script.string or script.get_text()
        if not raw.strip():
            continue
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            continue
        localized = localize_jsonld_value(data, lang)
        script.string = json.dumps(localized, ensure_ascii=False, separators=(",", ":"))


def absolutize_paths(soup):
    """Convert relative paths (../foo, ./foo) in head links/scripts to absolute /foo.
    Required so a page at /ru/motorcycle-service/ correctly resolves /photos, /assets."""
    for tag_name, attr in [("link", "href"), ("script", "src"), ("img", "src")]:
        for el in soup.find_all(tag_name):
            v = el.get(attr)
            if not v:
                continue
            if v.startswith(("../", "./")):
                # Replace leading ../ or ./ with /
                stripped = re.sub(r"^(\.\./)+|^\./", "", v)
                el[attr] = "/" + stripped


def remove_existing_hreflang(soup):
    for el in soup.head.find_all("link", attrs={"rel": "alternate", "hreflang": True}):
        el.decompose()


def upsert_meta(soup, *, prop=None, name=None, content):
    """Find <meta property=... or name=...> and update its content, or create."""
    sel = {}
    if prop is not None:
        sel = {"property": prop}
    elif name is not None:
        sel = {"name": name}
    el = soup.head.find("meta", attrs=sel)
    if el is None:
        el = soup.new_tag("meta")
        if prop is not None:
            el.attrs["property"] = prop
        if name is not None:
            el.attrs["name"] = name
        soup.head.append(el)
    el.attrs["content"] = content


def localize_page(en_html: str, lang: str, page_id: str, *, project_name=None) -> str:
    """Take English HTML, produce a fully translated version for `lang`."""
    soup = parse_html(en_html)

    # 1. html lang attribute
    html = soup.find("html")
    if html is not None:
        html["lang"] = lang
        html["data-lang"] = lang

    # 2. Absolutize relative paths so the page works at /lang/path/
    absolutize_paths(soup)

    # 3. Translate elements with data-i18n / data-i18n-html
    page_dict = I18N.get(lang, {})
    extra_dict = {}
    # ALL pages may have an inline ICM_I18N_PAGE (sub-page-specific translations)
    for script in soup.find_all("script"):
        txt = script.string or ""
        m = re.search(r"window\.ICM_I18N_PAGE\s*=\s*(\{.*?\});", txt, re.DOTALL)
        if m:
            try:
                proj_i18n = json.loads(m.group(1))
                extra_dict = proj_i18n.get(lang, {})
                break
            except json.JSONDecodeError:
                pass

    full_dict = {**page_dict, **extra_dict}  # page-specific keys override common ones

    for el in soup.find_all(attrs={"data-i18n": True}):
        key = el["data-i18n"]
        if key in full_dict:
            replace_element_html(el, full_dict[key])

    for el in soup.find_all(attrs={"data-i18n-html": True}):
        key = el["data-i18n-html"]
        if key in full_dict:
            replace_element_html(el, full_dict[key])

    # 4. Update title / description / OG / Twitter / canonical
    meta = PAGE_META.get(page_id, {}).get(lang, {})
    base_path = "" if page_id == "" else f"{page_id}/"
    if project_name:
        base_path = f"projects/{project_name}/"

    canonical_url = f"{DOMAIN}/{lang}/{base_path}" if lang != "en" else f"{DOMAIN}/{base_path}"

    # Title
    if "title" in meta:
        title_el = soup.title
        if title_el is None:
            title_el = soup.new_tag("title")
            soup.head.append(title_el)
        title_el.string = meta["title"]
    elif project_name:
        # Build title from project badge translation
        badge = extra_dict.get(f"proj.{project_name.replace('-', '_').replace('_', '-')}.badge", "")
        # Try both dash-form and underscore-form keys
        if not badge:
            badge_key = f"proj.{project_name}.badge"
            badge = extra_dict.get(badge_key, "")
        name = extra_dict.get(f"proj.{project_name}.name", project_name.title())
        if badge:
            title_text = f"{name} — {badge} | Iron Custom Motors"
        else:
            title_text = f"{name} | Iron Custom Motors"
        title_el = soup.title
        if title_el is None:
            title_el = soup.new_tag("title")
            soup.head.append(title_el)
        title_el.string = title_text
        meta = {"title": title_text}

    description = meta.get("description")
    if project_name and not description:
        # Use project tag translation as description
        description = extra_dict.get(f"proj.{project_name}.tag", "")
        # Pad to 140-160 chars with a localized brand tail for SEO
        BRAND_TAIL = {
            "en": "Custom build by Iron Custom Motors — Cascais workshop, Greater Lisbon.",
            "ru": "Кастом-сборка Iron Custom Motors — мастерская в Кашкайше, Большой Лиссабон.",
            "uk": "Кастом-збірка Iron Custom Motors — майстерня у Кашкайші, Великий Лісабон.",
            "pt": "Build custom da Iron Custom Motors — oficina em Cascais, Grande Lisboa.",
        }
        if description and len(description) < 140:
            tail = BRAND_TAIL.get(lang, BRAND_TAIL["en"])
            # Ensure tag ends with punctuation before concatenating
            sep = "" if description.endswith((".","!","?")) else "."
            description = f"{description}{sep} {tail}"
    if description:
        upsert_meta(soup, name="description", content=description)

    # OG
    og_title = meta.get("title", "")
    if og_title:
        upsert_meta(soup, prop="og:title", content=og_title)
    og_desc = meta.get("og_description") or description
    if og_desc:
        upsert_meta(soup, prop="og:description", content=og_desc)
    upsert_meta(soup, prop="og:url", content=canonical_url)
    upsert_meta(soup, prop="og:locale", content=OG_LOCALES[lang])

    # Twitter
    tw_title = meta.get("title", "")
    if tw_title:
        upsert_meta(soup, name="twitter:title", content=tw_title)
    tw_desc = meta.get("twitter_description") or og_desc or description
    if tw_desc:
        upsert_meta(soup, name="twitter:description", content=tw_desc)

    # Canonical
    can_el = soup.head.find("link", attrs={"rel": "canonical"})
    if can_el is None:
        can_el = soup.new_tag("link")
        can_el.attrs["rel"] = "canonical"
        soup.head.append(can_el)
    can_el["href"] = canonical_url

    # 5. Replace hreflang block
    remove_existing_hreflang(soup)
    for tag in make_hreflang_block(soup, page_id, project_name):
        soup.head.append(tag)

    # 6. Localize JSON-LD URLs so structured data matches the current URL.
    localize_jsonld_blocks(soup, lang)

    # 7. Make h1 textContent readable for crawlers and assistive tech.
    normalize_h1_break_spacing(soup)

    # 8. Optional: update og:locale:alternate entries for English locale
    # (kept on home page only — handled via upsert above)

    return str(soup)


def update_en_page(en_html: str, page_id: str, project_name=None) -> str:
    """For English source page: only update hreflang block & ensure canonical points to root."""
    soup = parse_html(en_html)
    remove_existing_hreflang(soup)
    for tag in make_hreflang_block(soup, page_id, project_name):
        soup.head.append(tag)
    normalize_h1_break_spacing(soup)
    # Also ensure og:locale:alternate covers all langs (for home page)
    if page_id == "" and project_name is None:
        # Remove existing alternates and add fresh
        for el in soup.head.find_all("meta", attrs={"property": "og:locale:alternate"}):
            el.decompose()
        for lang in ["ru", "uk", "pt"]:
            t = soup.new_tag("meta")
            t.attrs["property"] = "og:locale:alternate"
            t.attrs["content"] = OG_LOCALES[lang]
            soup.head.append(t)
    return str(soup)


def write_localized(out_path: Path, content: str):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(content, encoding="utf-8")


# --------- Main run ---------

def main():
    output_pairs = []  # (target_path, content)

    all_pages = MAIN_PAGES + PROJECT_PAGES

    for source_rel, page_id in all_pages:
        src = SITE_ROOT / source_rel
        if not src.exists():
            print(f"SKIP (missing): {source_rel}")
            continue

        en_html = src.read_text(encoding="utf-8")
        # is_project = an individual project page like projects/inspirium/...
        # NOT the projects/ gallery index itself (page_id == "projects")
        is_project = source_rel.startswith("projects/") and page_id in PROJECT_NAMES
        project_name = page_id if is_project else None

        # Localized versions
        for lang in TARGET_LANGS:
            translated = localize_page(en_html, lang, page_id, project_name=project_name)
            # Path: <lang>/<page>/index.html ; for home it's <lang>/index.html
            if is_project:
                out = SITE_ROOT / lang / "projects" / project_name / "index.html"
            elif page_id == "":
                out = SITE_ROOT / lang / "index.html"
            else:
                out = SITE_ROOT / lang / page_id / "index.html"
            output_pairs.append((out, translated))

        # Update English source: hreflang block
        updated_en = update_en_page(en_html, page_id, project_name=project_name)
        output_pairs.append((src, updated_en))

    # Write everything
    for path, content in output_pairs:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        rel = path.relative_to(SITE_ROOT)
        print(f"wrote {rel}  ({len(content):,} bytes)")

    print(f"\n--- Done. Wrote {len(output_pairs)} files. ---")


if __name__ == "__main__":
    main()
