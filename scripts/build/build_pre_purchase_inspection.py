#!/usr/bin/env python3
"""Build the localized pre-purchase inspection service pages."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

from bs4 import BeautifulSoup

from brand_pages_data import BRAND_ORDER
from hero_images import hero_background_css, hero_preload_links, optimized_hero_url
from nav_patch import (
    DROPDOWN_NAV_LINKS,
    FOOTER_COMPANY_LINKS,
    FOOTER_SERVICES_LINKS,
    PRIMARY_NAV_LINKS,
)

SITE_ROOT = Path(__file__).resolve().parents[2]
BUILD_DIR = Path(__file__).resolve().parent
DOMAIN = "https://ironcustommotors.com"
COPY_FILE = BUILD_DIR / "content" / "pre_purchase_inspection_copy_4lang.md"
I18N_FILE = BUILD_DIR / "i18n.json"

LANGS = ("en", "ru", "uk", "pt")
HREFLANG_CODES = {"en": "en", "ru": "ru", "uk": "uk", "pt": "pt-PT"}
PATHS = {
    "en": "/pre-purchase-inspection/",
    "ru": "/ru/pre-purchase-inspection/",
    "uk": "/uk/pre-purchase-inspection/",
    "pt": "/pt/pre-purchase-inspection/",
}
HERO_IMAGE = "photos/services/pre-purchase-inspection-main.jpg"

COMMON_LOCALIZED_PATHS = {
    "/",
    "/motorcycle-service/",
    "/parts/",
    "/upgrades-tuning/",
    "/custom/",
    "/harley/",
    "/harley-tuning/",
    "/harley-custom/",
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
        "services": "Services",
        "crumb": "Pre-purchase inspection",
        "book": "Book inspection",
        "whatsapp": "WhatsApp us",
        "contact": "Contact",
        "pricing": "See pricing",
        "hours": "Tue-Sat, 10:00-18:00",
        "service_type": "Motorcycle pre-purchase inspection",
        "offer": "from EUR 150, taxes included",
        "feature_label": "Key differentiator",
        "cta_fallback": "Book your inspection",
    },
    "ru": {
        "home": "Главная",
        "services": "Услуги",
        "crumb": "Инспекция перед покупкой",
        "book": "Записаться на проверку",
        "whatsapp": "Написать в WhatsApp",
        "contact": "Контакты",
        "pricing": "Смотреть цены",
        "hours": "Вт-Сб, 10:00-18:00",
        "service_type": "Проверка мотоцикла перед покупкой",
        "offer": "от 150 EUR, налоги включены",
        "feature_label": "Главное отличие",
        "cta_fallback": "Записаться на проверку",
    },
    "uk": {
        "home": "Головна",
        "services": "Послуги",
        "crumb": "Інспекція перед купівлею",
        "book": "Записатися на перевірку",
        "whatsapp": "Написати в WhatsApp",
        "contact": "Контакти",
        "pricing": "Дивитися ціни",
        "hours": "Вт-Сб, 10:00-18:00",
        "service_type": "Перевірка мотоцикла перед купівлею",
        "offer": "від 150 EUR, податки включено",
        "feature_label": "Головна відмінність",
        "cta_fallback": "Записатися на перевірку",
    },
    "pt": {
        "home": "Início",
        "services": "Serviços",
        "crumb": "Inspeção pré-compra",
        "book": "Marcar inspeção",
        "whatsapp": "WhatsApp",
        "contact": "Contacto",
        "pricing": "Ver preços",
        "hours": "Ter-Sáb, 10:00-18:00",
        "service_type": "Inspeção pré-compra de mota",
        "offer": "desde 150 EUR, impostos incluídos",
        "feature_label": "O diferencial",
        "cta_fallback": "Marcar inspeção",
    },
}


def detect_cache_bust() -> str:
    text = (SITE_ROOT / "index.html").read_text(encoding="utf-8")
    match = re.search(r"/assets/main\.css\?v=([a-zA-Z0-9]+)", text)
    return match.group(1) if match else "20260703a"


CACHE_BUST = detect_cache_bust()
GLOBAL_I18N = json.loads(I18N_FILE.read_text(encoding="utf-8"))


def canonical_url(lang: str) -> str:
    return DOMAIN + PATHS[lang]


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


def render_dropdown(key: str, href: str, fallback: str, links: list[tuple[str | None, str, str]], lang: str) -> str:
    label = html.escape(label_for(key, lang, fallback), quote=False)
    items = "\n".join(render_nav_link(item_key, item_href, item_fallback, lang) for item_key, item_href, item_fallback in links)
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
        parts.append(render_dropdown(key, href, fallback, links, lang) if links else render_nav_link(key, href, fallback, lang))
    return f'<nav aria-label="Primary" class="nav">\n' + "\n".join(parts) + "\n</nav>"


def render_mobile_nav(lang: str) -> str:
    parts = []
    for key, href, fallback in PRIMARY_NAV_LINKS:
        links = DROPDOWN_NAV_LINKS.get(key)
        if links:
            items = "\n".join(render_nav_link(item_key, item_href, item_fallback, lang) for item_key, item_href, item_fallback in links)
            parts.append(
                '<details class="mobile-nav-group">\n'
                f'<summary class="mobile-nav-summary"><span data-i18n="{key}">{html.escape(label_for(key, lang, fallback), quote=False)}</span></summary>\n'
                f'<div class="mobile-subnav">\n{items}\n</div>\n'
                "</details>"
            )
        else:
            parts.append(render_nav_link(key, href, fallback, lang))
    return f'<nav class="nav-mobile">\n' + "\n".join(parts) + "\n</nav>"


def render_footer_links(items: list[tuple[str, str, str]], lang: str) -> str:
    return "<ul>\n" + "\n".join(f"<li>{render_nav_link(key, href, fallback, lang)}</li>" for key, href, fallback in items) + "\n</ul>"


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
    matches = list(re.finditer(r"^## (.+?)\s*$", markdown, flags=re.MULTILINE))
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


def extract_field(block: str, labels: tuple[str, ...]) -> str:
    for label in labels:
        match = re.search(rf"^\*\*{re.escape(label)}:\*\*\s*(.+?)\s*$", block, flags=re.MULTILINE)
        if match:
            value = match.group(1).strip()
            return value.strip("`")
    raise ValueError(f"Missing field: {labels[0]}")


def extract_after_heading(block: str, pattern: str, end_pattern: str, flags: int = re.MULTILINE) -> str:
    match = re.search(pattern, block, flags=flags)
    if not match:
        raise ValueError(f"Missing heading: {pattern}")
    end = re.search(end_pattern, block[match.end():], flags=re.MULTILINE)
    end_index = match.end() + end.start() if end else len(block)
    return block[match.end():end_index].strip()


def extract_sections(block: str) -> list[dict[str, str]]:
    matches = list(re.finditer(r"^###\s+(\d{2})\s+·\s+(.+?)\s*$", block, flags=re.MULTILINE))
    sections: list[dict[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(block)
        cta = re.search(r"^###\s+CTA\s+—", block[match.end():end], flags=re.MULTILINE)
        if cta:
            end = match.end() + cta.start()
        sections.append({"number": match.group(1), "title": match.group(2).strip(), "body": block[match.end():end].strip()})
    if len(sections) != 8:
        raise ValueError(f"Expected 8 numbered sections, got {len(sections)}")
    return sections


def extract_cta(block: str) -> dict[str, str]:
    match = re.search(r"^###\s+CTA\s+—\s+(.+?)\s*$", block, flags=re.MULTILINE)
    if not match:
        raise ValueError("Missing CTA heading")
    faq = re.search(r"^###\s+FAQ\s*$", block[match.end():], flags=re.MULTILINE)
    end = match.end() + faq.start() if faq else len(block)
    return {"title": match.group(1).strip(), "body": block[match.end():end].strip()}


def extract_faq(block: str) -> list[dict[str, str]]:
    text = extract_after_heading(block, r"^###\s+FAQ\s*$", r"^## ")
    faq: list[dict[str, str]] = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        match = re.match(r"- \*\*(.+?)\*\*\s+(.+)", line)
        if match:
            faq.append({"question": match.group(1).strip(), "answer": match.group(2).strip()})
    if not faq:
        raise ValueError("Missing FAQ items")
    return faq


def parse_copy() -> dict[str, dict]:
    blocks = split_language_blocks(COPY_FILE.read_text(encoding="utf-8"))
    content: dict[str, dict] = {}
    for lang, block in blocks.items():
        content[lang] = {
            "seo_title": extract_field(block, ("SEO Title",)),
            "meta_description": extract_field(block, ("Meta", "Meta description")),
            "slug": extract_field(block, ("Slug",)),
            "eyebrow": extract_field(block, ("Eyebrow",)),
            "h1": extract_field(block, ("H1",)),
            "hero_alt": extract_field(block, ("Hero ALT",)),
            "hero": extract_after_heading(block, r"^###\s+.*hero.*$", r"^###\s+01\s+·", flags=re.MULTILINE | re.IGNORECASE),
            "sections": extract_sections(block),
            "cta": extract_cta(block),
            "faq": extract_faq(block),
        }
        expected_slug = PATHS[lang]
        if content[lang]["slug"] != expected_slug:
            raise ValueError(f"{lang} slug mismatch: {content[lang]['slug']} != {expected_slug}")
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


def split_paragraphs(markdown: str) -> list[str]:
    raw = markdown.strip()
    if not raw:
        return []
    chunks = [chunk.strip() for chunk in re.split(r"\n\s*\n", raw) if chunk.strip()]
    if len(chunks) == 1:
        lines = [line.strip() for line in raw.splitlines() if line.strip()]
        if len(lines) > 1 and all(line.startswith("**") for line in lines):
            return lines
    return chunks


def extract_link_buttons(markdown: str, lang: str) -> tuple[str, list[tuple[str, str]]]:
    lines = [line.rstrip() for line in markdown.strip().splitlines()]
    buttons: list[tuple[str, str]] = []
    while lines and lines[-1].strip().startswith("[") and re.search(r"\[[^\]]+\]\([^)]+\)", lines[-1]):
        line = lines.pop().strip()
        buttons.extend((label, localized_href(href, lang)) for label, href in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", line))
    return "\n".join(lines).strip(), buttons


def render_paragraphs(markdown: str, lang: str) -> str:
    return "\n".join(f"<p>{inline_markdown(chunk, lang)}</p>" for chunk in split_paragraphs(markdown))


def render_actions(buttons: list[tuple[str, str]], lang: str, *, include_hours: bool = False) -> str:
    if not buttons:
        buttons = [
            (UI[lang]["book"], localized_href("/contact/", lang)),
            (UI[lang]["whatsapp"], "https://wa.me/351917961230"),
        ]
    rendered = []
    for index, (label, href) in enumerate(buttons):
        cls = "btn btn-primary" if index == 0 else "btn btn-ghost"
        target = ' target="_blank" rel="noopener"' if href.startswith("http") and "ironcustommotors.com" not in href else ""
        rendered.append(f'<a class="{cls}" href="{html.escape(href, quote=True)}"{target}>{html.escape(label, quote=False)}</a>')
    if include_hours:
        rendered.append(f'<span class="ppi-hours">{html.escape(UI[lang]["hours"], quote=False)}</span>')
    return '<div class="ppi-actions">' + "".join(rendered) + "</div>"


def split_numbered_bold_items(markdown: str) -> tuple[str, list[str]]:
    intro_lines: list[str] = []
    items: list[str] = []
    for raw_line in markdown.strip().splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if re.match(r"^\*\*\d+\.\s+", line):
            items.append(line)
        elif items:
            items[-1] += " " + line
        else:
            intro_lines.append(line)
    return "\n".join(intro_lines).strip(), items


def render_check_cards(section: dict[str, str], lang: str) -> str:
    intro, numbered_items = split_numbered_bold_items(section["body"])
    source_items = numbered_items if numbered_items else split_paragraphs(section["body"])
    cards = []
    for item in source_items:
        match = re.match(r"\*\*(?:\d+\.\s*)?(.+?)\.\*\*\s*(.+)", item, flags=re.DOTALL)
        if match:
            title = match.group(1).strip()
            body = match.group(2).strip()
        else:
            title = ""
            body = item
        cards.append(
            f'<article class="ppi-check-card"><h3>{inline_markdown(title, lang)}</h3><p>{inline_markdown(body, lang)}</p></article>'
        )
    intro_html = f'<div class="ppi-copy ppi-check-intro">{render_paragraphs(intro, lang)}</div>' if intro else ""
    return intro_html + '<div class="ppi-check-grid">' + "\n".join(cards) + "</div>"


def render_process_rows(section: dict[str, str], lang: str) -> str:
    intro, numbered_items = split_numbered_bold_items(section["body"])
    source_items = numbered_items if numbered_items else split_paragraphs(section["body"])
    rows = []
    for item in source_items:
        match = re.match(r"\*\*(\d+)\.\s*(.+?)\.\*\*\s*(.+)", item, flags=re.DOTALL)
        if match:
            number, title, body = match.groups()
        else:
            number = f"{len(rows) + 1}"
            title = section["title"]
            body = item
        rows.append(
            f'<article class="ppi-process-row"><span class="num">{int(number):02d}</span><div><h3>{inline_markdown(title, lang)}</h3><p>{inline_markdown(body, lang)}</p></div></article>'
        )
    intro_html = f'<div class="ppi-copy ppi-process-intro">{render_paragraphs(intro, lang)}</div>' if intro else ""
    return intro_html + '<div class="ppi-process-list">' + "\n".join(rows) + "</div>"


def render_standard_copy(section: dict[str, str], lang: str) -> str:
    return f'<div class="ppi-copy">{render_paragraphs(section["body"], lang)}</div>'


def render_section(section: dict[str, str], lang: str) -> str:
    number = section["number"]
    special_class = " ppi-feature-section" if number == "02" else ""
    if number == "02":
        body = f'<div class="ppi-feature-card"><span>{html.escape(UI[lang]["feature_label"], quote=False)}</span>{render_paragraphs(section["body"], lang)}</div>'
    elif number == "03":
        body = render_check_cards(section, lang)
    elif number == "04":
        body = render_process_rows(section, lang)
    elif number == "07":
        body = f'<div class="ppi-price-card">{render_paragraphs(section["body"], lang)}{render_actions([(UI[lang]["pricing"], localized_href("/pricing/", lang)), (UI[lang]["whatsapp"], "https://wa.me/351917961230")], lang)}</div>'
    elif number == "08":
        body = f'{render_standard_copy(section, lang)}{render_actions([(UI[lang]["book"], localized_href("/contact/", lang)), (UI[lang]["whatsapp"], "https://wa.me/351917961230")], lang)}'
    else:
        body = render_standard_copy(section, lang)
    return f"""
