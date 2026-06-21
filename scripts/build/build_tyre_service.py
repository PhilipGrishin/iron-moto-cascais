#!/usr/bin/env python3
"""Build the localized motorcycle tyre fitting service pages."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

from bs4 import BeautifulSoup

from hero_images import hero_background_css, hero_preload_links, optimized_hero_url
from nav_patch import (
    FOOTER_COMPANY_LINKS,
    FOOTER_SERVICES_LINKS,
    PRIMARY_NAV_LINKS,
    SERVICE_NAV_LINKS,
)

SITE_ROOT = Path(__file__).resolve().parents[2]
BUILD_DIR = Path(__file__).resolve().parent
DOMAIN = "https://ironcustommotors.com"
COPY_FILE = BUILD_DIR / "content" / "tyre_service_copy_4lang.md"
I18N_FILE = BUILD_DIR / "i18n.json"
VIDEO_ID = "KGEPaj46fBg"
VIDEO_SHORT_URL = f"https://youtube.com/shorts/{VIDEO_ID}"
VIDEO_EMBED_URL = f"https://www.youtube-nocookie.com/embed/{VIDEO_ID}"
VIDEO_THUMB = f"https://i.ytimg.com/vi/{VIDEO_ID}/hqdefault.jpg"

LANGS = ("en", "ru", "uk", "pt")
PATHS = {
    "en": "/motorcycle-tyre-service/",
    "ru": "/ru/shinomontazh-mototsiklov/",
    "uk": "/uk/shynomontazh-mototsykliv/",
    "pt": "/pt/montagem-de-pneus-mota/",
}

COMMON_LOCALIZED_PATHS = {
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
    "/news/",
}

TYRE_PATH_BY_REST = {
    "/motorcycle-tyre-service/": PATHS,
    "/shinomontazh-mototsiklov/": PATHS,
    "/shynomontazh-mototsykliv/": PATHS,
    "/montagem-de-pneus-mota/": PATHS,
}

IMAGES = {
    "hero": "photos/services/motorcycle-tyre-service-workshop-cascais.jpg",
    "changer": "photos/services/motorcycle-specific-tyre-changer.jpg",
    "wide": "photos/services/wide-fat-motorcycle-tyre-400mm.jpg",
    "spoked": "photos/services/spoked-wheel-tyre-fitting-cascais.jpg",
    "balance_fat": "photos/services/motorcycle-wheel-balancing-fat-tyre.jpg",
    "balance_wide": "photos/services/motorcycle-wheel-balancing-wide-tyre.jpg",
}

ALT_TEXT = {
    "en": {
        "hero": "Motorcycle tyre fitting and wheel balancing workshop at Iron Custom Motors, Cascais",
        "changer": "Motorcycle-specific tyre changer for fitting without removing brake discs",
        "wide": "Wide 400 mm fat motorcycle tyre fitted at Iron Custom Motors, Cascais",
        "spoked": "Spoked motorcycle wheel tyre fitting in Cascais",
        "balance_fat": "Balancing a wide motorcycle wheel up to 30 inch at Iron Custom Motors",
        "balance_wide": "Motorcycle wheel balancing on dedicated moto equipment, Cascais",
        "video": "Watch the motorcycle tyre fitting process at Iron Custom Motors",
    },
    "ru": {
        "hero": "Мотоциклетный шиномонтаж и балансировка колёс в Iron Custom Motors, Кашкайш",
        "changer": "Мотоциклетный шиномонтажный станок для монтажа без снятия тормозных дисков",
        "wide": "Широкая мотоциклетная шина 400 мм в Iron Custom Motors, Кашкайш",
        "spoked": "Шиномонтаж спицованного мотоциклетного колеса в Кашкайше",
        "balance_fat": "Балансировка широкого мотоциклетного колеса до 30 дюймов в Iron Custom Motors",
        "balance_wide": "Балансировка мотоциклетного колеса на профильном оборудовании в Кашкайше",
        "video": "Посмотреть процесс мотоциклетного шиномонтажа в Iron Custom Motors",
    },
    "uk": {
        "hero": "Мотоциклетний шиномонтаж і балансування коліс в Iron Custom Motors, Кашкайш",
        "changer": "Мотоциклетний шиномонтажний верстат для монтажу без зняття гальмівних дисків",
        "wide": "Широка мотоциклетна шина 400 мм в Iron Custom Motors, Кашкайш",
        "spoked": "Шиномонтаж спицьованого мотоциклетного колеса в Кашкайші",
        "balance_fat": "Балансування широкого мотоциклетного колеса до 30 дюймів в Iron Custom Motors",
        "balance_wide": "Балансування мотоциклетного колеса на профільному обладнанні в Кашкайші",
        "video": "Подивитися процес мотоциклетного шиномонтажу в Iron Custom Motors",
    },
    "pt": {
        "hero": "Oficina de montagem de pneus de mota e equilibragem na Iron Custom Motors, Cascais",
        "changer": "Máquina específica para pneus de mota sem desmontar discos de travão",
        "wide": "Pneu largo de mota de 400 mm montado na Iron Custom Motors, Cascais",
        "spoked": "Montagem de pneu em roda de raios de mota em Cascais",
        "balance_fat": "Equilibragem de roda larga de mota até 30 polegadas na Iron Custom Motors",
        "balance_wide": "Equilibragem de roda de mota em equipamento dedicado, Cascais",
        "video": "Ver o processo de montagem de pneus de mota na Iron Custom Motors",
    },
}

UI = {
    "en": {
        "home": "Home",
        "services": "Services",
        "crumb": "Tyre service",
        "eyebrow": "Motorcycle tyre service · Cascais",
        "book": "Book tyre service",
        "pricing": "See pricing",
        "service": "General motorcycle service",
        "parts": "Order tyres or rims",
        "contact": "Book on WhatsApp",
        "faq": "Read FAQ",
        "video_eyebrow": "Workshop video",
        "video_title": "See the moto tyre changer at work",
        "video_text": "A short look at motorcycle-specific tyre fitting equipment for wide, spoked and custom wheels.",
        "ai_title": "Quick answers for riders",
    },
    "ru": {
        "home": "Главная",
        "services": "Услуги",
        "crumb": "Шиномонтаж",
        "eyebrow": "Мотоциклетный шиномонтаж · Кашкайш",
        "book": "Записаться на шиномонтаж",
        "pricing": "Смотреть цены",
        "service": "Общий мотосервис",
        "parts": "Заказать шины или диски",
        "contact": "Записаться в WhatsApp",
        "faq": "Читать FAQ",
        "video_eyebrow": "Видео из мастерской",
        "video_title": "Посмотрите мотоциклетный станок в работе",
        "video_text": "Короткий взгляд на профильное оборудование для широких, спицованных и кастомных колёс.",
        "ai_title": "Короткие ответы для райдеров",
    },
    "uk": {
        "home": "Головна",
        "services": "Послуги",
        "crumb": "Шиномонтаж",
        "eyebrow": "Мотоциклетний шиномонтаж · Кашкайш",
        "book": "Записатися на шиномонтаж",
        "pricing": "Дивитися ціни",
        "service": "Загальний мотосервіс",
        "parts": "Замовити шини або диски",
        "contact": "Записатися в WhatsApp",
        "faq": "Читати FAQ",
        "video_eyebrow": "Відео з майстерні",
        "video_title": "Подивіться мотоциклетний верстат у роботі",
        "video_text": "Короткий погляд на профільне обладнання для широких, спицьованих і кастомних коліс.",
        "ai_title": "Короткі відповіді для райдерів",
    },
    "pt": {
        "home": "Início",
        "services": "Serviços",
        "crumb": "Pneus de mota",
        "eyebrow": "Serviço de pneus de mota · Cascais",
        "book": "Marcar montagem",
        "pricing": "Ver preços",
        "service": "Serviço geral de motas",
        "parts": "Encomendar pneus ou jantes",
        "contact": "Marcar no WhatsApp",
        "faq": "Ler FAQ",
        "video_eyebrow": "Vídeo da oficina",
        "video_title": "Veja a máquina de pneus de mota em ação",
        "video_text": "Um olhar rápido sobre equipamento específico para rodas largas, de raios e custom.",
        "ai_title": "Respostas rápidas para motociclistas",
    },
}


def detect_cache_bust() -> str:
    text = (SITE_ROOT / "index.html").read_text(encoding="utf-8")
    match = re.search(r"/assets/main\.css\?v=([a-zA-Z0-9]+)", text)
    return match.group(1) if match else "20260620c"


CACHE_BUST = detect_cache_bust()
GLOBAL_I18N = json.loads(I18N_FILE.read_text(encoding="utf-8"))


def canonical_url(lang: str) -> str:
    return DOMAIN + PATHS[lang]


def localized_path_for(base_path: str, lang: str) -> str:
    if base_path in TYRE_PATH_BY_REST:
        return TYRE_PATH_BY_REST[base_path][lang]
    if lang == "en":
        return base_path
    if base_path == "/":
        return f"/{lang}/"
    if base_path in COMMON_LOCALIZED_PATHS or base_path.startswith("/projects/") or base_path.startswith("/blog/") or base_path.startswith("/news/"):
        return f"/{lang}{base_path}"
    return base_path


def localized_href(href: str, lang: str) -> str:
    if not href or href.startswith(("mailto:", "tel:", "#", "javascript:")):
        return href
    if href.startswith(("http://", "https://")):
        parsed = urlsplit(href)
        if parsed.netloc not in ("ironcustommotors.com", "www.ironcustommotors.com"):
            return href
        base = parsed.path or "/"
        localized = localized_path_for(base, lang)
        return urlunsplit((parsed.scheme, parsed.netloc, localized, parsed.query, parsed.fragment))
    if href.startswith(("/assets/", "/photos/", "/worker/", "/pricing/files/")):
        return href
    parsed = urlsplit(href)
    localized = localized_path_for(parsed.path or "/", lang)
    return urlunsplit(("", "", localized, parsed.query, parsed.fragment))


def label_for(key: str, lang: str, fallback: str) -> str:
    return GLOBAL_I18N.get(lang, {}).get(key) or GLOBAL_I18N["en"].get(key) or fallback


def render_service_dropdown(lang: str) -> str:
    items = []
    for key, href, fallback in SERVICE_NAV_LINKS:
        items.append(
            f'<a data-i18n="{key}" href="{localized_href(href, lang)}">{html.escape(label_for(key, lang, fallback), quote=False)}</a>'
        )
    return (
        '<div class="nav-dropdown">\n'
        f'<a aria-haspopup="true" class="nav-dropdown-trigger" data-i18n="nav.services" href="{localized_href("/services/", lang)}">'
        f'{html.escape(label_for("nav.services", lang, "Services"), quote=False)}</a>\n'
        '<div aria-label="Services" class="nav-dropdown-menu">\n'
        + "\n".join(items)
        + "\n</div>\n</div>"
    )


def render_primary_nav(lang: str) -> str:
    parts = []
    for key, href, fallback in PRIMARY_NAV_LINKS:
        if key == "nav.services":
            parts.append(render_service_dropdown(lang))
        else:
            parts.append(
                f'<a data-i18n="{key}" href="{localized_href(href, lang)}">{html.escape(label_for(key, lang, fallback), quote=False)}</a>'
            )
    joined = "\n".join(parts)
    return f'<nav aria-label="Primary" class="nav">\n{joined}\n</nav>'


def render_mobile_nav(lang: str) -> str:
    service_items = []
    for key, href, fallback in SERVICE_NAV_LINKS:
        service_items.append(
            f'<a data-i18n="{key}" href="{localized_href(href, lang)}">{html.escape(label_for(key, lang, fallback), quote=False)}</a>'
        )
    parts = [
        '<details class="mobile-nav-group">\n'
        f'<summary class="mobile-nav-summary"><span data-i18n="nav.services">{html.escape(label_for("nav.services", lang, "Services"), quote=False)}</span></summary>\n'
        '<div class="mobile-subnav">\n'
        + "\n".join(service_items)
        + "\n</div>\n</details>"
    ]
    for key, href, fallback in PRIMARY_NAV_LINKS:
        if key == "nav.services":
            continue
        parts.append(
            f'<a data-i18n="{key}" href="{localized_href(href, lang)}">{html.escape(label_for(key, lang, fallback), quote=False)}</a>'
        )
    joined = "\n".join(parts)
    return f'<nav class="nav-mobile">\n{joined}\n</nav>'


def render_footer_links(items: list[tuple[str, str, str]], lang: str) -> str:
    rows = []
    for key, href, fallback in items:
        rows.append(
            f'<li><a data-i18n="{key}" href="{localized_href(href, lang)}">{html.escape(label_for(key, lang, fallback), quote=False)}</a></li>'
        )
    return "<ul>\n" + "\n".join(rows) + "\n</ul>"


def apply_i18n(soup: BeautifulSoup, lang: str) -> None:
    dictionary = GLOBAL_I18N.get(lang, GLOBAL_I18N["en"])
    for element in soup.select("[data-i18n]"):
        key = element.get("data-i18n")
        if key in dictionary:
            element.clear()
            fragment = BeautifulSoup(dictionary[key], "html.parser")
            if fragment.contents:
                for child in list(fragment.contents):
                    element.append(child)
            else:
                element.string = dictionary[key]
    for element in soup.select("[data-i18n-html]"):
        key = element.get("data-i18n-html")
        if key in dictionary:
            element.clear()
            fragment = BeautifulSoup(dictionary[key], "html.parser")
            if fragment.contents:
                for child in list(fragment.contents):
                    element.append(child)
            else:
                element.string = dictionary[key]


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
            return match.group(1).strip()
    raise ValueError(f"Missing field: {labels[0]}")


def extract_h2_sections(block: str) -> list[dict[str, str]]:
    matches = list(re.finditer(r"^\*\*H2 — (.+?):\*\*\s*(.*?)\s*$", block, flags=re.MULTILINE))
    cta_match = re.search(r"^\*\*CTA:\*\*", block, flags=re.MULTILINE)
    stop = cta_match.start() if cta_match else len(block)
    sections: list[dict[str, str]] = []
    for index, match in enumerate(matches):
        next_start = matches[index + 1].start() if index + 1 < len(matches) else stop
        body = (match.group(2).strip() + "\n" + block[match.end():next_start].strip()).strip()
        sections.append({"title": match.group(1).strip(), "body": body})
    if len(sections) != 7:
        raise ValueError(f"Expected 7 H2 sections, got {len(sections)}")
    return sections


def extract_between(block: str, start_regex: str, end_regex: str | None = None) -> str:
    start = re.search(start_regex, block, flags=re.MULTILINE)
    if not start:
        return ""
    end = re.search(end_regex, block[start.end():], flags=re.MULTILINE) if end_regex else None
    end_index = start.end() + end.start() if end else len(block)
    return block[start.end():end_index].strip()


def extract_faq(block: str) -> list[dict[str, str]]:
    text = extract_between(block, r"^\*\*FAQ:\*\*\s*$", r"^\*\*(AI-answer blocks|Blocos de resposta IA|Блоки ответов для ИИ|Блоки відповідей для ШІ):\*\*\s*$")
    faq: list[dict[str, str]] = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        match = re.match(r"- \*(.+?)\*\s*(.+)", line)
        if not match:
            continue
        faq.append({"question": match.group(1).strip(), "answer": match.group(2).strip()})
    if len(faq) != 8:
        raise ValueError(f"Expected 8 FAQ items, got {len(faq)}")
    return faq


def extract_ai_blocks(block: str) -> list[dict[str, str]]:
    text = extract_between(block, r"^\*\*(AI-answer blocks|Blocos de resposta IA|Блоки ответов для ИИ|Блоки відповідей для ШІ):\*\*\s*$")
    items: list[dict[str, str]] = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        match = re.match(r"- \*(.+?):\*\s*(.+)", line)
        if match:
            items.append({"label": match.group(1).strip(), "text": match.group(2).strip()})
    if len(items) != 3:
        raise ValueError(f"Expected 3 AI-answer blocks, got {len(items)}")
    return items


def parse_copy() -> dict[str, dict]:
    blocks = split_language_blocks(COPY_FILE.read_text(encoding="utf-8"))
    content: dict[str, dict] = {}
    for lang, block in blocks.items():
        content[lang] = {
            "seo_title": extract_field(block, ("SEO Title",)),
            "meta_description": extract_field(block, ("Meta description",)),
            "h1": extract_field(block, ("H1",)),
            "hero": extract_field(block, ("Hero intro", "Introdução (Hero)", "Hero")),
            "sections": extract_h2_sections(block),
            "cta": extract_field(block, ("CTA",)),
            "faq": extract_faq(block),
            "ai": extract_ai_blocks(block),
        }
    return content


def rich_text(text: str) -> str:
    return html.escape(text, quote=False)


def render_paragraphs(text: str) -> str:
    chunks = [chunk.strip() for chunk in re.split(r"\n\s*\n", text.strip()) if chunk.strip()]
    return "\n".join(f"<p>{rich_text(chunk)}</p>" for chunk in chunks)


def parse_table(lines: list[str]) -> tuple[list[str], list[list[str]]]:
    rows = [[cell.strip() for cell in line.strip().strip("|").split("|")] for line in lines if line.strip()]
    if len(rows) < 3:
        return [], []
    header = rows[0]
    body = rows[2:]
    return header, body


def render_pricing_section(section: dict[str, str], lang: str) -> str:
    lines = section["body"].splitlines()
    table_lines = [line for line in lines if line.strip().startswith("|")]
    before = "\n".join(line for line in lines[: lines.index(table_lines[0])] if line.strip()) if table_lines else section["body"]
    last_table_line = lines.index(table_lines[-1]) if table_lines else -1
    after = "\n".join(line for line in lines[last_table_line + 1:] if line.strip()) if table_lines else ""
    header, rows = parse_table(table_lines)

    head_html = "".join(f"<th>{rich_text(cell)}</th>" for cell in header)
    row_html = []
    for row in rows:
        cells = "".join(f"<td>{rich_text(cell)}</td>" for cell in row)
        row_html.append(f"<tr>{cells}</tr>")

    return f"""
