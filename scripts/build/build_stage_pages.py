#!/usr/bin/env python3
"""Render every approved Stage page directly in its four languages."""
from __future__ import annotations
import json
import re
from html import escape
from pathlib import Path
from urllib.parse import quote
from build_output import write_html_if_changed
from build_new_pages import CACHE_BUST, SHARED_STYLES, header_html, footer_html, end_html
from build_authorized_dealer import apply_static_translations, dealer_business_reference, partner_srcset
from dealer_copy import inline, plain
from pricing_data import STAGE_PRICES, STAGE_SECTION
from stage_pages_data import STAGE_PAGES, LANGS
from site_chrome import patch_navigation_footer
from trust_strip import render_trust_strip, TRUST_STRIP_CSS

ROOT=Path(__file__).resolve().parents[2]
DOMAIN='https://ironcustommotors.com'


def item_parts(line):
    match=re.fullmatch(r'(?:- )?\*\*(.+?)\*\*(.*)',line)
    if not match: raise ValueError(f'Expected bold-led Stage unit: {line}')
    return match[1],match[2].strip()


def unit_text(line):
    """Remove source-only list/field markers, retaining all approved visible copy."""
    line=re.sub(r'^(?:- |> |\d+\. )','',line)
    return re.sub(r'^\*\*(?:Figure|Valor|Цифра|Price box|Caixa de preço|Блок цены|Блок ціни):\*\* ','',line)


def stage_schema(config,lang):
    copy=config['content'][lang];f=copy['fields'];url=DOMAIN+f['Slug'];media=config['hero']
    faq=next(s for s in copy['sections'] if s['key']=='faq')
    rows={r['id']:r for r in STAGE_SECTION['cards']}
    return {'@context':'https://schema.org','@graph':[
        dealer_business_reference(with_logo=True),
        {'@type':'ImageObject','@id':url+'#hero','url':DOMAIN+media['base']+f'-{media["width"]}.jpg','width':media['width'],'height':media['height'],'caption':f['Hero alt']},
        {'@type':'Service','@id':url+'#service','url':url,'name':config['service_name'],'description':f['Meta'],
         'provider':{'@id':DOMAIN+'/#business'},'brand':{'@type':'Brand',**config['brand']},'image':{'@id':url+'#hero'},'areaServed':{'@type':'Country','name':'Portugal'},
         'offers':[{'@type':'Offer','name':rows[key]['name'][lang],'description':rows[key]['desc'][lang], 'price':STAGE_PRICES[key],'priceCurrency':'EUR',
                    'priceSpecification':{'@type':'PriceSpecification','price':STAGE_PRICES[key],'priceCurrency':'EUR','valueAddedTaxIncluded':True},'url':url}
                   for key in config['price_ids']]},
        {'@type':'FAQPage','@id':url+'#faq','mainEntity':[{'@type':'Question','name':plain(item_parts(line)[0]),'acceptedAnswer':{'@type':'Answer','text':plain(item_parts(line)[1])}} for line in faq['lines']]},
        {'@type':'BreadcrumbList','@id':url+'#breadcrumbs','itemListElement':[{'@type':'ListItem','position':1,'name':f['Breadcrumb'].split(' → ')[0],'item':DOMAIN+('/' if lang=='en' else f'/{lang}/')},{'@type':'ListItem','position':2,'name':f['Breadcrumb'].split(' → ')[1],'item':url}]},
    ]}


