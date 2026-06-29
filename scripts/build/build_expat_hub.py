#!/usr/bin/env python3
"""Build the localized English-speaking workshop expat hub pages."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

from bs4 import BeautifulSoup

from brand_pages_data import BRAND_ORDER
from hero_images import hero_preload_links, optimized_hero_url
from nav_patch import (
    DROPDOWN_NAV_LINKS,
    FOOTER_COMPANY_LINKS,
    FOOTER_SERVICES_LINKS,
    PRIMARY_NAV_LINKS,
)

SITE_ROOT = Path(__file__).resolve().parents[2]
BUILD_DIR = Path(__file__).resolve().parent
DOMAIN = "https://ironcustommotors.com"
COPY_FILE = BUILD_DIR / "content" / "expat_hub_copy_4lang.md"
I18N_FILE = BUILD_DIR / "i18n.json"
HERO_IMAGE = "photos/services/english-speaking-motorcycle-workshop-main.jpg"

LANGS = ("en", "ru", "uk", "pt")
HREFLANG_CODES = {"en": "en", "ru": "ru", "uk": "uk", "pt": "pt-PT"}
PATHS = {
    "en": "/english-speaking-motorcycle-workshop/",
    "ru": "/ru/english-speaking-motorcycle-workshop/",
    "uk": "/uk/english-speaking-motorcycle-workshop/",
    "pt": "/pt/english-speaking-motorcycle-workshop/",
}

COMMON_LOCALIZED_PATHS = {
    "/",
    "/motorcycle-service/",
    "/parts/",
    "/upgrades-tuning/",
    "/custom/",
    "/authorized-dealer/",
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
    "/english-speaking-motorcycle-workshop/",
    *[f"/{slug}/" for slug in BRAND_ORDER],
    "/blog/",
    "/news/",
}

TYRE_PATH_BY_REST = {
    "/motorcycle-tyre-service/": {
        "en": "/motorcycle-tyre-service/",
        "ru": "/ru/shinomontazh-mototsiklov/",
        "uk": "/uk/shynomontazh-mototsykliv/",
        "pt": "/pt/montagem-de-pneus-mota/",
    },
    "/shinomontazh-mototsiklov/": {
        "en": "/motorcycle-tyre-service/",
        "ru": "/ru/shinomontazh-mototsiklov/",
        "uk": "/uk/shynomontazh-mototsykliv/",
        "pt": "/pt/montagem-de-pneus-mota/",
    },
    "/shynomontazh-mototsykliv/": {
        "en": "/motorcycle-tyre-service/",
        "ru": "/ru/shinomontazh-mototsiklov/",
        "uk": "/uk/shynomontazh-mototsykliv/",
        "pt": "/pt/montagem-de-pneus-mota/",
    },
    "/montagem-de-pneus-mota/": {
        "en": "/motorcycle-tyre-service/",
        "ru": "/ru/shinomontazh-mototsiklov/",
        "uk": "/uk/shynomontazh-mototsykliv/",
        "pt": "/pt/montagem-de-pneus-mota/",
    },
}

UI = {
    "en": {
        "home": "Home",
        "crumb": "English-speaking workshop",
        "faq": "FAQ",
        "area": "Local area",
    },
    "ru": {
        "home": "Главная",
        "crumb": "Англоязычная мастерская",
        "faq": "FAQ",
        "area": "Локация",
    },
    "uk": {
        "home": "Головна",
        "crumb": "Англомовна майстерня",
        "faq": "FAQ",
        "area": "Локація",
    },
    "pt": {
        "home": "Início",
        "crumb": "Oficina que fala inglês",
        "faq": "FAQ",
        "area": "Zona local",
    },
}


def detect_cache_bust() -> str:
    text = (SITE_ROOT / "index.html").read_text(encoding="utf-8")
    match = re.search(r"/assets/main\.css\?v=([a-zA-Z0-9]+)", text)
    return match.group(1) if match else "20260629c"


CACHE_BUST = detect_cache_bust()
GLOBAL_I18N = json.loads(I18N_FILE.read_text(encoding="utf-8"))


def canonical_url(lang: str) -> str:
    return DOMAIN + PATHS[lang]


def output_path(lang: str) -> Path:
    rel = PATHS[lang].strip("/")
    return SITE_ROOT / rel / "index.html"


def localized_path_for(base_path: str, lang: str) -> str:
    if base_path in TYRE_PATH_BY_REST:
        return TYRE_PATH_BY_REST[base_path][lang]
    if re.match(r"^/(ru|uk|pt)(/|$)", base_path):
        return base_path
    if lang == "en":
        return base_path
    if base_path == "/":
        return f"/{lang}/"
    if (
        base_path in COMMON_LOCALIZED_PATHS
        or base_path.startswith("/projects/")
        or base_path.startswith("/blog/")
        or base_path.startswith("/news/")
    ):
        return f"/{lang}{base_path}"
    return base_path


def localized_href(href: str, lang: str) -> str:
    if not href or href.startswith(("mailto:", "tel:", "#", "javascript:")):
        return href
    if href.startswith(("http://", "https://")):
        parsed = urlsplit(href)
        if parsed.netloc not in ("ironcustommotors.com", "www.ironcustommotors.com"):
            return href
        localized = localized_path_for(parsed.path or "/", lang)
        return urlunsplit((parsed.scheme, parsed.netloc, localized, parsed.query, parsed.fragment))
    if href.startswith(("/assets/", "/photos/", "/worker/", "/pricing/files/")):
        return href
    parsed = urlsplit(href)
    localized = localized_path_for(parsed.path or "/", lang)
    return urlunsplit(("", "", localized, parsed.query, parsed.fragment))


def label_for(key: str | None, lang: str, fallback: str) -> str:
    if not key:
        return fallback
    return GLOBAL_I18N.get(lang, {}).get(key) or GLOBAL_I18N["en"].get(key) or fallback


def render_nav_link(key: str | None, href: str, fallback: str, lang: str) -> str:
    label = html.escape(label_for(key, lang, fallback), quote=False)
    i18n = f' data-i18n="{key}"' if key else ""
    return f'<a{i18n} href="{localized_href(href, lang)}">{label}</a>'


def render_dropdown(
    key: str,
    href: str,
    fallback: str,
    links: list[tuple[str | None, str, str]],
    lang: str,
) -> str:
    label = html.escape(label_for(key, lang, fallback), quote=False)
    items = "\n".join(
        render_nav_link(item_key, item_href, item_fallback, lang)
        for item_key, item_href, item_fallback in links
    )
    return (
        '<div class="nav-dropdown">\n'
        f'<a aria-haspopup="true" class="nav-dropdown-trigger" data-i18n="{key}" href="{localized_href(href, lang)}">{label}</a>\n'
        f'<div aria-label="{label}" class="nav-dropdown-menu">\n{items}\n</div>\n'
        "</div>"
    )


def render_primary_nav(lang: str) -> str:
    parts = []
    for key, href, fallback in PRIMARY_NAV_LINKS:
        links = DROPDOWN_NAV_LINKS.get(key)
        parts.append(
            render_dropdown(key, href, fallback, links, lang)
            if links
            else render_nav_link(key, href, fallback, lang)
        )
    return '<nav aria-label="Primary" class="nav">\n' + "\n".join(parts) + "\n</nav>"


def render_mobile_nav(lang: str) -> str:
    parts = []
    for key, href, fallback in PRIMARY_NAV_LINKS:
        links = DROPDOWN_NAV_LINKS.get(key)
        if links:
            items = "\n".join(
                render_nav_link(item_key, item_href, item_fallback, lang)
                for item_key, item_href, item_fallback in links
            )
            parts.append(
                '<details class="mobile-nav-group">\n'
                f'<summary class="mobile-nav-summary"><span data-i18n="{key}">{html.escape(label_for(key, lang, fallback), quote=False)}</span></summary>\n'
                f'<div class="mobile-subnav">\n{items}\n</div>\n'
                "</details>"
            )
        else:
            parts.append(render_nav_link(key, href, fallback, lang))
    return '<nav class="nav-mobile">\n' + "\n".join(parts) + "\n</nav>"


def render_footer_links(items: list[tuple[str, str, str]], lang: str) -> str:
    return (
        "<ul>\n"
        + "\n".join(
            f"<li>{render_nav_link(key, href, fallback, lang)}</li>"
            for key, href, fallback in items
        )
        + "\n</ul>"
    )


def apply_i18n(soup: BeautifulSoup, lang: str) -> None:
    dictionary = GLOBAL_I18N.get(lang, GLOBAL_I18N["en"])
    for element in soup.select("[data-i18n], [data-i18n-html]"):
        key = element.get("data-i18n") or element.get("data-i18n-html")
        if key in dictionary:
            element.clear()
            fragment = BeautifulSoup(dictionary[key], "html.parser")
            for child in list(fragment.contents):
                element.append(child)


def rewrite_chrome_links(soup: BeautifulSoup, lang: str) -> None:
    for anchor in soup.find_all("a", href=True):
        anchor["href"] = localized_href(anchor["href"], lang)
    for button in soup.select("button[data-lang]"):
        if button.get("data-lang") == lang:
            button["aria-current"] = "true"
        elif button.has_attr("aria-current"):
            del button["aria-current"]


def chrome_fragments(lang: str) -> tuple[str, str]:
    soup = BeautifulSoup((SITE_ROOT / "index.html").read_text(encoding="utf-8"), "html.parser")

    primary = soup.find("nav", attrs={"aria-label": "Primary"})
    if primary:
        primary.replace_with(BeautifulSoup(render_primary_nav(lang), "html.parser").nav)
    mobile = soup.find("nav", class_="nav-mobile")
    if mobile:
        mobile.replace_with(BeautifulSoup(render_mobile_nav(lang), "html.parser").nav)

    for col in soup.find_all("div", class_="footer-col"):
        h5 = col.find("h5")
        if not h5:
            continue
        if h5.get("data-i18n") == "footer.col1":
            ul = col.find("ul")
            if ul:
                ul.replace_with(BeautifulSoup(render_footer_links(FOOTER_SERVICES_LINKS, lang), "html.parser").ul)
        elif h5.get("data-i18n") == "footer.col2":
            ul = col.find("ul")
            if ul:
                ul.replace_with(BeautifulSoup(render_footer_links(FOOTER_COMPANY_LINKS, lang), "html.parser").ul)

    apply_i18n(soup, lang)
    rewrite_chrome_links(soup, lang)

    before_selectors = ["#loader", "#cookieBanner", "#stickyCta", ".fab-wa", "header.site-header", "#mobileDrawer"]
    after_selectors = ["footer.site-footer", "#contactModal"]
    before = "\n".join(str(soup.select_one(selector)) for selector in before_selectors if soup.select_one(selector))
    after = "\n".join(str(soup.select_one(selector)) for selector in after_selectors if soup.select_one(selector))
    after += f'\n<script defer="" src="/assets/main.js?v={CACHE_BUST}"></script>'
    return before, after


def split_language_blocks(markdown: str) -> dict[str, str]:
    header_to_lang = {
        "ENGLISH": "en",
        "PORTUGUÊS (pt-PT)": "pt",
        "РУССКИЙ": "ru",
        "УКРАЇНСЬКА": "uk",
    }
    matches = list(re.finditer(r"^###\s+──\s+(.+?)\s+──\s*$", markdown, flags=re.MULTILINE))
    blocks: dict[str, str] = {}
    for index, match in enumerate(matches):
        title = match.group(1).strip()
        lang = header_to_lang.get(title)
        if not lang:
            continue
        end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        blocks[lang] = markdown[match.end():end].strip()
    missing = set(LANGS) - set(blocks)
    if missing:
        raise ValueError(f"Missing copy blocks: {', '.join(sorted(missing))}")
    return blocks


def extract_field(block: str, label: str) -> str:
    match = re.search(rf"^\*\*{re.escape(label)}:\*\*\s*(.+?)\s*$", block, flags=re.MULTILINE)
    if not match:
        raise ValueError(f"Missing field: {label}")
    return match.group(1).strip().strip("`")


def extract_hero_alt(block: str) -> str:
    match = re.search(r"^\`\[IMAGE:.+?\]\`\s+·\s+ALT:\s*(.+?)\s*$", block, flags=re.MULTILINE)
    if not match:
        raise ValueError("Missing hero ALT")
    return match.group(1).strip().strip('"').strip("«»")


def extract_hero(block: str) -> str:
    lines = block.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("**") and "hero" in line.lower():
            match = re.match(r"^\*\*.+?\*\*\s*(.*)$", line)
            body = [match.group(1).strip()] if match and match.group(1).strip() else []
            for next_line in lines[index + 1:]:
                if next_line.startswith("**## "):
                    break
                body.append(next_line.rstrip())
            return "\n".join(body).strip()
    raise ValueError("Missing hero intro")


def section_kind(title: str) -> str:
    lowered = title.lower()
    if "faq" in lowered:
        return "faq"
    if "cta" in lowered or "локация" in lowered or "локація" in lowered or "zona local" in lowered:
        return "cta"
    return "standard"


def extract_sections(block: str) -> list[dict[str, str]]:
    matches = list(re.finditer(r"^\*\*##\s+(.+?)\*\*\s*(.*?)\s*$", block, flags=re.MULTILINE))
    sections: list[dict[str, str]] = []
    for index, match in enumerate(matches):
        title = match.group(1).strip()
        trailing = match.group(2).strip()
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(block)
        raw_body = block[start:end].strip()
        if trailing:
            raw_body = f"{trailing}\n{raw_body}".strip()
        raw_body = re.split(r"^---\s*$", raw_body, maxsplit=1, flags=re.MULTILINE)[0].strip()
        sections.append({"title": title, "body": raw_body, "kind": section_kind(title)})
    if len(sections) != 8:
        raise ValueError(f"Expected 8 content sections, got {len(sections)}")
    return sections


def extract_faq_items(section: dict[str, str]) -> list[dict[str, str]]:
    items = []
    for line in section["body"].splitlines():
        line = line.strip()
        if not line:
            continue
        match = re.match(r"- \*\*(.+?)\*\*\s+(.+)$", line)
        if match:
            items.append({"question": match.group(1).strip(), "answer": match.group(2).strip()})
    if len(items) != 6:
        raise ValueError(f"Expected 6 FAQ items, got {len(items)}")
    return items


def parse_copy() -> dict[str, dict]:
    blocks = split_language_blocks(COPY_FILE.read_text(encoding="utf-8"))
    content: dict[str, dict] = {}
    for lang, block in blocks.items():
        sections = extract_sections(block)
        faq_sections = [section for section in sections if section["kind"] == "faq"]
        if len(faq_sections) != 1:
            raise ValueError(f"{lang}: expected one FAQ section, got {len(faq_sections)}")
        content[lang] = {
            "seo_title": extract_field(block, "SEO Title"),
            "meta_description": extract_field(block, "Meta"),
            "slug": extract_field(block, "Slug"),
            "eyebrow": extract_field(block, "Eyebrow"),
            "h1": extract_field(block, "H1"),
            "hero_alt": extract_hero_alt(block),
            "hero": extract_hero(block),
            "sections": sections,
            "faq": extract_faq_items(faq_sections[0]),
        }
        if content[lang]["slug"] != PATHS[lang]:
            raise ValueError(f"{lang} slug mismatch: {content[lang]['slug']} != {PATHS[lang]}")
    return content


def inline_markdown(text: str, lang: str) -> str:
    def apply_bold(segment: str) -> str:
        parts = re.split(r"(\*\*.+?\*\*)", segment)
        out = []
        for part in parts:
            if part.startswith("**") and part.endswith("**"):
                out.append(f"<strong>{html.escape(part[2:-2], quote=False)}</strong>")
            else:
                out.append(html.escape(part, quote=False))
        return "".join(out)

    result = []
    pos = 0
    for match in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", text):
        result.append(apply_bold(text[pos:match.start()]))
        label = apply_bold(match.group(1))
        href = html.escape(localized_href(match.group(2), lang), quote=True)
        target = ' target="_blank" rel="noopener"' if href.startswith("http") and "ironcustommotors.com" not in href else ""
        result.append(f'<a href="{href}"{target}>{label}</a>')
        pos = match.end()
    result.append(apply_bold(text[pos:]))
    return "".join(result)


def render_list_item(line: str, lang: str) -> str:
    body = line[2:].strip()
    return f"<li>{inline_markdown(body, lang)}</li>"


def render_flow(markdown: str, lang: str) -> str:
    out = []
    list_items = []

    def flush_list() -> None:
        nonlocal list_items
        if list_items:
            out.append("<ul>\n" + "\n".join(render_list_item(item, lang) for item in list_items) + "\n</ul>")
            list_items = []

    for raw_line in markdown.splitlines():
        line = raw_line.strip()
        if not line:
            flush_list()
            continue
        if line.startswith("- "):
            list_items.append(line)
            continue
        flush_list()
        cls = ' class="expat-linkline"' if line.startswith("[") else ""
        out.append(f"<p{cls}>{inline_markdown(line, lang)}</p>")
    flush_list()
    return "\n".join(out)


def render_standard_section(section: dict[str, str], lang: str, index: int) -> str:
    return f"""
