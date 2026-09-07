#!/usr/bin/env python3
"""
Generate registered brand-specific landing pages.
EN sources, then run build_i18n.py to produce /ru/, /uk/, /pt/ versions.

Same skeleton for every brand:
  HERO → Intro → Tools → Services → Issues → Models → Parts catalogs → FAQ → CTA
"""

import json
from html import escape
from pathlib import Path

from bs4 import BeautifulSoup

from build_output import write_html_if_changed
from brand_pages_data import (
    BRAND_BG,
    BRAND_HEAD,
    BRAND_NAME,
    BRAND_ORDER,
    BRAND_PRICING,
    BRAND_PRICING_LABELS,
    BRAND_PREFIX,
    BRAND_RELATED_LINKS,
    PAGE_I18N,
)
from pricing_data import LABELS as PRICING_PAGE_LABELS
from pricing_data import SEC_01, SEC_02, SEC_03, SEC_04, SEC_06
from hero_images import hero_background_css, optimized_hero_url
from site_chrome import (
    patch_navigation_footer,
    render_contact_modal,
    render_pre_body_chrome,
    render_site_footer,
)
from trust_strip import TRUST_STRIP_CSS, render_trust_strip, trust_i18n
from w3_shared_data import RELATED_DESCRIPTIONS, related_description_key

SITE_ROOT = Path(__file__).resolve().parents[2]
DOMAIN = "https://ironcustommotors.com"
CACHE_BUST = "20260907a"

SEO_I18N = {
    "en": {
        "seo.localEyebrow": "Local service area",
        "seo.localTitle": "Serving Cascais, Lisbon <em>and Greater Lisbon.</em>",
        "seo.localLead": "Iron Custom Motors is based in São Domingos de Rana, Cascais. We work with riders from Cascais, Estoril, Oeiras, Sintra, Lisbon and the wider Greater Lisbon area.",
        "seo.area1t": "Cascais workshop",
        "seo.area1d": "A real workshop and client lounge, not a remote parts counter. Book service, drop off the bike, or visit to discuss a project.",
        "seo.area2t": "Multilingual process",
        "seo.area2d": "English, Russian, Ukrainian and Portuguese communication with written estimates and clear next steps.",
        "seo.area3t": "One accountable path",
        "seo.area3d": "Diagnostics, parts sourcing, installation, upgrades and follow-up happen under one workshop standard.",
        "seo.relatedEyebrow": "Related workshop paths",
        "seo.relatedTitle": "Continue through the <em>same service system.</em>",
        "seo.relatedLead": "Six common next steps from every brand page: service, upgrades, parts, custom work, tyre service and pricing.",
        "seo.relatedService": "Service and repair",
        "seo.relatedUpgrades": "Upgrades and tuning",
        "seo.relatedParts": "Parts and consumables",
        "seo.relatedCustom": "Custom and special projects",
        "seo.relatedTyres": "Tyre service",
        "seo.relatedPricing": "Pricing",
        "seo.otherBrandsTitle": "Other brands we service",
        "seo.otherBrandsLead": "Compare the same workshop process across our brand-specific service pages.",
        "seo.harleyExploreTitle": "Explore more Harley",
        "seo.harleyHub": "Harley Hub",
        "seo.harleyTuning": "Harley tuning",
        "seo.harleyCustom": "Harley custom",
    },
    "ru": {
        "seo.localEyebrow": "Локальная зона сервиса",
        "seo.localTitle": "Работаем для Cascais, Lisbon <em>и Большого Лиссабона.</em>",
        "seo.localLead": "Iron Custom Motors находится в São Domingos de Rana, Cascais. Мы работаем с райдерами из Cascais, Estoril, Oeiras, Sintra, Lisbon и всего Greater Lisbon.",
        "seo.area1t": "Мастерская в Cascais",
        "seo.area1d": "Реальная мастерская и клиентский lounge, а не удалённая стойка запчастей. Можно записаться на сервис, оставить мотоцикл или приехать обсудить проект.",
        "seo.area2t": "Процесс на вашем языке",
        "seo.area2d": "Английский, русский, украинский и португальский, письменные сметы и понятные следующие шаги.",
        "seo.area3t": "Одна точка ответственности",
        "seo.area3d": "Диагностика, подбор запчастей, установка, апгрейды и сопровождение идут по одному стандарту мастерской.",
        "seo.relatedEyebrow": "Связанные направления",
        "seo.relatedTitle": "Двигайтесь дальше в <em>той же сервисной системе.</em>",
        "seo.relatedLead": "Шесть общих следующих шагов с любой брендовой страницы: сервис, апгрейды, запчасти, кастом, шиномонтаж и цены.",
        "seo.relatedService": "Сервис и ремонт",
        "seo.relatedUpgrades": "Апгрейды и тюнинг",
        "seo.relatedParts": "Запчасти и расходники",
        "seo.relatedCustom": "Кастом и спецпроекты",
        "seo.relatedTyres": "Шиномонтаж",
        "seo.relatedPricing": "Цены",
        "seo.otherBrandsTitle": "Другие бренды, которые мы обслуживаем",
        "seo.otherBrandsLead": "Сравните тот же процесс мастерской на брендовых страницах сервиса.",
        "seo.harleyExploreTitle": "Больше о Harley",
        "seo.harleyHub": "Harley Hub",
        "seo.harleyTuning": "Тюнинг Harley",
        "seo.harleyCustom": "Кастом Harley",
    },
    "uk": {
        "seo.localEyebrow": "Локальна зона сервісу",
        "seo.localTitle": "Працюємо для Cascais, Lisbon <em>і Великого Лісабона.</em>",
        "seo.localLead": "Iron Custom Motors знаходиться у São Domingos de Rana, Cascais. Ми працюємо з райдерами з Cascais, Estoril, Oeiras, Sintra, Lisbon і всього Greater Lisbon.",
        "seo.area1t": "Майстерня у Cascais",
        "seo.area1d": "Реальна майстерня і клієнтський lounge, а не віддалена стійка запчастин. Можна записатися на сервіс, залишити мотоцикл або приїхати обговорити проєкт.",
        "seo.area2t": "Процес вашою мовою",
        "seo.area2d": "Англійська, російська, українська і португальська, письмові кошториси і зрозумілі наступні кроки.",
        "seo.area3t": "Одна точка відповідальності",
        "seo.area3d": "Діагностика, підбір запчастин, встановлення, апґрейди і супровід ідуть за одним стандартом майстерні.",
        "seo.relatedEyebrow": "Пов'язані напрямки",
        "seo.relatedTitle": "Рухайтесь далі у <em>тій самій системі сервісу.</em>",
        "seo.relatedLead": "Шість спільних наступних кроків з будь-якої брендової сторінки: сервіс, апгрейди, запчастини, кастом, шиномонтаж і ціни.",
        "seo.relatedService": "Сервіс і ремонт",
        "seo.relatedUpgrades": "Апгрейди та тюнінг",
        "seo.relatedParts": "Запчастини та витратники",
        "seo.relatedCustom": "Кастом і спецпроєкти",
        "seo.relatedTyres": "Шиномонтаж",
        "seo.relatedPricing": "Ціни",
        "seo.otherBrandsTitle": "Інші бренди, які ми обслуговуємо",
        "seo.otherBrandsLead": "Порівняйте той самий процес майстерні на брендових сторінках сервісу.",
        "seo.harleyExploreTitle": "Більше про Harley",
        "seo.harleyHub": "Harley Hub",
        "seo.harleyTuning": "Тюнінг Harley",
        "seo.harleyCustom": "Кастом Harley",
    },
    "pt": {
        "seo.localEyebrow": "Área local de serviço",
        "seo.localTitle": "Servimos Cascais, Lisboa <em>e a Grande Lisboa.</em>",
        "seo.localLead": "A Iron Custom Motors fica em São Domingos de Rana, Cascais. Trabalhamos com riders de Cascais, Estoril, Oeiras, Sintra, Lisboa e toda a Grande Lisboa.",
        "seo.area1t": "Oficina em Cascais",
        "seo.area1d": "Uma oficina real com lounge para clientes, não um balcão remoto de peças. Marque serviço, deixe a moto ou visite para discutir um projeto.",
        "seo.area2t": "Processo multilingue",
        "seo.area2d": "Comunicação em inglês, russo, ucraniano e português, com orçamentos escritos e próximos passos claros.",
        "seo.area3t": "Uma rota responsável",
        "seo.area3d": "Diagnóstico, sourcing de peças, instalação, upgrades e acompanhamento seguem o mesmo padrão de oficina.",
        "seo.relatedEyebrow": "Caminhos relacionados",
        "seo.relatedTitle": "Continue no <em>mesmo sistema de serviço.</em>",
        "seo.relatedLead": "Seis próximos passos comuns em todas as páginas de marca: serviço, upgrades, peças, custom, pneus e preços.",
        "seo.relatedService": "Serviço e reparação",
        "seo.relatedUpgrades": "Upgrades e tuning",
        "seo.relatedParts": "Peças e consumíveis",
        "seo.relatedCustom": "Custom e projetos especiais",
        "seo.relatedTyres": "Pneus de mota",
        "seo.relatedPricing": "Preços",
        "seo.otherBrandsTitle": "Outras marcas que reparamos",
        "seo.otherBrandsLead": "Compare o mesmo processo de oficina nas nossas páginas de serviço por marca.",
        "seo.harleyExploreTitle": "Explore mais sobre Harley",
        "seo.harleyHub": "Harley Hub",
        "seo.harleyTuning": "Tuning Harley",
        "seo.harleyCustom": "Customização Harley",
    },
}

