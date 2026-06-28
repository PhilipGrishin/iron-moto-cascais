#!/usr/bin/env python3
"""Generate the Authorized Dealer hub source page.

The English page is the canonical source; build_i18n.py creates /ru/, /uk/
and /pt/ copies with localized visible text, metadata, hreflang and JSON-LD
URL adjustments. Future dealer-brand cards are added in
authorized_dealer_data.AUTHORIZED_DEALER_BRANDS.
"""

from __future__ import annotations

import json
from html import escape
from pathlib import Path

from authorized_dealer_data import (
    AUTHORIZED_DEALER_BRANDS,
    AUTHORIZED_DEALER_HEAD,
    AUTHORIZED_DEALER_HERO,
    AUTHORIZED_DEALER_I18N,
)
from build_new_pages import ARROW_SVG, CACHE_BUST, SHARED_STYLES, end_html, footer_html, header_html
from hero_images import hero_background_css, hero_preload_links, optimized_hero_url

SITE_ROOT = Path(__file__).resolve().parents[2]
DOMAIN = "https://ironcustommotors.com"
PAGE_ID = "authorized-dealer"
PAGE_PATH = "authorized-dealer/"
LANGS = ["en", "ru", "uk", "pt"]
HREFLANG_CODES = {"en": "en", "ru": "ru", "uk": "uk", "pt": "pt-PT"}


def localized_url(lang: str) -> str:
    if lang == "en":
        return f"{DOMAIN}/{PAGE_PATH}"
    return f"{DOMAIN}/{lang}/{PAGE_PATH}"


def lang_payload() -> str:
    return json.dumps(AUTHORIZED_DEALER_I18N, ensure_ascii=False)


def localized_brand_url(url: str, lang: str) -> str:
    if lang == "en" or not url.startswith("/"):
        return url
    if url.startswith(("/ru/", "/uk/", "/pt/")):
        return url
    return f"/{lang}{url}"


def render_brand_cards(lang: str) -> str:
    if not AUTHORIZED_DEALER_BRANDS:
        return """
<div class="dealer-brand-empty">
  <div class="dealer-brand-empty-mark">+</div>
  <h3 data-i18n="ad.brandsEmptyTitle">Brand cards are coming soon.</h3>
  <p data-i18n="ad.brandsEmptyText">Authorized dealer brand pages will appear here as soon as each official partner page is published.</p>
</div>
""".strip()

    cards = []
    for brand in AUTHORIZED_DEALER_BRANDS:
        name = brand["name"][lang]
        url = localized_brand_url(brand["url"], lang)
        logo = brand.get("logo")
        if logo:
            logo_html = f'<img alt="" loading="lazy" src="{escape(logo)}"/>'
        else:
            logo_html = f'<span>{escape(name[:2].upper())}</span>'
        cards.append(
            f"""
<a class="dealer-brand-card" href="{escape(url)}">
  <span class="dealer-brand-logo">{logo_html}</span>
  <span class="dealer-brand-name">{escape(name)}</span>
  <span class="dealer-brand-arrow" aria-hidden="true">→</span>
</a>
""".strip()
        )
    return "\n".join(cards)


def faq_items(lang: str) -> list[dict[str, str]]:
    t = AUTHORIZED_DEALER_I18N[lang]
    return [
        {"question": t[f"ad.q{idx}"], "answer": t[f"ad.a{idx}"]}
        for idx in range(1, 4)
    ]


def json_ld_blocks(lang: str) -> list[dict]:
    t = AUTHORIZED_DEALER_I18N[lang]
    meta = AUTHORIZED_DEALER_HEAD[lang]
    url = localized_url(lang)
    brand_items = [
        {
            "@type": "ListItem",
            "position": idx,
            "name": brand["name"][lang],
            "url": f"{DOMAIN}{localized_brand_url(brand['url'], lang)}",
        }
        for idx, brand in enumerate(AUTHORIZED_DEALER_BRANDS, start=1)
    ]
    return [
        {
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "@id": f"{url}#collection",
            "url": url,
            "name": meta["title"],
            "description": meta["description"],
            "inLanguage": HREFLANG_CODES[lang],
            "isPartOf": {"@id": f"{DOMAIN}/#website"},
            "provider": {"@id": f"{DOMAIN}/#business"},
            "publisher": {"@id": f"{DOMAIN}/#business"},
            "areaServed": ["Cascais", "Estoril", "Oeiras", "Sintra", "Lisbon", "Greater Lisbon"],
            "mainEntity": {
                "@type": "ItemList",
                "name": t["ad.brandsTitle"],
                "itemListElement": brand_items,
            },
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "@id": f"{url}#faq",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": item["question"],
                    "acceptedAnswer": {"@type": "Answer", "text": item["answer"]},
                }
                for item in faq_items(lang)
            ],
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "@id": f"{url}#breadcrumbs",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": t["ad.breadHome"], "item": f"{DOMAIN}/"},
                {"@type": "ListItem", "position": 2, "name": t["ad.breadCurrent"], "item": url},
            ],
        },
    ]