<section class="expat-section" id="section-{index:02d}">
<div class="container expat-section-grid">
<div class="expat-section-head">
<span class="h-eyebrow">{index:02d}</span>
<h2>{html.escape(section["title"], quote=False)}</h2>
</div>
<div class="expat-copy">
{render_flow(section["body"], lang)}
</div>
</div>
</section>"""


def render_faq(section: dict[str, str], lang: str) -> str:
    items = []
    for item in extract_faq_items(section):
        items.append(
            f"""
<details class="expat-faq-item">
<summary>{inline_markdown(item["question"], lang)}</summary>
<div class="answer">{render_flow(item["answer"], lang)}</div>
</details>"""
        )
    return f"""
<section class="expat-section expat-faq" id="faq">
<div class="container expat-section-grid">
<div class="expat-section-head">
<span class="h-eyebrow">{html.escape(UI[lang]["faq"], quote=False)}</span>
<h2>{html.escape(section["title"], quote=False)}</h2>
</div>
<div class="expat-faq-list">
{''.join(items)}
</div>
</div>
</section>"""


def render_cta(section: dict[str, str], lang: str) -> str:
    return f"""
<section class="expat-cta" id="local-area">
<div class="container">
<span class="h-eyebrow">{html.escape(UI[lang]["area"], quote=False)}</span>
<h2>{html.escape(section["title"], quote=False)}</h2>
<div class="expat-cta-copy">
{render_flow(section["body"], lang)}
</div>
</div>
</section>"""


def render_sections(sections: list[dict[str, str]], lang: str) -> str:
    html_parts = []
    standard_index = 1
    for section in sections:
        if section["kind"] == "faq":
            html_parts.append(render_faq(section, lang))
        elif section["kind"] == "cta":
            html_parts.append(render_cta(section, lang))
        else:
            html_parts.append(render_standard_section(section, lang, standard_index))
            standard_index += 1
    return "\n".join(html_parts)


def hero_picture(content: dict) -> str:
    source_url = "/" + HERO_IMAGE
    avif_srcset = ", ".join(
        f"{optimized_hero_url(source_url, width, 'avif')} {width}w" for width in (768, 1280, 1920)
    )
    webp_srcset = ", ".join(
        f"{optimized_hero_url(source_url, width, 'webp')} {width}w" for width in (768, 1280, 1920)
    )
    jpg_srcset = ", ".join(
        f"{optimized_hero_url(source_url, width, 'jpg')} {width}w" for width in (768, 1280, 1920)
    )
    fallback = optimized_hero_url(source_url, 1280, "jpg")
    alt = html.escape(content["hero_alt"], quote=True)
    return f"""