<section class="tyre-section tyre-pricing" id="pricing">
<div class="container">
<div class="tyre-heading">
<span class="h-eyebrow">05 · {rich_text(section["title"])}</span>
<h2>{rich_text(section["title"])}</h2>
</div>
<div class="tyre-copy">{render_paragraphs(before)}</div>
<div class="tyre-table-wrap">
<table class="tyre-price-table">
<thead><tr>{head_html}</tr></thead>
<tbody>{''.join(row_html)}</tbody>
</table>
</div>
<div class="tyre-copy tyre-note">{render_paragraphs(after)}</div>
<div class="tyre-actions">
<a class="btn btn-primary" href="{localized_href('/pricing/', lang)}">{rich_text(UI[lang]["pricing"])}</a>
<a class="btn btn-ghost" href="{localized_href('/contact/', lang)}">{rich_text(UI[lang]["contact"])}</a>
</div>
</div>
</section>"""


def picture(image_key: str, lang: str, class_name: str = "tyre-photo") -> str:
    source = "/" + IMAGES[image_key]
    srcsets = {}
    for ext in ("avif", "webp", "jpg"):
        srcsets[ext] = ", ".join(f"{optimized_hero_url(source, width, ext)} {width}w" for width in (768, 1280, 1920))
    fallback = optimized_hero_url(source, 1280, "jpg")
    alt = ALT_TEXT[lang][image_key]
    return f"""
