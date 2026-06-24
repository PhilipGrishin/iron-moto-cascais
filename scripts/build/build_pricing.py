#!/usr/bin/env python3
"""Generate /pricing/ pages in 4 languages using motorcycle-service as the chrome template.

Re-run after editing pricing_data.py to refresh all 4 pages.
"""

import html
import json
import re
from pathlib import Path
from copy import deepcopy
from bs4 import BeautifulSoup, FeatureNotFound

from hero_images import hero_background_css
from localize_internal_links import rewrite_href
from pricing_data import LABELS, SECTIONS, LANGS
from seo_meta import upsert_robots_image_preview

SITE_ROOT = Path(__file__).resolve().parents[2]
TEMPLATE = SITE_ROOT / "motorcycle-service" / "index.html"
DOMAIN = "https://ironcustommotors.com"
I18N_FILE = SITE_ROOT / "scripts" / "build" / "i18n.json"
GLOBAL_I18N = json.loads(I18N_FILE.read_text(encoding="utf-8"))

OG_LOCALES = {"en": "en_US", "ru": "ru_RU", "uk": "uk_UA", "pt": "pt_PT"}
HREFLANG_CODES = {"en": "en", "ru": "ru", "uk": "uk", "pt": "pt-PT"}

# Per-page background photo (shared across languages)
HERO_BG = "/photos/parts-shelf-1600.jpg"
HERO_BG_MOBILE = "/photos/parts-shelf-800.jpg"

try:
    BeautifulSoup("", "lxml")
    HTML_PARSER = "lxml"
except FeatureNotFound:
    HTML_PARSER = "html.parser"


def parse_html(markup: str) -> BeautifulSoup:
    return BeautifulSoup(markup, HTML_PARSER)