def head(lang: str = "en") -> str:
    meta = AUTHORIZED_DEALER_HEAD[lang]
    canonical = localized_url(lang)
    og_locale = {"en": "en_US", "ru": "ru_RU", "uk": "uk_UA", "pt": "pt_PT"}[lang]
    og_image = f"{DOMAIN}{optimized_hero_url(AUTHORIZED_DEALER_HERO, 1280, 'jpg')}"
    hreflang_html = "".join(
        f'<link rel="alternate" hreflang="{HREFLANG_CODES[item_lang]}" href="{localized_url(item_lang)}"/>'
        for item_lang in LANGS
    )
    hreflang_html += f'<link rel="alternate" hreflang="x-default" href="{localized_url("en")}"/>'
    json_ld_html = "\n".join(
        f'<script type="application/ld+json">{json.dumps(block, ensure_ascii=False)}</script>'
        for block in json_ld_blocks(lang)
    )
    return f"""<!DOCTYPE html>
<html data-lang="{lang}" lang="{lang}">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1, viewport-fit=cover" name="viewport"/>
<meta content="#0a0a0a" name="theme-color"/>
<meta content="max-image-preview:large" name="robots"/>
<title>{escape(meta["title"])}</title>
<meta content="{escape(meta["description"])}" name="description"/>
<link href="{canonical}" rel="canonical"/>
<meta content="{escape(meta["title"])}" property="og:title"/>
<meta content="{escape(meta["description"])}" property="og:description"/>
<meta content="website" property="og:type"/>
<meta content="{canonical}" property="og:url"/>
<meta content="Iron Custom Motors" property="og:site_name"/>
<meta content="{og_image}" property="og:image"/>
<meta content="1200" property="og:image:width"/>
<meta content="630" property="og:image:height"/>
<meta content="{og_locale}" property="og:locale"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="{escape(meta["title"])}" name="twitter:title"/>
<meta content="{escape(meta["description"])}" name="twitter:description"/>
<meta content="{og_image}" name="twitter:image"/>
<link href="/photos/favicon.ico" rel="icon" sizes="any"/>
<link href="/photos/favicon-32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="/photos/apple-touch-icon.png" rel="apple-touch-icon" sizes="180x180"/>
<link href="/photos/site.webmanifest" rel="manifest"/>
{hero_preload_links(AUTHORIZED_DEALER_HERO)}
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Saira:wght@300;400;500;600;700;800;900&amp;family=Saira+Condensed:wght@400;600;700;800;900&amp;family=Roboto+Condensed:wght@400;500;600;700;800;900&amp;family=Inter:wght@300;400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="/assets/main.css?v={CACHE_BUST}" rel="stylesheet"/>
<style>
{SHARED_STYLES}
.authorized-hero{{min-height:72vh;display:flex;align-items:flex-end;padding-bottom:90px}}
.authorized-hero .dealer-hero-bg{{position:absolute;inset:0;{hero_background_css(AUTHORIZED_DEALER_HERO, 1920)};background-size:cover;background-position:center;z-index:-1;filter:saturate(.9)}}
.authorized-hero::after{{background:linear-gradient(90deg,rgba(10,10,10,.96) 0%,rgba(10,10,10,.82) 42%,rgba(10,10,10,.48) 100%),linear-gradient(180deg,rgba(10,10,10,.35) 0%,rgba(10,10,10,.92) 100%)}}
.authorized-hero h1{{max-width:14ch}}
.authorized-hero .lead{{font-size:clamp(17px,1.35vw,21px);max-width:66ch}}
.hero-alt-img{{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}}
.dealer-why-grid{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px}}
.dealer-why-card{{min-height:240px;border:1px solid var(--border);background:var(--surface);border-radius:24px;padding:28px;display:flex;flex-direction:column;gap:18px}}
.dealer-why-card .num{{font-family:var(--font-display);font-weight:800;font-size:42px;color:var(--accent);line-height:1}}
.dealer-why-card h3{{font-family:var(--font-display);font-weight:800;text-transform:uppercase;font-size:clamp(22px,1.8vw,30px);line-height:1;color:#fff;margin:0}}
.dealer-why-card p{{margin:0;color:var(--text-dim);font-size:16px;line-height:1.55}}
.dealer-brands-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px}}
.dealer-brand-empty,.dealer-brand-card{{border:1px solid var(--border);background:linear-gradient(135deg,rgba(255,87,34,.09),rgba(18,18,24,.96));border-radius:22px;padding:24px;min-height:180px}}
.dealer-brand-empty{{grid-column:1/-1;display:grid;place-items:center;text-align:center;gap:10px;border-style:dashed}}
.dealer-brand-empty-mark{{width:48px;height:48px;border-radius:16px;border:1px solid rgba(255,87,34,.45);color:var(--accent);display:grid;place-items:center;font-family:var(--font-display);font-size:34px;line-height:1}}
.dealer-brand-empty h3{{font-family:var(--font-display);font-weight:800;text-transform:uppercase;font-size:clamp(22px,2vw,32px);line-height:1;margin:0;color:#fff}}
.dealer-brand-empty p{{max-width:52ch;margin:0;color:var(--text-dim)}}
.dealer-brand-card{{display:grid;grid-template-columns:auto 1fr auto;align-items:center;gap:16px;color:#fff;transition:transform .25s ease,border-color .25s ease,background .25s ease}}
.dealer-brand-card:hover{{transform:translateY(-2px);border-color:rgba(255,87,34,.75);background:linear-gradient(135deg,rgba(255,87,34,.16),rgba(18,18,24,.96))}}
.dealer-brand-logo{{width:58px;height:58px;border-radius:16px;border:1px solid var(--border);display:grid;place-items:center;background:#0b0b0d;font-family:var(--font-display);font-size:22px;font-weight:800;color:var(--accent)}}
.dealer-brand-logo img{{max-width:78%;max-height:78%;object-fit:contain}}
.dealer-brand-name{{font-family:var(--font-display);font-size:clamp(22px,1.8vw,30px);font-weight:800;text-transform:uppercase;line-height:1}}
.dealer-brand-arrow{{color:var(--accent);font-family:var(--font-display);font-size:26px}}
.authorized-faq-list{{display:grid;gap:12px;max-width:980px;margin:0 auto}}
.authorized-faq-list details{{border:1px solid var(--border);border-radius:18px;background:var(--surface);padding:0 22px}}
.authorized-faq-list summary{{cursor:pointer;list-style:none;padding:22px 0;font-family:var(--font-display);font-weight:800;text-transform:uppercase;color:#fff;font-size:clamp(18px,1.4vw,24px)}}
.authorized-faq-list summary::-webkit-details-marker{{display:none}}
.authorized-faq-list p{{margin:0 0 22px;color:var(--text-dim);line-height:1.6}}
.authorized-cta .lead a,.authorized-cta-copy a{{color:var(--accent);text-decoration:underline;text-underline-offset:4px}}
@media (max-width:1180px){{.dealer-why-grid{{grid-template-columns:repeat(2,minmax(0,1fr))}}}}
@media (max-width:760px){{.authorized-hero{{min-height:auto;padding-top:130px;padding-bottom:70px}}.dealer-why-grid{{grid-template-columns:1fr}}.dealer-why-card{{min-height:auto}}}}
</style>
{json_ld_html}
<script>window.ICM_I18N_PAGE = {lang_payload()};</script>
{hreflang_html}
</head>"""