<picture class="{class_name}">
<source srcset="{srcsets['avif']}" type="image/avif"/>
<source srcset="{srcsets['webp']}" type="image/webp"/>
<img alt="{html.escape(alt)}" loading="lazy" sizes="(max-width: 900px) 100vw, 50vw" src="{fallback}" srcset="{srcsets['jpg']}" width="1280" height="960"/>
</picture>"""


def video_facade(lang: str) -> str:
    return f"""
<div class="tyre-video-panel">
<div class="tyre-video-copy">
<span class="h-eyebrow">{rich_text(UI[lang]["video_eyebrow"])}</span>
<h3>{rich_text(UI[lang]["video_title"])}</h3>
<p>{rich_text(UI[lang]["video_text"])}</p>
</div>
<button aria-label="{html.escape(ALT_TEXT[lang]['video'])}" class="tyre-video-facade" data-youtube-id="{VIDEO_ID}" type="button">
<img alt="{html.escape(ALT_TEXT[lang]['video'])}" loading="lazy" src="{VIDEO_THUMB}" width="480" height="360"/>
<span class="play-dot">▶</span>
</button>
</div>"""


def render_standard_section(section: dict[str, str], index: int, lang: str) -> str:
    media = ""
    actions = ""
    layout_class = "tyre-split"
    if index == 1:
        media = picture("changer", lang) + video_facade(lang)
        layout_class = "tyre-split tyre-split-video"
    elif index == 2:
        media = '<div class="tyre-photo-stack">' + picture("wide", lang) + picture("spoked", lang) + "</div>"
    elif index == 3:
        media = '<div class="tyre-photo-stack">' + picture("balance_fat", lang) + picture("balance_wide", lang) + "</div>"
    elif index == 4:
        actions = f'<div class="tyre-actions"><a class="btn btn-primary" href="{localized_href("/parts/", lang)}">{rich_text(UI[lang]["parts"])}</a><a class="btn btn-ghost" href="{localized_href("/contact/", lang)}">{rich_text(UI[lang]["contact"])}</a></div>'
    elif index == 6:
        actions = f'<div class="tyre-actions"><a class="btn btn-primary" href="{localized_href("/contact/", lang)}">{rich_text(UI[lang]["contact"])}</a></div>'
    elif index == 7:
        actions = f'<div class="tyre-actions"><a class="btn btn-primary" href="{localized_href("/contact/", lang)}">{rich_text(UI[lang]["book"])}</a><a class="btn btn-ghost" href="{localized_href("/faq/", lang)}">{rich_text(UI[lang]["faq"])}</a></div>'

    return f"""