BRAND_SERVICE_LABELS = {
    "en": {
        "harley-service": "Harley-Davidson service",
        "bmw-service": "BMW Motorrad service",
        "ducati-service": "Ducati service",
        "suzuki-service": "Suzuki service",
        "honda-service": "Honda service",
        "royal-enfield-service": "Royal Enfield service",
        "triumph-service": "Triumph service",
    },
    "pt": {
        "harley-service": "serviço Harley-Davidson",
        "bmw-service": "serviço BMW",
        "ducati-service": "serviço Ducati",
        "suzuki-service": "serviço Suzuki",
        "honda-service": "serviço Honda",
        "royal-enfield-service": "serviço Royal Enfield",
        "triumph-service": "serviço Triumph",
    },
    "ru": {
        "harley-service": "сервис Harley-Davidson",
        "bmw-service": "сервис BMW",
        "ducati-service": "сервис Ducati",
        "suzuki-service": "сервис Suzuki",
        "honda-service": "сервис Honda",
        "royal-enfield-service": "сервис Royal Enfield",
        "triumph-service": "сервис Triumph",
    },
    "uk": {
        "harley-service": "сервіс Harley-Davidson",
        "bmw-service": "сервіс BMW",
        "ducati-service": "сервіс Ducati",
        "suzuki-service": "сервіс Suzuki",
        "honda-service": "сервіс Honda",
        "royal-enfield-service": "сервіс Royal Enfield",
        "triumph-service": "сервіс Triumph",
    },
}