<section class="ppi-section{special_class}" id="section-{number}">
<div class="container">
<div class="ppi-heading">
<span class="h-eyebrow">{number} · {html.escape(section["title"], quote=False)}</span>
<h2>{html.escape(section["title"], quote=False)}</h2>
</div>
{body}
</div>
</section>"""


def render_faq(faq: list[dict[str, str]], lang: str) -> str:
    items = []
    for item in faq:
        items.append(
            f"""
<details>
<summary><span>{inline_markdown(item["question"], lang)}</span><span class="chev">⌄</span></summary>
<div class="answer">{render_paragraphs(item["answer"], lang)}</div>
</details>"""
        )
    return f"""
<section class="ppi-section ppi-faq" id="faq">
<div class="container">
<div class="ppi-heading compact">
<span class="h-eyebrow">FAQ</span>
<h2>FAQ</h2>
</div>
<div class="ppi-faq-list">
{''.join(items)}
</div>
</div>
</section>"""


def json_ld(content: dict, lang: str) -> list[dict]:
    faq_entities = [
        {
            "@type": "Question",
            "name": item["question"],
            "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"\s+", " ", item["answer"]).strip()},
        }
        for item in content["faq"]
    ]
    area_served = [{"@type": "City", "name": name} for name in ("Cascais", "Estoril", "Oeiras", "Sintra", "Lisbon", "Greater Lisbon")]
    return [
        {
            "@context": "https://schema.org",
            "@type": "Service",
            "@id": canonical_url(lang) + "#service",
            "name": content["h1"],
            "serviceType": UI[lang]["service_type"],
            "description": content["meta_description"],
            "provider": {"@id": f"{DOMAIN}/#business"},
            "areaServed": area_served,
            "url": canonical_url(lang),
            "offers": {
                "@type": "Offer",
                "name": UI[lang]["offer"],
                "price": "150",
                "priceCurrency": "EUR",
                "availability": "https://schema.org/InStock",
                "url": canonical_url(lang),
                "priceSpecification": {
                    "@type": "PriceSpecification",
                    "price": "150",
                    "priceCurrency": "EUR",
                    "valueAddedTaxIncluded": True,
                },
            },
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": faq_entities,
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": UI[lang]["home"], "item": DOMAIN + localized_href("/", lang)},
                {"@type": "ListItem", "position": 2, "name": UI[lang]["services"], "item": DOMAIN + localized_href("/services/", lang)},
                {"@type": "ListItem", "position": 3, "name": UI[lang]["crumb"], "item": canonical_url(lang)},
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
    hero_url = "/" + HERO_IMAGE
    return f"""<!DOCTYPE html>