def head(config,lang):
    f=config['content'][lang]['fields'];m=config['hero'];url=DOMAIN+f['Slug'];og=DOMAIN+m['base']+f'-{m["width"]}.jpg'
    alternate=''.join(f'<link rel="alternate" hreflang="{ "pt-PT" if l=="pt" else l}" href="{DOMAIN}{config["content"][l]["fields"]["Slug"]}"/>' for l in LANGS)
    alternate+=f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}/{config["path"]}"/>'
    return f'''<!DOCTYPE html><html lang="{lang}" data-lang="{lang}"><head>
<meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"/>
<meta name="theme-color" content="#0a0a0a"/><meta name="robots" content="max-image-preview:large"/>
<title>{escape(f['SEO Title'])}</title><meta name="description" content="{escape(f['Meta'])}"/><link rel="canonical" href="{url}"/>{alternate}
<meta property="og:type" content="website"/><meta property="og:site_name" content="Iron Custom Motors"/>
<meta property="og:title" content="{escape(f['SEO Title'])}"/><meta property="og:description" content="{escape(f['Meta'])}"/><meta property="og:url" content="{url}"/><meta property="og:image" content="{og}"/>
<meta property="og:locale" content="{ {'en':'en_US','pt':'pt_PT','ru':'ru_RU','uk':'uk_UA'}[lang]}"/>
<meta name="twitter:card" content="summary_large_image"/><meta name="twitter:title" content="{escape(f['SEO Title'])}"/><meta name="twitter:description" content="{escape(f['Meta'])}"/><meta name="twitter:image" content="{og}"/>
<link rel="icon" href="/photos/favicon.ico" sizes="any"/><link rel="apple-touch-icon" href="/photos/apple-touch-icon.png"/><link rel="manifest" href="/photos/site.webmanifest"/>
<link rel="preload" as="image" type="image/avif" href="{m['base']}-{m['width']}.avif" imagesrcset="{partner_srcset(m,'avif')}" imagesizes="100vw"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin=""/>
<link href="https://fonts.googleapis.com/css2?family=Saira:wght@300;400;500;600;700;800;900&amp;family=Saira+Condensed:wght@400;600;700;800;900&amp;family=Roboto+Condensed:wght@400;500;600;700;800;900&amp;family=Inter:wght@300;400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="/assets/main.css?v={CACHE_BUST}"/><link rel="stylesheet" href="/assets/stage.css?v=20261111a"/>
<style>{SHARED_STYLES}{TRUST_STRIP_CSS}</style>
<script type="application/ld+json">{json.dumps(stage_schema(config,lang),ensure_ascii=False)}</script></head>'''


def render_section(section, config, lang):
    key=section['key'];lines=section['lines'];prefill=config['content'][lang]['fields']['WhatsApp prefill']
    def unit(line,tag='p',cls=''):
        return f'<{tag} data-copy-unit="" class="{cls}">{inline(unit_text(line),prefill)}</{tag}>'
    def cards(items,cls=''):
        return f'<div class="stage-grid {cls}">'+''.join(unit(line,'article','stage-card') for line in items)+'</div>'
    def listing(items): return '<ul class="stage-list">'+''.join(unit(line,'li') for line in items)+'</ul>'
    def notes(items): return '<div class="stage-notes">'+''.join(unit(line,'aside','stage-note') for line in items)+'</div>'
    if key=='facts': body=cards(lines,'stage-facts')
    elif key=='what': body=''.join(unit(line) for line in lines[:2])+cards(lines[2:],'stage-three')
    elif key=='max': body=unit(lines[0],'p','stage-figure')+unit(lines[1])
    elif key=='changes': body='<div class="stage-grid">'+''.join('<div>'+unit(lines[i],'h3')+listing(lines[i+1:i+5])+'</div>' for i in (0,5))+'</div>'
    elif key=='process': body=cards(lines[:6],'stage-steps')+notes(lines[6:])
    elif key=='included':
        box=unit_text(lines[7]);box=re.sub(r'(\d+\s*€\*)',r'<span class="stage-price">\1</span>',inline(box,prefill))
        body='<div class="stage-included">'+listing(lines[:7])+'<div><div class="stage-price-box" data-copy-unit="">'+box+'</div><div class="stage-card">'+unit(lines[8],'h3')+listing(lines[9:11])+'</div></div></div>'+notes(lines[11:])
    elif key=='options': body=unit(lines[0])+''.join('<div class="stage-card stage-option-group">'+unit(lines[i],'h3')+listing(lines[i+1:i+1+count])+'</div>' for i,count in ((1,4),(6,7),(14,1)))+notes(lines[-1:])
    elif key=='terms': body='<ol class="stage-terms">'+''.join(unit(line,'li') for line in lines)+'</ol>'
    elif key=='faq': body='<div class="stage-faq">'+''.join('<details data-copy-unit=""><summary>'+inline(item_parts(line)[0],prefill)+'</summary><p>'+inline(item_parts(line)[1],prefill)+'</p></details>' for line in lines)+'</div>'
    elif key=='links':
        body='<div class="stage-related">'
        for line in lines:
            m=re.fullmatch(r'- (.+?) → `([^`]+)`',line)
            body+=f'<a data-copy-unit="" href="{m[2]}">{escape(m[1])}</a>'
        body+='</div>'
    else: body=''.join(unit(line) for line in lines)
    if key=='dcf':body=f'<img class="stage-dcf-logo" src="{config["logo"]}" width="190" height="78" alt="DCF-Performance" loading="lazy"/>'+body
    heading=(f'<p class="eyebrow">{escape(section["eyebrow"])}</p>' if section['eyebrow'] else '')+f'<h2>{escape(section["title"])}</h2>'
    return f'<section class="stage-section stage-section--{key}" id="{key}" data-stage-section="{key}"><div class="container">{heading}{body}</div></section>'