def esc(text: str) -> str:
    """Escape for HTML attribute or text content (preserves &mdash; etc.)."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


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


def set_language_state(soup: BeautifulSoup, lang: str) -> None:
    current = soup.find(id="langCurrent")
    if current:
        current.string = lang.upper()
    for button in soup.select("button[data-lang]"):
        if button.get("data-lang") == lang:
            button["aria-current"] = "true"
        elif button.has_attr("aria-current"):
            del button["aria-current"]


def url_for(lang: str, path: str = "pricing/") -> str:
    if lang == "en":
        return f"{DOMAIN}/{path}"
    return f"{DOMAIN}/{lang}/{path}"


def build_pricing_main(lang: str) -> str:
    """Build the inner content for <main> as HTML string."""
    L = LABELS[lang]
    parts = []

    # --- Hero subpage ---
    parts.append(f'''<section class="subpage pricing-hero">
  <div class="bg" aria-hidden="true"></div>
  <div class="container">
    <div class="crumb">
      <a href="/{lang+"/" if lang!="en" else ""}">{ {"en":"Home","ru":"Главная","uk":"Головна","pt":"Início"}[lang] }</a>
      <span class="sep">→</span>
      <span>{L["eyebrow"]}</span>
    </div>
    <span class="proj-badge">{L["eyebrow"]}</span>
    <h1>{L["h1"]}</h1>
    <p class="lead">{L["lead"]}</p>
    <div class="subpage-cta">
      <a href="#contact" class="btn btn-primary" data-cta="book">{L["book_service"]}
        <svg class="arrow" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
      </a>
      <a href="{L["pdf_filename"]}" class="btn btn-ghost pdf-dl" target="_blank" rel="noopener" data-cta="pdf">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v12m0 0l-4-4m4 4l4-4M5 21h14"/></svg>
        {L["download_pdf"]}
      </a>
    </div>
    <p class="tax-note">{L["all_prices_include"]}</p>
  </div>
</section>''')

    # --- Sections ---
    for section in SECTIONS:
        num = section["num"]
        anchor = section["anchor"]
        sec_title = section["title"][lang]
        h2 = section["h2"][lang]
        intro = section["intro"][lang]

        parts.append(f'''
<section class="sub-section price-section" id="sec-{anchor}">
  <div class="container">
    <div class="section-eyebrow">{num} · <span>{sec_title}</span></div>
    <div class="heading reveal">
      <h2>{h2}</h2>
      <p class="lead">{intro}</p>
    </div>''')

        # Type-specific content
        if "cards" in section and "subgroups" not in section:
            # SEC_01, SEC_06 use cards
            parts.append('    <div class="price-cards">')
            for card in section["cards"]:
                name = card["name"][lang]
                desc = card["desc"][lang]
                price = card["price"]
                price_from = card.get("price_from")
                price_suffix = card.get("price_suffix")

                price_html = ""
                if price_from:
                    price_html += f'<span class="from">{LABELS[lang]["from"]}</span> '
                price_html += f'<span class="amount">{price}</span>'
                if price_suffix == "per_hour":
                    price_html += f'<span class="suffix">{LABELS[lang]["per_hour"]}</span>'

                tags_html = ""
                if "tags" in card:
                    tags_html = '<ul class="card-tags">'
                    for t in card["tags"][lang]:
                        tags_html += f'<li>{esc(t)}</li>'
                    tags_html += '</ul>'

                parts.append(f'''      <div class="price-card">
        <div class="card-head">
          <h3>{esc(name)}</h3>
          <div class="price">{price_html}</div>
        </div>
        <p class="card-desc">{esc(desc)}</p>
        {tags_html}
      </div>''')
            parts.append('    </div>')

            # Note
            if "note" in section:
                parts.append(f'    <p class="section-note">{esc(section["note"][lang])}</p>')

        elif num == "02":
            # Scheduled maintenance: 4 brand-group cards with checklists
            parts.append(f'    <div class="consumables-banner"><strong>{esc(section["consumables_label"][lang])}</strong> — {esc(section["consumables_text"][lang])}</div>')
            parts.append('    <div class="group-cards">')
            for g in section["groups"]:
                price = g["price"]
                from_html = f'<span class="from">{LABELS[lang]["from"]}</span> ' if g.get("price_from") else ""
                checklist_html = "".join(f'<li>{esc(item)}</li>' for item in g["checklist"][lang])
                parts.append(f'''      <div class="group-card">
        <div class="group-head">
          <h4>{esc(g["name"])}</h4>
          <div class="price">{from_html}<span class="amount">{price}</span></div>
        </div>
        <ul class="group-list">{checklist_html}</ul>
      </div>''')
            parts.append('    </div>')
            parts.append(f'    <p class="section-note">{esc(section["note"][lang])}</p>')

        elif num == "03":
            # Brakes / carbs: subgroups
            for sg in section["subgroups"]:
                parts.append(f'    <h3 class="subgroup-title">{esc(sg["label"][lang])}</h3>')
                parts.append('    <div class="price-list">')
                for it in sg["items"]:
                    name = it["name"][lang]
                    desc = it.get("desc", {}).get(lang, "")
                    price = it["price"]
                    from_html = f'<span class="from">{LABELS[lang]["from"]}</span> ' if it.get("price_from") else ""
                    parts.append(f'''      <div class="price-row">
        <div class="row-text">
          <div class="row-name">{esc(name)}</div>
          {f'<div class="row-desc">{esc(desc)}</div>' if desc else ""}
        </div>
        <div class="row-price">{from_html}<span class="amount">{price}</span></div>
      </div>''')
                parts.append('    </div>')

        elif num == "04":
            # Tables for valves + tyres + chain card
            vt = section["valve_table"]
            parts.append(f'    <h3 class="subgroup-title">{esc(vt["title"][lang])}</h3>')
            cols = vt["cols"][lang]
            head_cells = "".join(f'<th>{esc(c)}</th>' for c in cols)
            body_rows = ""
            for r in vt["rows"]:
                body_rows += "<tr>" + "".join(f'<td>{esc(c)}</td>' for c in r) + "</tr>"
            parts.append(f'''    <div class="price-table-wrap">
      <table class="price-table">
        <thead><tr>{head_cells}</tr></thead>
        <tbody>{body_rows}</tbody>
      </table>
    </div>
    <p class="section-note">{esc(vt["note"][lang])}</p>''')

            tt = section["tyre_table"]
            parts.append(f'    <h3 class="subgroup-title">{esc(tt["title"][lang])}</h3>')
            head_cells = "".join(f'<th>{esc(c)}</th>' for c in tt["cols"][lang])
            body_rows = ""
            for r in tt["rows"]:
                cells = [r[0][lang]] + r[1:]
                body_rows += "<tr>" + "".join(f'<td>{esc(c)}</td>' for c in cells) + "</tr>"
            parts.append(f'''    <div class="price-table-wrap">
      <table class="price-table">
        <thead><tr>{head_cells}</tr></thead>
        <tbody>{body_rows}</tbody>
      </table>
    </div>
    <p class="section-note">{esc(tt["note"][lang])}</p>''')

            ch = section["chain"]
            parts.append(f'''    <div class="price-card chain-card">
      <div class="card-head">
        <h3>{esc(ch["name"][lang])}</h3>
        <div class="price"><span class="amount">{ch["price"]}</span></div>
      </div>
      <p class="card-desc">{esc(ch["desc"][lang])}</p>
    </div>
    <p class="section-note">{esc(ch["note"][lang])}</p>''')

        elif num == "05":
            # 3 columns of accessories / electrical / tuning
            parts.append('    <div class="acc-cols">')
            for col in section["columns"]:
                parts.append(f'      <div class="acc-col"><h3 class="subgroup-title">{esc(col["label"][lang])}</h3><ul class="acc-list">')
                for name_dict, price in col["items"]:
                    parts.append(f'<li><span class="acc-name">{esc(name_dict[lang])}</span><span class="acc-price">{price}</span></li>')
                parts.append('      </ul></div>')
            parts.append('    </div>')
            parts.append(f'    <p class="section-note">{esc(section["note_install"][lang])}</p>')
            parts.append(f'    <p class="section-note section-note-alt">{esc(section["note_sourcing"][lang])}</p>')

        elif num == "07":
            # Customizing & community
            parts.append(f'''    <div class="custom-block">
      <h3>{esc(section["custom_title"][lang])}</h3>
      <p>{esc(section["custom_body"][lang])}</p>
    </div>''')
            parts.append('    <div class="community-trio">')
            for idx, c in enumerate(section["community"], 1):
                parts.append(f'''      <div class="trio-item">
        <span class="trio-num">{idx:02d}</span>
        <h4>{esc(c["title"][lang])}</h4>
        <p>{esc(c["body"][lang])}</p>
      </div>''')
            parts.append('    </div>')
            parts.append(f'    <p class="section-slogan">{esc(section["slogan"][lang])}</p>')

        parts.append('  </div>')
        parts.append('</section>')

    # --- CTA section ---
    home_for_lang = "/" + (lang + "/" if lang != "en" else "")
    parts.append(f'''
<section class="cta-back" id="contact">
  <div class="container">
    <h2>{L["cta_title"]}</h2>
    <p class="lead">{L["cta_text"]}</p>
    <div class="btns">
      <a href="https://wa.me/351917961230" data-wa class="btn btn-primary" target="_blank" rel="noopener">{L["whatsapp"]}</a>
      <a href="tel:+351917961230" class="btn btn-ghost">+351 917 961 230</a>
    </div>
  </div>
</section>''')

    # --- Disclaimer ---
    parts.append(f'''
<section class="sub-section disclaimer">
  <div class="container">
    <h3>{L["disclaimer_title"]}</h3>
    <p>{esc(L["disclaimer"])}</p>
  </div>
</section>''')

    return "\n".join(parts)


PAGE_STYLE = """
.pricing-hero{padding:160px 0 80px;min-height:auto}
.pricing-hero .bg{""" + hero_background_css(HERO_BG, 1280) + """;background-size:cover;background-position:center;filter:saturate(.8) contrast(1.05) brightness(.4)}
@media (max-width:900px){.pricing-hero .bg{""" + hero_background_css(HERO_BG_MOBILE, 768) + """}}
.pricing-hero .lead{font-family:var(--font-ui);font-size:clamp(16px,1.4vw,19px);line-height:1.65;color:var(--text-dim);max-width:62ch;margin-bottom:28px}
.pricing-hero .tax-note{margin-top:24px;font-family:var(--font-ui);font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--accent);font-weight:600}
.pdf-dl svg{stroke:currentColor;flex-shrink:0}