<picture class="expat-hero-media">
<source sizes="100vw" srcset="{avif_srcset}" type="image/avif"/>
<source sizes="100vw" srcset="{webp_srcset}" type="image/webp"/>
<img alt="{alt}" decoding="sync" fetchpriority="high" height="960" loading="eager" sizes="100vw" src="{fallback}" srcset="{jpg_srcset}" width="1280"/>
</picture>"""


def json_ld(content: dict, lang: str) -> list[dict]:
    faq_entities = [
        {
            "@type": "Question",
            "name": item["question"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": re.sub(r"\s+", " ", item["answer"]).strip(),
            },
        }
        for item in content["faq"]
    ]
    return [
        {
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "@id": canonical_url(lang) + "#webpage",
            "url": canonical_url(lang),
            "name": content["seo_title"],
            "headline": content["h1"],
            "description": content["meta_description"],
            "inLanguage": HREFLANG_CODES[lang],
            "isPartOf": {"@id": f"{DOMAIN}/#website"},
            "publisher": {"@id": f"{DOMAIN}/#business"},
            "about": {"@id": f"{DOMAIN}/#business"},
            "primaryImageOfPage": {
                "@type": "ImageObject",
                "url": f"{DOMAIN}/{HERO_IMAGE}",
                "caption": content["hero_alt"],
            },
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "@id": canonical_url(lang) + "#faq",
            "mainEntity": faq_entities,
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "@id": canonical_url(lang) + "#breadcrumbs",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": UI[lang]["home"], "item": DOMAIN + localized_href("/", lang)},
                {"@type": "ListItem", "position": 2, "name": UI[lang]["crumb"], "item": canonical_url(lang)},
            ],
        },
    ]


def head_html(content: dict, lang: str) -> str:
    alternates = "\n".join(
        f'<link rel="alternate" hreflang="{HREFLANG_CODES[code]}" href="{canonical_url(code)}"/>' for code in LANGS
    )
    json_scripts = "\n".join(
        f'<script type="application/ld+json">{json.dumps(block, ensure_ascii=False)}</script>' for block in json_ld(content, lang)
    )
    og_locale = {"en": "en_US", "ru": "ru_RU", "uk": "uk_UA", "pt": "pt_PT"}[lang]
    hero_preload = hero_preload_links("/" + HERO_IMAGE)
    return f"""<!DOCTYPE html>
