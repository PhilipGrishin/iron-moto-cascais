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

from bs4 import BeautifulSoup, FeatureNotFound

from build_output import write_html_if_changed
from authorized_dealer_data import (
    AUTHORIZED_DEALER_BRANDS,
    AUTHORIZED_DEALER_HEAD,
    AUTHORIZED_DEALER_HERO,
    AUTHORIZED_DEALER_I18N,
    CWAY_DEALER_HEAD,
    CWAY_DEALER_I18N,
    CWAY_MEDIA,
    CWAY_PAGE_PATH,
    CWAY_PRICE_VALID_UNTIL,
)
from build_new_pages import ARROW_SVG, CACHE_BUST, SHARED_STYLES, end_html, footer_html, header_html
from hero_images import hero_background_css, hero_preload_links, optimized_hero_url
from site_chrome import patch_navigation_footer

SITE_ROOT = Path(__file__).resolve().parents[2]
BUILD_DIR = Path(__file__).resolve().parent
DOMAIN = "https://ironcustommotors.com"
PAGE_ID = "authorized-dealer"
PAGE_PATH = "authorized-dealer/"
LANGS = ["en", "ru", "uk", "pt"]
HREFLANG_CODES = {"en": "en", "ru": "ru", "uk": "uk", "pt": "pt-PT"}
OG_LOCALES = {"en": "en_US", "ru": "ru_RU", "uk": "uk_UA", "pt": "pt_PT"}
ASSET_BASE = "/assets/img/c-way"

try:
    BeautifulSoup("", "lxml")
    HTML_PARSER = "lxml"
except FeatureNotFound:
    HTML_PARSER = "html.parser"

GLOBAL_I18N = json.loads((BUILD_DIR / "i18n.json").read_text(encoding="utf-8"))


def localized_url(lang: str) -> str:
    if lang == "en":
        return f"{DOMAIN}/{PAGE_PATH}"
    return f"{DOMAIN}/{lang}/{PAGE_PATH}"


def cway_url(lang: str) -> str:
    if lang == "en":
        return f"{DOMAIN}/{CWAY_PAGE_PATH}"
    return f"{DOMAIN}/{lang}/{CWAY_PAGE_PATH}"


def local_output_path(path: str, lang: str) -> Path:
    if lang == "en":
        return SITE_ROOT / path / "index.html"
    return SITE_ROOT / lang / path / "index.html"


def localize_path(path: str, lang: str) -> str:
    if lang == "en" or not path.startswith("/"):
        return path
    if path.startswith(("/ru/", "/uk/", "/pt/")):
        return path
    return f"/{lang}{path}"


def lang_payload() -> str:
    return json.dumps(AUTHORIZED_DEALER_I18N, ensure_ascii=False)


def cway_payload() -> str:
    return json.dumps(CWAY_DEALER_I18N, ensure_ascii=False)


def localized_brand_url(url: str, lang: str) -> str:
    if lang == "en" or not url.startswith("/"):
        return url
    if url.startswith(("/ru/", "/uk/", "/pt/")):
        return url
    return f"/{lang}{url}"


def replace_element_html(el, html_fragment: str) -> None:
    fragment_soup = BeautifulSoup(html_fragment, "html.parser")
    container = fragment_soup
    el.clear()
    for child in list(container.children):
        el.append(child)


def apply_static_translations(html: str, lang: str, page_dict: dict[str, str]) -> str:
    soup = BeautifulSoup(html, HTML_PARSER)
    dictionary = {**GLOBAL_I18N.get(lang, {}), **page_dict}
    for el in soup.find_all(attrs={"data-i18n": True}):
        key = el["data-i18n"]
        if key in dictionary:
            replace_element_html(el, dictionary[key])
    for el in soup.find_all(attrs={"data-i18n-html": True}):
        key = el["data-i18n-html"]
        if key in dictionary:
            replace_element_html(el, dictionary[key])
    for el in soup.find_all(attrs={"data-i18n-alt": True}):
        key = el["data-i18n-alt"]
        if key in dictionary:
            el["alt"] = dictionary[key]
    for el in soup.find_all(attrs={"data-i18n-title": True}):
        key = el["data-i18n-title"]
        if key in dictionary:
            el["title"] = dictionary[key]
    return str(soup)


def asset_url(base: str, ext: str = "webp") -> str:
    return f"{ASSET_BASE}/{base}.{ext}"


def image_picture(image: dict, alt: str, class_name: str = "", *, loading: str = "lazy", fetchpriority: str | None = None, sizes: str = "100vw") -> str:
    base = image["base"]
    width = image["width"]
    height = image["height"]
    class_attr = f' class="{escape(class_name)}"' if class_name else ""
    priority_attr = f' fetchpriority="{escape(fetchpriority)}"' if fetchpriority else ""
    loading_attr = f' loading="{escape(loading)}"' if loading else ""
    return f"""
<picture{class_attr}>
  <source srcset="{asset_url(base, 'avif')}" type="image/avif"/>
  <source srcset="{asset_url(base, 'webp')}" type="image/webp"/>
  <img alt="{escape(alt)}"{loading_attr}{priority_attr} decoding="async" height="{height}" sizes="{escape(sizes)}" src="{asset_url(base, 'webp')}" width="{width}"/>
</picture>
""".strip()