def render_page(lang: str = "en") -> str:
    t = AUTHORIZED_DEALER_I18N[lang]
    hero_alt_src = optimized_hero_url(AUTHORIZED_DEALER_HERO, 768, "jpg")
    hero_alt_srcset = ", ".join(
        f"{optimized_hero_url(AUTHORIZED_DEALER_HERO, width, 'webp')} {width}w"
        for width in (768, 1280, 1920)
    )
    why_cards = "\n".join(
        f"""
<article class="dealer-why-card">
  <span class="num">0{idx}</span>
  <h3 data-i18n="ad.w{idx}Title">{escape(t[f"ad.w{idx}Title"])}</h3>
  <p data-i18n="ad.w{idx}Text">{escape(t[f"ad.w{idx}Text"])}</p>
</article>
""".strip()
        for idx in range(1, 5)
    )
    faq_html = "\n".join(
        f"""
<details>
  <summary data-i18n="ad.q{idx}">{escape(t[f"ad.q{idx}"])}</summary>
  <p data-i18n="ad.a{idx}">{escape(t[f"ad.a{idx}"])}</p>
</details>
""".strip()
        for idx in range(1, 4)
    )
    return f"""{head(lang)}
<body>
{header_html()}
<main>
  <section class="subpage authorized-hero">
    <div aria-hidden="true" class="dealer-hero-bg"></div>
    <img alt="{escape(t["ad.heroAlt"])}" class="hero-alt-img" data-i18n-alt="ad.heroAlt" height="432" loading="eager" sizes="1px" src="{hero_alt_src}" srcset="{hero_alt_srcset}" width="768"/>
    <div class="container">
      <nav aria-label="Breadcrumb" class="crumb">
        <a data-i18n="ad.breadHome" href="/">{escape(t["ad.breadHome"])}</a>
        <span class="sep">→</span>
        <span data-i18n="ad.breadCurrent">{escape(t["ad.breadCurrent"])}</span>
      </nav>
      <p class="eyebrow" data-i18n="ad.eyebrow">{escape(t["ad.eyebrow"])}</p>
      <h1 data-i18n="ad.h1">{escape(t["ad.h1"])}</h1>
      <p class="lead" data-i18n="ad.intro">{escape(t["ad.intro"])}</p>
      <div class="subpage-cta">
        <a class="btn btn-primary" data-i18n="ad.btnWhatsapp" data-wa="" href="https://wa.me/351917961230" rel="noopener" target="_blank">{escape(t["ad.btnWhatsapp"])} {ARROW_SVG}</a>
        <a class="btn btn-ghost" data-i18n="ad.btnContact" href="/contact/">{escape(t["ad.btnContact"])} {ARROW_SVG}</a>
      </div>
    </div>
  </section>

  <section class="sub-section dealer-why">
    <div class="container">
      <div class="heading">
        <div>
          <p class="eyebrow" data-i18n="ad.whyEyebrow">{escape(t["ad.whyEyebrow"])}</p>
          <h2 data-i18n="ad.whyTitle">{escape(t["ad.whyTitle"])}</h2>
        </div>
      </div>
      <div class="dealer-why-grid">
        {why_cards}
      </div>
    </div>
  </section>

  <section class="sub-section dealer-brands">
    <div class="container">
      <div class="heading">
        <div>
          <p class="eyebrow" data-i18n="ad.brandsEyebrow">{escape(t["ad.brandsEyebrow"])}</p>
          <h2 data-i18n="ad.brandsTitle">{escape(t["ad.brandsTitle"])}</h2>
        </div>
        <p class="lead" data-i18n="ad.brandsIntro">{escape(t["ad.brandsIntro"])}</p>
      </div>
      <div class="dealer-brands-grid">
        {render_brand_cards(lang)}
      </div>
    </div>
  </section>

  <section class="sub-section authorized-faq">
    <div class="container">
      <div class="heading">
        <div>
          <p class="eyebrow" data-i18n="ad.faqEyebrow">{escape(t["ad.faqEyebrow"])}</p>
          <h2 data-i18n="ad.faqTitle">{escape(t["ad.faqTitle"])}</h2>
        </div>
      </div>
      <div class="authorized-faq-list">
        {faq_html}
      </div>
    </div>
  </section>

  <section class="cta-back authorized-cta">
    <div class="container">
      <p class="eyebrow" data-i18n="ad.ctaEyebrow">{escape(t["ad.ctaEyebrow"])}</p>
      <h2 data-i18n="ad.ctaTitle">{escape(t["ad.ctaTitle"])}</h2>
      <p class="lead authorized-cta-copy" data-i18n-html="ad.ctaText">{t["ad.ctaText"]}</p>
      <div class="btns">
        <a class="btn btn-primary" data-i18n="ad.btnWhatsapp" data-wa="" href="https://wa.me/351917961230" rel="noopener" target="_blank">{escape(t["ad.btnWhatsapp"])} {ARROW_SVG}</a>
        <a class="btn btn-ghost" data-i18n="ad.btnContact" href="/contact/">{escape(t["ad.btnContact"])} {ARROW_SVG}</a>
      </div>
    </div>
  </section>
</main>
{footer_html()}
{end_html()}"""


def main() -> None:
    out_dir = SITE_ROOT / PAGE_ID
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "index.html"
    out_path.write_text(render_page("en"), encoding="utf-8")
    print(f"Wrote {out_path.relative_to(SITE_ROOT)}")


if __name__ == "__main__":
    main()