def page_i18n_for(slug):
    pages = {}
    for lang, values in PAGE_I18N[slug].items():
        merged = {**values, **SEO_I18N[lang]}
        # W3 retired the generic related-card filler stored in legacy page data.
        # Filter it at the renderer boundary until the historical data module is
        # migrated independently; generated HTML must contain only registry copy.
        merged.pop("seo.relatedText", None)
        merged.pop("seo.otherBrandText", None)
        pricing = brand_pricing_source(slug)
        labels = BRAND_PRICING_LABELS[lang]
        pre = BRAND_PREFIX[slug]
        merged.update({
            f"{pre}.pricingEyebrow": labels["eyebrow"],
            f"{pre}.pricingTitle": labels["title"].format(brand=BRAND_NAME[slug]),
            "pricing.scheduled": labels["scheduled"],
            "pricing.included": labels["included"],
            "pricing.air": labels[f"air_{pricing['config']['air_filter']}"],
            "pricing.valves": labels["valves"],
            "pricing.engine": labels["engine"],
            "pricing.check": labels["check"],
            "pricing.adjust": labels["adjust"],
            "pricing.estimate": labels["estimate"],
            "pricing.specific": labels["specific"],
            "pricing.universal": labels["universal"],
            "pricing.link": labels["pricing_link"],
            "pricing.from": PRICING_PAGE_LABELS[lang]["from"],
            "pricing.perHour": PRICING_PAGE_LABELS[lang]["per_hour"],
        })
        for index, item in enumerate(pricing["group"]["checklist"][lang], 1):
            merged[f"pricing.checklist{index}"] = item
        for index, row in enumerate(pricing["valve_rows"], 1):
            merged[f"pricing.valveRow{index}"] = valve_row_name(slug, row, labels)
        for card in pricing["extras"]:
            merged[f"pricing.extra.{card['id']}.name"] = card["name"][lang]
            merged[f"pricing.extra.{card['id']}.desc"] = card["desc"][lang]
        for item in pricing["universal"]:
            merged[f"pricing.universal.{item['id']}"] = item["name"][lang]
        merged.update({
            f"seo.brand.{brand_slug}": label
            for brand_slug, label in BRAND_SERVICE_LABELS[lang].items()
        })
        merged.update(trust_i18n(lang))
        merged.update({
            related_description_key(path): descriptions[lang]
            for path, descriptions in RELATED_DESCRIPTIONS.items()
        })
        for key, value in values.items():
            if key.startswith("seo.") and not key.startswith(("seo.related", "seo.otherBrand")):
                merged[key] = value
        pages[lang] = merged
    return pages


def _item_by_id(items, item_id):
    for item in items:
        if item.get("id") == item_id:
            return item
    raise KeyError(f"Pricing item not found: {item_id}")


def brand_pricing_source(slug):
    config = BRAND_PRICING[slug]
    group = _item_by_id(SEC_02["groups"], config["group"])
    valve_table_rows = {row[0]: row for row in SEC_04["valve_table"]["rows"]}
    rows = []
    for row_config in config["valve_rows"]:
        source = valve_table_rows[row_config["row"]]
        if row_config.get("split"):
            check = [part.strip() for part in source[1].split("/")]
            adjust = [part.strip() for part in source[2].split("/")]
            rows.extend([
                {"kind": "twin", "check": check[0], "adjust": adjust[0]},
                {"kind": "inline_four", "check": check[1], "adjust": adjust[1]},
            ])
        else:
            rows.append({"kind": "source", "source_name": source[0], "check": source[1], "adjust": source[2]})
    for estimate_id in config["estimate_rows"]:
        rows.append({"kind": "estimate", "estimate_id": estimate_id, "check": None, "adjust": None})

    brake_items = SEC_03["subgroups"][0]["items"]
    universal = [
        _item_by_id(SEC_01["cards"], "fault_diagnostics"),
        _item_by_id(brake_items, "brake_fluid_non_abs"),
        _item_by_id(brake_items, "brake_fluid_abs"),
        _item_by_id(SEC_06["cards"], "other_work"),
        _item_by_id(SEC_01["cards"], "pre_purchase_inspection"),
    ]
    return {
        "config": config,
        "group": group,
        "valve_rows": rows,
        "extras": [_item_by_id(SEC_02["brand_specific_cards"], item_id) for item_id in config["extras"]],
        "universal": universal,
    }


def valve_row_name(slug, row, labels):
    if row["kind"] == "source":
        source_name = row["source_name"]
        if source_name == "Triumph / Royal Enfield twin":
            return f"{BRAND_NAME[slug]} {labels['twin']}"
        return source_name
    if row["kind"] == "estimate":
        return labels[row["estimate_id"]]
    return labels[row["kind"]]



def numbered_items(values, prefix, item_prefix, suffixes):
    items = []
    idx = 1
    while all(values.get(f"{prefix}.{item_prefix}{idx}{suffix}") for suffix in suffixes):
        items.append(idx)
        idx += 1
    return items

def numbered_text_blocks(values, prefix, item_prefix):
    items = []
    idx = 1
    while values.get(f"{prefix}.{item_prefix}{idx}"):
        items.append(idx)
        idx += 1
    return items

ARROW_SVG = '<svg fill="none" height="18" stroke="currentColor" stroke-width="2" viewbox="0 0 24 24" width="18"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>'

