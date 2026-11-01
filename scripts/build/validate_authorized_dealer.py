#!/usr/bin/env python3
"""Validate approved copy-driven dealer pages and their family integrations."""
from __future__ import annotations
import json
import re
from pathlib import Path
from urllib.parse import parse_qs,urlsplit
from bs4 import BeautifulSoup
from PIL import Image
from authorized_dealer_data import COPY_DEALER_PAGES, AUTHORIZED_DEALER_BRANDS, AUTHORIZED_DEALER_HEAD, AUTHORIZED_DEALER_I18N
from dealer_copy import plain
from site_chrome import AUTHORIZED_DEALER_NAV_LINKS,localized_href

ROOT=Path(__file__).resolve().parents[2]
DOMAIN='https://ironcustommotors.com'


def norm(value):
    value=re.sub(r'\s+',' ',value).strip()
    return re.sub(r'([([])\s+',r'\1',re.sub(r'\s+([.,;:)\]])',r'\1',value))


def text(node):
    return norm(node.get_text(' ',strip=True)) if node else ''


def check(condition, message):
    if not condition: raise AssertionError(message)


def main():
    pages=0
    for slug,config in COPY_DEALER_PAGES.items():
        media=config['hero']
        for width in media['widths']:
            for ext in ('avif','webp','jpg'):
                path=ROOT/(media['base'].lstrip('/')+f'-{width}.{ext}')
                with Image.open(path) as image:
                    check(image.width==width and image.height==round(media['height']*width/media['width']),f'{path}: dimensions')
                    check(not image.getexif(),f'{path}: unexpected EXIF')
        for lang,copy in config['content'].items():
            fields=copy['fields'];path=ROOT/fields['Slug'].strip('/')/'index.html'
            soup=BeautifulSoup(path.read_text(),'html.parser');main=soup.select_one(f'main[data-dealer="{slug}"]')
            label=f'{slug}/{lang}'
            check(main is not None,label+': missing main')
            for selector,value in [('title',fields['SEO Title']),('h1',fields['H1']),('.cway-hero .lead',fields['Hero offer']),('.cway-hero .eyebrow',fields['Eyebrow'])]:
                check(text(soup.select_one(selector))==norm(value),label+': '+selector)
            check(len(soup.select('h1'))==1,label+': H1 count')
            check(soup.select_one('meta[name="description"]')['content']==fields['Meta'],label+': meta')
            check(soup.select_one('link[rel="canonical"]')['href']==DOMAIN+fields['Slug'],label+': canonical')
            expected={('pt-PT' if l=='pt' else l):DOMAIN+c['fields']['Slug'] for l,c in config['content'].items()}
            expected['x-default']=DOMAIN+'/'+config['path']
            check({a['hreflang']:a['href'] for a in soup.select('link[hreflang]')}==expected,label+': hreflang')
            check(soup.select_one('meta[property="og:image"]')['content']==DOMAIN+media['base']+'-1280.jpg',label+': og:image')
            check([a['data-dealer-section'] for a in main.select('[data-dealer-section]')]==[s['key'] for s in copy['sections']],label+': sections')
            for section in copy['sections']:
                node=main.select_one('[data-dealer-section="'+section['key']+'"]');kind=section['kind'];items=section['items']
                check(text(node.h2)==norm(section['title']),label+'/'+section['key']+': title')
                check(text(node.select_one('.eyebrow'))==norm(section['eyebrow']),label+': eyebrow')
                if section['lead']:check(text(node.select_one('.lead'))==norm(plain(section['lead'])),label+': lead')
                if kind=='prose':
                    actual=[text(p) for p in node.select('.dealer-prose > p')];expected=[norm(plain(p)) for p in items]
                elif kind=='links':
                    actual=[(text(a),a['href']) for a in node.select('.cway-cta-links a')];expected=[(norm(i['title']),i['href']) for i in items]
                else:
                    selector='details' if kind=='faq' else 'article'
                    actual=[text(a) for a in node.select(selector)];expected=[norm(plain(i['title']+' '+i['text'])) for i in items]
                check(actual==expected,label+'/'+section['key']+': complete source-copy mismatch')
            buttons=main.select('.subpage-cta a');check([text(a) for a in buttons]==fields['Buttons'].split(' · '),label+': hero buttons')
            check(buttons[1]['href']=='#process',label+': process anchor')
            for anchor in main.select('a[data-wa]'):
                check(parse_qs(urlsplit(anchor['href']).query).get('text')==[fields['WhatsApp prefill']],label+': WhatsApp prefill')
            external=main.select('a[href="https://dcf-performance.com/dealers/iron-custom-motors"]')
            check(len(external)==1 and external[0].get('rel')==['noopener'] and external[0].get('target')=='_blank',label+': outbound partner link')
            check(text(external[0])==fields['DCF link anchor'],label+': outbound anchor')
            for anchor in main.select('a[href]'):
                href=anchor['href'];parts=urlsplit(href)
                if href.startswith('#'):check(soup.find(id=parts.fragment) is not None,label+': fragment')
                if not href.startswith('/'):continue
                prefix='/' if lang=='en' else f'/{lang}/'
                check(href.startswith(prefix),label+': link locality')
                check((ROOT/parts.path.strip('/')/'index.html').exists(),label+': broken '+href)
            graph=json.loads(soup.select_one('script[type="application/ld+json"]').string)['@graph']
            faq=next(n for n in graph if n['@type']=='FAQPage')
            visible=[(text(d.summary),text(d.p)) for d in main.select('#faq details')]
            check(visible==[(norm(i['name']),norm(i['acceptedAnswer']['text'])) for i in faq['mainEntity']],label+': FAQ schema')
            service=next(n for n in graph if n['@type']=='Service')
            check(service['serviceType']==config['service_type'][lang] and service['provider']['@id']==DOMAIN+'/#business',label+': Service')
            check(service['brand']=={'@type':'Brand',**config['brand']},label+': brand schema')
            check(len(next(n for n in graph if n['@type']=='BreadcrumbList')['itemListElement'])==3,label+': breadcrumbs')
            check(len(main.select('[fetchpriority="high"]'))==1,label+': priority image')
            hero=main.select_one('.cway-hero-media');preload=soup.select_one('link[rel="preload"][as="image"]')
            check(preload['imagesrcset']==hero.select_one('source[type="image/avif"]')['srcset'] and preload['imagesizes']=='100vw',label+': hero selection')
            check(hero.img['alt']==fields['Hero alt'],label+': hero ALT')
            check(not re.search(r'KESS|Alientech|Autotuner|MagicMotorsport',str(main),re.I),label+': tool brand')
            check(set(re.findall(r'\d+(?:–\d+)?\s*€',str(main))) <= {'50–350 €'},label+': price subset')
            hubpath=ROOT/('' if lang=='en' else lang)/'authorized-dealer/index.html'
            hub=BeautifulSoup(hubpath.read_text(),'html.parser');cards=hub.select('a.dealer-brand-card')
            check([a['href'] for a in cards]==[localized_href(b['url'],lang) for b in AUTHORIZED_DEALER_BRANDS],label+': hub cards')
            check(text(cards[-1].select_one('.dealer-brand-desc'))==AUTHORIZED_DEALER_BRANDS[-1]['description'][lang],label+': hub description')
            check(text(hub.select_one('[data-i18n="ad.intro"]'))==norm(AUTHORIZED_DEALER_I18N[lang]['ad.intro']),label+': hub intro')
            check(hub.select_one('meta[name="description"]')['content']==AUTHORIZED_DEALER_HEAD[lang]['description'],label+': hub metadata')
            pages+=1
    for path in ROOT.rglob('*.html'):
        if '.git' in path.parts or '.venv' in path.parts:continue
        raw=path.read_text()
        if 'nav.dealerCway' not in raw:continue
        soup=BeautifulSoup(raw,'html.parser');lang=soup.html.get('lang','en')
        expected=[localized_href(href,lang) for _,href,_ in AUTHORIZED_DEALER_NAV_LINKS]
        for a in soup.select('a[data-i18n="nav.dealerCway"]'):
            check([n['href'] for n in a.parent.select('a[href]')]==expected,str(path)+': dealer menu order')
    print(f'Authorized Dealer validation passed: {pages} approved partner variants, source copy, media, schema, hub and menus.')


if __name__=='__main__': main()