<html data-lang="{lang}" lang="{lang}">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1, viewport-fit=cover" name="viewport"/>
<meta content="#0a0a0a" name="theme-color"/>
<meta content="max-image-preview:large" name="robots"/>
<title>{html.escape(content["seo_title"])}</title>
<meta content="{html.escape(content["meta_description"])}" name="description"/>
<meta content="{html.escape(content["seo_title"])}" property="og:title"/>
<meta content="{html.escape(content["meta_description"])}" property="og:description"/>
<meta content="website" property="og:type"/>
<meta content="{canonical_url(lang)}" property="og:url"/>
<meta content="Iron Custom Motors" property="og:site_name"/>
<meta content="{DOMAIN}/{HERO_IMAGE}" property="og:image"/>
<meta content="{html.escape(content["hero_alt"])}" property="og:image:alt"/>
<meta content="{og_locale}" property="og:locale"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="{html.escape(content["seo_title"])}" name="twitter:title"/>
<meta content="{html.escape(content["meta_description"])}" name="twitter:description"/>
<meta content="{DOMAIN}/{HERO_IMAGE}" name="twitter:image"/>
<meta content="{html.escape(content["hero_alt"])}" name="twitter:image:alt"/>
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
{hero_preload_links(hero_url)}
{json_scripts}
<link href="/assets/main.css?v={CACHE_BUST}" rel="stylesheet"/>
<style>{PAGE_CSS}</style>
</head>"""


def render_page(content: dict, lang: str) -> str:
    before, after = chrome_fragments(lang)
    hero_body, hero_buttons = extract_link_buttons(content["hero"], lang)
    cta_body, cta_buttons = extract_link_buttons(content["cta"]["body"], lang)
    sections = "".join(render_section(section, lang) for section in content["sections"])
    body = f"""