SHARED_STYLES = """.subpage{padding:160px 0 100px;background:#0a0a0a;position:relative;overflow:hidden;isolation:isolate}
.subpage::before{content:"";position:absolute;top:-30%;right:-15%;width:600px;height:600px;background:radial-gradient(circle,rgba(255,87,34,.20),transparent 60%);pointer-events:none;z-index:1}
.subpage::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,10,10,.45) 0%,rgba(10,10,10,.6) 50%,rgba(10,10,10,.96) 100%);z-index:0;pointer-events:none}
.subpage .container{position:relative;z-index:1}
.crumb{display:flex;align-items:center;gap:10px;font-family:var(--font-ui);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--text-mute);margin-bottom:24px}
.crumb a{color:var(--text-dim)}
.crumb a:hover{color:var(--accent)}
.crumb .sep{color:var(--accent)}
.subpage h1{font-family:var(--font-display);font-weight:800;line-height:.92;letter-spacing:-.01em;text-transform:uppercase;font-size:clamp(30px,4vw,52px);color:#fff;max-width:18ch;margin-bottom:24px}
.subpage h1 .accent{color:var(--accent)}
.subpage .lead{max-width:60ch;color:var(--text-dim)}
.subpage-cta{display:flex;gap:14px;flex-wrap:wrap;margin-top:36px}
.sub-section{padding:var(--gap) 0;background:#0a0a0a;border-top:1px solid var(--border)}
.sub-section .heading{margin-bottom:60px;display:grid;grid-template-columns:1fr 1.4fr;gap:60px;align-items:end;padding-bottom:30px;border-bottom:1px solid var(--border)}
.sub-section .heading h2{margin:0;font-family:var(--font-display);font-weight:800;text-transform:uppercase;font-size:clamp(24px,3.2vw,44px);line-height:.95;letter-spacing:-.005em;color:#fff}
.sub-section .heading h2 em{color:var(--accent);font-style:italic}
.sub-section .heading p.lead{margin-top:18px}
.sub-intro p{font-family:var(--font-ui);font-weight:400;font-size:clamp(18px,1.6vw,22px);line-height:1.55;color:var(--text);max-width:64ch;margin-bottom:18px}
.sub-intro p:last-child{color:var(--text-dim);font-size:clamp(15px,1.2vw,18px)}
.cta-back{padding:var(--gap) 0;background:#0a0a0a;text-align:center;border-top:1px solid var(--border)}
.cta-back .container{max-width:760px}
.cta-back h2{margin-bottom:18px;font-family:var(--font-display);font-weight:800;text-transform:uppercase;font-size:clamp(24px,3.2vw,42px);line-height:.95;color:#fff}
.cta-back .lead{margin:0 auto 30px;max-width:54ch}
.cta-back .btns{display:flex;justify-content:center;gap:14px;flex-wrap:wrap}
@media (max-width:1100px){.sub-section .heading{grid-template-columns:1fr;gap:24px}}
@media (max-width:760px){.subpage{padding-top:130px}}"""

