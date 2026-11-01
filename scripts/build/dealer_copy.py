"""Parse checksum-approved, labelled multilingual partner-page Markdown."""
from __future__ import annotations

import hashlib
import re
from html import escape
from pathlib import Path
from urllib.parse import quote

LANG_HEADERS = {"ENGLISH": "en", "PORTUGUÊS (pt-PT)": "pt", "РУССКИЙ": "ru", "УКРАЇНСЬКА": "uk"}
SECTION_KINDS = {
    "intro": ("prose", 3), "changes": ("cards", 7), "offer": ("cards", 8),
    "process": ("steps", 6), "why": ("cards", 4), "honest": ("prose", 4),
    "bikes": ("prose", 1), "numbers": ("stats", 4), "faq": ("faq", 6),
    "cta": ("prose", 1), "links": ("links", 5),
}
FIELDS = ("SEO Title", "Meta", "Slug", "Breadcrumb", "Eyebrow", "H1", "Hero offer", "Hero alt", "Buttons", "WhatsApp prefill", "DCF link anchor")


def plain(value: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", value).replace("**", "")).strip()


def inline(value: str, prefill: str) -> str:
    """Escape approved text while preserving only links and strong emphasis."""
    parts = []
    pos = 0
    for m in re.finditer(r"\[([^]]+)\]\(([^)]+)\)|\*\*(.+?)\*\*", value):
        parts.append(escape(value[pos:m.start()]))
        if m.group(3) is not None:
            parts.append(f'<strong>{escape(m.group(3))}</strong>')
        else:
            label, href = m.group(1), m.group(2)
            if href.startswith('https://wa.me/'):
                href += '?text=' + quote(prefill, safe='')
                attrs = ' data-wa="" rel="noopener" target="_blank"'
            elif href.startswith('https://'):
                attrs = ' rel="noopener" target="_blank"'
            elif href.startswith('/'):
                attrs = ''
            else:
                raise ValueError(f'Unsupported partner-copy link: {href}')
            parts.append(f'<a href="{escape(href, quote=True)}"{attrs}>{escape(label)}</a>')
        pos = m.end()
    parts.append(escape(value[pos:]))
    return ''.join(parts)


def parse_dealer_copy(path: Path, expected_sha256: str, page_path: str) -> dict:
    data = path.read_bytes()
    actual = hashlib.sha256(data).hexdigest()
    if actual != expected_sha256:
        raise ValueError(f'{path.name}: SHA-256 {actual} != approved {expected_sha256}')
    text = data.decode('utf-8')
    headings = list(re.finditer(r'^## (.+)$', text, re.M))
    result = {}
    for i, match in enumerate(headings):
        lang = LANG_HEADERS[match.group(1)]
        block = text[match.end():headings[i+1].start() if i+1<len(headings) else len(text)]
        fields = {}
        for key in FIELDS:
            field = re.search(r'^\*\*'+re.escape(key)+r':\*\* (.*)$', block, re.M)
            if not field: raise ValueError(f'{lang}: missing field {key}')
            fields[key] = field.group(1).strip().strip('`')
        expected_path = ('/' if lang=='en' else f'/{lang}/') + page_path.strip('/') + '/'
        if fields['Slug'] != expected_path: raise ValueError(f'{lang}: slug mismatch')
        if len(fields['Breadcrumb'].split(' → ')) != 3: raise ValueError('Expected three breadcrumbs')
        if len(fields['Buttons'].split(' · ')) != 2: raise ValueError('Expected two hero buttons')
        sections = []
        matches = list(re.finditer(r'^### \[([a-z]+)\] (.+)$', block, re.M))
        if [m.group(1) for m in matches] != list(SECTION_KINDS): raise ValueError(f'{lang}: section order mismatch')
        for j,m in enumerate(matches):
            key, heading = m.group(1), m.group(2)
            kind,count = SECTION_KINDS[key]
            eyebrow = ''
            if heading.startswith('Eyebrow: '):
                eyebrow,title = heading.removeprefix('Eyebrow: ').split(' · Title: ',1)
            else: title = heading.removeprefix('Title: ')
            body=block[m.end():matches[j+1].start() if j+1<len(matches) else len(block)]
            lines=[line.strip() for line in body.splitlines() if line.strip() and line.strip()!='---']
            lead=''
            if key=='changes': lead=lines.pop(0)
            if len(lines)!=count: raise ValueError(f'{lang}/{key}: expected {count} units, got {len(lines)}')
            items=[]
            for line in lines:
                if kind in {'cards','steps','stats','faq'}:
                    item=re.fullmatch(r'(?:- )?\*\*(.+?)\*\*(.*)',line)
                    if not item: raise ValueError(f'{lang}/{key}: malformed item')
                    tail=item.group(2).strip()
                    if kind=='stats': tail=tail.removeprefix('— ')
                    items.append({'title':item.group(1),'text':tail})
                elif kind=='links':
                    item=re.fullmatch(r'- (.+?) → `([^`]+)`',line)
                    if not item: raise ValueError(f'{lang}: malformed internal link')
                    items.append({'title':item.group(1),'href':item.group(2)})
                else: items.append(line)
            sections.append({'key':key,'kind':kind,'eyebrow':eyebrow,'title':title,'lead':lead,'items':items,'source_lines':lines})
        result[lang]={'fields':fields,'sections':sections}
    if set(result)!=set(LANG_HEADERS.values()): raise ValueError('Expected four language blocks')
    return result