<html data-lang="{lang}" lang="{lang}">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1, viewport-fit=cover" name="viewport"/>
<meta content="#0a0a0a" name="theme-color"/>
<meta content="max-image-preview:large" name="robots"/>
<title>{html.escape(content["seo_title"])}</title>
<meta content="{html.escape(content["meta_description"], quote=True)}" name="description"/>
<meta content="{html.escape(content["seo_title"], quote=True)}" property="og:title"/>
<meta content="{html.escape(content["meta_description"], quote=True)}" property="og:description"/>
<meta content="website" property="og:type"/>
<meta content="{canonical_url(lang)}" property="og:url"/>
<meta content="Iron Custom Motors" property="og:site_name"/>
<meta content="{DOMAIN}/{HERO_IMAGE}" property="og:image"/>
<meta content="{html.escape(content["hero_alt"], quote=True)}" property="og:image:alt"/>
<meta content="{og_locale}" property="og:locale"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="{html.escape(content["seo_title"], quote=True)}" name="twitter:title"/>
<meta content="{html.escape(content["meta_description"], quote=True)}" name="twitter:description"/>
<meta content="{DOMAIN}/{HERO_IMAGE}" name="twitter:image"/>
<meta content="{html.escape(content["hero_alt"], quote=True)}" name="twitter:image:alt"/>
<link href="{canonical_url(lang)}" rel="canonical"/>
{alternates}
<link rel="alternate" hreflang="x-default" href="{canonical_url("en")}"/>
<link href="/photos/favicon.ico" rel="icon" sizes="any"/>
<link href="/photos/favicon-32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="/photos/apple-touch-icon.png" rel="apple-touch-icon" sizes="180x180"/>
<link href="/photos/site.webmanifest" rel="manifest"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Saira:wght@300;400;500;600;700;800;900&amp;family=Saira+Condensed:wght@400;600;700;800;900&amp;family=Roboto+Condensed:wght@400;500;600;700;800;900&amp;family=Inter:wght@300;400;500;600;700&amp;display=swap" rel="stylesheet"/>
{hero_preload}
{json_scripts}
<link href="/assets/main.css?v={CACHE_BUST}" rel="stylesheet"/>
<style>{PAGE_CSS}</style>
</head>"""


def render_page(content: dict, lang: str) -> str:
    before, after = chrome_fragments(lang)
    body = f"""