<section class="tyre-section" id="section-{index:02d}">
<div class="container">
<div class="tyre-heading">
<span class="h-eyebrow">{index:02d} · {rich_text(section["title"])}</span>
<h2>{rich_text(section["title"])}</h2>
</div>
<div class="{layout_class}">
<div class="tyre-copy">
{render_paragraphs(section["body"])}
{actions}
</div>
{media}
</div>
</div>
</section>"""


def render_ai_blocks(items: list[dict[str, str]], lang: str) -> str:
    cards = []
    for item in items:
        cards.append(
            f'<article class="tyre-answer-card"><h3>{rich_text(item["label"])}</h3><p>{rich_text(item["text"])}</p></article>'
        )
    return f"""
<section class="tyre-section tyre-ai">
<div class="container">
<div class="tyre-heading compact">
<span class="h-eyebrow">{rich_text(UI[lang]["ai_title"])}</span>
<h2>{rich_text(UI[lang]["ai_title"])}</h2>
</div>
<div class="tyre-answer-grid">
{''.join(cards)}
</div>
</div>
</section>"""


def render_faq(faq: list[dict[str, str]], lang: str) -> str:
    items = []
    for question in faq:
        items.append(
            f"""
<details>
<summary><span>{rich_text(question["question"])}</span><span class="chev">⌄</span></summary>
<div class="answer">{render_paragraphs(question["answer"])}</div>
</details>"""
        )
    return f"""
