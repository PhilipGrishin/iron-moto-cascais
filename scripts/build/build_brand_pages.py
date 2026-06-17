#!/usr/bin/env python3
"""
Generate brand-specific landing pages: /bmw-service/, /harley-service/, /ducati-service/.
EN sources, then run build_i18n.py to produce /ru/, /uk/, /pt/ versions.

Same skeleton for every brand:
  HERO → Intro → Tools → Services → Issues → Models → Parts catalogs → FAQ → CTA
"""

import json
from pathlib import Path

from brand_pages_data import BRAND_BG, BRAND_HEAD, PAGE_I18N

SITE_ROOT = Path(__file__).resolve().parents[2]
DOMAIN = "https://ironcustommotors.com"
CACHE_BUST = "20260617b"

# Per-brand prefix mapping (e.g. "bmw-service" → I18N key prefix "bmw")
BRAND_PREFIX = {
    "bmw-service":    "bmw",
    "harley-service": "hd",
    "ducati-service": "duc",
}

# Display name + schema brand for JSON-LD
BRAND_NAME = {
    "bmw-service":    "BMW Motorrad",
    "harley-service": "Harley-Davidson",
    "ducati-service": "Ducati",
}

LOGO_SVG = """<svg aria-hidden="true" class="logo-svg" viewbox="0 0 270.91 46.88" xmlns="http://www.w3.org/2000/svg">
<g fill="#fff"><path d="M18.01,28.94v-10.44h2.16v10.44h-2.16Z"></path><path d="M32.75,28.94v-3.3c0-.47-.37-.83-.83-.83h-8.16v4.13h-2.16v-10.44h10.31c1.13,0,2.05.6,2.59,1.49.27.47.41,1.07.41,1.67,0,.85-.26,1.53-.69,2.05.44.53.69,1.17.69,1.91v3.31h-2.15ZM32.5,22.41c.17-.17.25-.46.25-.75s-.09-.58-.25-.75c-.17-.16-.36-.24-.59-.24h-8.14v1.97h8.14c.23,0,.42-.08.59-.24Z"></path><path d="M39.32,28.94c-1.7,0-2.99-1.38-2.99-3v-4.45c0-1.7,1.37-2.99,2.99-2.99h8.27c1.67,0,2.99,1.34,2.99,2.99v4.45c0,1.69-1.34,3-2.99,3h-8.27ZM48.41,25.94v-4.45c0-.49-.37-.82-.83-.82h-8.27c-.46,0-.83.34-.83.82v4.45c0,.47.36.83.83.83h8.27c.47,0,.83-.37.83-.83Z"></path><path d="M63.45,28.94v-7.45c0-.45-.36-.83-.83-.83h-8.46v8.27h-2.16v-10.44h10.62c1.69,0,2.98,1.36,2.98,2.97v7.46h-2.15Z"></path><path d="M74.32,28.94c-1.69,0-2.99-1.37-2.99-3v-4.45c0-1.7,1.37-2.99,2.99-2.99h7.64c1.69,0,2.99,1.36,2.99,2.99v.19h-2.17v-.19c0-.47-.36-.82-.82-.82h-7.64c-.46,0-.83.35-.83.82v4.45c0,.47.36.83.83.83h7.64c.47,0,.82-.36.82-.83v-.19h2.17c0,.68-.06,1.13-.4,1.7-.52.87-1.44,1.49-2.59,1.49h-7.64Z"></path><path d="M89.17,28.94c-1.69,0-2.98-1.36-2.98-2.98v-7.46h2.16v7.44c0,.46.35.83.83.83h7.64c.47,0,.83-.37.83-.83v-7.44h2.16v7.44c0,1.69-1.36,3-2.99,3h-7.64Z"></path><path d="M104,28.94c-1.52,0-2.79-1.21-2.79-2.74v-.45h2.16v.45c0,.34.27.57.62.57h7.4c.35,0,.62-.24.62-.57v-.83c0-.34-.27-.57-.62-.57h-7.4c-1.55,0-2.79-1.24-2.79-2.74v-.83c0-1.54,1.28-2.74,2.79-2.74h7.4c1.59,0,2.79,1.26,2.79,2.74v.45h-2.16v-.45c0-.34-.27-.57-.62-.57h-7.4c-.35,0-.62.23-.62.57v.83c0,.34.27.57.62.57h7.4c1.59,0,2.79,1.26,2.79,2.73v.83c0,1.52-1.24,2.74-2.79,2.74h-7.4Z"></path><path d="M120.64,28.94v-8.27h-2.78c-.18,0-.32.05-.44.16-.12.11-.18.25-.18.42v.45h-2.16v-.45c0-.51.13-.97.38-1.38.25-.41.59-.73,1.01-.98s.88-.37,1.39-.37h7.72c.51,0,.97.12,1.39.37s.76.57,1.01.98c.25.41.38.87.38,1.38v.45h-2.16v-.45c0-.17-.06-.31-.18-.42-.12-.11-.26-.16-.44-.16h-2.78v8.27h-2.16Z"></path><path d="M132.25,28.94c-1.7,0-2.99-1.38-2.99-3v-4.45c0-1.7,1.37-2.99,2.99-2.99h8.27c1.67,0,2.99,1.34,2.99,2.99v4.45c0,1.69-1.34,3-2.99,3h-8.27ZM141.34,25.94v-4.45c0-.49-.37-.82-.83-.82h-8.27c-.46,0-.83.34-.83.82v4.45c0,.47.36.83.83.83h8.27c.47,0,.83-.37.83-.83Z"></path><path d="M157.18,28.94v-7.45c0-.45-.36-.83-.83-.83h-3.16c.08.27.12.54.12.83v7.45h-2.16v-7.45c0-.46-.36-.83-.83-.83h-2.41c-.47,0-.83.37-.83.83v7.45h-2.15v-7.46c0-1.7,1.37-2.97,2.98-2.97h8.44c1.69,0,2.98,1.36,2.98,2.97v7.46h-2.15Z"></path><path d="M177.32,28.94v-7.45c0-.45-.36-.83-.83-.83h-3.16c.08.27.12.54.12.83v7.45h-2.16v-7.45c0-.46-.36-.83-.83-.83h-2.41c-.47,0-.83.37-.83.83v7.45h-2.16v-7.46c0-1.7,1.37-2.97,2.98-2.97h8.44c1.69,0,2.98,1.36,2.98,2.97v7.46h-2.15Z"></path><path d="M183.87,28.94c-1.7,0-2.99-1.38-2.99-3v-4.45c0-1.7,1.37-2.99,2.99-2.99h8.27c1.67,0,2.99,1.34,2.99,2.99v4.45c0,1.69-1.34,3-2.99,3h-8.27ZM192.96,25.94v-4.45c0-.49-.37-.82-.83-.82h-8.27c-.46,0-.83.34-.83.82v4.45c0,.47.36.83.83.83h8.27c.47,0,.83-.37.83-.83Z"></path><path d="M201.58,28.94v-8.27h-2.78c-.18,0-.32.05-.44.16-.12.11-.18.25-.18.42v.45h-2.16v-.45c0-.51.13-.97.38-1.38.25-.41.59-.73,1.01-.98s.88-.37,1.39-.37h7.72c.51,0,.97.12,1.39.37s.76.57,1.01.98c.25.41.38.87.38,1.38v.45h-2.16v-.45c0-.17-.06-.31-.18-.42-.12-.11-.26-.16-.44-.16h-2.78v8.27h-2.16Z"></path><path d="M213.18,28.94c-1.7,0-2.99-1.38-2.99-3v-4.45c0-1.7,1.37-2.99,2.99-2.99h8.27c1.67,0,2.99,1.34,2.99,2.99v4.45c0,1.69-1.34,3-2.99,3h-8.27ZM222.27,25.94v-4.45c0-.49-.37-.82-.83-.82h-8.27c-.46,0-.83.34-.83.82v4.45c0,.47.36.83.83.83h8.27c.47,0,.83-.37.83-.83Z"></path><path d="M237.01,28.94v-3.3c0-.47-.37-.83-.83-.83h-8.16v4.13h-2.16v-10.44h10.31c1.13,0,2.05.6,2.59,1.49.27.47.41,1.07.41,1.67,0,.85-.26,1.53-.69,2.05.44.53.69,1.17.69,1.91v3.31h-2.15ZM236.76,22.41c.17-.17.25-.46.25-.75s-.09-.58-.25-.75c-.17-.16-.36-.24-.59-.24h-8.14v1.97h8.14c.23,0,.42-.08.59-.24Z"></path><path d="M243.37,28.94c-1.52,0-2.79-1.21-2.79-2.74v-.45h2.16v.45c0,.34.27.57.62.57h7.4c.35,0,.62-.24.62-.57v-.83c0-.34-.27-.57-.62-.57h-7.4c-1.55,0-2.79-1.24-2.79-2.74v-.83c0-1.54,1.28-2.74,2.79-2.74h7.4c1.59,0,2.79,1.26,2.79,2.74v.45h-2.16v-.45c0-.34-.27-.57-.62-.57h-7.4c-.35,0-.62.23-.62.57v.83c0,.34.27.57.62.57h7.4c1.59,0,2.79,1.26,2.79,2.73v.83c0,1.52-1.24,2.74-2.79,2.74h-7.4Z"></path></g>
<path d="M259.71,39.68h-2.47v-2.14h2.47c1.39,0,2.52-1.38,2.52-3.08V12.97c0-1.7-1.13-3.08-2.52-3.08H11.86c-1.39,0-2.52,1.38-2.52,3.08v21.5c0,1.7,1.13,3.08,2.52,3.08h200.03v2.14H11.86c-2.57,0-4.66-2.34-4.66-5.21V12.97c0-2.87,2.09-5.21,4.66-5.21h247.86c2.57,0,4.66,2.34,4.66,5.21v21.5c0,2.87-2.09,5.21-4.66,5.21Z" fill="#fff"></path>
<g fill="#fff"><path d="M216.56,38.3h1.02c0,.34.18.5.63.5.41,0,.55-.16.55-.34,0-.26-.32-.38-.71-.51-.63-.22-1.43-.48-1.43-1.45,0-.89.73-1.34,1.49-1.34s1.54.45,1.54,1.49h-1.02c0-.34-.17-.5-.52-.5-.32,0-.47.16-.47.34,0,.27.26.4.63.53.64.22,1.5.45,1.5,1.44,0,.89-.71,1.34-1.57,1.34s-1.65-.45-1.65-1.49Z"></path><path d="M221.76,35.24v4.46h-1.02v-4.46h1.02Z"></path><path d="M226.35,35.24v4.46h-.77l-1.59-2.49v2.49h-1.02v-4.46h.77l1.59,2.49v-2.49h1.02Z"></path><path d="M227.37,37.47c0-1.31.98-2.32,2.32-2.32,1.08,0,2,.72,2.19,1.75h-1.06c-.14-.47-.59-.75-1.12-.75-.79,0-1.3.53-1.3,1.33s.51,1.33,1.3,1.33c.54,0,.99-.29,1.12-.75h1.06c-.19,1.02-1.1,1.75-2.19,1.75-1.35,0-2.32-1.01-2.32-2.32Z"></path><path d="M235.46,38.72v.98h-2.68v-4.46h2.65v.98h-1.62v.75h1.47v.96h-1.47v.8h1.66Z"></path><path d="M238.33,38.96l1.49-1.5c.25-.25.47-.57.47-.85,0-.3-.15-.47-.44-.47-.32,0-.49.16-.49.5h-1.02c0-1.05.74-1.49,1.49-1.49s1.49.45,1.49,1.47c0,.49-.3,1-.66,1.36l-.77.75h1.5v.98h-3.04v-.74Z"></path><path d="M242.13,37.47c0-1.38.66-2.32,1.82-2.32s1.82.94,1.82,2.32-.66,2.32-1.82,2.32-1.82-.94-1.82-2.32ZM244.75,37.47c0-.86-.26-1.33-.8-1.33s-.8.47-.8,1.33.26,1.33.8,1.33.8-.47.8-1.33Z"></path><path d="M248.51,35.24v4.46h-1.02v-3.45l-1.02.57v-1.01l1.02-.57h1.02Z"></path><path d="M249.6,37.47c0-1.38.66-2.32,1.82-2.32s1.82.94,1.82,2.32-.66,2.32-1.82,2.32-1.82-.94-1.82-2.32ZM252.21,37.47c0-.86-.26-1.33-.8-1.33s-.8.47-.8,1.33.26,1.33.8,1.33.8-.47.8-1.33Z"></path></g>
</svg>"""