# Brand-page-specific CSS
BRAND_CSS = """.subpage.brand{padding:140px 0 90px}
.subpage.brand .bg{position:absolute;inset:0;z-index:-1;background-size:cover;background-position:center;filter:saturate(.85) contrast(1.05) brightness(.5)}
.tools-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:18px;margin-top:30px}
.tool-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);padding:24px 22px}
.tool-card h3{font-family:var(--font-display);font-weight:800;text-transform:uppercase;font-size:20px;color:#fff;margin-bottom:8px}
.tool-card p{font-size:14px;color:var(--text-dim);max-width:46ch}
.brand-srv-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;margin-top:30px}
.brand-srv{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);padding:24px 22px;display:grid;grid-template-columns:48px 1fr;gap:14px;align-items:start}
.brand-srv .num{font-family:var(--font-display);font-weight:800;font-size:28px;color:var(--accent);line-height:1}
.brand-srv h3{font-family:var(--font-display);font-weight:800;text-transform:uppercase;font-size:18px;color:#fff;margin-bottom:6px;line-height:1.1}
.brand-srv p{font-size:14px;color:var(--text-dim)}
.brand-pricing .heading{align-items:start}
.brand-pricing-intro{font-size:16px;line-height:1.65;color:var(--text-dim);max-width:72ch}
.brand-price-panel{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);padding:26px 28px;margin-bottom:22px}
.brand-price-head{display:flex;justify-content:space-between;align-items:flex-start;gap:18px;flex-wrap:wrap;margin-bottom:16px}
.brand-price-head h3,.brand-price-subtitle{font-family:var(--font-display);font-weight:800;text-transform:uppercase;color:#fff;line-height:1.05}
.brand-price-head h3{font-size:clamp(18px,1.7vw,24px)}
.brand-price-subtitle{font-size:clamp(19px,2vw,27px);margin:34px 0 16px}
.brand-price-amount{font-family:var(--font-display);font-weight:800;color:var(--accent);font-size:clamp(22px,2.2vw,30px);white-space:nowrap}
.brand-price-amount .from,.brand-price-amount .suffix{font-family:var(--font-ui);font-size:.5em;font-weight:600;text-transform:uppercase;letter-spacing:.08em;color:var(--text-mute);margin-right:5px}
.brand-price-amount .suffix{margin:0 0 0 5px}
.brand-price-note{font-size:14px;color:var(--text-dim);margin:0 0 14px}
.brand-price-note.air{color:var(--text);margin-top:16px}
.brand-price-checklist{list-style:none;padding:16px 0 0;margin:0;border-top:1px solid var(--border);display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:7px 22px}
.brand-price-checklist li{position:relative;padding-left:15px;font-size:13px;line-height:1.45;color:var(--text-dim)}
.brand-price-checklist li::before{content:"";position:absolute;left:0;top:9px;width:7px;height:1px;background:var(--accent)}
.brand-price-table-wrap{overflow-x:auto;border:1px solid var(--border);border-radius:var(--radius-lg)}
.brand-price-table{width:100%;border-collapse:collapse;font-family:var(--font-ui);min-width:620px}
.brand-price-table th,.brand-price-table td{text-align:left;padding:14px 18px;border-bottom:1px solid var(--border)}
.brand-price-table th{font-size:11px;text-transform:uppercase;letter-spacing:.1em;color:var(--accent);background:rgba(255,87,34,.05)}
.brand-price-table td{font-size:14px;color:var(--text)}
.brand-price-table td:not(:first-child){font-family:var(--font-display);font-weight:700;color:var(--accent);font-size:17px}
.brand-price-table tr:last-child td{border-bottom:0}
.brand-price-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
.brand-price-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);padding:22px 20px}
.brand-price-card h4{font-family:var(--font-display);font-size:18px;line-height:1.1;text-transform:uppercase;color:#fff;margin:0 0 10px}
.brand-price-card p{font-size:13px;line-height:1.5;color:var(--text-dim);margin:0}
.brand-price-card .brand-price-amount{font-size:22px;margin:14px 0 0}
.brand-price-link{display:inline-flex;margin-top:26px;font-family:var(--font-ui);font-size:13px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--accent)}
.issue-row{display:grid;grid-template-columns:50px 1fr;gap:18px;padding:20px 0;border-bottom:1px solid var(--border);align-items:start;transition:padding-left .25s var(--ease)}
.issue-row:hover{padding-left:10px}
.issue-row .bullet{width:12px;height:12px;background:var(--accent);clip-path:polygon(0 0, 100% 0, 100% 70%, 70% 100%, 0 100%);margin-top:6px}
.issue-row h4{font-family:var(--font-display);font-weight:700;text-transform:uppercase;font-size:17px;color:#fff;margin-bottom:5px;letter-spacing:.01em}
.issue-row p{font-size:14px;color:var(--text-dim);max-width:64ch}
.models-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:30px}
.model-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);padding:22px 20px}
.model-card h3{font-family:var(--font-display);font-weight:800;text-transform:uppercase;font-size:18px;color:#fff;margin-bottom:8px}
.model-card p{font-size:13px;color:var(--text-dim)}
.parts-block{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);padding:30px 28px;margin-top:24px}
.parts-block p{font-size:15px;color:var(--text-dim);line-height:1.65}
.brand-faq{display:grid;grid-template-columns:1fr;gap:12px;margin-top:30px}
.brand-faq details{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);overflow:hidden}
.brand-faq summary{cursor:pointer;list-style:none;padding:20px 24px;display:flex;align-items:flex-start;gap:18px;font-family:var(--font-display);font-weight:700;text-transform:uppercase;font-size:clamp(15px,1.3vw,18px);color:#fff;line-height:1.25;letter-spacing:.01em;transition:color .2s var(--ease)}
.brand-faq summary:hover{color:var(--accent)}
.brand-faq summary::-webkit-details-marker{display:none}
.brand-faq .chev{margin-left:auto;color:var(--text-dim);transition:transform .25s var(--ease);flex-shrink:0}
.brand-faq details[open] .chev{transform:rotate(180deg)}
.brand-faq .a{padding:0 24px 22px 24px;color:var(--text-dim);font-size:14px;line-height:1.65;max-width:84ch}
.trust-row{display:grid;grid-template-columns:30px 1fr;gap:26px;padding:24px 0;border-bottom:1px solid var(--border);align-items:start;transition:padding-left .25s var(--ease)}
.trust-row:hover{padding-left:10px}
.trust-row .bullet{width:14px;height:14px;background:var(--accent);clip-path:polygon(0 0, 100% 0, 100% 70%, 70% 100%, 0 100%);margin-top:6px}
.trust-row h4{margin-bottom:8px;color:#fff;font-size:clamp(16px,1.4vw,20px)}
.trust-row p{font-size:15px;color:var(--text-dim);max-width:64ch}
.related-card-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin-top:24px}
.related-card{position:relative;display:flex;min-height:128px;flex-direction:column;justify-content:space-between;gap:18px;padding:20px 18px;border:1px solid var(--border);border-radius:16px;background:var(--surface);color:#fff;text-decoration:none;overflow:hidden;transition:transform .25s var(--ease),border-color .25s var(--ease),background .25s var(--ease)}
.related-card::after{content:"";position:absolute;inset:0;background:radial-gradient(circle at 80% 10%,rgba(255,87,34,.16),transparent 52%);opacity:0;transition:opacity .25s var(--ease);pointer-events:none}
.related-card:hover,.related-card:focus-visible{transform:translateY(-4px);border-color:var(--accent);background:var(--surface-2);outline:none}
.related-card:hover::after,.related-card:focus-visible::after{opacity:1}
.related-card-label{position:relative;z-index:1;font-family:var(--font-display);font-weight:800;text-transform:uppercase;font-size:clamp(17px,1.35vw,22px);line-height:1;color:#fff}
.related-card-text{position:relative;z-index:1;font-size:13px;line-height:1.45;color:var(--text-dim);max-width:26ch}
.related-card-arrow{position:relative;z-index:1;align-self:flex-start;font-family:var(--font-ui);font-weight:700;color:var(--accent);letter-spacing:.08em}
.related-subhead{margin:36px 0 14px;padding-top:20px;border-top:1px solid var(--border)}
.related-subhead h3{font-family:var(--font-display);font-weight:800;text-transform:uppercase;font-size:clamp(20px,2vw,30px);line-height:1;color:#fff;margin-bottom:8px}
.related-subhead p{font-size:14px;color:var(--text-dim);max-width:62ch}
.brand-pill-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.brand-pill{display:flex;min-height:104px;align-items:center;justify-content:space-between;gap:14px;padding:15px 16px;border:1px solid var(--border);border-radius:8px;background:rgba(255,255,255,.035);font-family:var(--font-ui);font-weight:700;color:#fff;text-decoration:none;transition:transform .25s var(--ease),border-color .25s var(--ease),background .25s var(--ease),color .25s var(--ease)}
.brand-pill::after{content:"→";color:var(--accent);font-size:16px;line-height:1}
.brand-pill:hover,.brand-pill:focus-visible{transform:translateY(-3px);border-color:var(--accent);background:rgba(255,87,34,.08);color:var(--accent);outline:none}
.brand-pill-copy{display:flex;min-width:0;flex-direction:column;gap:7px}.brand-pill-label{font-weight:800;text-transform:uppercase;letter-spacing:.08em;font-size:13px;line-height:1.15}.brand-pill-text{font-weight:400;letter-spacing:0;font-size:12px;line-height:1.4;text-transform:none;color:var(--text-dim)}
.hero-alt-img{position:absolute!important;width:1px!important;height:1px!important;overflow:hidden!important;clip:rect(0 0 0 0)!important;clip-path:inset(50%)!important;white-space:nowrap!important}
@media (max-width:900px){.tools-grid,.brand-srv-grid,.models-grid,.brand-price-grid{grid-template-columns:1fr}.issue-row{grid-template-columns:30px 1fr}}
@media (max-width:600px){.brand-price-panel{padding:22px 18px}.brand-price-checklist{grid-template-columns:1fr}}
@media (max-width:900px){.related-card-grid,.brand-pill-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:760px){.related-card-grid,.brand-pill-grid{grid-template-columns:1fr}.related-card{min-height:112px}.trust-row{grid-template-columns:20px 1fr;gap:16px}}""" + TRUST_STRIP_CSS