<section class="tyre-section tyre-faq" id="faq">
<div class="container">
<div class="tyre-heading compact">
<span class="h-eyebrow">FAQ</span>
<h2>FAQ</h2>
</div>
<div class="tyre-faq-list">
{''.join(items)}
</div>
</div>
</section>"""


def json_ld(content: dict, lang: str) -> list[dict]:
    faq_entities = [
        {
            "@type": "Question",
            "name": item["question"],
            "acceptedAnswer": {"@type": "Answer", "text": item["answer"]},
        }
        for item in content["faq"]
    ]
    return [
        {
            "@context": "https://schema.org",
            "@type": "Service",
            "@id": canonical_url(lang) + "#service",
            "name": content["h1"],
            "serviceType": content["h1"],
            "description": content["meta_description"],
            "provider": {"@id": f"{DOMAIN}/#business"},
            "areaServed": [
                {"@type": "City", "name": "Cascais"},
                {"@type": "City", "name": "Estoril"},
                {"@type": "City", "name": "Oeiras"},
                {"@type": "City", "name": "Lisbon"},
            ],
            "url": canonical_url(lang),
            "offers": {
                "@type": "AggregateOffer",
                "priceCurrency": "EUR",
                "lowPrice": "40",
                "offerCount": "4",
                "availability": "https://schema.org/InStock",
                "url": canonical_url(lang),
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
        {
            "@context": "https://schema.org",
            "@type": "VideoObject",
            "name": UI[lang]["video_title"],
            "description": UI[lang]["video_text"],
            "thumbnailUrl": VIDEO_THUMB,
            "embedUrl": VIDEO_EMBED_URL,
            "contentUrl": VIDEO_SHORT_URL,
        },
    ]


def head_html(content: dict, lang: str) -> str:
    alternates = "\n".join(
        f'<link rel="alternate" hreflang="{code}" href="{canonical_url(code)}"/>' for code in LANGS
    )
    json_scripts = "\n".join(
        f'<script type="application/ld+json">{json.dumps(block, ensure_ascii=False)}</script>' for block in json_ld(content, lang)
    )
    preload = hero_preload_links("/" + IMAGES["hero"])
    og_locale = {"en": "en_US", "ru": "ru_RU", "uk": "uk_UA", "pt": "pt_PT"}[lang]
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
<meta content="{DOMAIN}/{IMAGES["hero"]}" property="og:image"/>
<meta content="{html.escape(ALT_TEXT[lang]["hero"])}" property="og:image:alt"/>
<meta content="{og_locale}" property="og:locale"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="{html.escape(content["seo_title"])}" name="twitter:title"/>
<meta content="{html.escape(content["meta_description"])}" name="twitter:description"/>
<meta content="{DOMAIN}/{IMAGES["hero"]}" name="twitter:image"/>
<meta content="{html.escape(ALT_TEXT[lang]["hero"])}" name="twitter:image:alt"/>
<link href="{canonical_url(lang)}" rel="canonical"/>
{alternates}
<link rel="alternate" hreflang="x-default" href="{canonical_url("en")}"/>
<link href="/photos/favicon.ico" rel="icon" sizes="any"/>
<link href="/photos/favicon-32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="/photos/apple-touch-icon.png" rel="apple-touch-icon" sizes="180x180"/>
<link href="/photos/site.webmanifest" rel="manifest"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Saira:wght@300;400;500;600;700;800;900&amp;family=Saira+Condensed:wght@400;600;700;800;900&amp;family=Inter:wght@300;400;500;600;700&amp;display=swap" rel="stylesheet"/>
{preload}
{json_scripts}
<link href="/assets/main.css?v={CACHE_BUST}" rel="stylesheet"/>
<style>{PAGE_CSS}</style>
</head>"""