ARROW_SVG = '<svg fill="none" height="18" stroke="currentColor" stroke-width="2" viewbox="0 0 24 24" width="18"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>'

SHARED_STYLES = """.subpage{padding:160px 0 100px;background:#0a0a0a;position:relative;overflow:hidden;isolation:isolate}
.subpage::before{content:"";position:absolute;top:-30%;right:-15%;width:600px;height:600px;background:radial-gradient(circle,rgba(255,87,34,.20),transparent 60%);pointer-events:none;z-index:1}
.subpage::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,10,10,.45) 0%,rgba(10,10,10,.6) 50%,rgba(10,10,10,.96) 100%);z-index:0;pointer-events:none}
.subpage .container{position:relative;z-index:1}
.crumb{display:flex;align-items:center;gap:10px;font-family:'Saira',monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--text-mute);margin-bottom:24px}
.crumb a{color:var(--text-dim)}
.crumb a:hover{color:var(--accent)}
.crumb .sep{color:var(--accent)}
.subpage h1{font-family:'Saira Condensed',sans-serif;font-weight:800;line-height:.92;letter-spacing:-.01em;text-transform:uppercase;font-size:clamp(40px,7vw,104px);color:#fff;max-width:18ch;margin-bottom:24px}
.subpage h1 .accent{color:var(--accent)}
.subpage .lead{max-width:60ch;color:var(--text-dim)}
.subpage-cta{display:flex;gap:14px;flex-wrap:wrap;margin-top:36px}
.sub-section{padding:var(--gap) 0;background:#0a0a0a;border-top:1px solid var(--border)}
.sub-section .heading{margin-bottom:60px;display:grid;grid-template-columns:1fr 1.4fr;gap:60px;align-items:end;padding-bottom:30px;border-bottom:1px solid var(--border)}
.sub-section .heading h2{margin:0;font-family:'Saira Condensed',sans-serif;font-weight:800;text-transform:uppercase;font-size:clamp(30px,4.6vw,62px);line-height:.95;letter-spacing:-.005em;color:#fff}
.sub-section .heading h2 em{color:var(--accent);font-style:italic}
.sub-section .heading p.lead{margin-top:18px}
.sub-intro p{font-family:'Saira',sans-serif;font-weight:400;font-size:clamp(18px,1.6vw,22px);line-height:1.55;color:var(--text);max-width:64ch;margin-bottom:18px}
.sub-intro p:last-child{color:var(--text-dim);font-size:clamp(15px,1.2vw,18px)}
.cta-back{padding:var(--gap) 0;background:#0a0a0a;text-align:center;border-top:1px solid var(--border)}
.cta-back .container{max-width:760px}
.cta-back h2{margin-bottom:18px;font-family:'Saira Condensed',sans-serif;font-weight:800;text-transform:uppercase;font-size:clamp(30px,4.6vw,60px);line-height:.95;color:#fff}
.cta-back .lead{margin:0 auto 30px;max-width:54ch}
.cta-back .btns{display:flex;justify-content:center;gap:14px;flex-wrap:wrap}
@media (max-width:1100px){.sub-section .heading{grid-template-columns:1fr;gap:24px}}
@media (max-width:760px){.subpage{padding-top:130px}}"""

