#!/usr/bin/env python3
"""Protect Stage source contracts, prices, discovery, shared navigation and assets."""
from __future__ import annotations
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import parse_qs, urlsplit
from bs4 import BeautifulSoup
from PIL import Image
from pypdf import PdfReader
from stage_pages_data import STAGE_PAGES, LANGS
from build_stage_pages import unit_text, presentation_parts
from dealer_copy import plain
from pricing_data import STAGE_PRICES, STAGE_SECTION, STAGE_CATALOGUES, LABELS
from site_chrome import PRIMARY_NAV_LINKS, DROPDOWN_NAV_LINKS, localized_href, label_for

ROOT=Path(__file__).resolve().parents[2]
DOMAIN='https://ironcustommotors.com'
PDF_HASHES={'en':'2a0aaafe627e81225a5ff7c8f030e101523431fd8ef7f56d44bcb46949a012b8','pt':'c3ddfd286f7c271a61dea6f645a768f8fbda710ea18a220a16c4f56c98b67e47','ru':'7135bb0eb45be8c49106e468c7066c172ff1a4b02f98a636dbc39dbd3ef8eaef','uk':'f5ee76ba61f1c40e1c60748bf9b391007270232ec74474d3c44b5be1f53ced91'}


def norm(value):return ' '.join(value.split())
def text(node):return norm(node.get_text(' ',strip=True)) if node else ''
def check(value,message):
    if not value:raise AssertionError(message)

def graph(soup):
    result=[]
    for node in soup.select('script[type="application/ld+json"]'):
        data=json.loads(node.string);result.extend(data.get('@graph',[data]))
    return result

def check_links(soup,lang,path):
    for a in soup.select('main a[href]'):
        url=urlsplit(a['href'])
        if url.scheme or url.netloc:continue
        if not url.path:
            check(soup.find(id=url.fragment) is not None,f'{path}: missing anchor {url.fragment}');continue
        target=ROOT/url.path.lstrip('/')
        if url.path.endswith('/'):target=target/'index.html'
        check(target.exists(),f'{path}: missing target {a["href"]}')
        if url.path.startswith('/pricing/files/'):continue
        check(url.path.startswith('/'+lang+'/') if lang!='en' else not re.match(r'^/(pt|ru|uk)/',url.path),f'{path}: link locality')
        if url.fragment:
            check(BeautifulSoup(target.read_text(),'html.parser').find(id=url.fragment) is not None,f'{path}: target fragment {a["href"]}')


def validate_navigation():
    count=0
    keys=['nav.services','nav.brands','nav.harleyHub','nav.stage','nav.projects','nav.about','nav.pricing','nav.contact']
    check([key for key,_,_ in PRIMARY_NAV_LINKS]==keys,'Primary registry order')
    check(all(DROPDOWN_NAV_LINKS.values()),'Empty dropdown registry')
    for path in ROOT.rglob('*.html'):
        if any(part.startswith('.') for part in path.relative_to(ROOT).parts):continue
        raw=path.read_text();soup=BeautifulSoup(raw,'html.parser');nav=soup.select_one('nav.nav')
        check(not any(value in raw for value in ('Stage 1 and 2','Stage 1 e 2','Stage 1 и 2','Stage 1 і 2')),f'{path}: obsolete DCF description')
        check(not any(text(h) in ('Internal links','Ligações internas','Внутренние ссылки','Внутрішні посилання') for h in soup.select('h1,h2,h3,h4,h5,h6')),f'{path}: internal editorial heading')
        # Bare 404/legacy redirects have no managed site header; thank-you pages do.
        if not nav:continue
        count+=1;lang=soup.html.get('lang','en');mobile=soup.select_one('.nav-mobile')
        expected=[label_for(k,lang,fallback) for k,_,fallback in PRIMARY_NAV_LINKS]
        actual=[text(node if node.name=='a' else node.select_one('.nav-dropdown-trigger')) for node in nav.find_all(recursive=False)]
        check(actual==expected,f'{path}: primary labels/order')
        actual_mobile=[text(node if node.name=='a' else node.select_one('summary')) for node in mobile.find_all(recursive=False)]
        check(actual_mobile==expected,f'{path}: mobile labels/order')
        for region in (nav,mobile):
            check(not any('/authorized-dealer/' in a['href'] for a in region.select('a[href]')),f'{path}: dealer header link remains')
        stage=nav.select_one('[data-i18n="nav.stage"]')
        check(stage['href']==localized_href('/'+next(iter(STAGE_PAGES.values()))['path'],lang),f'{path}: Stage parent URL')
        check([a['href'] for a in stage.parent.select('.nav-dropdown-menu a')]==[localized_href('/'+c['path'],lang) for c in STAGE_PAGES.values() if c.get('nav_key')],f'{path}: Stage dropdown')
        footer=soup.select_one('[data-i18n="footer.col1"]').parent
        links=[a['href'] for a in footer.select('a[href]')]
        start=links.index(localized_href('/fuel-system-service/',lang))
        check(links[start:start+3]==[localized_href(p,lang) for p in ('/fuel-system-service/','/stage-1/','/authorized-dealer/')],f'{path}: footer position')
    for key in ('nav.dealerCway','nav.dealerDcf','nav.authorizedDealerHub'):
        check(key not in (ROOT/'assets/main.js').read_text(),'Retired navigation-only label remains: '+key)
    return count