def render_page(content: dict, lang: str) -> str:
    before, after = chrome_fragments(lang)
    sections_html = []
    for index, section in enumerate(content["sections"], start=1):
        if index == 5:
            sections_html.append(render_pricing_section(section, lang))
        else:
            sections_html.append(render_standard_section(section, index, lang))
    body = f"""
<body>
{before}
<main>
<section class="tyre-hero">
<div aria-hidden="true" class="tyre-hero-bg"></div>
<div class="container">
<div class="crumb"><a href="{localized_href('/', lang)}">{rich_text(UI[lang]["home"])}</a><span class="sep">→</span><a href="{localized_href('/services/', lang)}">{rich_text(UI[lang]["services"])}</a><span class="sep">→</span><span>{rich_text(UI[lang]["crumb"])}</span></div>
<span class="h-eyebrow">{rich_text(UI[lang]["eyebrow"])}</span>
<h1>{rich_text(content["h1"])}</h1>
<p class="lead">{rich_text(content["hero"])}</p>
<div class="subpage-cta">
<a class="btn btn-primary" href="{localized_href('/contact/', lang)}">{rich_text(UI[lang]["book"])}</a>
<a class="btn btn-ghost" href="{localized_href('/pricing/', lang)}">{rich_text(UI[lang]["pricing"])}</a>
<a class="btn btn-ghost" href="{localized_href('/motorcycle-service/', lang)}">{rich_text(UI[lang]["service"])}</a>
</div>
</div>
</section>
{''.join(sections_html)}
{render_ai_blocks(content["ai"], lang)}
<section class="tyre-cta">
<div class="container">
<p>{rich_text(content["cta"])}</p>
<div class="tyre-actions">
<a class="btn btn-primary" data-wa="" href="https://wa.me/351917961230" rel="noopener" target="_blank">{rich_text(UI[lang]["contact"])}</a>
<a class="btn btn-ghost" href="{localized_href('/faq/', lang)}">{rich_text(UI[lang]["faq"])}</a>
</div>
</div>
</section>
{render_faq(content["faq"], lang)}
</main>
{after}
<script>
document.querySelectorAll('.tyre-video-facade').forEach(function(button) {{
  button.addEventListener('click', function() {{
    var id = button.getAttribute('data-youtube-id');
    var iframe = document.createElement('iframe');
    iframe.src = 'https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0';
    iframe.title = button.getAttribute('aria-label') || 'Workshop video';
    iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
    iframe.allowFullscreen = true;
    iframe.loading = 'lazy';
    button.replaceWith(iframe);
  }});
}});
</script>
</body>
</html>"""
    return head_html(content, lang) + body