# Brand-page-specific CSS
BRAND_CSS = """.subpage.brand{padding:140px 0 90px}
.subpage.brand .bg{position:absolute;inset:0;z-index:-1;background-size:cover;background-position:center;filter:saturate(.85) contrast(1.05) brightness(.5)}
.tools-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:18px;margin-top:30px}
.tool-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);padding:24px 22px}
.tool-card h3{font-family:'Saira Condensed',sans-serif;font-weight:800;text-transform:uppercase;font-size:20px;color:#fff;margin-bottom:8px}
.tool-card p{font-size:14px;color:var(--text-dim);max-width:46ch}
.brand-srv-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;margin-top:30px}
.brand-srv{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);padding:24px 22px;display:grid;grid-template-columns:48px 1fr;gap:14px;align-items:start}
.brand-srv .num{font-family:'Saira Condensed',sans-serif;font-weight:800;font-size:28px;color:var(--accent);line-height:1}
.brand-srv h3{font-family:'Saira Condensed',sans-serif;font-weight:800;text-transform:uppercase;font-size:18px;color:#fff;margin-bottom:6px;line-height:1.1}
.brand-srv p{font-size:14px;color:var(--text-dim)}
.issue-row{display:grid;grid-template-columns:50px 1fr;gap:18px;padding:20px 0;border-bottom:1px solid var(--border);align-items:start;transition:padding-left .25s var(--ease)}
.issue-row:hover{padding-left:10px}
.issue-row .bullet{width:12px;height:12px;background:var(--accent);clip-path:polygon(0 0, 100% 0, 100% 70%, 70% 100%, 0 100%);margin-top:6px}
.issue-row h4{font-family:'Saira Condensed',sans-serif;font-weight:700;text-transform:uppercase;font-size:17px;color:#fff;margin-bottom:5px;letter-spacing:.01em}
.issue-row p{font-size:14px;color:var(--text-dim);max-width:64ch}
.models-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:30px}
.model-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);padding:22px 20px}
.model-card h3{font-family:'Saira Condensed',sans-serif;font-weight:800;text-transform:uppercase;font-size:18px;color:#fff;margin-bottom:8px}
.model-card p{font-size:13px;color:var(--text-dim)}
.parts-block{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);padding:30px 28px;margin-top:24px}
.parts-block p{font-size:15px;color:var(--text-dim);line-height:1.65}
.brand-faq{display:grid;grid-template-columns:1fr;gap:12px;margin-top:30px}
.brand-faq details{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);overflow:hidden}
.brand-faq summary{cursor:pointer;list-style:none;padding:20px 24px;display:flex;align-items:flex-start;gap:18px;font-family:'Saira Condensed',sans-serif;font-weight:700;text-transform:uppercase;font-size:clamp(15px,1.3vw,18px);color:#fff;line-height:1.25;letter-spacing:.01em;transition:color .2s var(--ease)}
.brand-faq summary:hover{color:var(--accent)}
.brand-faq summary::-webkit-details-marker{display:none}
.brand-faq .chev{margin-left:auto;color:var(--text-dim);transition:transform .25s var(--ease);flex-shrink:0}
.brand-faq details[open] .chev{transform:rotate(180deg)}
.brand-faq .a{padding:0 24px 22px 24px;color:var(--text-dim);font-size:14px;line-height:1.65;max-width:84ch}
@media (max-width:900px){.tools-grid,.brand-srv-grid,.models-grid{grid-template-columns:1fr}.issue-row{grid-template-columns:30px 1fr}}"""