<body>
{before}
<main>
<section class="ppi-hero">
<div aria-hidden="true" class="ppi-hero-bg"></div>
<img alt="{html.escape(content["hero_alt"], quote=True)}" class="ppi-hero-alt" height="960" src="{optimized_hero_url('/' + HERO_IMAGE, 1280, 'jpg')}" width="1280"/>
<div class="container">
<div class="crumb"><a href="{localized_href('/', lang)}">{html.escape(UI[lang]["home"], quote=False)}</a><span class="sep">→</span><a href="{localized_href('/services/', lang)}">{html.escape(UI[lang]["services"], quote=False)}</a><span class="sep">→</span><span>{html.escape(UI[lang]["crumb"], quote=False)}</span></div>
<span class="h-eyebrow">{html.escape(content["eyebrow"], quote=False)}</span>
<h1>{html.escape(content["h1"], quote=False)}</h1>
<div class="lead">{render_paragraphs(hero_body, lang)}</div>
{render_actions(hero_buttons, lang, include_hours=True)}
</div>
</section>
{sections}
<section class="ppi-cta">
<div class="container">
<span class="h-eyebrow">{html.escape(content["cta"]["title"], quote=False)}</span>
<div class="ppi-cta-copy">{render_paragraphs(cta_body, lang)}</div>
{render_actions(cta_buttons, lang, include_hours=True)}
</div>
</section>
{render_faq(content["faq"], lang)}
</main>
{after}
</body>
</html>"""
    return head_html(content, lang) + body


PAGE_CSS = """.ppi-hero{position:relative;isolation:isolate;overflow:hidden;min-height:78vh;padding:150px 0 84px;background:#080808}
.ppi-hero::after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(90deg,rgba(8,8,8,.94),rgba(8,8,8,.72) 48%,rgba(8,8,8,.28)),linear-gradient(180deg,rgba(8,8,8,.18),#080808 95%)}
.ppi-hero-bg{position:absolute;inset:0;z-index:-2;background-size:cover;background-position:center;filter:saturate(.92) contrast(1.08) brightness(.68);""" + hero_background_css("/" + HERO_IMAGE) + """}
.ppi-hero-alt{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);clip-path:inset(50%);white-space:nowrap}
.ppi-hero h1{max-width:min(930px,76vw,calc(100vw - 40px));margin:18px 0 24px;font-family:var(--font-display);font-size:clamp(30px,4vw,58px);font-weight:900;line-height:.9;text-transform:uppercase;color:#fff;overflow-wrap:anywhere}
.ppi-hero .lead{max-width:min(920px,76vw,calc(100vw - 40px));font-size:clamp(18px,1.35vw,23px);line-height:1.62;color:var(--text)}
.ppi-hero .lead p{margin:0 0 16px}
.ppi-section{padding:clamp(34px,4vw,52px) 0;background:#080808;border-top:1px solid var(--border)}
.ppi-heading{display:grid;grid-template-columns:minmax(180px,.62fr) minmax(0,1.38fr);gap:36px;align-items:end;margin-bottom:34px}
.ppi-heading.compact{display:block;max-width:780px}
.ppi-heading h2{max-width:min(860px,76vw,calc(100vw - 40px));margin:0;font-family:var(--font-display);font-size:clamp(26px,3.5vw,50px);font-weight:900;line-height:.94;text-transform:uppercase;color:#fff;overflow-wrap:anywhere}
.ppi-copy{font-size:clamp(17px,1.28vw,21px);line-height:1.68;color:var(--text)}
.ppi-copy p{margin:0 0 18px;max-width:min(1120px,76vw,calc(100vw - 40px));overflow-wrap:break-word}
.ppi-check-intro,.ppi-process-intro{margin-bottom:26px}
.ppi-copy a,.lead a,.ppi-cta-copy a,.ppi-check-card a,.ppi-process-row a,.answer a{color:var(--accent);text-decoration:none;border-bottom:1px solid rgba(255,87,34,.5)}
.ppi-copy strong,.lead strong,.ppi-check-card strong,.ppi-process-row strong,.ppi-price-card strong,.answer strong{color:#fff}
.ppi-actions{display:flex;gap:14px;flex-wrap:wrap;align-items:center;max-width:min(850px,76vw,calc(100vw - 40px));margin-top:26px}
.ppi-actions .btn{white-space:normal}
.ppi-hours{display:inline-flex;align-items:center;min-height:46px;padding:0 18px;border:1px solid var(--border);border-radius:999px;color:var(--text-dim);font-family:var(--font-ui);font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.ppi-feature-section{background:radial-gradient(circle at 78% 20%,rgba(255,87,34,.18),transparent 38%),#080808}
.ppi-feature-card{position:relative;overflow:hidden;border:1px solid rgba(255,87,34,.55);border-radius:var(--radius-lg);background:linear-gradient(135deg,rgba(255,87,34,.12),rgba(255,255,255,.035));padding:clamp(26px,4vw,48px);box-shadow:0 24px 90px rgba(255,87,34,.08)}
.ppi-feature-card::before{content:"02";position:absolute;right:clamp(18px,4vw,42px);top:clamp(10px,2vw,22px);font-family:var(--font-display);font-size:clamp(64px,11vw,150px);font-weight:900;line-height:1;color:rgba(255,87,34,.12)}
.ppi-feature-card>span{position:relative;z-index:1;display:inline-flex;margin-bottom:22px;color:var(--accent);font-family:var(--font-ui);font-size:13px;font-weight:800;letter-spacing:.18em;text-transform:uppercase}
.ppi-feature-card p{position:relative;z-index:1;max-width:min(980px,76vw,calc(100vw - 40px));margin:0 0 18px;color:var(--text);font-size:clamp(18px,1.42vw,23px);line-height:1.62}
.ppi-check-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
.ppi-check-card{border:1px solid var(--border);border-radius:var(--radius-lg);background:var(--surface);padding:24px 22px}
.ppi-check-card h3{margin:0 0 10px;font-family:var(--font-display);font-size:clamp(20px,1.8vw,28px);font-weight:900;line-height:1;text-transform:uppercase;color:#fff}
.ppi-check-card p{font-size:15px;line-height:1.62;color:var(--text-dim)}
.ppi-process-list{display:grid;gap:14px;max-width:980px}
.ppi-process-row{display:grid;grid-template-columns:70px 1fr;gap:22px;padding:22px;border:1px solid var(--border);border-radius:var(--radius-lg);background:var(--surface)}
.ppi-process-row .num{font-family:var(--font-display);font-weight:900;font-size:32px;line-height:1;color:var(--accent)}
.ppi-process-row h3{margin:0 0 8px;font-family:var(--font-display);font-size:clamp(20px,1.8vw,28px);font-weight:900;line-height:1;text-transform:uppercase;color:#fff}
.ppi-process-row p{font-size:16px;line-height:1.62;color:var(--text-dim)}
.ppi-price-card{border:1px solid var(--border);border-radius:var(--radius-lg);background:linear-gradient(135deg,rgba(255,87,34,.11),rgba(255,255,255,.035));padding:clamp(26px,4vw,42px);max-width:980px}
.ppi-price-card p{font-size:clamp(18px,1.4vw,23px);line-height:1.65;color:var(--text);margin:0 0 18px}
.ppi-cta{padding:clamp(32px,4vw,48px) 0;background:#101010;border-top:1px solid var(--border);text-align:center}
.ppi-cta .container{max-width:980px}
.ppi-cta-copy{font-size:clamp(19px,1.6vw,25px);line-height:1.6;color:#fff}
.ppi-cta-copy p{margin:16px 0 0}
.ppi-cta .ppi-actions{justify-content:center;margin-left:auto;margin-right:auto}
.ppi-faq-list{display:grid;gap:12px}
.ppi-faq-list details{border:1px solid var(--border);border-radius:var(--radius-lg);background:var(--surface);overflow:hidden}
.ppi-faq-list summary{display:flex;gap:18px;align-items:flex-start;justify-content:space-between;cursor:pointer;padding:22px 24px;list-style:none;font-family:var(--font-display);font-size:clamp(18px,1.6vw,24px);font-weight:800;line-height:1.1;text-transform:uppercase;color:#fff}
.ppi-faq-list summary::-webkit-details-marker{display:none}
.ppi-faq-list .chev{color:var(--accent);transition:transform .2s var(--ease)}
.ppi-faq-list details[open] .chev{transform:rotate(180deg)}
.ppi-faq-list .answer{padding:0 24px 24px;color:var(--text-dim);font-size:16px;line-height:1.65}
.ppi-faq-list .answer p{margin:0}
@media (max-width:980px){.ppi-heading{grid-template-columns:1fr}.ppi-check-grid{grid-template-columns:1fr}.ppi-process-list{max-width:none}}
@media (max-width:640px){.ppi-hero{min-height:auto;padding:124px 0 62px}.ppi-hero h1{max-width:calc(100vw - 40px);font-size:clamp(28px,8vw,34px);line-height:.94}.ppi-hero .lead,.ppi-copy p,.ppi-feature-card p{max-width:calc(100vw - 40px);overflow-wrap:break-word}.ppi-section{padding:32px 0}.ppi-heading{gap:16px;margin-bottom:24px}.ppi-heading h2{font-size:clamp(26px,9vw,34px)}.ppi-actions{display:grid;grid-template-columns:1fr;max-width:calc(100vw - 40px)}.ppi-actions .btn{width:100%;justify-content:center;text-align:center;line-height:1.15;padding-left:18px;padding-right:18px}.ppi-hours{justify-content:center;border-radius:14px}.ppi-feature-card{padding:24px 20px}.ppi-process-row{grid-template-columns:48px 1fr;gap:16px;padding:18px}.ppi-process-row .num{font-size:25px}.ppi-check-card{padding:22px 18px}}
"""


def write_page(lang: str, content: dict) -> Path:
    relative = PATHS[lang].strip("/")
    out = SITE_ROOT / relative / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_page(content, lang), encoding="utf-8")
    return out


def main() -> int:
    content = parse_copy()
    for lang in LANGS:
        out = write_page(lang, content[lang])
        print(f"wrote {out.relative_to(SITE_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