def hero_picture(alt: str) -> str:
    image = CWAY_MEDIA["hero"]
    avif_srcset = ", ".join(
        f"{ASSET_BASE}/{image['base']}-{width}.avif {width}w"
        for width in image["widths"]
    )
    webp_srcset = ", ".join(
        f"{ASSET_BASE}/{image['base']}-{width}.webp {width}w"
        for width in image["widths"]
    )
    src = f"{ASSET_BASE}/{image['base']}-1536.webp"
    return f"""
<picture class="cway-hero-media">
  <source sizes="100vw" srcset="{avif_srcset}" type="image/avif"/>
  <source sizes="100vw" srcset="{webp_srcset}" type="image/webp"/>
  <img alt="{escape(alt)}" data-i18n-alt="heroAlt" decoding="async" fetchpriority="high" height="1024" loading="eager" sizes="100vw" src="{src}" width="1536"/>
</picture>
""".strip()


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
        description = brand.get("description", {}).get("en", "")
        image = brand.get("image")
        if image:
            media_html = image_picture(
                image,
                f"{name} official dealer page",
                "dealer-brand-media",
                sizes="(max-width: 760px) 100vw, 46vw",
            )
        else:
            media_html = f'<span class="dealer-brand-media dealer-brand-media-placeholder">{escape(name[:2].upper())}</span>'
        cards.append(
            f"""
<a class="dealer-brand-card" href="{escape(url)}">
  {media_html}
  <span class="dealer-brand-content">
    <span class="dealer-brand-name">{escape(name)}</span>
    <span class="dealer-brand-desc">{escape(description)}</span>
    <span class="dealer-brand-arrow" aria-hidden="true">{ARROW_SVG}</span>
  </span>
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
    home_url = f"{DOMAIN}/" if lang == "en" else f"{DOMAIN}/{lang}/"
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
            "name": t["ad.h1"],
            "description": meta["description"],
            "inLanguage": lang,
            "isPartOf": {"@id": f"{DOMAIN}/#website"},
            "provider": {"@id": f"{DOMAIN}/#business"},
            "publisher": {"@id": f"{DOMAIN}/#business"},
            "areaServed": ["Cascais", "Estoril", "Oeiras", "Sintra", "Lisbon", "Greater Lisbon"],
            "mainEntity": {
                "@type": "ItemList",
                "name": AUTHORIZED_DEALER_I18N["en"]["ad.brandsTitle"],
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
                {"@type": "ListItem", "position": 1, "name": t["ad.breadHome"], "item": home_url},
                {"@type": "ListItem", "position": 2, "name": t["ad.breadCurrent"], "item": url},
            ],
        },
    ]


def cway_faq_items(lang: str) -> list[dict[str, str]]:
    return CWAY_DEALER_I18N[lang]["faq"]


def cway_business_reference(*, with_logo: bool = False) -> dict:
    reference = {
        "@type": "LocalBusiness",
        "@id": f"{DOMAIN}/#business",
        "name": "Iron Custom Motors",
        "image": f"{DOMAIN}/photos/og.jpg",
        "telephone": "+351917961230",
        "priceRange": "€€",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "R. António José da Silva 100 B",
            "addressLocality": "São Domingos de Rana",
            "addressRegion": "Lisbon",
            "postalCode": "2785-253",
            "addressCountry": "PT",
        },
    }
    if with_logo:
        reference["logo"] = {
            "@type": "ImageObject",
            "url": f"{DOMAIN}/photos/icon-512.png",
            "width": 512,
            "height": 512,
        }
    return reference


def cway_product_id(lang: str, key: str) -> str:
    return f"{cway_url(lang)}#product-{key.replace('_', '-')}"


def cway_schema_blocks(lang: str) -> list[dict]:
    t = CWAY_DEALER_I18N[lang]
    meta = CWAY_DEALER_HEAD[lang]
    url = cway_url(lang)
    product_blocks = []
    catalog_items = []
    for product_media in CWAY_MEDIA["products"]:
        key = product_media["key"]
        product = t["products"][key]
        product_id = cway_product_id(lang, key)
        price = product_media["price"]
        catalog_items.append({"@id": product_id})
        product_blocks.append(
            {
                "@context": "https://schema.org",
                "@type": "Product",
                "@id": product_id,
                "url": product_id,
                "name": product["name"],
                "image": f"{DOMAIN}{asset_url(product_media['base'])}",
                "description": product["text"],
                "brand": {"@type": "Brand", "name": "C-Way"},
                "offers": {
                    "@type": "Offer",
                    "url": product_id,
                    "price": price,
                    "priceCurrency": "EUR",
                    "availability": "https://schema.org/InStock",
                    "validFrom": "2026-07-15",
                    "priceValidUntil": CWAY_PRICE_VALID_UNTIL,
                    "priceSpecification": {
                        "@type": "UnitPriceSpecification",
                        "price": price,
                        "priceCurrency": "EUR",
                        "valueAddedTaxIncluded": False,
                    },
                    "seller": cway_business_reference(),
                },
            }
        )

    video_main = CWAY_MEDIA["videos"]["main"]
    video_review = CWAY_MEDIA["videos"]["review"]
    blocks = [
        {
            "@context": "https://schema.org",
            "@type": "Service",
            "@id": f"{url}#service",
            "url": url,
            "name": t["h1"],
            "description": meta["description"],
            "serviceType": "Honda Gold Wing luggage system supply and installation",
            "brand": {"@type": "Brand", "name": "C-Way"},
            "provider": cway_business_reference(),
            "areaServed": ["Portugal", "Cascais", "Lisbon", "Greater Lisbon"],
            "mainEntityOfPage": {"@id": url},
            "hasOfferCatalog": {
                "@type": "OfferCatalog",
                "name": t["productsTitle"],
                "itemListElement": catalog_items,
            },
        },
        *product_blocks,
        {
            "@context": "https://schema.org",
            "@type": "VideoObject",
            "@id": f"{url}#main-video",
            "name": t["videoTitle"],
            "description": t["videoTitle"],
            "thumbnailUrl": video_main["poster"],
            "contentUrl": video_main["content_url"],
            "uploadDate": video_main["upload_date"],
            "duration": video_main["duration"],
            "inLanguage": HREFLANG_CODES[lang],
            "publisher": cway_business_reference(with_logo=True),
        },
        {
            "@context": "https://schema.org",
            "@type": "VideoObject",
            "@id": f"{url}#review-video",
            "name": t["reviewTitle"],
            "description": t["reviewText"],
            "thumbnailUrl": video_review["poster"],
            "contentUrl": video_review["content_url"],
            "uploadDate": video_review["upload_date"],
            "duration": video_review["duration"],
            "inLanguage": HREFLANG_CODES[lang],
            "publisher": cway_business_reference(with_logo=True),
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "@id": f"{url}#faq",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": item["q"],
                    "acceptedAnswer": {"@type": "Answer", "text": item["a"]},
                }
                for item in cway_faq_items(lang)
            ],
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "@id": f"{url}#breadcrumbs",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": t["breadHome"], "item": f"{DOMAIN}/" if lang == "en" else f"{DOMAIN}/{lang}/"},
                {"@type": "ListItem", "position": 2, "name": t["breadDealer"], "item": localized_url(lang)},
                {"@type": "ListItem", "position": 3, "name": t["breadCurrent"], "item": url},
            ],
        },
    ]
    return blocks


def cway_hreflang_html() -> str:
    html = "".join(
        f'<link rel="alternate" hreflang="{HREFLANG_CODES[item_lang]}" href="{cway_url(item_lang)}"/>'
        for item_lang in LANGS
    )
    html += f'<link rel="alternate" hreflang="x-default" href="{cway_url("en")}"/>'
    return html


def cway_head(lang: str) -> str:
    meta = CWAY_DEALER_HEAD[lang]
    canonical = cway_url(lang)
    hero = CWAY_MEDIA["hero"]
    preload = "\n".join(
        [
            f'<link rel="preload" as="image" href="{ASSET_BASE}/{hero["base"]}-768.avif" type="image/avif" media="(max-width: 767px)" fetchpriority="high"/>',
            f'<link rel="preload" as="image" href="{ASSET_BASE}/{hero["base"]}-1280.avif" type="image/avif" media="(min-width: 768px) and (max-width: 1279px)" fetchpriority="high"/>',
            f'<link rel="preload" as="image" href="{ASSET_BASE}/{hero["base"]}-1536.avif" type="image/avif" media="(min-width: 1280px)" fetchpriority="high"/>',
        ]
    )
    json_ld_html = "\n".join(
        f'<script type="application/ld+json">{json.dumps(block, ensure_ascii=False, separators=(",", ":"))}</script>'
        for block in cway_schema_blocks(lang)
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
<meta content="{DOMAIN}{ASSET_BASE}/{hero["base"]}-1280.webp" property="og:image"/>
<meta content="1280" property="og:image:width"/>
<meta content="853" property="og:image:height"/>
<meta content="{OG_LOCALES[lang]}" property="og:locale"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="{escape(meta["title"])}" name="twitter:title"/>
<meta content="{escape(meta["description"])}" name="twitter:description"/>
<meta content="{DOMAIN}{ASSET_BASE}/{hero["base"]}-1280.webp" name="twitter:image"/>
<link href="/photos/favicon.ico" rel="icon" sizes="any"/>
<link href="/photos/favicon-32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="/photos/apple-touch-icon.png" rel="apple-touch-icon" sizes="180x180"/>
<link href="/photos/site.webmanifest" rel="manifest"/>
{preload}
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Saira:wght@300;400;500;600;700;800;900&amp;family=Saira+Condensed:wght@400;600;700;800;900&amp;family=Roboto+Condensed:wght@400;500;600;700;800;900&amp;family=Inter:wght@300;400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="/assets/main.css?v={CACHE_BUST}" rel="stylesheet"/>
<style>
{SHARED_STYLES}
.cway-hero{{position:relative;min-height:calc(100vh - 34px);display:flex;align-items:flex-end;overflow:hidden;padding:142px 0 84px;background:#050505}}
.cway-hero-media{{position:absolute;inset:0;z-index:0}}
.cway-hero-media img{{width:100%;height:100%;object-fit:cover;object-position:center;display:block}}
.cway-hero::after{{content:"";position:absolute;inset:0;z-index:1;background:linear-gradient(90deg,rgba(5,5,5,.92) 0%,rgba(5,5,5,.68) 46%,rgba(5,5,5,.24) 100%),linear-gradient(180deg,rgba(5,5,5,.22) 0%,rgba(5,5,5,.88) 100%)}}
.cway-hero .container{{position:relative;z-index:2}}
.cway-hero h1{{max-width:min(760px,76vw);font-size:clamp(34px,4.2vw,60px);line-height:.92}}
.cway-hero .lead{{max-width:62ch;font-size:clamp(17px,1.35vw,22px)}}
.cway-section{{padding:clamp(34px,4vw,48px) 0;border-top:1px solid rgba(255,255,255,.08);background:#070707}}
.cway-section.alt{{background:#0d0d10}}
.cway-heading{{display:grid;grid-template-columns:minmax(0,0.95fr) minmax(0,1.05fr);gap:clamp(18px,3vw,44px);align-items:end;margin-bottom:24px}}
.cway-heading h2{{margin:0;color:#fff;font-family:var(--font-display);font-size:clamp(24px,3.2vw,50px);line-height:.98;text-transform:uppercase}}
.cway-heading .lead{{margin:0;color:var(--text-dim);font-size:clamp(16px,1.15vw,19px);line-height:1.58}}
.cway-copy{{display:grid;grid-template-columns:minmax(0,.85fr) minmax(0,1.15fr);gap:clamp(22px,3.6vw,52px);align-items:start}}
.cway-copy p{{margin:0 0 18px;color:var(--text-dim);font-size:clamp(17px,1.25vw,21px);line-height:1.68}}
.cway-video-title{{margin:0 0 14px;color:#fff;font-family:var(--font-display);font-size:clamp(18px,1.6vw,24px);font-weight:800;line-height:1;text-transform:uppercase;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
html[lang="ru"] .cway-video-title,html[lang="uk"] .cway-video-title{{font-size:clamp(14px,1.05vw,18px)}}
.cway-video-wrap{{display:grid;gap:10px}}
.cway-video{{width:100%;aspect-ratio:16/9;border:1px solid rgba(255,255,255,.16);border-radius:8px;background:#000;display:block}}
.cway-caption{{margin:0;color:var(--text-muted);font-size:15px}}
.cway-why-grid{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px}}
.cway-why-card{{border:1px solid var(--border);background:linear-gradient(135deg,rgba(255,87,34,.09),rgba(18,18,24,.94));border-radius:8px;padding:20px;min-height:170px}}
.cway-why-card .num{{font-family:var(--font-display);font-size:30px;font-weight:900;color:var(--accent);line-height:1}}
.cway-why-card h3{{margin:14px 0 10px;color:#fff;font-family:var(--font-display);font-size:clamp(20px,1.4vw,25px);line-height:1;text-transform:uppercase}}
.cway-why-card p{{margin:0;color:var(--text-dim);line-height:1.55}}
.cway-price-note{{margin:0 0 24px;color:var(--text-muted);font-family:var(--font-ui);font-size:13px;font-weight:700;text-transform:uppercase}}
.cway-product-groups{{display:grid;gap:34px}}
.cway-product-group{{display:grid;gap:14px}}
.cway-product-group-head{{display:flex;align-items:center;gap:16px;padding-bottom:10px;border-bottom:1px solid rgba(255,255,255,.14)}}
.cway-product-group-head h3{{margin:0;color:#fff;font-family:var(--font-display);font-size:clamp(24px,2.3vw,36px);font-weight:800;line-height:1;text-transform:uppercase}}
.cway-products{{display:grid;gap:12px}}
.cway-product{{display:grid;grid-template-columns:220px minmax(0,1fr);gap:22px;border:1px solid var(--border);background:#111116;border-radius:8px;padding:12px;align-items:center}}
.cway-product picture{{display:block;width:100%;aspect-ratio:1;background:#fff;border-radius:6px;overflow:hidden}}
.cway-product img{{display:block;width:100%;height:100%;object-fit:contain}}
.cway-product-body{{display:flex;min-width:0;min-height:100%;flex-direction:column;justify-content:center;padding:8px 12px 8px 0}}
.cway-product h4{{margin:0 0 10px;color:#fff;font-family:var(--font-display);font-size:clamp(22px,1.8vw,31px);font-weight:800;line-height:1.08;text-transform:uppercase}}
.cway-product p{{margin:0 0 18px;color:var(--text-dim);font-size:clamp(15px,1.05vw,18px);line-height:1.55}}
.cway-product-meta{{display:flex;flex-wrap:wrap;align-items:center;gap:12px 20px;margin-top:auto}}
.cway-price{{color:#fff;font-family:var(--font-display);font-size:clamp(24px,2vw,32px);font-weight:800;line-height:1}}
.cway-price-vat{{color:var(--text-dim);font-family:var(--font-ui);font-size:17px;font-weight:400;line-height:1.2;white-space:nowrap}}
.cway-stock{{display:inline-flex;align-items:center;gap:7px;color:#48d67a;font-family:var(--font-ui);font-size:13px;font-weight:800}}
.cway-stock::before{{content:"";width:8px;height:8px;border-radius:50%;background:#48d67a;box-shadow:0 0 0 4px rgba(72,214,122,.12)}}
.cway-studio-scroll{{display:grid;grid-auto-flow:column;grid-auto-columns:minmax(260px,360px);gap:16px;overflow-x:auto;scroll-snap-type:x proximity;padding-bottom:10px}}
.cway-studio-scroll picture{{scroll-snap-align:start;background:#fff;border-radius:8px;overflow:hidden;border:1px solid rgba(255,255,255,.12)}}
.cway-studio-scroll img{{display:block;width:100%;height:auto}}
.cway-studio-note{{margin:0 0 18px;color:var(--text-dim);font-size:clamp(16px,1.1vw,18px);line-height:1.55}}
.cway-world picture{{display:block;border-radius:8px;overflow:hidden;border:1px solid rgba(255,255,255,.12)}}
.cway-world img{{display:block;width:100%;height:auto}}
.cway-review{{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(280px,.95fr);gap:28px;align-items:center}}
.cway-quote{{border-left:3px solid var(--accent);padding-left:24px;color:#fff;font-size:clamp(18px,1.45vw,24px);line-height:1.42}}
.cway-quote cite{{display:block;margin-top:18px;color:var(--accent);font-family:var(--font-ui);font-size:14px;font-style:normal;font-weight:800;text-transform:uppercase;letter-spacing:.08em}}
.cway-compat{{max-width:980px}}
.cway-compat p{{font-size:clamp(17px,1.25vw,21px);line-height:1.58;color:#fff;margin:0}}
.cway-compat .cway-install{{margin-top:12px;color:var(--accent);font-weight:700}}
.cway-faq-list{{display:grid;gap:12px;max-width:980px;margin:0 auto}}
.cway-faq-list details{{border:1px solid var(--border);border-radius:8px;background:var(--surface);padding:0 22px}}
.cway-faq-list summary{{cursor:pointer;list-style:none;padding:22px 0;font-family:var(--font-display);font-weight:800;text-transform:uppercase;color:#fff;font-size:clamp(18px,1.4vw,24px)}}
.cway-faq-list summary::-webkit-details-marker{{display:none}}
.cway-faq-list p{{margin:0 0 22px;color:var(--text-dim);line-height:1.6}}
.cway-cta-links{{display:flex;flex-wrap:nowrap;gap:10px;margin-top:18px;overflow-x:auto;white-space:nowrap;scrollbar-width:thin}}
.cway-cta-links a{{flex:0 0 auto;color:#fff;border:1px solid var(--border);border-radius:999px;padding:9px 12px;text-decoration:none;font-family:var(--font-ui);font-size:12px;font-weight:800;text-transform:uppercase}}
.cway-cta-links a:hover{{border-color:var(--accent);color:var(--accent)}}
@media (max-width:1100px){{.cway-why-grid{{grid-template-columns:repeat(2,minmax(0,1fr))}}}}
@media (max-width:820px){{.cway-hero{{min-height:auto;padding:124px 0 62px}}.cway-hero h1{{max-width:calc(100vw - 40px);font-size:clamp(30px,8vw,40px)}}.cway-heading,.cway-copy,.cway-review{{grid-template-columns:1fr}}.cway-why-grid{{grid-template-columns:1fr}}}}
@media (max-width:640px){{.cway-product{{grid-template-columns:1fr;gap:16px;padding:10px}}.cway-product-body{{padding:2px 4px 6px}}.cway-product-group-head{{justify-content:space-between}}.cway-product h4{{font-size:24px}}}}
</style>
{json_ld_html}
<script>window.ICM_I18N_PAGE = {cway_payload()};</script>
{cway_hreflang_html()}
</head>"""


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
.dealer-brands-grid{{display:grid;gap:18px}}
.dealer-brand-empty,.dealer-brand-card{{border:1px solid var(--border);background:linear-gradient(135deg,rgba(255,87,34,.09),rgba(18,18,24,.96));border-radius:8px;min-height:180px}}
.dealer-brand-empty{{grid-column:1/-1;display:grid;place-items:center;text-align:center;gap:10px;border-style:dashed}}
.dealer-brand-empty-mark{{width:48px;height:48px;border-radius:16px;border:1px solid rgba(255,87,34,.45);color:var(--accent);display:grid;place-items:center;font-family:var(--font-display);font-size:34px;line-height:1}}
.dealer-brand-empty h3{{font-family:var(--font-display);font-weight:800;text-transform:uppercase;font-size:clamp(22px,2vw,32px);line-height:1;margin:0;color:#fff}}
.dealer-brand-empty p{{max-width:52ch;margin:0;color:var(--text-dim)}}
.dealer-brand-empty{{padding:24px}}
.dealer-brand-card{{display:grid;grid-template-columns:minmax(260px,.82fr) minmax(0,1.18fr);align-items:stretch;gap:0;padding:0;overflow:hidden;color:#fff;background:#111116;transition:transform .25s ease,border-color .25s ease,background .25s ease}}
.dealer-brand-card:hover{{transform:translateY(-2px);border-color:rgba(255,87,34,.75);background:#15151b}}
.dealer-brand-media{{display:block;min-height:260px;background:#0b0b0d;overflow:hidden}}
.dealer-brand-media img{{display:block;width:100%;height:100%;object-fit:cover;aspect-ratio:3/2}}
.dealer-brand-media-placeholder{{display:grid;place-items:center;font-family:var(--font-display);font-size:42px;font-weight:800;color:var(--accent)}}
.dealer-brand-content{{display:flex;flex-direction:column;justify-content:center;gap:14px;padding:28px;min-width:0}}
.dealer-brand-name{{font-family:var(--font-display);font-size:clamp(24px,2.2vw,38px);font-weight:800;text-transform:uppercase;line-height:1;color:#fff}}
.dealer-brand-desc{{color:var(--text-dim);font-size:clamp(16px,1.15vw,19px);line-height:1.58;max-width:68ch}}
.dealer-brand-arrow{{color:var(--accent);width:42px;height:42px;border:1px solid rgba(255,87,34,.42);border-radius:50%;display:grid;place-items:center;margin-top:4px}}
.dealer-brand-arrow svg{{width:17px;height:17px}}
.authorized-faq-list{{display:grid;gap:12px;max-width:980px;margin:0 auto}}
.authorized-faq-list details{{border:1px solid var(--border);border-radius:18px;background:var(--surface);padding:0 22px}}
.authorized-faq-list summary{{cursor:pointer;list-style:none;padding:22px 0;font-family:var(--font-display);font-weight:800;text-transform:uppercase;color:#fff;font-size:clamp(18px,1.4vw,24px)}}
.authorized-faq-list summary::-webkit-details-marker{{display:none}}
.authorized-faq-list p{{margin:0 0 22px;color:var(--text-dim);line-height:1.6}}
.authorized-cta .lead a,.authorized-cta-copy a{{color:var(--accent);text-decoration:underline;text-underline-offset:4px}}
@media (max-width:1180px){{.dealer-why-grid{{grid-template-columns:repeat(2,minmax(0,1fr))}}}}
@media (max-width:760px){{.authorized-hero{{min-height:auto;padding-top:130px;padding-bottom:70px}}.dealer-why-grid{{grid-template-columns:1fr}}.dealer-why-card{{min-height:auto}}.dealer-brand-card{{grid-template-columns:1fr}}.dealer-brand-media{{min-height:220px}}.dealer-brand-content{{padding:22px}}}}
</style>
{json_ld_html}
<script>window.ICM_I18N_PAGE = {lang_payload()};</script>
{hreflang_html}
</head>"""


def cway_studio_alt(lang: str, kind: str) -> str:
    kind_labels = {
        "en": {
            "rack": "rack",
            "hitch": "hitch",
            "aluminum box": "aluminum box",
            "luggage bag": "luggage bag",
            "bracket": "bracket",
            "parts": "parts and units",
        },
        "pt": {
            "rack": "suporte",
            "hitch": "engate",
            "aluminum box": "caixa de alumínio",
            "luggage bag": "mala",
            "bracket": "suporte de fixação",
            "parts": "peças e unidades",
        },
        "ru": {
            "rack": "багажная рама",
            "hitch": "сцепка",
            "aluminum box": "алюминиевый кофр",
            "luggage bag": "багажная сумка",
            "bracket": "кронштейн",
            "parts": "запчасти и узлы",
        },
        "uk": {
            "rack": "багажна рама",
            "hitch": "зчіпка",
            "aluminum box": "алюмінієвий кофр",
            "luggage bag": "багажна сумка",
            "bracket": "кронштейн",
            "parts": "запчастини та вузли",
        },
    }
    label = kind_labels[lang][kind]
    if lang == "en":
        return f"C-Way {label} for Honda Gold Wing"
    if lang == "pt":
        return f"C-Way {label} para Honda Gold Wing"
    if lang == "ru":
        return f"C-Way {label} для Honda Gold Wing"
    return f"C-Way {label} для Honda Gold Wing"


def cway_product_alt(lang: str, name: str) -> str:
    if lang == "en":
        return f"{name} for Honda Gold Wing"
    if lang == "pt":
        return f"{name} para Honda Gold Wing"
    return f"{name} для Honda Gold Wing"


def cway_display_price(price: float) -> str:
    return f"{price:.2f}".replace(".", ",") + " €"


def render_cway_products(lang: str) -> str:
    t = CWAY_DEALER_I18N[lang]
    vat_suffix = t["priceVatSuffix"]
    if vat_suffix not in t["priceNote"] or vat_suffix not in t["installText"]:
        raise ValueError(
            f"C-Way VAT suffix for {lang} must reuse the existing price wording"
        )
    groups = []
    for group in ("steel", "aluminium"):
        cards = []
        for media in (item for item in CWAY_MEDIA["products"] if item["group"] == group):
            key = media["key"]
            product = t["products"][key]
            cards.append(
                f"""
<article class="cway-product" id="product-{key.replace('_', '-')}">
  {image_picture(media, cway_product_alt(lang, product["name"]), "cway-product-media", sizes="(max-width: 640px) calc(100vw - 60px), 220px")}
  <div class="cway-product-body">
    <h4>{escape(product["name"])}</h4>
    <p>{escape(product["text"])}</p>
    <div class="cway-product-meta">
      <span class="cway-price">{escape(cway_display_price(media["price"]))}<wbr/><span class="cway-price-vat">, {escape(vat_suffix)}</span></span>
      <span class="cway-stock">{escape(t["stockLabel"])}</span>
    </div>
  </div>
</article>
""".strip()
            )
        groups.append(
            f"""
<section class="cway-product-group" aria-labelledby="cway-group-{group}">
  <div class="cway-product-group-head">
    <h3 id="cway-group-{group}">{escape(t["groupLabels"][group])}</h3>
  </div>
  <div class="cway-products">{"".join(cards)}</div>
</section>
""".strip()
        )
    return f'<div class="cway-product-groups">{"".join(groups)}</div>'


def render_cway_studio_gallery(lang: str) -> str:
    return "\n".join(
        image_picture(item, cway_studio_alt(lang, item["kind"]), sizes="360px")
        for item in CWAY_MEDIA["studio_gallery"]
    )


def render_cway_faq(lang: str) -> str:
    return "\n".join(
        f"""
<details>
  <summary>{escape(item["q"])}</summary>
  <p>{escape(item["a"])}</p>
</details>
""".strip()
        for item in cway_faq_items(lang)
    )


def render_cway_page(lang: str) -> str:
    t = CWAY_DEALER_I18N[lang]
    video_main = CWAY_MEDIA["videos"]["main"]
    video_review = CWAY_MEDIA["videos"]["review"]
    intro_html = "\n".join(f"<p>{escape(text)}</p>" for text in t["intro"])
    why_html = "\n".join(
        f"""
<article class="cway-why-card">
  <span class="num">0{idx}</span>
  <h3>{escape(item["title"])}</h3>
  <p>{escape(item["text"])}</p>
</article>
""".strip()
        for idx, item in enumerate(t["why"], start=1)
    )
    links = t["links"]
    internal_links = [
        (links["dealer"], "/authorized-dealer/"),
        (links["honda"], "/honda-service/"),
        (links["tuning"], "/upgrades-tuning/"),
        (links["contact"], "/contact/"),
    ]
    cta_links = "\n".join(
        f'<a href="{escape(localize_path(url, lang))}">{escape(label)}</a>'
        for label, url in internal_links
    )
    raw = f"""{cway_head(lang)}
<body>
{header_html()}
<main>
  <section class="cway-hero">
    {hero_picture(t["heroAlt"])}
    <div class="container">
      <nav aria-label="Breadcrumb" class="crumb">
        <a href="{escape(localize_path('/', lang))}">{escape(t["breadHome"])}</a>
        <span class="sep">→</span>
        <a href="{escape(localize_path('/authorized-dealer/', lang))}">{escape(t["breadDealer"])}</a>
        <span class="sep">→</span>
        <span>{escape(t["breadCurrent"])}</span>
      </nav>
      <p class="eyebrow">{escape(t["eyebrow"])}</p>
      <h1>{escape(t["h1"])}</h1>
      <p class="lead">{escape(t["heroOffer"])}</p>
      <div class="subpage-cta">
        <a class="btn btn-primary" data-wa="" href="https://wa.me/351917961230" rel="noopener" target="_blank">{escape(t["btnWhatsapp"])} {ARROW_SVG}</a>
        <a class="btn btn-ghost" href="#cway-products">{escape(t["btnProducts"])} {ARROW_SVG}</a>
      </div>
    </div>
  </section>

  <section class="cway-section" id="intro">
    <div class="container cway-copy">
      <div>
        <p class="eyebrow">{escape(t["introEyebrow"])}</p>
        <h2>{escape(t["introTitle"])}</h2>
      </div>
      <div>{intro_html}</div>
    </div>
  </section>

  <section class="cway-section alt" id="cway-main-video">
    <div class="container">
      <h2 class="cway-video-title">{escape(t["videoTitle"])}</h2>
      <div class="cway-video-wrap">
        <video class="cway-video" controls playsinline poster="{escape(video_main["poster"])}" preload="none">
          <source src="{escape(video_main["content_url"])}" type="video/mp4"/>
        </video>
      </div>
    </div>
  </section>

  <section class="cway-section" id="authorized-dealer-trust">
    <div class="container">
      <div class="cway-heading">
        <div>
          <p class="eyebrow">{escape(t["whyEyebrow"])}</p>
          <h2>{escape(t["whyTitle"])}</h2>
        </div>
      </div>
      <div class="cway-why-grid">{why_html}</div>
    </div>
  </section>

  <section class="cway-section alt" id="cway-products">
    <div class="container">
      <div class="cway-heading">
        <div>
          <p class="eyebrow">{escape(t["productsEyebrow"])}</p>
          <h2>{escape(t["productsTitle"])}</h2>
        </div>
        <p class="lead">{escape(t["productsIntro"])}</p>
      </div>
      <p class="cway-price-note">{escape(t["priceNote"])}</p>
      {render_cway_products(lang)}
    </div>
  </section>

  <section class="cway-section" id="studio-gallery">
    <div class="container">
      <div class="cway-heading">
        <div>
          <p class="eyebrow">{escape(t["studioEyebrow"])}</p>
          <h2>{escape(t["studioTitle"])}</h2>
        </div>
      </div>
      <p class="cway-studio-note">{escape(t["studioNote"])}</p>
      <div class="cway-studio-scroll">{render_cway_studio_gallery(lang)}</div>
    </div>
  </section>

  <section class="cway-section cway-world" id="worldwide">
    <div class="container">
      <div class="cway-heading">
        <div>
          <p class="eyebrow">{escape(t["worldEyebrow"])}</p>
          <h2>{escape(t["worldTitle"])}</h2>
        </div>
      </div>
      {image_picture(CWAY_MEDIA["worldwide"], t["worldAlt"], loading="lazy", sizes="100vw")}
    </div>
  </section>

  <section class="cway-section alt" id="review-video">
    <div class="container cway-review">
      <div>
        <p class="eyebrow">{escape(t["reviewEyebrow"])}</p>
        <video class="cway-video" controls playsinline poster="{escape(video_review["poster"])}" preload="none">
          <source src="{escape(video_review["content_url"])}" type="video/mp4"/>
        </video>
      </div>
      <blockquote class="cway-quote">
        {escape(t["reviewText"])}
        <cite>{escape(t["reviewTitle"])}</cite>
      </blockquote>
    </div>
  </section>

  <section class="cway-section" id="compatibility">
    <div class="container cway-compat">
      <p class="eyebrow">{escape(t["compatEyebrow"])}</p>
      <h2>{escape(t["compatTitle"])}</h2>
      <p>{escape(t["compatText"])}</p>
      <p class="cway-install">{escape(t["installText"])}</p>
    </div>
  </section>

  <section class="cway-section alt" id="faq">
    <div class="container">
      <div class="cway-heading">
        <div>
          <p class="eyebrow">{escape(t["faqEyebrow"])}</p>
          <h2>{escape(t["faqTitle"])}</h2>
        </div>
      </div>
      <div class="cway-faq-list">{render_cway_faq(lang)}</div>
    </div>
  </section>

  <section class="cta-back authorized-cta" id="order">
    <div class="container">
      <p class="eyebrow">{escape(t["ctaEyebrow"])}</p>
      <h2>{escape(t["ctaTitle"])}</h2>
      <p class="lead authorized-cta-copy">{escape(t["ctaText"])}</p>
      <div class="btns">
        <a class="btn btn-primary" data-wa="" href="https://wa.me/351917961230" rel="noopener" target="_blank">{escape(t["btnWhatsapp"])} {ARROW_SVG}</a>
        <a class="btn btn-ghost" href="{escape(localize_path("/contact/", lang))}">{escape(links["contact"])} {ARROW_SVG}</a>
      </div>
      <p class="cway-caption">{escape(t["linksLabel"])}</p>
      <div class="cway-cta-links">{cta_links}</div>
    </div>
  </section>
</main>
{footer_html()}
{end_html()}"""
    raw = patch_navigation_footer(raw, lang)
    return apply_static_translations(raw, lang, CWAY_DEALER_I18N[lang])


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
    raw = f"""{head(lang)}
<body>
{header_html()}
<main>
  <section class="subpage authorized-hero">
    <div aria-hidden="true" class="dealer-hero-bg"></div>
    <img alt="{escape(t["ad.heroAlt"])}" class="hero-alt-img" data-i18n-alt="ad.heroAlt" height="432" loading="eager" sizes="1px" src="{hero_alt_src}" srcset="{hero_alt_srcset}" width="768"/>
    <div class="container">
      <nav aria-label="Breadcrumb" class="crumb">
        <a data-i18n="ad.breadHome" href="{escape(localize_path('/', lang))}">{escape(t["ad.breadHome"])}</a>
        <span class="sep">→</span>
        <span data-i18n="ad.breadCurrent">{escape(t["ad.breadCurrent"])}</span>
      </nav>
      <p class="eyebrow" data-i18n="ad.eyebrow">{escape(t["ad.eyebrow"])}</p>
      <h1 data-i18n="ad.h1">{escape(t["ad.h1"])}</h1>
      <p class="lead" data-i18n="ad.intro">{escape(t["ad.intro"])}</p>
      <div class="subpage-cta">
        <a class="btn btn-primary" data-i18n="ad.btnWhatsapp" data-wa="" href="https://wa.me/351917961230" rel="noopener" target="_blank">{escape(t["ad.btnWhatsapp"])} {ARROW_SVG}</a>
        <a class="btn btn-ghost" data-i18n="ad.btnContact" href="{escape(localize_path('/contact/', lang))}">{escape(t["ad.btnContact"])} {ARROW_SVG}</a>
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
        <a class="btn btn-ghost" data-i18n="ad.btnContact" href="{escape(localize_path('/contact/', lang))}">{escape(t["ad.btnContact"])} {ARROW_SVG}</a>
      </div>
    </div>
  </section>
</main>
{footer_html()}
{end_html()}"""
    raw = patch_navigation_footer(raw, lang)
    return apply_static_translations(raw, lang, AUTHORIZED_DEALER_I18N[lang])


def main() -> None:
    hub_path = PAGE_PATH.strip("/")
    for lang in LANGS:
        out_path = local_output_path(hub_path, lang)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        write_html_if_changed(
            out_path,
            render_page(lang),
            preserve_body_shell=True,
            merge_page_i18n=True,
            preserve_downstream_head=True,
        )
        print(f"Wrote {out_path.relative_to(SITE_ROOT)}")

    cway_path = CWAY_PAGE_PATH.strip("/")
    for lang in LANGS:
        cway_out = local_output_path(cway_path, lang)
        cway_out.parent.mkdir(parents=True, exist_ok=True)
        write_html_if_changed(
            cway_out,
            render_cway_page(lang),
            preserve_body_shell=True,
            merge_page_i18n=True,
            preserve_downstream_head=True,
        )
        print(f"Wrote {cway_out.relative_to(SITE_ROOT)}")


if __name__ == "__main__":
    main()