def head(slug, lang):
    meta = BRAND_HEAD[slug][lang]
    pre = BRAND_PREFIX[slug]
    canonical = f"{DOMAIN}/{slug}/"
    og_locale = {"en":"en_US","ru":"ru_RU","uk":"uk_UA","pt":"pt_PT"}[lang]
    brand_name = BRAND_NAME[slug]

    page_url = canonical

    service_name = BeautifulSoup(
        page_i18n_for(slug)["en"][f"{pre}.h1"], "html.parser"
    ).get_text(" ", strip=True)
    json_ld_blocks = [
        {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": service_name,
            "serviceType": f"{brand_name} motorcycle service and repair",
            "provider": {"@id": f"{DOMAIN}/#business"},
            "brand": {"@type": "Brand", "name": brand_name},
            "areaServed": [
                {"@type": "City", "name": "Cascais"},
                {"@type": "City", "name": "Estoril"},
                {"@type": "City", "name": "Oeiras"},
                {"@type": "City", "name": "Sintra"},
                {"@type": "City", "name": "Lisbon"},
                {"@type": "AdministrativeArea", "name": "Greater Lisbon"},
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
    en = page_i18n_for(slug)["en"]
    faq_main_entity = []
    i = 1
    while True:
        q = en.get(f"{pre}.q{i}")
        a = en.get(f"{pre}.a{i}")
        if not (q and a):
            break
        faq_main_entity.append({
            "@type": "Question", "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": BeautifulSoup(a, "html.parser").get_text(" ", strip=True),
            },
        })
        i += 1
    if faq_main_entity:
        json_ld_blocks.append({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "url": page_url,
            "mainEntity": faq_main_entity,
            "name": meta["title"],
        })

    json_ld_html = "".join(
        f'<script type="application/ld+json">{json.dumps(b, ensure_ascii=False)}</script>' for b in json_ld_blocks
    )

    hreflang_codes = {"en": "en", "ru": "ru", "uk": "uk", "pt": "pt-PT"}
    hreflang_html = "".join(
        f'<link rel="alternate" hreflang="{hreflang_codes[lg]}" href="{DOMAIN}/{slug}/"/>' if lg == "en"
        else f'<link rel="alternate" hreflang="{hreflang_codes[lg]}" href="{DOMAIN}/{lg}/{slug}/"/>'
        for lg in ["en","ru","uk","pt"]
    )
    hreflang_html += f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}/{slug}/"/>'

    i18n_json = json.dumps(page_i18n_for(slug), ensure_ascii=False)

    return f'''<!DOCTYPE html>
<html data-lang="{lang}" lang="{lang}">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1, viewport-fit=cover" name="viewport"/>
<meta content="#0a0a0a" name="theme-color"/>
<meta content="max-image-preview:large" name="robots"/>
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
<link href="https://fonts.googleapis.com/css2?family=Saira:wght@300;400;500;600;700;800;900&amp;family=Saira+Condensed:wght@400;600;700;800;900&amp;family=Roboto+Condensed:wght@400;500;600;700;800;900&amp;family=Inter:wght@300;400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="/assets/main.css?v={CACHE_BUST}" rel="stylesheet"/>
<style>
{SHARED_STYLES}
{BRAND_CSS}
</style>
{json_ld_html}<script>window.ICM_I18N_PAGE = {i18n_json};</script>
{hreflang_html}
</head>'''


HEADER_HTML = render_pre_body_chrome("en")


FOOTER_HTML = render_site_footer("en")


MODAL_HTML = render_contact_modal("en")


def display_price(value, suffix=""):
    if value.endswith(" EUR"):
        value = value[:-4] + suffix + " €"
    elif suffix:
        value += suffix
    return value


def render_price(item):
    from_html = '<span class="from" data-i18n="pricing.from">from</span>' if item.get("price_from") else ""
    suffix = item.get("price_suffix", "")
    amount_suffix = suffix if suffix != "per_hour" else ""
    per_hour = '<span class="suffix" data-i18n="pricing.perHour">/hour</span>' if suffix == "per_hour" else ""
    return f'<div class="brand-price-amount">{from_html}<span class="amount">{escape(display_price(item["price"], amount_suffix))}</span>{per_hour}</div>'


def render_pricing_section(slug, en):
    pre = BRAND_PREFIX[slug]
    source = brand_pricing_source(slug)
    group = source["group"]
    checklist = "".join(
        f'<li data-i18n="pricing.checklist{index}">{escape(item)}</li>'
        for index, item in enumerate(group["checklist"]["en"], 1)
    )
    valves = ""
    if source["valve_rows"]:
        rows = []
        for index, row in enumerate(source["valve_rows"], 1):
            if row["kind"] == "estimate":
                estimate = '<span data-i18n="pricing.estimate">Written estimate per model</span>'
                check = adjust = estimate
            else:
                check = escape(f'{row["check"]} €')
                adjust = escape(f'{row["adjust"]} €')
            rows.append(f'''<tr>
<td data-i18n="pricing.valveRow{index}">{escape(en[f"pricing.valveRow{index}"])}</td>
<td>{check}</td><td>{adjust}</td>
</tr>''')
        valves = f'''<h3 class="brand-price-subtitle" data-i18n="pricing.valves">{escape(en["pricing.valves"])}</h3>
<div class="brand-price-table-wrap"><table class="brand-price-table">
<thead><tr><th data-i18n="pricing.engine">{escape(en["pricing.engine"])}</th><th data-i18n="pricing.check">{escape(en["pricing.check"])}</th><th data-i18n="pricing.adjust">{escape(en["pricing.adjust"])}</th></tr></thead>
<tbody>{''.join(rows)}</tbody></table></div>'''

    extras = ""
    if source["extras"]:
        cards = "".join(
            f'''<article class="brand-price-card" data-price-id="{escape(card["id"])}">
<h4 data-i18n="pricing.extra.{escape(card["id"])}.name">{escape(card["name"]["en"])}</h4>
<p data-i18n="pricing.extra.{escape(card["id"])}.desc">{escape(card["desc"]["en"])}</p>
{render_price(card)}
</article>'''
            for card in source["extras"]
        )
        extras = f'''<h3 class="brand-price-subtitle" data-i18n="pricing.specific">{escape(en["pricing.specific"])}</h3>
<div class="brand-price-grid">{cards}</div>'''

    universal_cards = "".join(
        f'''<article class="brand-price-card" data-price-id="{escape(item["id"])}">
<h4 data-i18n="pricing.universal.{escape(item["id"])}">{escape(item["name"]["en"])}</h4>
{render_price(item)}
</article>'''
        for item in source["universal"]
    )
    return f'''<section class="sub-section brand-pricing" data-brand-pricing="" data-source-group="{escape(source["config"]["group"])}">
<div class="container">
<div class="heading"><span class="h-eyebrow" data-i18n="{pre}.pricingEyebrow">{escape(en[f"{pre}.pricingEyebrow"])}</span><div><h2 data-i18n="{pre}.pricingTitle">{escape(en[f"{pre}.pricingTitle"])}</h2><p class="brand-pricing-intro" data-i18n="{pre}.pricingIntro">{escape(en[f"{pre}.pricingIntro"])}</p></div></div>
<article class="brand-price-panel" data-price-id="scheduled-service">
<div class="brand-price-head"><h3><span data-i18n="pricing.scheduled">{escape(en["pricing.scheduled"])}</span> · {escape(group["name"])}</h3>{render_price(group)}</div>
<p class="brand-price-note" data-i18n="pricing.included">{escape(en["pricing.included"])}</p>
<ul class="brand-price-checklist">{checklist}</ul>
<p class="brand-price-note air" data-i18n="pricing.air">{escape(en["pricing.air"])}</p>
</article>
{valves}
{extras}
<h3 class="brand-price-subtitle" data-i18n="pricing.universal">{escape(en["pricing.universal"])}</h3>
<div class="brand-price-grid">{universal_cards}</div>
<a class="brand-price-link" data-i18n="pricing.link" href="/pricing/">{escape(en["pricing.link"])}</a>
</div>
</section>'''


def render_related_sections(slug, en):
    related = "\n".join(
        f'''<a class="related-card" href="{href}">
<span class="related-card-label" data-i18n="{key}">{label}</span>
<span class="related-card-text" data-i18n="{related_description_key(href)}">{en[related_description_key(href)]}</span>
<span aria-hidden="true" class="related-card-arrow">→</span>
</a>'''
        for key, href, label in BRAND_RELATED_LINKS[slug]
    )
    other_brands = "\n".join(
        f'''<a class="brand-pill" href="/{other_slug}/"><span class="brand-pill-copy"><span class="brand-pill-label" data-i18n="seo.brand.{other_slug}">{en[f"seo.brand.{other_slug}"]}</span><span class="brand-pill-text" data-i18n="{related_description_key(f"/{other_slug}/")}">{en[related_description_key(f"/{other_slug}/")]}</span></span></a>'''
        for other_slug in BRAND_ORDER
        if other_slug != slug
    )

    return f'''<section class="sub-section" data-enhancement="money-related">
<div class="container">
<div class="heading reveal">
<span class="h-eyebrow" data-i18n="seo.relatedEyebrow">{en["seo.relatedEyebrow"]}</span>
<div>
<h2 data-i18n="seo.relatedTitle">{en["seo.relatedTitle"]}</h2>
<p class="lead" data-i18n="seo.relatedLead">{en["seo.relatedLead"]}</p>
</div>
</div>
<div class="reveal-stagger">
<div class="related-card-grid">
{related}
</div>
<div class="related-subhead">
<h3 data-i18n="seo.otherBrandsTitle">{en["seo.otherBrandsTitle"]}</h3>
</div>
<div class="brand-pill-grid">
{other_brands}
</div>
</div>
</div>
</section>

<section class="sub-section" data-enhancement="money-local">
<div class="container">
<div class="heading reveal">
<span class="h-eyebrow" data-i18n="seo.localEyebrow">{en["seo.localEyebrow"]}</span>
<div>
<h2 data-i18n="seo.localTitle">{en["seo.localTitle"]}</h2>
<p class="lead" data-i18n="seo.localLead">{en["seo.localLead"]}</p>
</div>
</div>
<div class="reveal-stagger">
<div class="trust-row"><span class="bullet"></span><div><h4 data-i18n="seo.area1t">{en["seo.area1t"]}</h4><p data-i18n="seo.area1d">{en["seo.area1d"]}</p></div></div>
<div class="trust-row"><span class="bullet"></span><div><h4 data-i18n="seo.area2t">{en["seo.area2t"]}</h4><p data-i18n="seo.area2d">{en["seo.area2d"]}</p></div></div>
<div class="trust-row"><span class="bullet"></span><div><h4 data-i18n="seo.area3t">{en["seo.area3t"]}</h4><p data-i18n="seo.area3d">{en["seo.area3d"]}</p></div></div>
</div>
</div>
</section>'''


def render_harley_explore(slug, en):
    if slug != "harley-service":
        return ""
    links = (
        ("seo.harleyHub", "/harley/"),
        ("seo.harleyTuning", "/harley-tuning/"),
        ("seo.harleyCustom", "/harley-custom/"),
    )
    items = "\n".join(
        f'<a class="brand-pill" data-i18n="{key}" href="{href}">{en[key]}</a>'
        for key, href in links
    )
    return f'''<section class="sub-section">
<div class="container">
<div class="related-subhead" style="margin-top:0;padding-top:0;border-top:0">
<h3 data-i18n="seo.harleyExploreTitle">{en["seo.harleyExploreTitle"]}</h3>
</div>
<div class="brand-pill-grid">
{items}
</div>
</div>
</section>'''


def render(slug):
    pre = BRAND_PREFIX[slug]
    en = page_i18n_for(slug)["en"]
    bg = BRAND_BG[slug]
    hero_alt = en.get(f"{pre}.heroAlt", f"{BRAND_NAME[slug]} motorcycle service at Iron Custom Motors")
    hero_alt_src = optimized_hero_url(bg, 768, "jpg")
    hero_alt_srcset = ", ".join(
        f"{optimized_hero_url(bg, width, 'jpg')} {width}w" for width in (768, 1280, 1920)
    )

    service_keys = numbered_items(en, pre, "s", ("t", "d"))
    issue_keys = numbered_items(en, pre, "i", ("t", "d"))
    model_keys = numbered_items(en, pre, "m", ("t", "d"))
    tool_keys = numbered_items(en, pre, "t", ("t", "d"))
    intro_keys = numbered_text_blocks(en, pre, "introP")

    services_html = "\n".join(
        f'<article class="brand-srv"><div class="num">{i:02d}</div><div><h3 data-i18n="{pre}.s{i}t">{en[f"{pre}.s{i}t"]}</h3><p data-i18n="{pre}.s{i}d">{en[f"{pre}.s{i}d"]}</p></div></article>'
        for i in service_keys
    )
    issues_html = "\n".join(
        f'<div class="issue-row"><div class="bullet"></div><div><h4 data-i18n="{pre}.i{i}t">{en[f"{pre}.i{i}t"]}</h4><p data-i18n="{pre}.i{i}d">{en[f"{pre}.i{i}d"]}</p></div></div>'
        for i in issue_keys
    )
    models_html = "\n".join(
        f'<div class="model-card"><h3 data-i18n="{pre}.m{i}t">{en[f"{pre}.m{i}t"]}</h3><p data-i18n="{pre}.m{i}d">{en[f"{pre}.m{i}d"]}</p></div>'
        for i in model_keys
    )
    tools_html = "\n".join(
        f'<div class="tool-card"><h3 data-i18n="{pre}.t{i}t">{en[f"{pre}.t{i}t"]}</h3><p data-i18n="{pre}.t{i}d">{en[f"{pre}.t{i}d"]}</p></div>'
        for i in tool_keys
    )
    intro_html = "\n".join(
        f'<p data-i18n="{pre}.introP{i}">{en[f"{pre}.introP{i}"]}</p>'
        for i in intro_keys
    )
    faq_keys = []
    faq_idx = 1
    while en.get(f"{pre}.q{faq_idx}") and en.get(f"{pre}.a{faq_idx}"):
        faq_keys.append(faq_idx)
        faq_idx += 1
    faq_html = "\n".join(
        f'<details><summary><span class="q" data-i18n="{pre}.q{i}">{en[f"{pre}.q{i}"]}</span><svg class="chev" fill="none" height="18" stroke="currentColor" stroke-width="2" viewbox="0 0 24 24" width="18"><path d="M6 9l6 6 6-6"></path></svg></summary><div class="a" data-i18n="{pre}.a{i}">{en[f"{pre}.a{i}"]}</div></details>'
        for i in faq_keys
    )

    body = f'''<main>
<section class="subpage brand">
<div aria-hidden="true" class="bg" style="{hero_background_css(bg)}"></div>
<img alt="{hero_alt}" class="hero-alt-img" data-i18n-alt="{pre}.heroAlt" height="432" loading="lazy" sizes="1px" src="{hero_alt_src}" srcset="{hero_alt_srcset}" width="768"/>
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
{render_trust_strip("en", i18n=True)}

<section class="sub-section sub-intro">
<div class="container">
<div class="heading"><span class="h-eyebrow" data-i18n="{pre}.introEyebrow">{en[f"{pre}.introEyebrow"]}</span><div><h2 data-i18n="{pre}.introTitle">{en[f"{pre}.introTitle"]}</h2></div></div>
<div>
{intro_html}
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

{render_pricing_section(slug, en)}

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

{render_harley_explore(slug, en)}
{render_related_sections(slug, en)}

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
    html = patch_navigation_footer(html, "en")

    out = SITE_ROOT / slug / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    # This renderer owns the complete brand-page dictionary. Writing it as a
    # replacement (rather than merging) lets retired keys disappear instead of
    # surviving forever in generated HTML.
    write_html_if_changed(out, html, preserve_body_shell=True, preserve_downstream_head=True)
    return out


def main():
    for slug in BRAND_ORDER:
        out = render(slug)
        size = out.stat().st_size
        print(f"  wrote {out.relative_to(SITE_ROOT)} ({size:,} bytes)")
    print(f"\nDone. {len(BRAND_ORDER)} brand pages written.")


if __name__ == "__main__":
    main()