def main():
    sitemap=(ROOT/'sitemap.xml').read_text();llms=(ROOT/'llms.txt').read_text();pages=0
    for slug,config in STAGE_PAGES.items():
        for lang,copy in config['content'].items():
            f=copy['fields'];path=ROOT/f['Slug'].strip('/')/'index.html';soup=BeautifulSoup(path.read_text(),'html.parser');main=soup.select_one('main.stage-page')
            check(main is not None,f'{path}: Stage main')
            check(text(soup.h1)==f['H1'] and text(soup.title)==f['SEO Title'],f'{path}: H1/title')
            check(soup.select_one('meta[name="description"]')['content']==f['Meta'],f'{path}: metadata')
            check(soup.select_one('link[rel="canonical"]')['href']==DOMAIN+f['Slug'],f'{path}: canonical')
            expected_alt={('pt-PT' if l=='pt' else l):DOMAIN+c['fields']['Slug'] for l,c in config['content'].items()};expected_alt['x-default']=DOMAIN+'/'+config['path']
            check({a['hreflang']:a['href'] for a in soup.select('link[hreflang]')}==expected_alt,f'{path}: hreflang')
            check(DOMAIN+f['Slug'] in sitemap,f'{path}: sitemap')
            check(llms.count(']('+DOMAIN+'/'+config['path']+')')==1,f'{path}: machine index')
            check([s['data-stage-section'] for s in main.select('[data-stage-section]')]==[s['key'] for s in copy['sections']],f'{path}: section order')
            for section in copy['sections']:
                node=main.select_one('[data-stage-section="'+section['key']+'"]')
                check(text(node.h2)==section['title'],f'{path}/{section["key"]}: heading')
                if section['eyebrow']:check(text(node.select_one('.eyebrow'))==section['eyebrow'],f'{path}: eyebrow')
                expected=[norm(plain(unit_text(line))) for line in section['lines']]
                if section['key']=='facts':
                    expected=[plain(' '.join(presentation_parts('facts',line))) for line in section['lines']]
                    check(len(node.select('.stage-fact-value'))==5 and not any(text(v).startswith('—') for v in node.select('.stage-fact-value')),f'{path}: fact label/value formatting')
                if section['key']=='max':
                    expected[0]=plain(' '.join(presentation_parts('max',section['lines'][0])))
                    check(text(node.select_one('.stage-figure-value'))=='~10%' and node.select_one('.stage-figure-caption') is not None,f'{path}: figure/caption formatting')
                if section['key']=='included':
                    expected[7]=plain(' '.join(presentation_parts('included',section['lines'][7])))
                    box=node.select_one('.stage-price-box')
                    check([n.get('class',[None])[0] for n in box.find_all(recursive=False)]==['stage-price-label','stage-price','stage-price-detail','stage-price-detail','stage-price-footnote'],f'{path}: price box line structure')
                    check(text(box.select_one('.stage-price-footnote')).startswith('* ') and box.select_one('.stage-price-footnote strong') is not None,f'{path}: price box footnote')
                if section['key']=='links':expected=[re.fullmatch(r'- (.+?) → `([^`]+)`',line)[1] for line in section['lines']]
                check([re.sub(r'\s+','',text(n)) for n in node.select('[data-copy-unit]')]==[re.sub(r'\s+','',value) for value in expected],f'{path}/{section["key"]}: full copy/order/count')
            hero=main.select_one('.stage-hero')
            for key,selector in [('Eyebrow','.eyebrow'),('Hero offer','.stage-hero-offer'),('Hero badge','.stage-lockup p'),('Hero price','.stage-hero-price .stage-price'),('Hero price facts','.stage-hero-price p'),('Hero price note','.stage-price-note')]:
                check(re.sub(r'\s+','',text(hero.select_one(selector)))==re.sub(r'\s+','',plain(f[key])),f'{path}: {key}')
            buttons=hero.select('.stage-buttons a');check([text(a) for a in buttons]==f['Buttons'].split(' · '),f'{path}: buttons')
            check(parse_qs(urlsplit(buttons[0]['href']).query)['text']==[f['WhatsApp prefill']],f'{path}: WhatsApp')
            check(buttons[1]['href']==f['PDF'] and buttons[1]['target']=='_blank' and buttons[2]['href']=='#process',f'{path}: CTA targets')
            check(hashlib.sha256((ROOT/f['PDF'].lstrip('/')).read_bytes()).hexdigest()==PDF_HASHES[lang],f'{path}: catalogue hash')
            check_links(soup,lang,path)
            nodes=graph(soup);service=next(n for n in nodes if n['@type']=='Service');faq=next(n for n in nodes if n['@type']=='FAQPage')
            check(service['name']==f['Schema name'],f'{path}: localized Service name')
            check([o['price'] for o in service['offers']]==[STAGE_PRICES[key] for key in config['price_ids']],f'{path}: offers')
            check(all(o['priceCurrency']=='EUR' and o['priceSpecification']['valueAddedTaxIncluded'] for o in service['offers']),f'{path}: VAT')
            visible=[(text(d.summary),text(d.p)) for d in main.select('#faq details')]
            check(visible==[(norm(q['name']),norm(q['acceptedAnswer']['text'])) for q in faq['mainEntity']],f'{path}: FAQ parity')
            check(set(re.findall(r'(\d+)\s*(?:€|EUR)',text(main)))==set(STAGE_PRICES[key] for key in config['price_ids']),f'{path}: prices')
            check(service['provider']['@id']==DOMAIN+'/#business' and sum(n.get('@id')==DOMAIN+'/#business' for n in nodes)==1,f'{path}: provider resolution')
            preload=soup.select('link[as="image"][rel="preload"]');picture=hero.picture
            check(len(preload)==1 and preload[0]['imagesrcset']==picture.source['srcset'] and preload[0]['imagesizes']==picture.source['sizes'],f'{path}: preload')
            check(picture.img['alt']==f['Hero alt'] and int(picture.img['width'])==config['hero']['width'],f'{path}: hero')
            check(all(img.get('width') and img.get('height') for img in main.select('img')),f'{path}: image dimensions')
            check(not re.search(r'Stage [234]\b',str(main)),f'{path}: unlaunched stage')
            pages+=1
        manifest=json.loads((ROOT/config['hero']['base'].lstrip('/')).with_name(slug+'-media.json').read_text())
        check(manifest['source_sha256']==config['hero']['source_sha256'],'Hero provenance')
        for item in manifest['files']:
            path=ROOT/item['path'];check(hashlib.sha256(path.read_bytes()).hexdigest()==item['sha256'],'Media hash '+str(path))
            with Image.open(path) as image:check(list(image.size)==item['dimensions'] and image.width<=config['hero']['width'] and not image.getexif(),'Media dimensions/EXIF')
    check(hashlib.sha256((ROOT/'photos/stage/dcf-performance-logo.svg').read_bytes()).hexdigest()=='c0e98ee95454394fd05ab782aba04717bc2d66a2b1ef8a73132d986801069b34','Official logo hash')
    for lang in LANGS:
        path=ROOT/('' if lang=='en' else lang)/'pricing/index.html';soup=BeautifulSoup(path.read_text(),'html.parser');section=soup.select_one('#stage-1')
        check(section is not None,f'{lang}: pricing anchor')
        check([text(c.h3) for c in section.select('.price-card')]==[c['name'][lang] for c in STAGE_SECTION['cards']],f'{lang}: pricing rows')
        check([text(c.select_one('.amount')) for c in section.select('.price-card')]==[c['price'][lang] if isinstance(c['price'],dict) else c['price'] for c in STAGE_SECTION['cards']],f'{lang}: pricing values')
        check(text(section.select_one('.section-note'))==STAGE_SECTION['note'][lang],f'{lang}: pricing note')
        check([a['href'] for a in soup.select('.pricing-hero .pdf-dl')]==[LABELS[lang]['pdf_filename'],STAGE_CATALOGUES[lang]],f'{lang}: PDF buttons')
        catalogue=next(n for n in graph(soup) if n['@type']=='OfferCatalog')['itemListElement']
        offers=[o for o in catalogue if o.get('name') in [c['name'][lang] for c in STAGE_SECTION['cards']]]
        check([o['price'] for o in offers]==list(STAGE_PRICES.values()),f'{lang}: pricing offers')
        pdf=PdfReader(ROOT/LABELS[lang]['pdf_filename'].lstrip('/'))
        pdf_text=re.sub(r'\s+','', '\n'.join(page.extract_text() for page in pdf.pages))
        for row in STAGE_SECTION['cards']:
            for value in (row['name'][lang], row['desc'][lang], row['price'][lang] if isinstance(row['price'],dict) else row['price']):
                check(re.sub(r'\s+','',value) in pdf_text,f'{lang}: generated service PDF row')
        check(re.sub(r'\s+','',STAGE_SECTION['note'][lang]) in pdf_text,f'{lang}: generated service PDF note')
        for path_part in ('authorized-dealer/','authorized-dealer/c-way/','authorized-dealer/dcf-performance/'):
            url=DOMAIN+('/' if lang=='en' else f'/{lang}/')+path_part
            check(url in sitemap and url in llms,f'{lang}: dealer discovery {url}')

    chrome=validate_navigation()
    print(f'Stage validation passed: {pages} pages, exact copy/schema/prices/assets/links; {chrome} shared headers and footers.')

if __name__=='__main__':main()