.price-section{padding:var(--gap) 0;background:#0a0a0a;border-top:1px solid var(--border)}
.section-eyebrow{font-family:var(--font-ui);font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--text-mute);margin-bottom:18px}
.section-eyebrow span{color:var(--accent);font-weight:600}
.price-section .heading{margin-bottom:40px;padding-bottom:30px;border-bottom:1px solid var(--border);display:grid;grid-template-columns:1fr 1.4fr;gap:60px;align-items:end}
.price-section .heading h2{margin:0;font-family:var(--font-display);font-weight:800;text-transform:uppercase;font-size:clamp(24px,3.2vw,42px);line-height:.95;letter-spacing:-.005em;color:#fff}
.price-section .heading .lead{margin:0;font-family:var(--font-ui);font-size:clamp(16px,1.4vw,19px);line-height:1.55;color:var(--text-dim)}
@media (max-width:1100px){.price-section .heading{grid-template-columns:1fr;gap:18px}}

/* Cards */
.price-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
@media (max-width:900px){.price-cards{grid-template-columns:1fr}}
.price-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);padding:28px 26px;transition:border-color .25s var(--ease),transform .25s var(--ease)}
.price-card:hover{border-color:var(--accent);transform:translateY(-2px)}
.card-head{display:flex;justify-content:space-between;align-items:flex-start;gap:18px;margin-bottom:16px;flex-wrap:wrap}
.card-head h3{margin:0;font-family:var(--font-display);font-weight:800;text-transform:uppercase;font-size:clamp(17px,1.6vw,22px);line-height:1.05;color:#fff;letter-spacing:-.005em}
.price{font-family:var(--font-display);font-weight:800;text-transform:uppercase;font-size:clamp(20px,2.2vw,28px);line-height:1;color:var(--accent);white-space:nowrap;flex-shrink:0}
.price .from,.price .suffix{font-family:var(--font-ui);font-weight:500;font-size:.55em;letter-spacing:.05em;color:var(--text-mute);text-transform:uppercase;margin-right:4px}
.price .suffix{margin-left:4px;margin-right:0}
.card-desc{font-family:var(--font-ui);font-size:15px;line-height:1.55;color:var(--text-dim);margin-bottom:18px}
.card-tags{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:6px}
.card-tags li{position:relative;padding-left:18px;font-family:var(--font-ui);font-size:13px;color:var(--text);line-height:1.45}
.card-tags li:before{content:'';position:absolute;left:0;top:8px;width:8px;height:1px;background:var(--accent)}

/* Group cards (section 02) */
.consumables-banner{background:linear-gradient(135deg,rgba(255,87,34,.08),transparent 60%);border:1px solid var(--border);border-radius:var(--radius-lg);padding:22px 28px;margin-bottom:32px;font-family:var(--font-ui);font-size:15px;line-height:1.55;color:var(--text-dim)}
.consumables-banner strong{display:inline-block;color:var(--accent);font-weight:700;text-transform:uppercase;letter-spacing:.08em;font-size:13px;margin-right:8px}
.group-cards{display:grid;grid-template-columns:repeat(2,1fr);gap:18px;margin-bottom:24px}
@media (max-width:900px){.group-cards{grid-template-columns:1fr}}
.group-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);padding:26px 28px}
.group-head{display:flex;justify-content:space-between;align-items:center;gap:16px;margin-bottom:18px;padding-bottom:16px;border-bottom:1px solid var(--border)}
.group-head h4{margin:0;font-family:var(--font-display);font-weight:800;text-transform:uppercase;font-size:18px;letter-spacing:.02em;color:#fff;line-height:1}
.group-list{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:1fr 1fr;gap:6px 18px}
.group-list li{font-family:var(--font-ui);font-size:13px;color:var(--text-dim);position:relative;padding-left:14px;line-height:1.4}
.group-list li:before{content:'';position:absolute;left:0;top:8px;width:6px;height:1px;background:var(--accent)}
@media (max-width:600px){.group-list{grid-template-columns:1fr}}

/* Section 03 / list */
.subgroup-title{margin:36px 0 18px;font-family:var(--font-display);font-weight:800;text-transform:uppercase;font-size:clamp(20px,2.4vw,28px);color:#fff;letter-spacing:.005em;line-height:1.05}
.price-list{display:flex;flex-direction:column;border-top:1px solid var(--border)}
.price-row{display:grid;grid-template-columns:1fr auto;gap:20px;padding:18px 4px;border-bottom:1px solid var(--border);align-items:start}
.row-text .row-name{font-family:var(--font-ui);font-weight:600;color:#fff;font-size:16px;line-height:1.3;margin-bottom:4px}
.row-text .row-desc{font-family:var(--font-ui);font-size:14px;color:var(--text-dim);line-height:1.45}
.row-price{font-family:var(--font-display);font-weight:800;font-size:clamp(18px,2vw,24px);color:var(--accent);white-space:nowrap;line-height:1;align-self:center}

/* Section 04 tables */
.price-table-wrap{overflow-x:auto;margin-bottom:14px;border:1px solid var(--border);border-radius:var(--radius-lg)}
.price-table{width:100%;border-collapse:collapse;font-family:var(--font-ui)}
.price-table thead{background:rgba(255,87,34,.06)}
.price-table th{padding:14px 18px;font-family:var(--font-ui);font-weight:700;text-transform:uppercase;font-size:11px;letter-spacing:.12em;text-align:left;color:var(--accent);border-bottom:1px solid var(--border)}
.price-table td{padding:14px 18px;font-size:14px;color:var(--text);border-bottom:1px solid var(--border)}
.price-table tbody tr:last-child td{border-bottom:none}
.price-table tbody tr:hover{background:rgba(255,255,255,.02)}
.price-table td:first-child{font-weight:600;color:#fff}
.price-table td:not(:first-child){font-family:var(--font-display);font-weight:700;color:var(--accent);font-size:16px}

/* Accessories columns (sec 05) */
.acc-cols{display:grid;grid-template-columns:repeat(3,1fr);gap:30px}
@media (max-width:900px){.acc-cols{grid-template-columns:1fr;gap:20px}}
.acc-col h3.subgroup-title{margin-top:0;font-size:clamp(18px,1.8vw,22px)}
.acc-list{list-style:none;padding:0;margin:0;border-top:1px solid var(--border)}
.acc-list li{display:flex;justify-content:space-between;gap:14px;padding:11px 0;border-bottom:1px solid var(--border);align-items:baseline}
.acc-name{font-family:var(--font-ui);font-size:14px;color:#fff}
.acc-price{font-family:var(--font-display);font-weight:700;color:var(--accent);font-size:14px;white-space:nowrap;letter-spacing:.02em}

/* Section 06: chain card already covered by .price-card */
.chain-card{margin-top:24px;max-width:560px}

/* Section 07: customizing & community */
.custom-block{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);padding:36px clamp(24px,4vw,48px);margin-bottom:30px}
.custom-block h3{margin:0 0 14px;font-family:var(--font-display);font-weight:800;text-transform:uppercase;font-size:clamp(22px,2.6vw,32px);color:#fff;line-height:1.05;letter-spacing:-.005em}
.custom-block p{margin:0;font-family:var(--font-ui);font-size:15px;line-height:1.6;color:var(--text-dim)}
.community-trio{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-bottom:24px}
@media (max-width:900px){.community-trio{grid-template-columns:1fr}}
.trio-item{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);padding:26px 24px}
.trio-num{display:inline-block;font-family:var(--font-display);font-weight:800;color:var(--accent);font-size:32px;line-height:1;margin-bottom:14px}
.trio-item h4{margin:0 0 10px;font-family:var(--font-display);font-weight:800;text-transform:uppercase;font-size:16px;color:#fff;letter-spacing:.02em}
.trio-item p{margin:0;font-family:var(--font-ui);font-size:13px;line-height:1.5;color:var(--text-dim)}
.section-slogan{margin-top:24px;font-family:var(--font-ui);font-size:15px;line-height:1.55;color:var(--text-dim);font-style:italic;max-width:80ch}

/* Notes */
.section-note{margin-top:18px;font-family:var(--font-ui);font-size:13px;line-height:1.55;color:var(--text-mute);max-width:80ch;font-style:italic}
.section-note-alt{color:var(--text-dim);font-style:normal}

/* Disclaimer */
.disclaimer{background:#0e0e12}
.disclaimer h3{font-family:var(--font-ui);font-weight:700;text-transform:uppercase;font-size:12px;letter-spacing:.2em;color:var(--accent);margin-bottom:14px}
.disclaimer p{font-family:var(--font-ui);font-size:13px;line-height:1.65;color:var(--text-mute);max-width:90ch}
"""


def build_jsonld(lang: str) -> dict:
    """Schema.org Service + Offer markup — what AI engines and Google use."""
    L = LABELS[lang]
    page_url = url_for(lang)

    offers = []
    for section in SECTIONS:
        if section["num"] == "07":
            continue
        # Skip table-only and column-style sections in JSON-LD (only push card-style)
        if section["num"] in ("01", "02", "06"):
            items = section.get("cards") or section.get("groups", [])
            for it in items:
                name_dict = it.get("name", {"en": it.get("name")} if isinstance(it.get("name"), str) else it.get("name", {}))
                if isinstance(name_dict, dict):
                    name = name_dict[lang]
                else:
                    name = name_dict
                price = it.get("price", "")
                # Parse price number
                m = re.search(r"(\d+)", price)
                if not m: continue
                amount = m.group(1)
                offer = {
                    "@type": "Offer",
                    "name": name,
                    "price": amount,
                    "priceCurrency": "EUR",
                    "url": f"{page_url}#sec-{section['anchor']}",
                }
                offers.append(offer)

    return {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": f"{page_url}#webpage",
                "url": page_url,
                "name": L["page_title"],
                "description": L["page_description"],
                "inLanguage": lang,
                "isPartOf": {"@id": f"{DOMAIN}/#website"},
                "about": {"@id": f"{DOMAIN}/#business"},
                "breadcrumb": {
                    "@type": "BreadcrumbList",
                    "itemListElement": [
                        {"@type": "ListItem", "position": 1, "name": {"en":"Home","ru":"Главная","uk":"Головна","pt":"Início"}[lang], "item": f"{DOMAIN}/{lang+'/' if lang!='en' else ''}"},
                        {"@type": "ListItem", "position": 2, "name": L["eyebrow"], "item": page_url},
                    ],
                },
            },
            {
                "@type": "OfferCatalog",
                "name": L["page_title"],
                "url": page_url,
                "inLanguage": lang,
                "provider": {"@id": f"{DOMAIN}/#business"},
                "itemListElement": offers,
            },
        ],
    }


def absolutize_paths(soup):
    """Convert relative paths (../foo, ./foo) in head links/scripts/imgs to absolute /foo.
    Required so a page at /ru/pricing/ correctly resolves /photos, /assets."""
    for tag_name, attr in [("link", "href"), ("script", "src"), ("img", "src")]:
        for el in soup.find_all(tag_name):
            v = el.get(attr)
            if not v:
                continue
            if v.startswith(("../", "./")):
                stripped = re.sub(r"^(\.\./)+|^\./", "", v)
                el[attr] = "/" + stripped


def build_page(lang: str) -> str:
    # Load template (motorcycle-service is fully self-contained with all chrome)
    template = TEMPLATE.read_text(encoding="utf-8")
    soup = parse_html(template)

    # 0) Absolutize all asset paths — pricing pages live at /pricing/ AND /ru/pricing/
    # etc., so relative paths from /motorcycle-service/ template would break.
    absolutize_paths(soup)

    # 1) html lang
    html_el = soup.find("html")
    html_el["lang"] = lang
    html_el["data-lang"] = lang

    L = LABELS[lang]
    page_url = url_for(lang)
    page_path = "pricing/" if lang == "en" else f"{lang}/pricing/"

    # 2) <title>
    soup.title.string = L["page_title"]

    # 3) Meta description
    md = soup.find("meta", attrs={"name": "description"})
    md["content"] = L["page_description"]

    # 4) Canonical
    can = soup.find("link", attrs={"rel": "canonical"})
    can["href"] = page_url

    # 5) OG / Twitter
    def set_meta(prop=None, name=None, content=None):
        sel = {"property": prop} if prop else {"name": name}
        el = soup.find("meta", attrs=sel)
        if el:
            el["content"] = content
    set_meta(prop="og:title", content=L["page_title"])
    set_meta(prop="og:description", content=L["page_description"])
    set_meta(prop="og:url", content=page_url)
    set_meta(prop="og:locale", content=OG_LOCALES[lang])
    set_meta(name="twitter:title", content=L["page_title"])
    set_meta(name="twitter:description", content=L["page_description"])
    upsert_robots_image_preview(soup)

    # 6) Remove existing JSON-LD; add new one
    for s in soup.head.find_all("script", attrs={"type": "application/ld+json"}):
        s.decompose()
    jsonld = soup.new_tag("script", type="application/ld+json")
    jsonld.string = json.dumps(build_jsonld(lang), ensure_ascii=False)
    soup.head.append(jsonld)

    # 7) Replace hreflang block
    for el in soup.head.find_all("link", attrs={"rel": "alternate", "hreflang": True}):
        el.decompose()
    for hl in ["en", "ru", "uk", "pt"]:
        link = soup.new_tag("link", rel="alternate", hreflang=HREFLANG_CODES[hl], href=url_for(hl))
        soup.head.append(link)
    xd = soup.new_tag("link", rel="alternate", hreflang="x-default", href=url_for("en"))
    soup.head.append(xd)

    # 8) Replace inline <style> with pricing-specific styles
    style_tag = soup.head.find("style")
    if style_tag:
        style_tag.string = PAGE_STYLE
    else:
        style_tag = soup.new_tag("style")
        style_tag.string = PAGE_STYLE
        soup.head.append(style_tag)

    # 9) Replace <main> children with pricing content
    main = soup.find("main")
    main.clear()
    main_html = build_pricing_main(lang)
    new_main = parse_html(f"<wrapper>{main_html}</wrapper>")
    for child in list(new_main.find("wrapper").children):
        main.append(child)

    # 10) Update chrome links to the correct localized URLs, including custom slugs.
    if lang != "en":
        for a in soup.find_all("a", href=True):
            a["href"] = rewrite_href(a["href"], lang)

    apply_i18n(soup, lang)
    set_language_state(soup, lang)

    return str(soup)


def main():
    for lang in LANGS:
        html_out = build_page(lang)
        if lang == "en":
            out = SITE_ROOT / "pricing" / "index.html"
        else:
            out = SITE_ROOT / lang / "pricing" / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html_out, encoding="utf-8")
        print(f"wrote {out.relative_to(SITE_ROOT)}  ({len(html_out):,} bytes)")


if __name__ == "__main__":
    main()