def heading_html(value):
    return re.sub(r'(\d+\s+€)', r'<span class="stage-amount">\1</span>', escape(value))


def render_page(slug,config,lang):
    content=config['content'][lang];f=content['fields'];m=config['hero'];buttons=f['Buttons'].split(' · ');crumbs=f['Breadcrumb'].split(' → ')
    logo=f'<img class="stage-dcf-logo" src="{config["logo"]}" width="190" height="78" alt="DCF-Performance"/>'
    raw=f'''{head(config,lang)}<body>{header_html()}<main class="stage-page" data-stage="{slug}">
<section class="stage-hero"><picture class="stage-hero-media"><source type="image/avif" srcset="{partner_srcset(m,'avif')}" sizes="100vw"/><source type="image/webp" srcset="{partner_srcset(m,'webp')}" sizes="100vw"/><img src="{m['base']}-{m['width']}.jpg" width="{m['width']}" height="{m['height']}" alt="{escape(f['Hero alt'])}" loading="eager" fetchpriority="high" decoding="async" sizes="100vw"/></picture>
<div class="container"><nav class="crumb" aria-label="Breadcrumb"><a href="{'/' if lang=='en' else '/'+lang+'/'}">{escape(crumbs[0])}</a><span class="sep">→</span><span>{escape(crumbs[1])}</span></nav>
<p class="eyebrow">{escape(f['Eyebrow'])}</p><h1>{heading_html(f['H1'])}</h1><p class="stage-hero-offer">{escape(f['Hero offer'])}</p>
<div class="stage-lockup">{logo}<p>{escape(f['Hero badge'])}</p></div>
<div class="stage-hero-price"><strong class="stage-price">{escape(f['Hero price'])}</strong><p>{inline(f['Hero price facts'],'')}</p></div><p class="stage-price-note">{inline(f['Hero price note'],'')}</p>
<div class="stage-buttons"><a class="btn btn-primary" data-wa="" href="https://wa.me/351917961230?text={quote(f['WhatsApp prefill'],safe='')}" target="_blank" rel="noopener">{escape(buttons[0])}</a><a class="btn btn-ghost" data-cta="pdf" href="{f['PDF']}" target="_blank" rel="noopener">{escape(buttons[1])}</a><a class="btn btn-ghost" href="#process">{escape(buttons[2])}</a></div>
</div></section>{render_trust_strip(lang)}
{''.join(render_section(section,config,lang) for section in content['sections'])}</main>{footer_html()}{end_html()}'''
    return apply_static_translations(patch_navigation_footer(raw,lang),lang,{})


def main():
    for slug,config in STAGE_PAGES.items():
        for lang in LANGS:
            out=ROOT/('' if lang=='en' else lang)/config['path']/'index.html';out.parent.mkdir(parents=True,exist_ok=True)
            write_html_if_changed(out,render_page(slug,config,lang),preserve_body_shell=True,preserve_downstream_head=True)
            print('Wrote',out.relative_to(ROOT))

if __name__=='__main__':main()
