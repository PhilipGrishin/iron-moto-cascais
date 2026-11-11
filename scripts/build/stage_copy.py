"""Checksum-pinned Stage copy and supplemental integration-table contracts."""
from __future__ import annotations
import hashlib
import re
from pathlib import Path
from dealer_copy import LANG_HEADERS

CONTENT = Path(__file__).resolve().parent / 'content'
INTEGRATION_SHA256 = '96ca56e284774ac80837f72ab7fb854f951760844351c8e25cf31312df07f5a8'
FIELDS = ('SEO Title', 'Meta', 'Slug', 'Breadcrumb', 'Eyebrow', 'H1', 'Hero offer', 'Hero badge', 'Hero price', 'Hero price facts', 'Hero price note', 'Hero alt', 'Buttons', 'WhatsApp prefill', 'PDF', 'Schema name')
COUNTS = {'facts':5, 'what':5, 'max':2, 'changes':10, 'process':8, 'included':13, 'bikes':1, 'options':17, 'terms':7, 'dcf':1, 'faq':8, 'cta':1, 'links':5}


def approved_text(path: Path, expected: str) -> str:
    data = path.read_bytes()
    actual = hashlib.sha256(data).hexdigest()
    if actual != expected:
        raise ValueError(f'{path.name}: SHA-256 {actual} != approved {expected}')
    return data.decode('utf-8')


def integration_section(key: str) -> str:
    source = approved_text(CONTENT / 'stage1_integrations_4lang.md', INTEGRATION_SHA256)
    pattern = r'^## ' + re.escape(key) + r'\.' if key[-1].isdigit() else r'^# Part ' + re.escape(key) + r' —'
    match = re.search(pattern + r'.*$', source, re.M)
    if not match:
        raise ValueError(f'Missing integration section {key}')
    return re.split(r'^#{1,2} ', source[match.end():], maxsplit=1, flags=re.M)[0]


def table_rows(section: str) -> list[list[str]]:
    return [[cell.strip().strip('`') for cell in line.strip('|').split('|')] for line in section.splitlines() if line.startswith('|') and not line.startswith('|---')]


def language_lines(key: str) -> dict[str, str]:
    return {row[0].lower():row[-1].strip('`') for row in table_rows(integration_section(key)) if row[0] in ('EN','PT','RU','UK')}


def parse_stage_copy(path: Path, expected: str, page_path: str, price_ids: tuple[str, ...]) -> dict:
    from pricing_data import resolve_stage_prices
    source = resolve_stage_prices(approved_text(path, expected), price_ids=price_ids)
    matches = list(re.finditer(r'^## (.+)$', source, re.M))
    result = {}
    for i, match in enumerate(matches):
        lang = LANG_HEADERS[match[1]]
        if lang in result: raise ValueError('Duplicate language block')
        block = source[match.end():matches[i+1].start() if i+1<len(matches) else len(source)]
        fields = {}
        for key in FIELDS:
            m = re.search(r'^\*\*'+re.escape(key)+r':\*\* (.*)$', block, re.M)
            if not m: raise ValueError(f'{lang}: missing {key}')
            fields[key] = m[1].strip().strip('`')
        if fields['Slug'] != ('/' if lang=='en' else f'/{lang}/')+page_path: raise ValueError('Stage slug mismatch')
        if len(fields['Breadcrumb'].split(' → '))!=2 or len(fields['Buttons'].split(' · '))!=3: raise ValueError('Stage header contract')
        sections=[]
        headings=list(re.finditer(r'^### \[([a-z]+)\] (.+)$',block,re.M))
        if [m[1] for m in headings]!=list(COUNTS): raise ValueError('Stage section order')
        for j,m in enumerate(headings):
            key,heading=m[1],m[2]; eyebrow=''
            if heading.startswith('Eyebrow: '): eyebrow,title=heading[9:].split(' · Title: ',1)
            else: title=heading.removeprefix('Title: ')
            lines=[line.strip() for line in block[m.end():headings[j+1].start() if j+1<len(headings) else len(block)].splitlines() if line.strip() and line.strip()!='---']
            if len(lines)!=COUNTS[key]: raise ValueError(f'{lang}/{key}: {len(lines)} units, expected {COUNTS[key]}')
            sections.append({'key':key,'eyebrow':eyebrow,'title':title,'lines':lines})
        bykey={s['key']:s['lines'] for s in sections}
        for key,count in [('facts',5),('faq',8),('links',5)]:
            if sum(line.startswith('- ') for line in bykey[key])!=count: raise ValueError(f'{key} list contract')
        for key,positions in [('changes',[0,5]),('options',[1,6,14])]:
            if not all(re.fullmatch(r'\*\*.+\*\*',bykey[key][p]) for p in positions): raise ValueError(f'{key} group contract')
        if sum(line.startswith('> ') for s in sections for line in s['lines'])!=5: raise ValueError('Stage notes contract')
        if not all(bykey['process'][i].startswith(f'**{i+1}. ') for i in range(6)): raise ValueError('Stage step order')
        if not all(bykey['terms'][i].startswith(f'{i+1}. ') for i in range(7)): raise ValueError('Stage term order')
        result[lang]={'fields':fields,'sections':sections}
    if set(result)!=set(LANG_HEADERS.values()): raise ValueError('Expected four Stage languages')
    return result