PAGE_CSS = """.tyre-hero{position:relative;isolation:isolate;overflow:hidden;min-height:78vh;padding:150px 0 84px;background:#080808}
.tyre-hero::after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(90deg,rgba(8,8,8,.92),rgba(8,8,8,.68) 45%,rgba(8,8,8,.22)),linear-gradient(180deg,rgba(8,8,8,.2),#080808 95%)}
.tyre-hero-bg{position:absolute;inset:0;z-index:-2;background-size:cover;background-position:center;filter:saturate(.94) contrast(1.04) brightness(.72);""" + hero_background_css("/" + IMAGES["hero"]) + """}
.tyre-hero h1{max-width:min(880px,76vw,calc(100vw - 40px));margin:18px 0 24px;font-family:'Saira Condensed',sans-serif;font-size:clamp(34px,7.6vw,116px);font-weight:900;line-height:.9;text-transform:uppercase;color:#fff;overflow-wrap:anywhere}
.tyre-hero .lead{max-width:min(900px,76vw,calc(100vw - 40px));font-size:clamp(18px,1.35vw,23px);line-height:1.62;color:var(--text)}
.tyre-section{padding:clamp(58px,7vw,96px) 0;background:#080808;border-top:1px solid var(--border)}
.tyre-heading{display:grid;grid-template-columns:minmax(180px,.62fr) minmax(0,1.38fr);gap:36px;align-items:end;margin-bottom:34px}
.tyre-heading.compact{display:block;max-width:780px}
.tyre-heading h2{max-width:min(820px,76vw,calc(100vw - 40px));margin:0;font-family:'Saira Condensed',sans-serif;font-size:clamp(34px,5vw,72px);font-weight:900;line-height:.94;text-transform:uppercase;color:#fff;overflow-wrap:anywhere}
.tyre-split{display:grid;grid-template-columns:minmax(0,1fr) minmax(340px,.86fr);gap:34px;align-items:start}
.tyre-split-video{grid-template-columns:minmax(0,.9fr) minmax(390px,1fr)}
.tyre-copy{font-size:clamp(17px,1.28vw,21px);line-height:1.68;color:var(--text)}
.tyre-copy p{margin:0 0 18px;max-width:min(820px,76vw,calc(100vw - 40px));overflow-wrap:break-word}
.tyre-note p{font-size:16px;color:var(--text-dim)}
.tyre-actions{display:flex;gap:14px;flex-wrap:wrap;max-width:min(760px,76vw,calc(100vw - 40px));margin-top:26px}
.tyre-photo{display:block;overflow:hidden;border:1px solid var(--border);border-radius:var(--radius-lg);background:#111}
.tyre-photo img{display:block;width:100%;height:100%;min-height:360px;object-fit:cover}
.tyre-photo-stack{display:grid;gap:18px}
.tyre-video-panel{display:grid;grid-template-columns:.9fr 1fr;gap:18px;align-items:stretch;margin-top:18px;border:1px solid var(--border);border-radius:var(--radius-lg);background:var(--surface);overflow:hidden}
.tyre-video-copy{padding:28px 26px;align-self:center}
.tyre-video-copy h3{margin:12px 0 10px;font-family:'Saira Condensed',sans-serif;font-size:clamp(25px,3vw,42px);font-weight:900;line-height:.98;text-transform:uppercase;color:#fff}
.tyre-video-copy p{color:var(--text-dim);line-height:1.55}
.tyre-video-facade{position:relative;display:block;min-height:280px;border:0;padding:0;background:#000;cursor:pointer;overflow:hidden}
.tyre-video-facade img{width:100%;height:100%;object-fit:cover;filter:brightness(.72)}
.tyre-video-panel iframe{display:block;width:100%;height:100%;min-height:340px;border:0}
.play-dot{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:70px;height:70px;border-radius:50%;display:grid;place-items:center;background:var(--accent);color:#fff;font-size:24px;box-shadow:0 12px 32px rgba(255,87,34,.35)}
.tyre-table-wrap{overflow-x:auto;border:1px solid var(--border);border-radius:var(--radius-lg);background:rgba(255,255,255,.025)}
.tyre-price-table{width:100%;border-collapse:collapse;min-width:760px}
.tyre-price-table th,.tyre-price-table td{padding:22px 24px;border-bottom:1px solid var(--border);text-align:left}
.tyre-price-table th{font-family:'Saira',sans-serif;font-size:13px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);background:rgba(255,87,34,.05)}
.tyre-price-table td{font-family:'Saira Condensed',sans-serif;font-size:24px;font-weight:800;color:#fff}
.tyre-price-table td:first-child{color:var(--text)}
.tyre-ai{background:#0b0b0b}
.tyre-answer-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:28px}
.tyre-answer-card{border:1px solid var(--border);border-radius:var(--radius-lg);background:var(--surface);padding:26px 24px}
.tyre-answer-card h3{font-family:'Saira Condensed',sans-serif;font-size:24px;font-weight:900;line-height:1;text-transform:uppercase;color:#fff;margin-bottom:12px}
.tyre-answer-card p{font-size:15px;line-height:1.65;color:var(--text-dim)}
.tyre-cta{padding:clamp(54px,6vw,82px) 0;background:#101010;border-top:1px solid var(--border);text-align:center}
.tyre-cta .container{max-width:980px}
.tyre-cta p{font-size:clamp(19px,1.6vw,25px);line-height:1.6;color:#fff}
.tyre-cta .tyre-actions{justify-content:center}
.tyre-faq-list{display:grid;gap:12px}
.tyre-faq-list details{border:1px solid var(--border);border-radius:var(--radius-lg);background:var(--surface);overflow:hidden}
.tyre-faq-list summary{display:flex;gap:18px;align-items:flex-start;justify-content:space-between;cursor:pointer;padding:22px 24px;list-style:none;font-family:'Saira Condensed',sans-serif;font-size:clamp(18px,1.6vw,24px);font-weight:800;line-height:1.1;text-transform:uppercase;color:#fff}
.tyre-faq-list summary::-webkit-details-marker{display:none}
.tyre-faq-list .chev{color:var(--accent);transition:transform .2s var(--ease)}
.tyre-faq-list details[open] .chev{transform:rotate(180deg)}
.tyre-faq-list .answer{padding:0 24px 24px;color:var(--text-dim);font-size:16px;line-height:1.65}
@media (max-width:980px){.tyre-heading,.tyre-split,.tyre-split-video{grid-template-columns:1fr}.tyre-answer-grid{grid-template-columns:1fr}.tyre-video-panel{grid-template-columns:1fr}.tyre-photo img{min-height:260px}}
@media (max-width:640px){.tyre-hero{min-height:auto;padding:124px 0 62px}.tyre-hero h1{max-width:calc(100vw - 40px);font-size:clamp(30px,9vw,38px);line-height:.94;overflow-wrap:anywhere}.tyre-hero .lead,.tyre-copy,.tyre-copy p{max-width:calc(100vw - 40px);overflow-wrap:break-word}.tyre-section{padding:48px 0}.tyre-heading{gap:16px;margin-bottom:24px}.tyre-heading h2{font-size:clamp(31px,11vw,42px);overflow-wrap:anywhere}.tyre-actions{display:grid;grid-template-columns:1fr;max-width:calc(100vw - 40px)}.tyre-actions .btn{width:100%;justify-content:center;white-space:normal;text-align:center;line-height:1.15;padding-left:18px;padding-right:18px}.tyre-video-copy{padding:24px 20px}.tyre-price-table th,.tyre-price-table td{padding:18px}.play-dot{width:58px;height:58px}}
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
