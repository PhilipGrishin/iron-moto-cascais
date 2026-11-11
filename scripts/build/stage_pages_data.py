"""Registry for approved Stage pages; shared discovery and chrome consume it."""
from pathlib import Path
from stage_copy import parse_stage_copy, table_rows, integration_section

BUILD_DIR = Path(__file__).resolve().parent
LANGS = ('en','pt','ru','uk')
_labels = {row[0].split('`')[0]:dict(zip(LANGS,row[1:])) for part in ('A1','A2') for row in table_rows(integration_section(part)) if row[0].startswith('nav.')}
STAGE_PAGES = {
    'stage-1': {
        'path':'stage-1/', 'name':'Stage 1 ECU remap',
        'source':BUILD_DIR/'content/stage1_copy_4lang.md',
        'sha256':'c24a158577037c7d3604772950aac573d47dff9307f88a256dd47b56a869fda6',
        'price_ids':('stage1','stage1_chinese_brands'),
        'nav_key':'nav.stage1', 'nav_labels':_labels['nav.stage1'],
        'footer_key':'nav.stage1Footer', 'footer_labels':_labels['nav.stage1Footer'],
        'hero':{'base':'/photos/stage/stage-1-hero','widths':[768,1280,1504], 'width':1504,'height':1200,
                'source_sha256':'ea8fd9054c624d28627c03993be9d900db1c4d1590d0ca915f1a6ff788d0574f'},
        'logo':'/photos/stage/dcf-performance-logo.svg',
        'brand':{'name':'DCF-Performance','url':'https://dcf-performance.com/'},
    },
}
for config in STAGE_PAGES.values():
    config['content']=parse_stage_copy(config['source'],config['sha256'],config['path'],config['price_ids'])

STAGE_I18N = {lang:{'nav.stage':_labels['nav.stage'][lang]} for lang in LANGS}
for config in STAGE_PAGES.values():
    for lang in LANGS:
        for kind in ('nav','footer'):
            if config.get(kind+'_key'):
                STAGE_I18N[lang][config[kind+'_key']]=config[kind+'_labels'][lang]