<body>
{before}
<main>
<section class="expat-hero">
{hero_picture(content)}
<div class="expat-hero-overlay"></div>
<div class="container expat-hero-content">
<div class="crumb"><a href="{localized_href('/', lang)}">{html.escape(UI[lang]["home"], quote=False)}</a><span class="sep">→</span><span>{html.escape(UI[lang]["crumb"], quote=False)}</span></div>
<span class="h-eyebrow">{html.escape(content["eyebrow"], quote=False)}</span>
<h1>{html.escape(content["h1"], quote=False)}</h1>
<div class="expat-hero-lead">
{render_flow(content["hero"], lang)}
</div>
</div>
</section>
{render_sections(content["sections"], lang)}
</main>
{after}
</body>
</html>"""
    return head_html(content, lang) + body


PAGE_CSS = """.expat-hero{position:relative;min-height:82vh;display:flex;align-items:flex-end;isolation:isolate;overflow:hidden;background:#080808;padding:150px 0 84px}
.expat-hero-media{position:absolute;inset:0;z-index:-2;display:block;background:#111}
.expat-hero-media img{width:100%;height:100%;object-fit:cover;object-position:58% 44%;filter:saturate(.94) contrast(1.05) brightness(.72)}
.expat-hero-overlay{position:absolute;inset:0;z-index:-1;background:linear-gradient(90deg,rgba(8,8,8,.94),rgba(8,8,8,.74) 46%,rgba(8,8,8,.24)),linear-gradient(180deg,rgba(8,8,8,.08),#080808 96%)}
.expat-hero-content{position:relative;z-index:1}
.crumb{display:flex;align-items:center;gap:10px;font-family:var(--font-ui);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--text-mute);margin-bottom:24px;flex-wrap:wrap}
.crumb a{color:var(--text-dim);text-decoration:none}
.crumb a:hover{color:var(--accent)}
.crumb .sep{color:var(--accent)}
.expat-hero h1{max-width:min(1040px,80vw,calc(100vw - 40px));margin:18px 0 24px;font-family:var(--font-display);font-size:clamp(34px,4.8vw,72px);font-weight:900;line-height:.88;text-transform:uppercase;color:#fff;overflow-wrap:anywhere}
.expat-hero-lead{max-width:min(900px,76vw,calc(100vw - 40px));font-size:clamp(18px,1.35vw,23px);line-height:1.62;color:var(--text)}
.expat-hero-lead p{margin:0 0 16px}
.expat-section{padding:clamp(58px,7vw,96px) 0;background:#080808;border-top:1px solid var(--border)}
.expat-section:nth-of-type(odd){background:#0b0b0d}
.expat-section-grid{display:grid;grid-template-columns:minmax(190px,.62fr) minmax(0,1.38fr);gap:clamp(28px,5vw,62px);align-items:start}
.expat-section-head{position:sticky;top:105px}
.expat-section-head h2{max-width:min(720px,76vw,calc(100vw - 40px));margin:12px 0 0;font-family:var(--font-display);font-size:clamp(26px,3.5vw,50px);font-weight:900;line-height:.94;text-transform:uppercase;color:#fff;overflow-wrap:anywhere}
.expat-copy{font-size:clamp(17px,1.23vw,20px);line-height:1.68;color:var(--text)}
.expat-copy p,.expat-cta-copy p{margin:0 0 18px;max-width:min(980px,78vw,calc(100vw - 40px));overflow-wrap:break-word}
.expat-copy ul{display:grid;gap:15px;margin:0;padding:0;list-style:none}
.expat-copy li{position:relative;padding:18px 18px 18px 46px;border:1px solid var(--border);border-radius:14px;background:rgba(255,255,255,.035);color:var(--text-dim)}
.expat-copy li::before{content:"";position:absolute;left:18px;top:25px;width:10px;height:10px;background:var(--accent);clip-path:polygon(0 0,100% 0,100% 70%,70% 100%,0 100%)}
.expat-copy strong,.expat-hero-lead strong,.expat-cta-copy strong,.answer strong{color:#fff}
.expat-copy a,.expat-hero-lead a,.expat-cta-copy a,.answer a{color:var(--accent);text-decoration:none;border-bottom:1px solid rgba(255,87,34,.52)}
.expat-linkline{font-family:var(--font-ui);font-size:clamp(14px,1vw,16px);font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--text-dim)}
.expat-faq-list{display:grid;gap:14px}
.expat-faq-item{border:1px solid var(--border);border-radius:14px;background:rgba(255,255,255,.035);overflow:hidden}
.expat-faq-item summary{cursor:pointer;padding:20px 22px;font-family:var(--font-ui);font-weight:800;font-size:clamp(16px,1.35vw,20px);line-height:1.35;color:#fff;list-style:none}
.expat-faq-item summary::-webkit-details-marker{display:none}
.expat-faq-item .answer{padding:0 22px 20px;color:var(--text-dim);font-size:clamp(15px,1.08vw,18px);line-height:1.65}
.expat-faq-item .answer p{margin:0}
.expat-cta{padding:clamp(68px,8vw,112px) 0;background:#0e0e12;border-top:1px solid var(--border);text-align:center}
.expat-cta .container{max-width:900px}
.expat-cta h2{margin:14px auto 24px;font-family:var(--font-display);font-size:clamp(28px,4vw,58px);font-weight:900;line-height:.92;text-transform:uppercase;color:#fff;overflow-wrap:anywhere}
.expat-cta-copy{margin:0 auto;font-size:clamp(17px,1.25vw,21px);line-height:1.68;color:var(--text);text-align:left}
.expat-cta-copy .expat-linkline{text-align:center;margin-top:28px}
@media (max-width:1000px){.expat-section-grid{grid-template-columns:1fr}.expat-section-head{position:static}.expat-hero h1,.expat-hero-lead,.expat-copy p,.expat-cta-copy p{max-width:calc(100vw - 40px)}}
@media (max-width:760px){.expat-hero{min-height:76vh;padding:128px 0 64px}.expat-hero-media img{object-position:62% 50%}.expat-hero-overlay{background:linear-gradient(90deg,rgba(8,8,8,.96),rgba(8,8,8,.78) 58%,rgba(8,8,8,.38)),linear-gradient(180deg,rgba(8,8,8,.08),#080808 95%)}.expat-copy li{padding-left:38px}.expat-copy li::before{left:15px}}"""


def main() -> int:
    content = parse_copy()
    for lang in LANGS:
        path = output_path(lang)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render_page(content[lang], lang), encoding="utf-8")
        print(f"wrote {path.relative_to(SITE_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