def head(slug, lang):
    meta = BRAND_HEAD[slug][lang]
    pre = BRAND_PREFIX[slug]
    canonical = f"{DOMAIN}/{slug}/"
    og_locale = {"en":"en_US","ru":"ru_RU","uk":"uk_UA","pt":"pt_PT"}[lang]
    brand_name = BRAND_NAME[slug]

    page_url = canonical

    json_ld_blocks = [
        {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": f"{brand_name} service",
            "serviceType": f"{brand_name} motorcycle service and repair",
            "provider": {"@id": f"{DOMAIN}/#business"},
            "brand": {"@type": "Brand", "name": brand_name},
            "areaServed": [
                {"@type": "City", "name": "Cascais"},
                {"@type": "City", "name": "Lisbon"},
                {"@type": "City", "name": "Estoril"},
            ],
            "url": page_url,
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{DOMAIN}/"},
                {"@type": "ListItem", "position": 2, "name": f"{brand_name} service", "item": page_url},
            ],
        },
    ]

    # Build FAQPage from in-page Q/A (en source — translated copy at /lang)
    en = PAGE_I18N[slug]["en"]
    faq_main_entity = []
    for i in range(1, 6):
        q = en.get(f"{pre}.q{i}")
        a = en.get(f"{pre}.a{i}")
        if q and a:
            faq_main_entity.append({
                "@type": "Question", "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            })
    if faq_main_entity:
        json_ld_blocks.append({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "url": page_url,
            "mainEntity": faq_main_entity,
        })

    json_ld_html = "".join(
        f'<script type="application/ld+json">{json.dumps(b, ensure_ascii=False)}</script>' for b in json_ld_blocks
    )

    hreflang_html = "".join(
        f'<link rel="alternate" hreflang="{lg}" href="{DOMAIN}/{slug}/"/>' if lg == "en"
        else f'<link rel="alternate" hreflang="{lg}" href="{DOMAIN}/{lg}/{slug}/"/>'
        for lg in ["en","ru","uk","pt"]
    )
    hreflang_html += f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}/{slug}/"/>'

    i18n_json = json.dumps(PAGE_I18N[slug], ensure_ascii=False)

    return f'''<!DOCTYPE html>
<html data-lang="{lang}" lang="{lang}">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1, viewport-fit=cover" name="viewport"/>
<meta content="#0a0a0a" name="theme-color"/>
<title>{meta["title"]}</title>
<meta content="{meta["description"]}" name="description"/>
<link href="{canonical}" rel="canonical"/>
<meta content="{meta["title"]}" property="og:title"/>
<meta content="{meta["description"]}" property="og:description"/>
<meta content="website" property="og:type"/>
<meta content="{canonical}" property="og:url"/>
<meta content="Iron Custom Motors" property="og:site_name"/>
<meta content="{DOMAIN}/photos/og.jpg" property="og:image"/>
<meta content="1200" property="og:image:width"/>
<meta content="630" property="og:image:height"/>
<meta content="{og_locale}" property="og:locale"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="{meta["title"]}" name="twitter:title"/>
<meta content="{meta["description"]}" name="twitter:description"/>
<meta content="{DOMAIN}/photos/og.jpg" name="twitter:image"/>
<link href="/photos/favicon.ico" rel="icon" sizes="any"/>
<link href="/photos/favicon-32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="/photos/apple-touch-icon.png" rel="apple-touch-icon" sizes="180x180"/>
<link href="/photos/site.webmanifest" rel="manifest"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Saira:wght@300;400;500;600;700;800;900&amp;family=Saira+Condensed:wght@400;600;700;800;900&amp;family=Inter:wght@300;400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="/assets/main.css?v={CACHE_BUST}" rel="stylesheet"/>
<style>
{SHARED_STYLES}
{BRAND_CSS}
</style>
{json_ld_html}<script>window.ICM_I18N_PAGE = {i18n_json};</script>
{hreflang_html}
</head>'''


HEADER_HTML = f'''<div aria-label="Cookie consent" class="cookie-banner" id="cookieBanner" role="dialog">
<p data-i18n="cookie.text">We use cookies to measure traffic and improve the site. No third-party advertising.</p>
<div class="cb-actions">
<button class="btn btn-ghost" data-i18n="cookie.reject" id="cookieReject">Reject</button>
<button class="btn btn-primary" data-i18n="cookie.accept" id="cookieAccept">Accept</button>
</div>
</div>
<div aria-hidden="true" class="sticky-cta" id="stickyCta">
<a class="btn btn-primary" data-i18n="cta.bookService" href="/contact/">Book service</a>
<a class="btn btn-wa" data-i18n="cta.whatsapp" data-wa="" href="https://wa.me/351917961230" rel="noopener" target="_blank">WhatsApp</a>
</div>
<a aria-label="WhatsApp" class="fab-wa" data-wa="" href="https://wa.me/351917961230" rel="noopener" target="_blank">
<svg aria-hidden="true" fill="currentColor" viewbox="0 0 24 24"><path d="M17.5 14.4c-.3-.2-1.7-.8-1.9-.9-.3-.1-.5-.2-.7.2-.2.3-.8 1-1 1.2-.2.2-.4.2-.6.1-1-.5-2.2-1.1-3.1-2.5-.7-1.2-.4-1.1.4-1.7.1-.1.2-.3.3-.5.1-.2 0-.4 0-.5-.1-.1-.7-1.6-.9-2.2-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.2.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.7-.7 1.9-1.4.2-.7.2-1.3.2-1.4-.1-.1-.3-.2-.6-.4zM12 2C6.5 2 2 6.5 2 12c0 2 .6 3.8 1.6 5.4L2 22l4.7-1.6c1.5.9 3.4 1.6 5.3 1.6 5.5 0 10-4.5 10-10S17.5 2 12 2z"></path></svg>
</a>
<header class="site-header" id="header">
<a aria-label="Iron Custom Motors" class="brand" href="/">{LOGO_SVG}</a>
<nav aria-label="Primary" class="nav">
<a data-i18n="nav.services" href="/services/">Services</a>
<a data-i18n="nav.projects" href="/projects/">Projects</a>
<a data-i18n="nav.pricing" href="/pricing/">Pricing</a>
<a data-i18n="nav.about" href="/about/">About</a>
<a data-i18n="nav.faq" href="/faq/">FAQ</a>
<a data-i18n="nav.contact" href="/contact/">Contact</a>
</nav>
<div class="header-actions">
<div class="lang-switcher">
<button aria-expanded="false" aria-haspopup="true" class="lang-current" id="langBtn">
<span id="langCurrent">EN</span>
<svg fill="none" height="10" stroke="currentColor" stroke-width="1.6" viewbox="0 0 12 12" width="10"><path d="M3 5l3 3 3-3"></path></svg>
</button>
<div class="lang-menu" id="langMenu" role="menu">
<button aria-current="true" data-lang="en">EN · English</button>
<button data-lang="ru">RU · Русский</button>
<button data-lang="uk">UK · Українська</button>
<button data-lang="pt">PT · Português</button>
</div>
</div>
<a class="btn btn-primary btn-sm" data-i18n="cta.bookHeader" href="/contact/">Book service</a>
<button aria-label="Open menu" class="menu-toggle" id="menuToggle"><span></span></button>
</div>
</header>
<div class="mobile-drawer" id="mobileDrawer">
<nav class="nav-mobile">
<a data-i18n="nav.services" href="/services/">Services</a>
<a data-i18n="nav.projects" href="/projects/">Projects</a>
<a data-i18n="nav.pricing" href="/pricing/">Pricing</a>
<a data-i18n="nav.about" href="/about/">About</a>
<a data-i18n="nav.faq" href="/faq/">FAQ</a>
<a data-i18n="nav.contact" href="/contact/">Contact</a>
</nav>
<div class="mobile-actions">
<a class="btn btn-primary" data-i18n="cta.bookHeader" href="/contact/">Book service</a>
<a class="btn btn-ghost" data-i18n="cta.whatsapp" data-wa="" href="https://wa.me/351917961230" rel="noopener" target="_blank">WhatsApp us</a>
<div class="mobile-langs">
<button aria-current="true" data-lang="en">EN</button>
<button data-lang="ru">RU</button>
<button data-lang="uk">UK</button>
<button data-lang="pt">PT</button>
</div>
</div>
</div>'''


FOOTER_HTML = f'''<footer class="site-footer">
<div class="container">
<div class="footer-grid">
<div class="footer-brand">
<a aria-label="Iron Custom Motors" class="logo" href="/">{LOGO_SVG}</a>
<p data-i18n="footer.tagline">Premium motorcycle service, parts, upgrades and custom expertise in Cascais.</p>
</div>
<div class="footer-col">
<h5 data-i18n="footer.col1">Services</h5>
<ul>
<li><a data-i18n="services.s1.title" href="/motorcycle-service/">Motorcycle service &amp; repair</a></li>
<li><a data-i18n="services.s2.title" href="/parts/">Parts &amp; consumables</a></li>
<li><a data-i18n="services.s3.title" href="/upgrades-tuning/">Upgrades &amp; tuning</a></li>
<li><a data-i18n="services.s4.title" href="/custom/">Custom &amp; special projects</a></li>
<li><a data-i18n="nav.preInsp" href="/pre-purchase-inspection/">Pre-purchase inspection</a></li>
<li><a data-i18n="nav.pricing" href="/pricing/">Pricing</a></li>
</ul>
</div>
<div class="footer-col">
<h5 data-i18n="footer.col2">Company</h5>
<ul>
<li><a data-i18n="nav.about" href="/about/">About</a></li>
<li><a data-i18n="nav.projects" href="/projects/">Projects</a></li>
<li><a data-i18n="nav.reviews" href="/#reviews">Reviews</a></li>
<li><a data-i18n="nav.faq" href="/faq/">FAQ</a></li>
<li><a data-i18n="nav.contact" href="/contact/">Contact</a></li>
</ul>
</div>
<div class="footer-col">
<h5 data-i18n="footer.col3">Workshop</h5>
<ul class="footer-contacts">
<li><svg fill="none" stroke="currentColor" stroke-width="1.8" viewbox="0 0 24 24"><path d="M12 22s8-7 8-13a8 8 0 10-16 0c0 6 8 13 8 13z"></path><circle cx="12" cy="9" r="3"></circle></svg><span>R. António José da Silva 100 B, São Domingos de Rana<br/>Cascais, Portugal</span></li>
<li><svg fill="none" stroke="currentColor" stroke-width="1.8" viewbox="0 0 24 24"><path d="M5 4h4l2 5-3 2c1 2 3 4 5 5l2-3 5 2v4c0 1-1 2-2 2-9 0-15-6-15-15 0-1 1-2 2-2z"></path></svg><span>+351 917 961 230</span></li>
<li><svg fill="none" stroke="currentColor" stroke-width="1.8" viewbox="0 0 24 24"><rect height="14" rx="2" width="18" x="3" y="5"></rect><path d="M3 7l9 6 9-6"></path></svg><span>Ironcustom.office@gmail.com</span></li>
<li><svg fill="none" stroke="currentColor" stroke-width="1.8" viewbox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><path d="M12 3v18M3 12h18"></path></svg><span data-i18n="footer.hours">Tue–Sat · 10:00–18:00<br/>Closed Sun &amp; Mon</span></li>
</ul>
</div>
</div>
<div class="footer-bottom">
<span>© <span id="yr">2026</span> Iron Custom Motors · <span data-i18n="footer.rights">All rights reserved</span></span>
<div class="legal-links"><a href="/privacy/" data-i18n="footer.privacy">Privacy</a><a href="/cookies/" data-i18n="footer.cookies">Cookies</a><a href="/terms/" data-i18n="footer.terms">Terms</a></div>
<div class="socials">
<a aria-label="Instagram" href="https://www.instagram.com/ironcustommotors/" rel="noopener" target="_blank"><svg fill="none" height="16" stroke="currentColor" stroke-width="1.8" viewbox="0 0 24 24" width="16"><rect height="18" rx="5" width="18" x="3" y="3"></rect><circle cx="12" cy="12" r="4"></circle><circle cx="17.5" cy="6.5" fill="currentColor" r="1"></circle></svg></a>
<a aria-label="Facebook" href="https://www.facebook.com/IronCustomMotors/" rel="noopener" target="_blank"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M14 9h3V5h-3c-2 0-4 2-4 4v2H7v4h3v8h4v-8h3l1-4h-4V9z"></path></svg></a>
<a aria-label="YouTube" href="https://www.youtube.com/@IronCustomMotors" rel="noopener" target="_blank"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M22 8s-.2-1.5-.8-2.1c-.8-.8-1.7-.8-2.1-.9C16 4.7 12 4.7 12 4.7s-4 0-7 .3c-.4 0-1.3.1-2.1.9C2.2 6.5 2 8 2 8s-.2 1.7-.2 3.5v1.7c0 1.7.2 3.5.2 3.5s.2 1.5.8 2.1c.8.8 1.9.8 2.4.9 1.7.2 7 .3 7 .3s4 0 7-.3c.4 0 1.3-.1 2.1-.9.6-.6.8-2.1.8-2.1s.2-1.7.2-3.5v-1.7C22.2 9.7 22 8 22 8zM10 15V9l5 3-5 3z"></path></svg></a>
</div>
</div>
</div>
</footer>'''

MODAL_HTML = '''<div aria-labelledby="modalTitle" aria-modal="true" class="modal-backdrop" id="modal" role="dialog">
<div class="modal">
<button aria-label="Close" class="modal-close" id="closeModal">
<svg fill="none" height="16" stroke="currentColor" stroke-width="2" viewbox="0 0 24 24" width="16"><path d="M6 6l12 12M18 6l-12 12"></path></svg>
</button>
<h3 data-i18n="form.title" id="modalTitle">Send a service request</h3>
<p class="modal-sub" data-i18n="form.sub">We'll come back to you with the next step within business hours.</p>
<form action="https://formsubmit.co/Ironcustom.office@gmail.com" class="form" id="leadForm" method="POST">
<input name="_subject" type="hidden" value="New ICM website lead"/>
<input name="_template" type="hidden" value="table"/>
<input name="_captcha" type="hidden" value="false"/>
<input autocomplete="off" name="_honey" style="display:none" tabindex="-1" type="text"/>
<div class="form-grid">
<div class="field"><label data-i18n="form.name">Your name</label><input name="name" required="" type="text"/></div>
<div class="field"><label data-i18n="form.phone">Phone / WhatsApp</label><input name="phone" placeholder="+351 ..." required="" type="tel"/></div>
<div class="field full"><label data-i18n="form.email">Email (optional)</label><input name="email" type="email"/></div>
<div class="field"><label data-i18n="form.vehicle">Vehicle (brand · model · year)</label><input name="vehicle" placeholder="e.g. BMW R nineT 2020" type="text"/></div>
<div class="field"><label data-i18n="form.service">Request type</label><select name="service"><option data-i18n="form.opt1">Motorcycle service &amp; repair</option><option data-i18n="form.opt2">Parts &amp; consumables</option><option data-i18n="form.opt3">Upgrades &amp; tuning</option><option data-i18n="form.opt4">Custom &amp; special project</option><option data-i18n="form.opt5">Other / not sure</option></select></div>
<div class="field full"><label data-i18n="form.message">Tell us about the job</label><textarea name="message" placeholder="Symptoms, history, anything that helps us prepare."></textarea></div>
</div>
<div class="form-actions">
<p class="note" data-i18n="form.note">By sending you agree to be contacted about this request. No spam, ever.</p>
<button class="btn btn-primary" type="submit"><span data-i18n="form.submit">Send request</span><svg class="arrow" fill="none" height="16" stroke="currentColor" stroke-width="2" viewbox="0 0 24 24" width="16"><path d="M5 12h14M13 6l6 6-6 6"></path></svg></button>
</div>
</form>
<div class="form-success" id="formSuccess">
<div class="check"><svg fill="none" height="32" stroke="currentColor" stroke-width="2.4" viewbox="0 0 24 24" width="32"><path d="M5 12l5 5L20 7"></path></svg></div>
<h4 data-i18n="form.successT">Request received</h4>
<p data-i18n="form.successP">We'll reply via WhatsApp or email within business hours. Talk soon.</p>
</div>
</div>
</div>'''


def render(slug):
    pre = BRAND_PREFIX[slug]
    en = PAGE_I18N[slug]["en"]
    bg = BRAND_BG[slug]

    # 8 services, 5 issues, 6 models
    services_html = "\n".join(
        f'<article class="brand-srv"><div class="num">{i:02d}</div><div><h3 data-i18n="{pre}.s{i}t">{en[f"{pre}.s{i}t"]}</h3><p data-i18n="{pre}.s{i}d">{en[f"{pre}.s{i}d"]}</p></div></article>'
        for i in range(1, 9)
    )
    issues_html = "\n".join(
        f'<div class="issue-row"><div class="bullet"></div><div><h4 data-i18n="{pre}.i{i}t">{en[f"{pre}.i{i}t"]}</h4><p data-i18n="{pre}.i{i}d">{en[f"{pre}.i{i}d"]}</p></div></div>'
        for i in range(1, 6)
    )
    models_html = "\n".join(
        f'<div class="model-card"><h3 data-i18n="{pre}.m{i}t">{en[f"{pre}.m{i}t"]}</h3><p data-i18n="{pre}.m{i}d">{en[f"{pre}.m{i}d"]}</p></div>'
        for i in range(1, 7)
    )
    tools_html = "\n".join(
        f'<div class="tool-card"><h3 data-i18n="{pre}.t{i}t">{en[f"{pre}.t{i}t"]}</h3><p data-i18n="{pre}.t{i}d">{en[f"{pre}.t{i}d"]}</p></div>'
        for i in range(1, 5)
    )
    faq_html = "\n".join(
        f'<details><summary><span class="q" data-i18n="{pre}.q{i}">{en[f"{pre}.q{i}"]}</span><svg class="chev" fill="none" height="18" stroke="currentColor" stroke-width="2" viewbox="0 0 24 24" width="18"><path d="M6 9l6 6 6-6"></path></svg></summary><div class="a" data-i18n="{pre}.a{i}">{en[f"{pre}.a{i}"]}</div></details>'
        for i in range(1, 6)
    )

    body = f'''<main>
<section class="subpage brand">
<div aria-hidden="true" class="bg" style="background-image:url('{bg}')"></div>
<div class="container">
<div class="crumb"><a data-i18n="{pre}.breadHome" href="/">Home</a><span class="sep">→</span><span data-i18n="{pre}.h1Crumb">{en[f"{pre}.h1Crumb"]}</span></div>
<div class="h-eyebrow" data-i18n="{pre}.eyebrow" style="margin-bottom:18px">{en[f"{pre}.eyebrow"]}</div>
<h1 data-i18n="{pre}.h1">{en[f"{pre}.h1"]}</h1>
<p class="lead" data-i18n="{pre}.sub">{en[f"{pre}.sub"]}</p>
<div class="subpage-cta">
<a class="btn btn-primary" data-wa="" href="https://wa.me/351917961230" rel="noopener" target="_blank"><span data-i18n="{pre}.btnWA">{en[f"{pre}.btnWA"]}</span>{ARROW_SVG}</a>
<a class="btn btn-ghost" data-i18n="{pre}.btnSend" href="/contact/">{en[f"{pre}.btnSend"]}</a>
</div>
</div>
</section>

<section class="sub-section sub-intro">
<div class="container">
<div class="heading"><span class="h-eyebrow" data-i18n="{pre}.introEyebrow">{en[f"{pre}.introEyebrow"]}</span><div><h2 data-i18n="{pre}.introTitle">{en[f"{pre}.introTitle"]}</h2></div></div>
<div>
<p data-i18n="{pre}.introP1">{en[f"{pre}.introP1"]}</p>
<p data-i18n="{pre}.introP2">{en[f"{pre}.introP2"]}</p>
<p data-i18n="{pre}.introP3">{en[f"{pre}.introP3"]}</p>
</div>
</div>
</section>

<section class="sub-section">
<div class="container">
<div class="heading"><span class="h-eyebrow" data-i18n="{pre}.toolsEyebrow">{en[f"{pre}.toolsEyebrow"]}</span><div><h2 data-i18n="{pre}.toolsTitle">{en[f"{pre}.toolsTitle"]}</h2><p class="lead" data-i18n="{pre}.toolsLead">{en[f"{pre}.toolsLead"]}</p></div></div>
<div class="tools-grid">
{tools_html}
</div>
</div>
</section>

<section class="sub-section">
<div class="container">
<div class="heading"><span class="h-eyebrow" data-i18n="{pre}.servicesEyebrow">{en[f"{pre}.servicesEyebrow"]}</span><div><h2 data-i18n="{pre}.servicesTitle">{en[f"{pre}.servicesTitle"]}</h2><p class="lead" data-i18n="{pre}.servicesLead">{en[f"{pre}.servicesLead"]}</p></div></div>
<div class="brand-srv-grid">
{services_html}
</div>
</div>
</section>

<section class="sub-section">
<div class="container">
<div class="heading"><span class="h-eyebrow" data-i18n="{pre}.issuesEyebrow">{en[f"{pre}.issuesEyebrow"]}</span><div><h2 data-i18n="{pre}.issuesTitle">{en[f"{pre}.issuesTitle"]}</h2><p class="lead" data-i18n="{pre}.issuesLead">{en[f"{pre}.issuesLead"]}</p></div></div>
<div>
{issues_html}
</div>
</div>
</section>

<section class="sub-section">
<div class="container">
<div class="heading"><span class="h-eyebrow" data-i18n="{pre}.modelsEyebrow">{en[f"{pre}.modelsEyebrow"]}</span><div><h2 data-i18n="{pre}.modelsTitle">{en[f"{pre}.modelsTitle"]}</h2><p class="lead" data-i18n="{pre}.modelsLead">{en[f"{pre}.modelsLead"]}</p></div></div>
<div class="models-grid">
{models_html}
</div>
</div>
</section>

<section class="sub-section">
<div class="container">
<div class="heading"><span class="h-eyebrow" data-i18n="{pre}.partsEyebrow">{en[f"{pre}.partsEyebrow"]}</span><div><h2 data-i18n="{pre}.partsTitle">{en[f"{pre}.partsTitle"]}</h2><p class="lead" data-i18n="{pre}.partsLead">{en[f"{pre}.partsLead"]}</p></div></div>
<div class="parts-block">
<p data-i18n="{pre}.partsList">{en[f"{pre}.partsList"]}</p>
</div>
</div>
</section>

<section class="sub-section">
<div class="container">
<div class="heading"><span class="h-eyebrow" data-i18n="{pre}.faqEyebrow">{en[f"{pre}.faqEyebrow"]}</span><div><h2 data-i18n="{pre}.faqTitle">{en[f"{pre}.faqTitle"]}</h2></div></div>
<div class="brand-faq">
{faq_html}
</div>
</div>
</section>

<section class="cta-back">
<div class="container">
<span class="h-eyebrow" data-i18n="{pre}.ctaEyebrow">{en[f"{pre}.ctaEyebrow"]}</span>
<h2 data-i18n="{pre}.ctaTitle">{en[f"{pre}.ctaTitle"]}</h2>
<p class="lead" data-i18n="{pre}.ctaText">{en[f"{pre}.ctaText"]}</p>
<div class="btns">
<a class="btn btn-primary" data-wa="" href="https://wa.me/351917961230" rel="noopener" target="_blank"><span data-i18n="{pre}.btnWA">{en[f"{pre}.btnWA"]}</span>{ARROW_SVG}</a>
<a class="btn btn-ghost" data-i18n="{pre}.btnBack" href="/">{en[f"{pre}.btnBack"]}</a>
</div>
</div>
</section>
</main>'''

    html = head(slug, "en") + "\n<body>\n" + HEADER_HTML + body + FOOTER_HTML + MODAL_HTML + f'\n<script defer="" src="/assets/main.js?v={CACHE_BUST}"></script>\n</body>\n</html>'

    out = SITE_ROOT / slug / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    return out


def main():
    for slug in BRAND_HEAD:
        out = render(slug)
        size = out.stat().st_size
        print(f"  wrote {out.relative_to(SITE_ROOT)} ({size:,} bytes)")
    print(f"\nDone. {len(BRAND_HEAD)} brand pages written.")


if __name__ == "__main__":
    main()
