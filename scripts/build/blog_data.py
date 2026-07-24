"""
Blog section content: hub + future workshop articles.
Each future post should have full multilingual content (en, ru, uk, pt).

Post slug will be keyed in BLOG_POSTS.
"""

import html
import re
from pathlib import Path

# ============================================================
# Hub /blog/ — title + description + heading per language
# ============================================================

BLOG_HUB_META = {
    "en": {
        "title": "Blog — Motorcycle Workshop Guides | Iron Custom Motors",
        "description": "Practical motorcycle blog from Iron Custom Motors in Cascais: workshop notes, maintenance guidance, diagnostics, parts, upgrades and used-bike advice.",
    },
    "ru": {
        "title": "Блог — полезные материалы мотомастерской | Iron Custom Motors",
        "description": "Практический мотоблог Iron Custom Motors в Кашкайше: заметки из мастерской, обслуживание, диагностика, запчасти, апгрейды и советы по покупке мотоциклов.",
    },
    "uk": {
        "title": "Блог — корисні матеріали мотомайстерні | Iron Custom Motors",
        "description": "Практичний мотоблог Iron Custom Motors у Кашкайші: нотатки з майстерні, обслуговування, діагностика, запчастини, апґрейди та поради щодо купівлі мотоциклів.",
    },
    "pt": {
        "title": "Blog — Guias de Oficina de Motas | Iron Custom Motors",
        "description": "Blog prático de motos da Iron Custom Motors em Cascais: notas de oficina, manutenção, diagnóstico, peças, upgrades e conselhos para comprar motos usadas.",
    },
}

_BEAR650_SLUG = "royal-enfield-bear-650-fork-oil-case-study"
_BEAR650_SOURCE = Path(__file__).resolve().parent / "content" / "bear650_fork_blog_4lang.md"
_BEAR650_LANGS = (
    ("en", "ENGLISH"),
    ("pt", "PORTUGUÊS"),
    ("ru", "РУССКИЙ"),
    ("uk", "УКРАЇНСЬКА"),
)
_BEAR650_LABELS = {
    "en": {
        "eyebrow": "Workshop case study · 29 June 2026",
        "publishedLabel": "Published 29 June 2026",
        "breadHome": "Home",
        "breadBlog": "Blog",
        "faqTitle": "FAQ",
    },
    "pt": {
        "eyebrow": "Caso de oficina · 29 de junho de 2026",
        "publishedLabel": "Publicado 29 de junho de 2026",
        "breadHome": "Início",
        "breadBlog": "Blog",
        "faqTitle": "FAQ",
    },
    "ru": {
        "eyebrow": "Кейс из мастерской · 29 июня 2026",
        "publishedLabel": "Опубликовано 29 июня 2026",
        "breadHome": "Главная",
        "breadBlog": "Блог",
        "faqTitle": "FAQ",
    },
    "uk": {
        "eyebrow": "Кейс із майстерні · 29 червня 2026",
        "publishedLabel": "Опубліковано 29 червня 2026",
        "breadHome": "Головна",
        "breadBlog": "Блог",
        "faqTitle": "FAQ",
    },
}

_HARLEY_SERVICE_SLUG = "harley-davidson-full-service-done-right"
_HARLEY_SERVICE_SOURCE = Path(__file__).resolve().parent / "content" / "harley_service_blog_4lang.md"
_HARLEY_SERVICE_LANGS = (
    ("en", "ENGLISH"),
    ("pt", "PORTUGUÊS (pt-PT)"),
    ("ru", "РУССКИЙ"),
    ("uk", "УКРАЇНСЬКА"),
)
_HARLEY_SERVICE_LABELS = {
    "en": {
        "eyebrow": "Published 10 July 2026",
        "publishedLabel": "Published 10 July 2026",
        "breadHome": "Home",
        "breadBlog": "Blog",
        "faqTitle": "FAQ",
    },
    "pt": {
        "eyebrow": "Publicado em 10 de julho de 2026",
        "publishedLabel": "Publicado em 10 de julho de 2026",
        "breadHome": "Início",
        "breadBlog": "Blog",
        "faqTitle": "FAQ",
    },
    "ru": {
        "eyebrow": "Опубликовано 10 июля 2026",
        "publishedLabel": "Опубликовано 10 июля 2026",
        "breadHome": "Главная",
        "breadBlog": "Блог",
        "faqTitle": "FAQ",
    },
    "uk": {
        "eyebrow": "Опубліковано 10 липня 2026",
        "publishedLabel": "Опубліковано 10 липня 2026",
        "breadHome": "Головна",
        "breadBlog": "Блог",
        "faqTitle": "FAQ",
    },
}

_BEAR650_BUILD_SLUG = "royal-enfield-bear-650-scrambler-build"
_BEAR650_BUILD_SOURCE = Path(__file__).resolve().parent / "content" / "bear650_scrambler_build_blog_4lang.md"
_BEAR650_BUILD_LANGS = (
    ("en", "ENGLISH"),
    ("pt", "PORTUGUÊS (pt-PT)"),
    ("ru", "РУССКИЙ"),
    ("uk", "УКРАЇНСЬКА"),
)
_BEAR650_BUILD_LABELS = {
    "en": {
        "eyebrow": "Published 19 July 2026",
        "publishedLabel": "Published 19 July 2026",
        "breadHome": "Home",
        "breadBlog": "Blog",
        "faqTitle": "FAQ",
        "videoSchemaName": "Royal Enfield Bear 650 scrambler build — full aftermarket works at Iron Custom Motors",
        "videoSchemaDescription": "A complete Royal Enfield Bear 650 scrambler build covering protection, luggage, ergonomics, exhaust, brakes and suspension.",
    },
    "pt": {
        "eyebrow": "Publicado em 19 de julho de 2026",
        "publishedLabel": "Publicado em 19 de julho de 2026",
        "breadHome": "Início",
        "breadBlog": "Blog",
        "faqTitle": "Perguntas frequentes",
        "videoSchemaName": "Preparação scrambler da Royal Enfield Bear 650 — aftermarket completo na Iron Custom Motors",
        "videoSchemaDescription": "Uma preparação scrambler completa da Royal Enfield Bear 650, com proteção, malas, ergonomia, escape, travões e suspensão.",
    },
    "ru": {
        "eyebrow": "Опубликовано 19 июля 2026",
        "publishedLabel": "Опубликовано 19 июля 2026",
        "breadHome": "Главная",
        "breadBlog": "Блог",
        "faqTitle": "FAQ",
        "videoSchemaName": "Скрамблер-билд Royal Enfield Bear 650 — полный афтермаркет в Iron Custom Motors",
        "videoSchemaDescription": "Полный скрамблер-билд Royal Enfield Bear 650: защита, багаж, эргономика, выхлоп, тормоза и подвеска.",
    },
    "uk": {
        "eyebrow": "Опубліковано 19 липня 2026",
        "publishedLabel": "Опубліковано 19 липня 2026",
        "breadHome": "Головна",
        "breadBlog": "Блог",
        "faqTitle": "FAQ",
        "videoSchemaName": "Скрамблер-білд Royal Enfield Bear 650 — повний афтермаркет у Iron Custom Motors",
        "videoSchemaDescription": "Повний скрамблер-білд Royal Enfield Bear 650: захист, багаж, ергономіка, вихлоп, гальма та підвіска.",
    },
}


def _inline_markdown(value):
    tokens = []

    def stash(rendered):
        tokens.append(rendered)
        return f"@@ICM_TOKEN_{len(tokens) - 1}@@"

    def link_repl(match):
        label, href = match.group(1), match.group(2)
        return stash(f'<a href="{html.escape(href, quote=True)}">{html.escape(label, quote=False)}</a>')

    value = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link_repl, value)
    value = re.sub(
        r"\*\*(.+?)\*\*",
        lambda match: stash(f"<strong>{_inline_markdown(match.group(1))}</strong>"),
        value,
    )
    value = re.sub(
        r"(?<!\*)\*(.+?)\*(?!\*)",
        lambda match: stash(f"<em>{_inline_markdown(match.group(1))}</em>"),
        value,
    )
    value = html.escape(value, quote=False)

    def restore(match):
        return tokens[int(match.group(1))]

    return re.sub(r"@@ICM_TOKEN_(\d+)@@", restore, value)


def _split_localized_sections(source, languages, source_name):
    found = []
    for code, heading in languages:
        match = re.search(rf"^## {re.escape(heading)}\s*$", source, re.MULTILINE)
        if not match:
            raise ValueError(f"Missing {source_name} language heading: {heading}")
        found.append((code, match.start()))
    found.sort(key=lambda item: item[1])
    sections = {}
    for idx, (code, start) in enumerate(found):
        end = found[idx + 1][1] if idx + 1 < len(found) else len(source)
        sections[code] = source[start:end].strip()
    return sections


def _flush_markdown_paragraph(blocks, buffer):
    if buffer:
        text = " ".join(line.strip() for line in buffer).strip()
        blocks.append({"type": "p", "text": _inline_markdown(text)})
        buffer.clear()


def _flush_markdown_list(blocks, items, list_type):
    if items:
        blocks.append({"type": "ol" if list_type == "ol" else "ul", "items": [_inline_markdown(item) for item in items]})
        items.clear()
    return None


def _parse_markdown_blocks(lines):
    blocks = []
    paragraph = []
    list_items = []
    list_type = None
    for line in lines:
        stripped = line.strip()
        if stripped == "---":
            continue
        if not stripped:
            _flush_markdown_paragraph(blocks, paragraph)
            list_type = _flush_markdown_list(blocks, list_items, list_type)
            continue
        image_match = re.match(r"`\[IMAGE (\d+)\]` ALT:\s*(.+)", stripped)
        if image_match:
            _flush_markdown_paragraph(blocks, paragraph)
            list_type = _flush_markdown_list(blocks, list_items, list_type)
            blocks.append({"type": "image", "image": int(image_match.group(1)), "alt": image_match.group(2).strip()})
            continue
        if re.fullmatch(r"\[VIDEO:.*\]", stripped):
            _flush_markdown_paragraph(blocks, paragraph)
            list_type = _flush_markdown_list(blocks, list_items, list_type)
            blocks.append({"type": "video"})
            continue
        bullet_match = re.match(r"-\s+(.+)", stripped)
        ordered_match = re.match(r"\d+\.\s+(.+)", stripped)
        if bullet_match or ordered_match:
            _flush_markdown_paragraph(blocks, paragraph)
            current_type = "ol" if ordered_match else "ul"
            if list_type and list_type != current_type:
                list_type = _flush_markdown_list(blocks, list_items, list_type)
            list_type = current_type
            list_items.append((ordered_match or bullet_match).group(1).strip())
            continue
        list_type = _flush_markdown_list(blocks, list_items, list_type)
        paragraph.append(stripped)
    _flush_markdown_paragraph(blocks, paragraph)
    _flush_markdown_list(blocks, list_items, list_type)
    return blocks


def _parse_bear650_language(raw):
    lines = raw.splitlines()
    meta = {}
    h1 = None
    body_lines = []
    in_body = False
    for line in lines[1:]:
        if line.startswith("**SEO title:**"):
            meta["title"] = line.split("**SEO title:**", 1)[1].strip()
        elif line.startswith("**Meta:**"):
            meta["description"] = line.split("**Meta:**", 1)[1].strip()
        elif line.startswith("**Slug:**"):
            meta["slug"] = line.split("**Slug:**", 1)[1].strip()
        elif line.startswith("# "):
            h1 = line[2:].strip()
            in_body = True
        elif in_body:
            body_lines.append(line)
    if not (meta.get("title") and meta.get("description") and h1):
        raise ValueError("Incomplete Bear 650 blog source metadata")

    body = "\n".join(body_lines).strip()
    before_faq, after_faq = body.split("\n## FAQ\n", 1)
    faq_text, cta_text = after_faq.split("\n## ", 1)
    cta_title, cta_rest = cta_text.split("\n", 1)

    faq_items = []
    for paragraph in [part.strip() for part in faq_text.strip().split("\n\n") if part.strip()]:
        match = re.match(r"\*\*(.*?)\*\*\s*(.*)", paragraph, re.S)
        if not match:
            raise ValueError(f"Cannot parse Bear 650 FAQ item: {paragraph[:80]}")
        faq_items.append({"q": match.group(1).strip(), "a": _inline_markdown(match.group(2).strip())})
    if len(faq_items) != 6:
        raise ValueError(f"Expected 6 Bear 650 FAQ items, got {len(faq_items)}")

    content_sections = []
    chunks = re.split(r"\n(?=## )", before_faq.strip())
    preamble_blocks = _parse_markdown_blocks(chunks[0].splitlines())
    preamble_paragraphs = [block for block in preamble_blocks if block["type"] == "p"]
    if not preamble_paragraphs:
        raise ValueError("Bear 650 source has no lead paragraph")
    lede = preamble_paragraphs[0]["text"]
    remaining_preamble = preamble_blocks[1:]
    if remaining_preamble:
        content_sections.append({"blocks": remaining_preamble})

    for chunk in chunks[1:]:
        chunk_lines = chunk.splitlines()
        title = chunk_lines[0][3:].strip()
        content_sections.append({"title": title, "blocks": _parse_markdown_blocks(chunk_lines[1:])})

    cta_blocks = _parse_markdown_blocks([line for line in cta_rest.splitlines() if line.strip() != "---"])
    content_sections.append({"title": cta_title.strip(), "blocks": cta_blocks, "className": "blog-cta-box"})

    hero_alt = ""
    for section in content_sections:
        for block in section.get("blocks", []):
            if block.get("type") == "image" and block.get("image") == 1:
                hero_alt = block["alt"]
                break
        if hero_alt:
            break

    return {
        "meta": meta,
        "h1": h1,
        "lede": lede,
        "heroAlt": hero_alt,
        "contentSections": content_sections,
        "faqs": faq_items,
    }


def _load_bear650_post():
    source = _BEAR650_SOURCE.read_text(encoding="utf-8")
    parsed = {
        code: _parse_bear650_language(raw)
        for code, raw in _split_localized_sections(source, _BEAR650_LANGS, "Bear 650").items()
    }
    post_meta = {}
    post_body = {}
    for code in ("en", "ru", "uk", "pt"):
        item = parsed[code]
        post_meta[code] = {
            "title": item["meta"]["title"],
            "description": item["meta"]["description"],
            "excerpt": item["meta"]["description"],
        }
        post_body[code] = {
            **_BEAR650_LABELS[code],
            "h1": item["h1"],
            "h1Crumb": item["h1"],
            "lede": item["lede"],
            "heroAlt": item["heroAlt"],
            "contentSections": item["contentSections"],
            "faqs": item["faqs"],
        }
    return {
        "publishedISO": "2026-06-29T10:00:00+01:00",
        "modifiedISO": "2026-07-20T08:29:09+01:00",
        "heroImage": "/photos/blog/blog-royal-enfield-bear-650-fork-oil-case-study-hero-1600.jpg",
        "heroImageDims": (1536, 1024),
        "imageBase": "/photos/blog/blog-royal-enfield-bear-650-fork-oil-case-study",
        "imageHero": 1,
        "imageCount": 2,
        "imageDims": {1: (1600, 1200), 2: (1600, 1200)},
        "sourceLocalizedSlugs": {code: _BEAR650_SLUG for code in ("en", "ru", "pt", "uk")},
        "meta": post_meta,
        "body": post_body,
    }


def _parse_harley_service_language(raw):
    lines = raw.splitlines()
    meta = {}
    h1 = None
    body_lines = []
    in_body = False
    for line in lines[1:]:
        if line.startswith("**SEO Title:**"):
            meta["title"] = line.split("**SEO Title:**", 1)[1].strip()
        elif line.startswith("**Meta description:**"):
            meta["description"] = line.split("**Meta description:**", 1)[1].strip()
        elif line.startswith("**URL slug:**"):
            meta["slug"] = line.split("**URL slug:**", 1)[1].strip()
        elif line.startswith("# "):
            h1 = line[2:].strip()
            in_body = True
        elif in_body:
            body_lines.append(line)
    if not (meta.get("title") and meta.get("description") and meta.get("slug") and h1):
        raise ValueError("Incomplete Harley service blog source metadata")

    body = "\n".join(body_lines).strip()
    before_faq, faq_tail = body.split("\n## FAQ\n", 1)
    hero_match = re.search(r"^\[IMAGE:.*\|\s*ALT:\s*(.+)\]\s*$", faq_tail, re.MULTILINE)
    if not hero_match:
        raise ValueError("Missing Harley service hero image slot")
    hero_alt = hero_match.group(1).strip()
    faq_and_cta = faq_tail[:hero_match.start()].strip()

    faq_items = []
    cta_parts = []
    for paragraph in [part.strip() for part in faq_and_cta.split("\n\n") if part.strip()]:
        match = re.match(r"\*\*(.*?)\*\*\s*(.*)", paragraph, re.S)
        if not match:
            raise ValueError(f"Cannot parse Harley service FAQ or CTA block: {paragraph[:80]}")
        title, text = match.group(1).strip(), match.group(2).strip()
        if title.endswith("?"):
            faq_items.append({"q": title, "a": _inline_markdown(text)})
        else:
            cta_parts.append(paragraph)
    if len(faq_items) != 6:
        raise ValueError(f"Expected 6 Harley service FAQ items, got {len(faq_items)}")
    if len(cta_parts) != 1:
        raise ValueError(f"Expected 1 Harley service CTA block, got {len(cta_parts)}")

    content_sections = []
    chunks = re.split(r"\n(?=## )", before_faq.strip())
    preamble_blocks = _parse_markdown_blocks(chunks[0].splitlines())
    preamble_paragraphs = [block for block in preamble_blocks if block["type"] == "p"]
    if not preamble_paragraphs:
        raise ValueError("Harley service source has no lead paragraph")
    lede = preamble_paragraphs[0]["text"]
    if preamble_blocks[1:]:
        content_sections.append({"blocks": preamble_blocks[1:], "className": "blog-article-lead"})

    video_title = ""
    video_text = ""
    for chunk in chunks[1:]:
        chunk_lines = chunk.splitlines()
        title = chunk_lines[0][3:].strip()
        blocks = _parse_markdown_blocks(chunk_lines[1:])
        section = {"title": title, "blocks": blocks}
        if any(block["type"] == "video" for block in blocks):
            section["className"] = "blog-video-section"
            video_title = title
            video_text = next((block["text"] for block in blocks if block["type"] == "p"), "")
        content_sections.append(section)

    content_sections.append({
        "blocks": [{"type": "p", "text": _inline_markdown(cta_parts[0])}],
        "className": "blog-cta-box",
    })
    if not (video_title and video_text):
        raise ValueError("Missing Harley service video section copy")

    return {
        "meta": meta,
        "h1": h1,
        "lede": lede,
        "heroAlt": hero_alt,
        "contentSections": content_sections,
        "faqs": faq_items,
        "videoTitle": video_title,
        "videoText": video_text,
    }


def _load_harley_service_post():
    source = _HARLEY_SERVICE_SOURCE.read_text(encoding="utf-8")
    parsed = {
        code: _parse_harley_service_language(raw)
        for code, raw in _split_localized_sections(
            source, _HARLEY_SERVICE_LANGS, "Harley service"
        ).items()
    }
    post_meta = {}
    post_body = {}
    for code in ("en", "ru", "uk", "pt"):
        item = parsed[code]
        expected_slug = f"/{'' if code == 'en' else code + '/'}blog/{_HARLEY_SERVICE_SLUG}/"
        if item["meta"]["slug"] != expected_slug:
            raise ValueError(
                f"Unexpected Harley service slug for {code}: {item['meta']['slug']}"
            )
        post_meta[code] = {
            "title": item["meta"]["title"],
            "description": item["meta"]["description"],
            "excerpt": item["meta"]["description"],
        }
        post_body[code] = {
            **_HARLEY_SERVICE_LABELS[code],
            "h1": item["h1"],
            "h1Crumb": item["h1"],
            "lede": item["lede"],
            "heroAlt": item["heroAlt"],
            "contentSections": item["contentSections"],
            "faqs": item["faqs"],
            "videoTitle": item["videoTitle"],
            "videoText": item["videoText"],
        }
    return {
        "publishedISO": "2026-07-10T12:00:00+01:00",
        "modifiedISO": "2026-07-24T20:58:26+01:00",
        "topics": ("harley",),
        "heroImage": "/photos/blog/blog-harley-davidson-full-service-done-right-hero.png",
        "heroImageDims": (1672, 941),
        "schemaImage": "/photos/optimized/blog-blog-harley-davidson-full-service-done-right-hero-1920.webp",
        "schemaEntityName": "Iron Custom Motors",
        "publisherLogo": {
            "url": "https://ironcustommotors.com/photos/icon-512.png",
            "width": 512,
            "height": 512,
        },
        "imageBase": "/photos/blog/blog-harley-davidson-full-service-done-right",
        "imageHero": 0,
        "imageCount": 0,
        "imageDims": {},
        "nativeVideo": {
            "contentUrl": "https://media.ironcustommotors.com/harley-service-asmr.mp4",
            "poster": "https://media.ironcustommotors.com/harley-service-asmr-poster.jpg",
            "uploadDate": "2026-07-10T12:00:00+01:00",
            "duration": "PT1M24S",
            "width": 1080,
            "height": 1920,
        },
        "sourceLocalizedSlugs": {
            code: _HARLEY_SERVICE_SLUG for code in ("en", "ru", "pt", "uk")
        },
        "meta": post_meta,
        "body": post_body,
    }


def _parse_bear650_build_language(raw):
    lines = raw.splitlines()
    meta = {}
    h1 = None
    body_lines = []
    in_body = False
    for line in lines[1:]:
        if line.startswith("**SEO Title:**"):
            meta["title"] = line.split("**SEO Title:**", 1)[1].strip()
        elif line.startswith("**Meta Description:**"):
            meta["description"] = line.split("**Meta Description:**", 1)[1].strip()
        elif line.startswith("**URL:**"):
            meta["slug"] = line.split("**URL:**", 1)[1].strip()
        elif line.startswith("# "):
            h1 = line[2:].strip()
            in_body = True
        elif in_body:
            body_lines.append(line)
    if not (meta.get("title") and meta.get("description") and meta.get("slug") and h1):
        raise ValueError("Incomplete Bear 650 scrambler build metadata")

    body = "\n".join(body_lines).strip()
    faq_match = re.search(r"\n## (?:FAQ|Perguntas frequentes)\n", body)
    if not faq_match:
        raise ValueError("Missing Bear 650 scrambler build FAQ section")
    before_faq = body[:faq_match.start()].strip()
    faq_text = body[faq_match.end():].strip()

    hero_match = re.search(
        r'^\[IMAGE:.*?\|\s*ALT:\s*(?:"([^"]+)"|(.+?))\]\s*$',
        before_faq,
        re.MULTILINE,
    )
    if not hero_match:
        raise ValueError("Missing Bear 650 scrambler build hero image slot")
    hero_alt = (hero_match.group(1) or hero_match.group(2)).strip()
    before_faq = f"{before_faq[:hero_match.start()]}\n{before_faq[hero_match.end():]}".strip()

    faq_items = []
    for paragraph in [
        part.strip()
        for part in faq_text.split("\n\n")
        if part.strip() and part.strip() != "---"
    ]:
        match = re.match(r"\*\*(.*?)\*\*\s*(.*)", paragraph, re.S)
        if not match:
            raise ValueError(f"Cannot parse Bear 650 scrambler build FAQ item: {paragraph[:80]}")
        faq_items.append({"q": match.group(1).strip(), "a": _inline_markdown(match.group(2).strip())})
    if len(faq_items) != 6:
        raise ValueError(f"Expected 6 Bear 650 scrambler build FAQ items, got {len(faq_items)}")

    chunks = re.split(r"\n(?=## )", before_faq)
    preamble_blocks = _parse_markdown_blocks(chunks[0].splitlines())
    preamble_paragraphs = [block for block in preamble_blocks if block["type"] == "p"]
    if not preamble_paragraphs:
        raise ValueError("Bear 650 scrambler build source has no lead paragraph")
    lede = preamble_paragraphs[0]["text"]
    content_sections = []
    if preamble_blocks[1:]:
        content_sections.append({"blocks": preamble_blocks[1:], "className": "blog-article-lead"})

    video_title = ""
    video_text = ""
    for chunk in chunks[1:]:
        chunk_lines = chunk.splitlines()
        title = chunk_lines[0][3:].strip()
        blocks = _parse_markdown_blocks(chunk_lines[1:])
        section = {"title": title, "blocks": blocks}
        if any(block["type"] == "video" for block in blocks):
            section["className"] = "blog-video-section"
            video_title = title
            video_text = next((block["text"] for block in blocks if block["type"] == "p"), "")
        content_sections.append(section)
    if content_sections:
        content_sections[-1]["className"] = "blog-cta-box"
    if not (video_title and video_text):
        raise ValueError("Missing Bear 650 scrambler build video section copy")

    return {
        "meta": meta,
        "h1": h1,
        "lede": lede,
        "heroAlt": hero_alt,
        "contentSections": content_sections,
        "faqs": faq_items,
        "videoTitle": video_title,
        "videoText": video_text,
    }


def _load_bear650_build_post():
    source = _BEAR650_BUILD_SOURCE.read_text(encoding="utf-8")
    parsed = {
        code: _parse_bear650_build_language(raw)
        for code, raw in _split_localized_sections(
            source, _BEAR650_BUILD_LANGS, "Bear 650 scrambler build"
        ).items()
    }
    post_meta = {}
    post_body = {}
    for code in ("en", "ru", "uk", "pt"):
        item = parsed[code]
        expected_slug = f"/{'' if code == 'en' else code + '/'}blog/{_BEAR650_BUILD_SLUG}/"
        if item["meta"]["slug"] != expected_slug:
            raise ValueError(
                f"Unexpected Bear 650 scrambler build slug for {code}: {item['meta']['slug']}"
            )
        post_meta[code] = {
            "title": item["meta"]["title"],
            "description": item["meta"]["description"],
            "excerpt": item["meta"]["description"],
        }
        post_body[code] = {
            **_BEAR650_BUILD_LABELS[code],
            "h1": item["h1"],
            "h1Crumb": item["h1"],
            "lede": item["lede"],
            "heroAlt": item["heroAlt"],
            "contentSections": item["contentSections"],
            "faqs": item["faqs"],
            "videoTitle": item["videoTitle"],
            "videoText": item["videoText"],
        }
    return {
        "publishedISO": "2026-07-19T12:00:00+01:00",
        "modifiedISO": "2026-07-20T09:00:53+01:00",
        "heroImage": "/photos/blog/blog-royal-enfield-bear-650-scrambler-build-hero.png",
        "heroImageDims": (1672, 941),
        "schemaImage": "/photos/optimized/blog-blog-royal-enfield-bear-650-scrambler-build-hero-1920.webp",
        "schemaEntityName": "Iron Custom Motors",
        "publisherLogo": {
            "url": "https://ironcustommotors.com/photos/icon-512.png",
            "width": 512,
            "height": 512,
        },
        "imageBase": "/photos/blog/blog-royal-enfield-bear-650-scrambler-build",
        "imageHero": 0,
        "imageCount": 0,
        "imageDims": {},
        "nativeVideo": {
            "contentUrl": "https://media.ironcustommotors.com/bear650-scrambler-build.mp4",
            "poster": "https://media.ironcustommotors.com/bear650-scrambler-build-cover.png",
            "uploadDate": "2026-07-19T12:00:00+01:00",
            "duration": "PT6M43S",
            "width": 1920,
            "height": 1080,
        },
        "sourceLocalizedSlugs": {
            code: _BEAR650_BUILD_SLUG for code in ("en", "ru", "pt", "uk")
        },
        "meta": post_meta,
        "body": post_body,
    }

BLOG_HUB_BODY = {
    "en": {
        "eyebrow": "Blog · Workshop knowledge",
        "h1": "Workshop notes for<br/><span class=\"accent\">real riders.</span>",
        "sub": "Useful articles from the Iron Custom Motors bench: maintenance, diagnostics, parts choices, upgrades, pre-purchase checks and the small details that keep motorcycles honest.",
        "breadHome": "Home",
        "h1Crumb": "Blog",
        "readMore": "Read the guide →",
        "noPosts": "The first workshop guide is being prepared.",
        "topicsEyebrow": "What will live here",
        "topicsTitle": "Practical articles, <em>not noise.</em>",
        "topicsLead": "The blog is for useful, searchable material: what riders ask us in the workshop, what we check before buying a bike, how we choose parts, and why some jobs should be done before they become expensive.",
        "topic1Title": "Maintenance",
        "topic1Text": "Service intervals, fluids, brakes, chains, tires and seasonal preparation for Portugal.",
        "topic2Title": "Diagnostics",
        "topic2Text": "How symptoms turn into real causes: electrical, engine, suspension and running issues.",
        "topic3Title": "Parts & upgrades",
        "topic3Text": "OEM, aftermarket and tuning choices explained from a workshop point of view.",
        "topic4Title": "Buying used",
        "topic4Text": "What to inspect before buying a motorcycle and when a cheap bike becomes expensive.",
        "topic5Title": "Workshop life",
        "topic5Text": "Stories from the bench, project decisions and the culture behind Iron Custom Motors.",
        "ctaEyebrow": "Need an answer now?",
        "ctaTitle": "Ask the workshop.",
        "ctaText": "Send your motorcycle model and question via WhatsApp. If it needs a proper check, we will tell you the next step.",
        "btnWA": "WhatsApp us",
        "btnContact": "Contact page",
    },
    "ru": {
        "eyebrow": "Блог · знания из мастерской",
        "h1": "Заметки из мастерской<br/>для <span class=\"accent\">реальных райдеров.</span>",
        "sub": "Полезные материалы от Iron Custom Motors: обслуживание, диагностика, выбор запчастей, апгрейды, предпокупочные проверки и мелочи, которые помогают мотоциклу оставаться честным.",
        "breadHome": "Главная",
        "h1Crumb": "Блог",
        "readMore": "Читать материал →",
        "noPosts": "Первый материал уже готовится.",
        "topicsEyebrow": "Что здесь будет",
        "topicsTitle": "Практические статьи, <em>а не шум.</em>",
        "topicsLead": "Блог нужен для полезных материалов, которые ищут владельцы мотоциклов: что спрашивают в мастерской, что проверять перед покупкой, как выбирать запчасти и почему некоторые работы лучше сделать до того, как они станут дорогими.",
        "topic1Title": "Обслуживание",
        "topic1Text": "Интервалы сервиса, жидкости, тормоза, цепи, шины и сезонная подготовка для Португалии.",
        "topic2Title": "Диагностика",
        "topic2Text": "Как симптомы превращаются в реальные причины: электрика, двигатель, подвеска и ходовая.",
        "topic3Title": "Запчасти и апгрейды",
        "topic3Text": "OEM, aftermarket и тюнинг-решения с точки зрения мастерской.",
        "topic4Title": "Покупка б/у",
        "topic4Text": "Что проверять перед покупкой мотоцикла и когда дешёвый байк становится дорогим.",
        "topic5Title": "Жизнь мастерской",
        "topic5Text": "Истории со стенда, решения по проектам и культура Iron Custom Motors.",
        "ctaEyebrow": "Нужен ответ сейчас?",
        "ctaTitle": "Спросите мастерскую.",
        "ctaText": "Отправьте модель мотоцикла и вопрос в WhatsApp. Если нужна проверка, подскажем следующий шаг.",
        "btnWA": "WhatsApp",
        "btnContact": "Контакты",
    },
    "uk": {
        "eyebrow": "Блог · знання з майстерні",
        "h1": "Нотатки з майстерні<br/>для <span class=\"accent\">реальних райдерів.</span>",
        "sub": "Корисні матеріали від Iron Custom Motors: обслуговування, діагностика, вибір запчастин, апґрейди, передкупівельні перевірки й дрібниці, що допомагають мотоциклу залишатися чесним.",
        "breadHome": "Головна",
        "h1Crumb": "Блог",
        "readMore": "Читати матеріал →",
        "noPosts": "Перший матеріал уже готується.",
        "topicsEyebrow": "Що тут буде",
        "topicsTitle": "Практичні статті, <em>а не шум.</em>",
        "topicsLead": "Блог потрібен для корисних матеріалів, які шукають власники мотоциклів: що запитують у майстерні, що перевіряти перед купівлею, як обирати запчастини і чому деякі роботи краще зробити до того, як вони стануть дорогими.",
        "topic1Title": "Обслуговування",
        "topic1Text": "Інтервали сервісу, рідини, гальма, ланцюги, шини та сезонна підготовка для Португалії.",
        "topic2Title": "Діагностика",
        "topic2Text": "Як симптоми перетворюються на реальні причини: електрика, двигун, підвіска та ходова.",
        "topic3Title": "Запчастини й апґрейди",
        "topic3Text": "OEM, aftermarket і тюнінг-рішення з точки зору майстерні.",
        "topic4Title": "Купівля б/в",
        "topic4Text": "Що перевіряти перед купівлею мотоцикла і коли дешевий байк стає дорогим.",
        "topic5Title": "Життя майстерні",
        "topic5Text": "Історії зі стенда, рішення щодо проєктів і культура Iron Custom Motors.",
        "ctaEyebrow": "Потрібна відповідь зараз?",
        "ctaTitle": "Запитайте майстерню.",
        "ctaText": "Надішліть модель мотоцикла і питання у WhatsApp. Якщо потрібна перевірка, підкажемо наступний крок.",
        "btnWA": "WhatsApp",
        "btnContact": "Контакти",
    },
    "pt": {
        "eyebrow": "Blog · Conhecimento de oficina",
        "h1": "Notas de oficina<br/>para <span class=\"accent\">riders reais.</span>",
        "sub": "Artigos úteis da bancada da Iron Custom Motors: manutenção, diagnóstico, escolha de peças, upgrades, inspeções pré-compra e detalhes que mantêm a moto honesta.",
        "breadHome": "Início",
        "h1Crumb": "Blog",
        "readMore": "Ler o guia →",
        "noPosts": "O primeiro guia de oficina está a ser preparado.",
        "topicsEyebrow": "O que vai viver aqui",
        "topicsTitle": "Artigos práticos, <em>não ruído.</em>",
        "topicsLead": "O blog é para material útil e pesquisável: o que os riders nos perguntam na oficina, o que verificar antes de comprar uma moto, como escolher peças e porque alguns trabalhos devem ser feitos antes de ficarem caros.",
        "topic1Title": "Manutenção",
        "topic1Text": "Intervalos de serviço, fluidos, travões, correntes, pneus e preparação sazonal em Portugal.",
        "topic2Title": "Diagnóstico",
        "topic2Text": "Como sintomas viram causas reais: elétrica, motor, suspensão e comportamento em andamento.",
        "topic3Title": "Peças e upgrades",
        "topic3Text": "OEM, aftermarket e tuning explicados do ponto de vista da oficina.",
        "topic4Title": "Comprar usada",
        "topic4Text": "O que verificar antes de comprar uma moto e quando uma moto barata fica cara.",
        "topic5Title": "Vida de oficina",
        "topic5Text": "Histórias da bancada, decisões de projeto e a cultura por trás da Iron Custom Motors.",
        "ctaEyebrow": "Precisa de resposta agora?",
        "ctaTitle": "Pergunte à oficina.",
        "ctaText": "Envie o modelo da moto e a pergunta por WhatsApp. Se precisar de uma verificação, dizemos o próximo passo.",
        "btnWA": "WhatsApp",
        "btnContact": "Contacto",
    },
}

# Blog posts. Individual posts are generated by build_blog.py.
BLOG_POSTS = {'revtech-110-oil-service-engine-gearbox-drive': {'publishedISO': '2026-06-17',
                                                  'modifiedISO': '2026-06-17',
                                                  'imageBase': '/photos/blog/blog-revtech-110-oil-service',
                                                  'imageHero': 1,
                                                  'imageCount': 1,
                                                  'imageDims': {1: (1600, 900)},
                                                  'youtubeUrl': 'https://www.youtube.com/shorts/ylsQq_bnvU0',
                                                  'youtubeEmbed': 'https://www.youtube.com/embed/ylsQq_bnvU0',
                                                  'sourceLocalizedSlugs': {'en': 'revtech-110-oil-service-engine-gearbox-drive',
                                                                           'ru': 'revtech-110-zamena-masla-dvigatel-korobka-privod',
                                                                           'pt': 'servico-oleo-revtech-110-motor-caixa-transmissao',
                                                                           'uk': 'revtech-110-zamina-olyvy-dvyhun-korobka-pryvid'},
                                                  'meta': {'en': {'title': 'RevTech 110 Oil Service: Engine, Gearbox & '
                                                                           'Drive | Iron Custom Motors',
                                                                  'description': 'Why oil service matters on RevTech '
                                                                                 '110 and similar V-twin engines: '
                                                                                 'engine, gearbox and drive '
                                                                                 'lubrication explained by Iron Custom '
                                                                                 'Motors.',
                                                                  'excerpt': 'Why oil service matters on RevTech 110 '
                                                                             'and similar V-twin engines: engine, '
                                                                             'gearbox and drive lubrication explained '
                                                                             'by Iron Custom Motors.'},
                                                           'ru': {'title': 'Сервис масла RevTech 110: двигатель, КПП и '
                                                                           'привод | Iron Custom Motors',
                                                                  'description': 'Почему замена масла важна для '
                                                                                 'RevTech 110 и похожих V-twin '
                                                                                 'моторов: двигатель, коробка и привод '
                                                                                 'глазами Iron Custom Motors.',
                                                                  'excerpt': 'Почему замена масла важна для RevTech '
                                                                             '110 и похожих V-twin моторов: двигатель, '
                                                                             'коробка и привод глазами Iron Custom '
                                                                             'Motors.'},
                                                           'pt': {'title': 'Serviço de Óleo RevTech 110: Motor, Caixa '
                                                                           'e Transmissão | Iron Custom Motors',
                                                                  'description': 'Porque o serviço de óleo é essencial '
                                                                                 'no RevTech 110 e em V-twin '
                                                                                 'semelhantes: motor, caixa e '
                                                                                 'transmissão explicados pela Iron '
                                                                                 'Custom Motors.',
                                                                  'excerpt': 'Porque o serviço de óleo é essencial no '
                                                                             'RevTech 110 e em V-twin semelhantes: '
                                                                             'motor, caixa e transmissão explicados '
                                                                             'pela Iron Custom Motors.'},
                                                           'uk': {'title': 'Сервіс оливи RevTech 110: двигун, КПП і '
                                                                           'привід | Iron Custom Motors',
                                                                  'description': 'Чому заміна оливи важлива для '
                                                                                 'RevTech 110 і схожих V-twin моторів: '
                                                                                 'двигун, коробка та привід від Iron '
                                                                                 'Custom Motors.',
                                                                  'excerpt': 'Чому заміна оливи важлива для RevTech '
                                                                             '110 і схожих V-twin моторів: двигун, '
                                                                             'коробка та привід від Iron Custom '
                                                                             'Motors.'}},
                                                  'body': {'en': {'eyebrow': 'Workshop guide · 17 June 2026',
                                                                  'publishedLabel': 'Published 17 June 2026',
                                                                  'breadHome': 'Home',
                                                                  'breadBlog': 'Blog',
                                                                  'introTitle': 'What the service includes',
                                                                  'videoEyebrow': 'Workshop video',
                                                                  'videoTitle': 'Watch the RevTech 110 oil service',
                                                                  'videoText': 'A short look at the service: engine '
                                                                               'oil, gearbox oil and drive-side '
                                                                               'lubrication checked as separate '
                                                                               'mechanical zones.',
                                                                  'videoLink': 'Open on YouTube',
                                                                  'faqTitle': 'RevTech 110 oil service FAQ',
                                                                  'ctaEyebrow': 'Need this service?',
                                                                  'ctaTitle': 'Book an oil service or inspection.',
                                                                  'btnWA': 'WhatsApp us',
                                                                  'btnBack': 'Back to blog',
                                                                  'imageAlt': 'RevTech 110 oil service cover graphic '
                                                                              'showing a custom V-twin motorcycle in '
                                                                              'the Iron Custom Motors workshop.',
                                                                  'imageCaption': 'RevTech 110 oil service at Iron '
                                                                                  'Custom Motors: engine, gearbox and '
                                                                                  'drive-side lubrication treated as '
                                                                                  'separate systems.',
                                                                  'h1': 'RevTech 110 Oil Service:<br/><span '
                                                                        'class="accent">Engine, Gearbox & Final '
                                                                        'Drive.</span>',
                                                                  'h1Crumb': 'RevTech 110 Oil Service: Engine, Gearbox '
                                                                             '& Final Drive',
                                                                  'lede': 'A big V-twin rarely fails without giving '
                                                                          'small warnings first. Sometimes the signs '
                                                                          'are obvious: rough shifting, more '
                                                                          'mechanical noise than usual, a clutch that '
                                                                          'feels different, or oil that comes out '
                                                                          'darker and thinner than expected. Sometimes '
                                                                          'there is no clear symptom at all — just a '
                                                                          'motorcycle that has been ridden, heated, '
                                                                          'cooled, stored, started again, and slowly '
                                                                          'asked to work with tired fluids.',
                                                                  'intro': {'title': 'What the service includes',
                                                                            'paragraphs': ['This short video shows an '
                                                                                           'oil service on a RevTech '
                                                                                           '110 setup: engine oil, '
                                                                                           'gearbox oil and drive-side '
                                                                                           'lubrication. For this type '
                                                                                           'of Harley-style custom '
                                                                                           'motorcycle, it is not just '
                                                                                           '“an oil change.” It is a '
                                                                                           'basic health check of '
                                                                                           'three different mechanical '
                                                                                           'zones that work under very '
                                                                                           'different loads.',
                                                                                           'The engine oil deals with '
                                                                                           'heat, combustion '
                                                                                           'by-products and internal '
                                                                                           'friction. The gearbox oil '
                                                                                           'protects loaded gears and '
                                                                                           'bearings. The primary or '
                                                                                           'drive-side lubrication, '
                                                                                           'depending on the exact '
                                                                                           'build, has to work around '
                                                                                           'chain, clutch and rotating '
                                                                                           'components. Treating all '
                                                                                           'of them as the same thing '
                                                                                           'is a common mistake.',
                                                                                           'At Iron Custom Motors, we '
                                                                                           'look at this type of '
                                                                                           'service as a system check, '
                                                                                           'not just a drain-and-fill '
                                                                                           'job.']},
                                                                  'sections': [{'title': 'Why It Matters',
                                                                                'paragraphs': ['On a '
                                                                                               'large-displacement '
                                                                                               'air-cooled or '
                                                                                               'air/oil-cooled V-twin, '
                                                                                               'oil has a difficult '
                                                                                               'life. The engine works '
                                                                                               'with big pistons, '
                                                                                               'strong pulses, high '
                                                                                               'internal loads and a '
                                                                                               'lot of heat. In city '
                                                                                               'traffic around Lisbon '
                                                                                               'or Cascais, that heat '
                                                                                               'does not disappear '
                                                                                               'quickly. Short trips, '
                                                                                               'stop-and-go riding and '
                                                                                               'coastal humidity all '
                                                                                               'make the service '
                                                                                               'environment harder '
                                                                                               'than it looks on '
                                                                                               'paper.',
                                                                                               'Fresh oil does more '
                                                                                               'than reduce friction. '
                                                                                               'It helps carry heat '
                                                                                               'away from critical '
                                                                                               'parts, suspends '
                                                                                               'contamination, '
                                                                                               'protects metal '
                                                                                               'surfaces and keeps '
                                                                                               'internal components '
                                                                                               'working with the '
                                                                                               'correct film strength. '
                                                                                               'When oil is old, '
                                                                                               'contaminated, diluted '
                                                                                               'or simply wrong for '
                                                                                               'the application, the '
                                                                                               'motorcycle may still '
                                                                                               'run — but the '
                                                                                               'protection margin '
                                                                                               'becomes smaller.',
                                                                                               'The gearbox has a '
                                                                                               'different problem. It '
                                                                                               'does not deal with '
                                                                                               'combustion, but it '
                                                                                               'sees high pressure '
                                                                                               'between gear teeth and '
                                                                                               'load changes every '
                                                                                               'time the rider opens '
                                                                                               'or closes the '
                                                                                               'throttle. Old or '
                                                                                               'incorrect gearbox oil '
                                                                                               'can make shifting feel '
                                                                                               'heavier, increase wear '
                                                                                               'on gears and bearings, '
                                                                                               'and make small '
                                                                                               'internal problems '
                                                                                               'harder to detect '
                                                                                               'early.',
                                                                                               'The drive side is '
                                                                                               'another story. On many '
                                                                                               'Harley-style '
                                                                                               'motorcycles, the belt '
                                                                                               'final drive itself is '
                                                                                               'not oil-filled. The '
                                                                                               'oil service usually '
                                                                                               'refers to the primary '
                                                                                               'drive or '
                                                                                               'transmission-related '
                                                                                               'lubricant zones. On a '
                                                                                               'custom motorcycle, '
                                                                                               'especially one built '
                                                                                               'around an aftermarket '
                                                                                               'engine such as a '
                                                                                               'RevTech, the exact '
                                                                                               'configuration must be '
                                                                                               'confirmed before '
                                                                                               'choosing oil, quantity '
                                                                                               'or procedure.']},
                                                                               {'title': 'Main Technical Explanation',
                                                                                'paragraphs': ['Engine oil is the most '
                                                                                               'obvious part of the '
                                                                                               'service, but also the '
                                                                                               'easiest to '
                                                                                               'oversimplify. In a '
                                                                                               'RevTech 110 or similar '
                                                                                               'large V-twin engine, '
                                                                                               'oil works under high '
                                                                                               'thermal and mechanical '
                                                                                               'stress. It must '
                                                                                               'protect bearings, '
                                                                                               'pistons, cylinder '
                                                                                               'walls, cam components '
                                                                                               'and other internal '
                                                                                               'parts while carrying '
                                                                                               'contamination away '
                                                                                               'from those surfaces.',
                                                                                               'Over time, oil loses '
                                                                                               'part of its protective '
                                                                                               'properties. It can '
                                                                                               'oxidize, collect fuel '
                                                                                               'dilution, hold '
                                                                                               'microscopic metal '
                                                                                               'particles and become '
                                                                                               'less stable under '
                                                                                               'heat. That is why an '
                                                                                               'engine oil service '
                                                                                               'should also include '
                                                                                               'looking at the drained '
                                                                                               'oil condition, '
                                                                                               'checking the filter '
                                                                                               'area, inspecting for '
                                                                                               'leaks, and confirming '
                                                                                               'that there are no '
                                                                                               'signs of oil '
                                                                                               'migration, overfilling '
                                                                                               'or external '
                                                                                               'contamination.',
                                                                                               'The oil level and '
                                                                                               'checking procedure can '
                                                                                               'be different depending '
                                                                                               'on the oil tank, '
                                                                                               'frame, engine '
                                                                                               'configuration and '
                                                                                               'whether the bike is '
                                                                                               'checked hot, cold, '
                                                                                               'upright or on the side '
                                                                                               'stand. There is no '
                                                                                               'universal number that '
                                                                                               'should be trusted '
                                                                                               'without the correct '
                                                                                               'manual.',
                                                                                               'The gearbox lives a '
                                                                                               'different life from '
                                                                                               'the engine. It does '
                                                                                               'not see combustion '
                                                                                               'gases, but it sees '
                                                                                               'high pressure between '
                                                                                               'gear teeth and load '
                                                                                               'changes every time the '
                                                                                               'rider opens or closes '
                                                                                               'the throttle. When '
                                                                                               'gearbox oil gets old '
                                                                                               'or contaminated, the '
                                                                                               'rider may notice '
                                                                                               'heavier shifting, more '
                                                                                               'mechanical noise, a '
                                                                                               'less precise feel '
                                                                                               'through the lever, or '
                                                                                               'difficulty finding '
                                                                                               'neutral.',
                                                                                               'The phrase “final '
                                                                                               'drive” can mean '
                                                                                               'different things '
                                                                                               'depending on the '
                                                                                               'motorcycle layout. On '
                                                                                               'many Harley-style '
                                                                                               'motorcycles, the belt '
                                                                                               'final drive itself is '
                                                                                               'not oil-filled. The '
                                                                                               'oil service usually '
                                                                                               'refers to the primary '
                                                                                               'drive or '
                                                                                               'transmission-related '
                                                                                               'lubricant zones. The '
                                                                                               'exact configuration '
                                                                                               'must be confirmed '
                                                                                               'before choosing oil, '
                                                                                               'quantity or '
                                                                                               'procedure.']},
                                                                               {'title': 'Workshop Nuances Riders '
                                                                                         'Often Miss',
                                                                                'bullets': ['Three oil zones do not '
                                                                                            'always want the same oil. '
                                                                                            'The engine, gearbox and '
                                                                                            'clutch or primary area '
                                                                                            'have different mechanical '
                                                                                            'needs. The right choice '
                                                                                            'depends on the actual '
                                                                                            'components installed on '
                                                                                            'the motorcycle.',
                                                                                            '“It starts and rides” '
                                                                                            'does not mean the oil is '
                                                                                            'healthy. A big V-twin can '
                                                                                            'still pull strongly with '
                                                                                            'old oil, but the '
                                                                                            'protection margin may '
                                                                                            'already be reduced.',
                                                                                            'Drain plug debris is '
                                                                                            'information. Fine paste '
                                                                                            'can be normal wear '
                                                                                            'residue, while chips, '
                                                                                            'flakes or heavy metal '
                                                                                            'build-up mean the service '
                                                                                            'should become an '
                                                                                            'inspection.',
                                                                                            'Coastal climate matters. '
                                                                                            'Around Cascais and '
                                                                                            'Lisbon, humidity and sea '
                                                                                            'air can accelerate '
                                                                                            'corrosion around '
                                                                                            'fasteners, electrical '
                                                                                            'connectors, exposed metal '
                                                                                            'and sealing surfaces.',
                                                                                            'Custom builds need '
                                                                                            'rechecking. A '
                                                                                            'RevTech-powered '
                                                                                            'motorcycle may combine '
                                                                                            'aftermarket engine, '
                                                                                            'frame, oil tank, hoses, '
                                                                                            'fittings, gearbox, '
                                                                                            'primary components and '
                                                                                            'exhaust layout. After '
                                                                                            'service, the bike should '
                                                                                            'be checked as a complete '
                                                                                            'system.']},
                                                                               {'title': 'Common Mistakes',
                                                                                'bullets': ['Treating a '
                                                                                            'high-displacement custom '
                                                                                            'V-twin like a generic '
                                                                                            'motorcycle.',
                                                                                            'Changing only engine oil '
                                                                                            'and forgetting the '
                                                                                            'gearbox or primary-drive '
                                                                                            'lubricant.',
                                                                                            'Using universal numbers '
                                                                                            'from the internet instead '
                                                                                            'of the correct '
                                                                                            'documentation.',
                                                                                            'Overfilling. More oil is '
                                                                                            'not automatically safer '
                                                                                            'and can cause leaks, '
                                                                                            'clutch issues or messy '
                                                                                            'breather behavior.',
                                                                                            'Ignoring small leaks '
                                                                                            'after service. A light '
                                                                                            'oil mark can be a simple '
                                                                                            'O-ring issue, but it can '
                                                                                            'also point to a sealing '
                                                                                            'surface, hose, fitting or '
                                                                                            'venting problem.']},
                                                                               {'title': 'When to Visit a Workshop',
                                                                                'paragraphs': ['Book an inspection if '
                                                                                               'shifting becomes '
                                                                                               'heavier or less '
                                                                                               'precise, neutral is '
                                                                                               'harder to find, the '
                                                                                               'clutch starts '
                                                                                               'dragging, the engine '
                                                                                               'sounds harsher than '
                                                                                               'usual, oil leaks '
                                                                                               'appear after a ride, '
                                                                                               'the oil smells burnt '
                                                                                               'or looks unusually '
                                                                                               'contaminated, there '
                                                                                               'are visible metal '
                                                                                               'particles on a drain '
                                                                                               'plug, or the '
                                                                                               'motorcycle has been '
                                                                                               'stored for a long '
                                                                                               'time.',
                                                                                               'These symptoms do not '
                                                                                               'always mean something '
                                                                                               'serious has failed. '
                                                                                               'But they are good '
                                                                                               'reasons to check the '
                                                                                               'motorcycle before a '
                                                                                               'small issue becomes a '
                                                                                               'major repair.']},
                                                                               {'title': 'What We Check at Iron Custom '
                                                                                         'Motors',
                                                                                'paragraphs': ['At Iron Custom Motors, '
                                                                                               'an oil service on a '
                                                                                               'RevTech 110 or similar '
                                                                                               'V-twin is handled as a '
                                                                                               'mechanical inspection, '
                                                                                               'not just a fluid '
                                                                                               'replacement.',
                                                                                               'We check the engine, '
                                                                                               'gearbox and drive-side '
                                                                                               'areas as separate '
                                                                                               'systems. We verify the '
                                                                                               'correct lubricant '
                                                                                               'specification for the '
                                                                                               'actual build, inspect '
                                                                                               'drain plugs and '
                                                                                               'sealing parts, look '
                                                                                               'for signs of oil '
                                                                                               'contamination, check '
                                                                                               'for leaks and make '
                                                                                               'sure the motorcycle is '
                                                                                               'clean and safe before '
                                                                                               'it leaves the '
                                                                                               'workshop.',
                                                                                               'For custom '
                                                                                               'motorcycles, we also '
                                                                                               'pay attention to oil '
                                                                                               'line routing, heat '
                                                                                               'exposure, vibration '
                                                                                               'points, fastener '
                                                                                               'condition, corrosion '
                                                                                               'signs and whether the '
                                                                                               'setup makes sense as a '
                                                                                               'complete system. A '
                                                                                               'good service is not '
                                                                                               'only fresh oil. It is '
                                                                                               'a chance to read the '
                                                                                               'motorcycle.']},
                                                                               {'title': 'Conclusion',
                                                                                'paragraphs': ['Oil service on a '
                                                                                               'RevTech 110 or similar '
                                                                                               'Harley-style V-twin is '
                                                                                               'one of the '
                                                                                               'simplest-looking jobs '
                                                                                               'on the outside and one '
                                                                                               'of the most important '
                                                                                               'maintenance routines '
                                                                                               'for long-term '
                                                                                               'reliability.',
                                                                                               'The engine, gearbox '
                                                                                               'and drive-side '
                                                                                               'components all need '
                                                                                               'the right lubricant, '
                                                                                               'the right level and '
                                                                                               'the right inspection '
                                                                                               'approach. Done '
                                                                                               'properly, this service '
                                                                                               'helps protect the '
                                                                                               'bike, improve riding '
                                                                                               'feel and catch early '
                                                                                               'signs of wear before '
                                                                                               'they become expensive '
                                                                                               'problems.']}],
                                                                  'ctaText': 'If you ride a RevTech-powered custom '
                                                                             'bike, Harley-Davidson, or another big '
                                                                             'V-twin around Cascais or Lisbon, book an '
                                                                             'oil service or inspection at Iron Custom '
                                                                             'Motors. We will check the motorcycle as '
                                                                             'a complete system and explain what needs '
                                                                             'attention, what can wait, and what is '
                                                                             'worth preventing now.',
                                                                  'faqs': [{'q': 'Is oil service on a RevTech 110 the '
                                                                                 'same as on a Harley-Davidson?',
                                                                            'a': 'It can be similar in concept, but it '
                                                                                 'should not be treated as identical '
                                                                                 'without checking the actual engine, '
                                                                                 'gearbox and primary-drive '
                                                                                 'configuration.'},
                                                                           {'q': 'Can the same oil be used for engine, '
                                                                                 'gearbox and primary?',
                                                                            'a': 'Sometimes a lubricant may be '
                                                                                 'approved for multiple zones, but '
                                                                                 'this is not universal. The correct '
                                                                                 'oil depends on the specific engine, '
                                                                                 'transmission, clutch and primary '
                                                                                 'setup.'},
                                                                           {'q': 'Why change gearbox oil if the bike '
                                                                                 'shifts normally?',
                                                                            'a': 'Because wear and oil degradation can '
                                                                                 'build slowly. Fresh, correct oil '
                                                                                 'helps protect gears and bearings and '
                                                                                 'can improve shift feel.'},
                                                                           {'q': 'What happens if the primary or '
                                                                                 'drive-side oil is wrong?',
                                                                            'a': 'Depending on the setup, incorrect '
                                                                                 'lubricant or level can affect clutch '
                                                                                 'behavior, neutral selection, chain '
                                                                                 'lubrication, sealing and component '
                                                                                 'wear.'},
                                                                           {'q': 'How often should oil be changed on a '
                                                                                 'RevTech 110?',
                                                                            'a': 'The interval depends on the engine '
                                                                                 'specification, motorcycle '
                                                                                 'configuration, oil type, riding '
                                                                                 'conditions and manufacturer '
                                                                                 'recommendations.'}]},
                                                           'ru': {'eyebrow': 'Гайд мастерской · 17 июня 2026',
                                                                  'publishedLabel': 'Опубликовано 17 июня 2026',
                                                                  'breadHome': 'Главная',
                                                                  'breadBlog': 'Блог',
                                                                  'introTitle': 'Что входит в этот сервис',
                                                                  'videoEyebrow': 'Видео из мастерской',
                                                                  'videoTitle': 'Смотрите масляный сервис RevTech 110',
                                                                  'videoText': 'Короткий взгляд на сервис: моторное '
                                                                               'масло, масло коробки передач и смазка '
                                                                               'приводной зоны проверяются как '
                                                                               'отдельные механические системы.',
                                                                  'videoLink': 'Открыть на YouTube',
                                                                  'faqTitle': 'FAQ по сервису масла RevTech 110',
                                                                  'ctaEyebrow': 'Нужен такой сервис?',
                                                                  'ctaTitle': 'Запишитесь на замену масла или '
                                                                              'инспекцию.',
                                                                  'btnWA': 'WhatsApp',
                                                                  'btnBack': 'К блогу',
                                                                  'imageAlt': 'Обложка масляного сервиса RevTech 110 с '
                                                                              'кастомным V-twin мотоциклом в '
                                                                              'мастерской Iron Custom Motors.',
                                                                  'imageCaption': 'Масляный сервис RevTech 110 в Iron '
                                                                                  'Custom Motors: двигатель, коробка и '
                                                                                  'приводная зона рассматриваются как '
                                                                                  'отдельные системы.',
                                                                  'h1': 'Сервис масла RevTech 110:<br/><span '
                                                                        'class="accent">двигатель, коробка передач и '
                                                                        'привод.</span>',
                                                                  'h1Crumb': 'Сервис масла RevTech 110: двигатель, '
                                                                             'коробка передач и привод',
                                                                  'lede': 'Большой V-twin редко выходит из строя без '
                                                                          'предупреждения. Иногда признаки заметны '
                                                                          'сразу: передачи включаются грубее, мотор '
                                                                          'звучит механически жёстче, сцепление '
                                                                          'ощущается иначе, а слитое масло выглядит '
                                                                          'темнее и жиже, чем должно. Иногда явных '
                                                                          'симптомов нет вообще — просто мотоцикл '
                                                                          'ездил, грелся, остывал, стоял, снова '
                                                                          'запускался и постепенно работал на уставших '
                                                                          'жидкостях.',
                                                                  'intro': {'title': 'Что входит в этот сервис',
                                                                            'paragraphs': ['В этом коротком видео '
                                                                                           'показан масляный сервис '
                                                                                           'RevTech 110: масло '
                                                                                           'двигателя, масло коробки '
                                                                                           'передач и смазка зоны '
                                                                                           'привода. Для Harley-style '
                                                                                           'custom motorcycle это не '
                                                                                           'просто “замена масла”. Это '
                                                                                           'базовая проверка здоровья '
                                                                                           'трёх разных механических '
                                                                                           'зон, которые работают под '
                                                                                           'разными нагрузками.',
                                                                                           'Моторное масло борется с '
                                                                                           'температурой, продуктами '
                                                                                           'сгорания и внутренним '
                                                                                           'трением. Масло в коробке '
                                                                                           'защищает нагруженные '
                                                                                           'шестерни и подшипники. '
                                                                                           'Первичный привод или зона '
                                                                                           'привода, в зависимости от '
                                                                                           'конкретной сборки, '
                                                                                           'работает с цепью, '
                                                                                           'сцеплением и вращающимися '
                                                                                           'деталями. Считать всё это '
                                                                                           'одной и той же задачей — '
                                                                                           'частая ошибка.',
                                                                                           'В Iron Custom Motors мы '
                                                                                           'относимся к такому сервису '
                                                                                           'как к проверке системы, а '
                                                                                           'не просто как к операции '
                                                                                           '“слил-залил”.']},
                                                                  'sections': [{'title': 'Почему это важно',
                                                                                'paragraphs': ['В крупнообъёмном '
                                                                                               'воздушном или '
                                                                                               'воздушно-масляном '
                                                                                               'V-twin масло живёт '
                                                                                               'тяжёлой жизнью. '
                                                                                               'Большие поршни, '
                                                                                               'сильные импульсы, '
                                                                                               'высокая внутренняя '
                                                                                               'нагрузка и много тепла '
                                                                                               '— нормальная среда для '
                                                                                               'такого мотора. В '
                                                                                               'городском трафике '
                                                                                               'Лиссабона или Кашкайша '
                                                                                               'это тепло уходит не '
                                                                                               'сразу. Короткие '
                                                                                               'поездки, пробки и '
                                                                                               'влажность у океана '
                                                                                               'делают условия работы '
                                                                                               'сложнее, чем кажется '
                                                                                               'по сухому регламенту.',
                                                                                               'Свежее масло не только '
                                                                                               'уменьшает трение. Оно '
                                                                                               'помогает отводить '
                                                                                               'тепло от важных '
                                                                                               'деталей, удерживает '
                                                                                               'загрязнения во взвеси, '
                                                                                               'защищает металл и '
                                                                                               'поддерживает '
                                                                                               'правильную масляную '
                                                                                               'плёнку. Когда масло '
                                                                                               'старое, загрязнённое, '
                                                                                               'разбавленное или '
                                                                                               'просто неподходящее, '
                                                                                               'мотоцикл может '
                                                                                               'продолжать ехать — но '
                                                                                               'запас защиты '
                                                                                               'становится меньше.',
                                                                                               'У коробки передач '
                                                                                               'другая задача. В ней '
                                                                                               'нет продуктов '
                                                                                               'сгорания, зато есть '
                                                                                               'высокое давление между '
                                                                                               'зубьями шестерён и '
                                                                                               'ударные нагрузки при '
                                                                                               'каждом открытии и '
                                                                                               'закрытии газа. Старое '
                                                                                               'или неправильное масло '
                                                                                               'может сделать '
                                                                                               'переключения тяжелее, '
                                                                                               'ускорить износ '
                                                                                               'шестерён и подшипников '
                                                                                               'и скрыть мелкую '
                                                                                               'проблему до того '
                                                                                               'момента, когда она '
                                                                                               'станет дорогой.',
                                                                                               'С зоной привода всё '
                                                                                               'ещё тоньше. На многих '
                                                                                               'Harley-style '
                                                                                               'мотоциклах ременной '
                                                                                               'final drive сам по '
                                                                                               'себе не заполнен '
                                                                                               'маслом. Обычно '
                                                                                               'масляный сервис '
                                                                                               'касается primary drive '
                                                                                               'или трансмиссионных '
                                                                                               'зон, связанных со '
                                                                                               'смазкой. На кастомном '
                                                                                               'мотоцикле, особенно с '
                                                                                               'aftermarket engine '
                                                                                               'вроде RevTech, '
                                                                                               'конкретную '
                                                                                               'конфигурацию нужно '
                                                                                               'подтвердить до выбора '
                                                                                               'масла, объёма и '
                                                                                               'процедуры.']},
                                                                               {'title': 'Основное техническое '
                                                                                         'объяснение',
                                                                                'paragraphs': ['Моторное масло — самая '
                                                                                               'очевидная часть '
                                                                                               'сервиса, но именно её '
                                                                                               'часто упрощают слишком '
                                                                                               'сильно. В RevTech 110 '
                                                                                               'или похожем большом '
                                                                                               'V-twin масло работает '
                                                                                               'при высокой '
                                                                                               'температурной и '
                                                                                               'механической нагрузке. '
                                                                                               'Оно защищает '
                                                                                               'подшипники, поршни, '
                                                                                               'стенки цилиндров, '
                                                                                               'компоненты ГРМ и '
                                                                                               'другие внутренние '
                                                                                               'детали, одновременно '
                                                                                               'уводя загрязнения от '
                                                                                               'рабочих поверхностей.',
                                                                                               'Со временем масло '
                                                                                               'теряет часть защитных '
                                                                                               'свойств. Оно '
                                                                                               'окисляется, может '
                                                                                               'накапливать следы '
                                                                                               'топлива, удерживать '
                                                                                               'микроскопические '
                                                                                               'металлические частицы '
                                                                                               'и хуже переносить '
                                                                                               'высокую температуру. '
                                                                                               'Поэтому сервис '
                                                                                               'двигателя — это не '
                                                                                               'только свежее масло. '
                                                                                               'Нужно оценить '
                                                                                               'состояние слитого '
                                                                                               'масла, проверить зону '
                                                                                               'фильтра, осмотреть '
                                                                                               'возможные подтёки и '
                                                                                               'убедиться, что нет '
                                                                                               'признаков миграции '
                                                                                               'масла, перелива или '
                                                                                               'внешнего загрязнения.',
                                                                                               'Процедура проверки '
                                                                                               'уровня зависит от '
                                                                                               'маслобака, рамы, '
                                                                                               'конфигурации двигателя '
                                                                                               'и даже от того, '
                                                                                               'проверяется ли '
                                                                                               'мотоцикл горячим или '
                                                                                               'холодным, вертикально '
                                                                                               'или на боковой '
                                                                                               'подножке. '
                                                                                               'Универсальных цифр '
                                                                                               'здесь быть не должно: '
                                                                                               'нужен правильный '
                                                                                               'manual под конкретную '
                                                                                               'сборку.',
                                                                                               'Коробка передач живёт '
                                                                                               'иначе, чем двигатель. '
                                                                                               'Она не видит продуктов '
                                                                                               'сгорания, но постоянно '
                                                                                               'работает с давлением '
                                                                                               'между зубьями шестерён '
                                                                                               'и нагрузками при смене '
                                                                                               'тяги. Когда масло в '
                                                                                               'коробке старое или '
                                                                                               'загрязнённое, райдер '
                                                                                               'может почувствовать '
                                                                                               'более тяжёлое '
                                                                                               'переключение, лишний '
                                                                                               'механический шум, '
                                                                                               'менее точный ход лапки '
                                                                                               'или трудности с '
                                                                                               'поиском нейтрали.',
                                                                                               'Фраза “final drive” '
                                                                                               'зависит от конструкции '
                                                                                               'мотоцикла. На многих '
                                                                                               'Harley-style байках '
                                                                                               'ременной финальный '
                                                                                               'привод не имеет '
                                                                                               'масляной ванны. Чаще '
                                                                                               'речь идёт о primary '
                                                                                               'drive или смазке '
                                                                                               'отдельных '
                                                                                               'трансмиссионных зон. '
                                                                                               'Поэтому перед сервисом '
                                                                                               'нужно понимать, что '
                                                                                               'именно установлено на '
                                                                                               'конкретном '
                                                                                               'мотоцикле.']},
                                                                               {'title': 'Нюансы мастерской, которые '
                                                                                         'часто пропускают',
                                                                                'bullets': ['Три масляные зоны не '
                                                                                            'всегда требуют одного и '
                                                                                            'того же масла. Двигатель, '
                                                                                            'коробка и зона сцепления '
                                                                                            'или primary имеют разные '
                                                                                            'механические задачи. '
                                                                                            'Правильный выбор зависит '
                                                                                            'от реально установленных '
                                                                                            'компонентов.',
                                                                                            '“Заводится и едет” не '
                                                                                            'означает, что масло ещё '
                                                                                            'здоровое. Большой V-twin '
                                                                                            'может уверенно тянуть '
                                                                                            'даже на старом масле, но '
                                                                                            'запас защиты уже может '
                                                                                            'быть снижен.',
                                                                                            'Состояние сливной пробки '
                                                                                            '— это информация. Лёгкая '
                                                                                            'металлическая паста может '
                                                                                            'быть обычным следом '
                                                                                            'износа. Стружка, хлопья '
                                                                                            'или необычно большое '
                                                                                            'количество металла — '
                                                                                            'повод превратить замену '
                                                                                            'масла в диагностику.',
                                                                                            'Климат побережья имеет '
                                                                                            'значение. В Кашкайше и '
                                                                                            'Лиссабоне влажность и '
                                                                                            'морской воздух ускоряют '
                                                                                            'коррозию крепежа, '
                                                                                            'контактов, открытого '
                                                                                            'металла и уплотнительных '
                                                                                            'поверхностей.',
                                                                                            'Кастомные сборки нужно '
                                                                                            'перепроверять. Мотоцикл с '
                                                                                            'RevTech может объединять '
                                                                                            'aftermarket двигатель, '
                                                                                            'раму, маслобак, шланги, '
                                                                                            'фитинги, коробку, '
                                                                                            'primary-компоненты и '
                                                                                            'нестандартный выхлоп. '
                                                                                            'После сервиса такой байк '
                                                                                            'нужно смотреть как единую '
                                                                                            'систему.']},
                                                                               {'title': 'Типичные ошибки',
                                                                                'bullets': ['Относиться к крупному '
                                                                                            'кастомному V-twin как к '
                                                                                            'обычному универсальному '
                                                                                            'мотоциклу.',
                                                                                            'Менять только моторное '
                                                                                            'масло и забывать про '
                                                                                            'коробку или primary-drive '
                                                                                            'lubricant.',
                                                                                            'Брать универсальные цифры '
                                                                                            'из интернета вместо '
                                                                                            'документации по '
                                                                                            'конкретному двигателю и '
                                                                                            'компонентам.',
                                                                                            'Переливать масло. Больше '
                                                                                            'масла — не значит '
                                                                                            'безопаснее. В некоторых '
                                                                                            'узлах это приводит к '
                                                                                            'подтёкам, проблемам '
                                                                                            'сцепления или грязной '
                                                                                            'работе вентиляции.',
                                                                                            'Игнорировать небольшие '
                                                                                            'следы масла после '
                                                                                            'сервиса. Маленькое пятно '
                                                                                            'может быть простой '
                                                                                            'проблемой O-ring, а может '
                                                                                            'указывать на '
                                                                                            'уплотнительную '
                                                                                            'поверхность, шланг, '
                                                                                            'фитинг или вентиляцию.']},
                                                                               {'title': 'Когда стоит обратиться в '
                                                                                         'мастерскую',
                                                                                'paragraphs': ['Запишитесь на '
                                                                                               'проверку, если '
                                                                                               'передачи стали '
                                                                                               'включаться тяжелее или '
                                                                                               'менее точно, нейтраль '
                                                                                               'ищется хуже, сцепление '
                                                                                               'начало “тянуть”, мотор '
                                                                                               'звучит жёстче '
                                                                                               'обычного, после '
                                                                                               'поездки появились '
                                                                                               'подтёки, масло пахнет '
                                                                                               'горелым или выглядит '
                                                                                               'необычно загрязнённым, '
                                                                                               'на сливной пробке '
                                                                                               'видны металлические '
                                                                                               'частицы, или мотоцикл '
                                                                                               'долго стоял без '
                                                                                               'обслуживания.',
                                                                                               'Эти признаки не всегда '
                                                                                               'означают серьёзную '
                                                                                               'поломку. Но это '
                                                                                               'хороший повод '
                                                                                               'проверить мотоцикл до '
                                                                                               'того, как маленькая '
                                                                                               'проблема станет '
                                                                                               'большим ремонтом.']},
                                                                               {'title': 'Что мы проверяем в Iron '
                                                                                         'Custom Motors',
                                                                                'paragraphs': ['В Iron Custom Motors '
                                                                                               'масляный сервис '
                                                                                               'RevTech 110 или '
                                                                                               'похожего V-twin — это '
                                                                                               'механическая '
                                                                                               'инспекция, а не просто '
                                                                                               'замена жидкостей.',
                                                                                               'Мы рассматриваем '
                                                                                               'двигатель, коробку и '
                                                                                               'приводную зону как '
                                                                                               'отдельные системы. '
                                                                                               'Проверяем правильную '
                                                                                               'спецификацию масла для '
                                                                                               'конкретной сборки, '
                                                                                               'осматриваем сливные '
                                                                                               'пробки и уплотнения, '
                                                                                               'ищем признаки '
                                                                                               'загрязнения, проверяем '
                                                                                               'подтёки и убеждаемся, '
                                                                                               'что мотоцикл чистый и '
                                                                                               'безопасный перед '
                                                                                               'выдачей.',
                                                                                               'Для кастомных '
                                                                                               'мотоциклов мы также '
                                                                                               'смотрим прокладку '
                                                                                               'масляных линий, зоны '
                                                                                               'нагрева, точки '
                                                                                               'вибрации, состояние '
                                                                                               'крепежа, признаки '
                                                                                               'коррозии и общую '
                                                                                               'логику сборки. Хороший '
                                                                                               'сервис — это не только '
                                                                                               'свежее масло. Это '
                                                                                               'возможность прочитать '
                                                                                               'мотоцикл.']},
                                                                               {'title': 'Вывод',
                                                                                'paragraphs': ['Масляный сервис '
                                                                                               'RevTech 110 или '
                                                                                               'похожего Harley-style '
                                                                                               'V-twin снаружи '
                                                                                               'выглядит простой '
                                                                                               'работой, но для долгой '
                                                                                               'и надёжной жизни '
                                                                                               'мотоцикла это одна из '
                                                                                               'ключевых процедур.',
                                                                                               'Двигатель, коробка и '
                                                                                               'зона привода требуют '
                                                                                               'правильной смазки, '
                                                                                               'правильного уровня и '
                                                                                               'правильного подхода к '
                                                                                               'осмотру. Если всё '
                                                                                               'сделано грамотно, '
                                                                                               'сервис помогает '
                                                                                               'защитить мотоцикл, '
                                                                                               'улучшить ощущение от '
                                                                                               'езды и поймать ранние '
                                                                                               'признаки износа до '
                                                                                               'дорогого ремонта.']}],
                                                                  'ctaText': 'Если вы ездите на кастомном мотоцикле с '
                                                                             'RevTech, Harley-Davidson или другом '
                                                                             'большом V-twin в районе Cascais или '
                                                                             'Lisbon, запишитесь на масляный сервис '
                                                                             'или инспекцию в Iron Custom Motors. Мы '
                                                                             'проверим мотоцикл как систему и спокойно '
                                                                             'объясним, что требует внимания, что '
                                                                             'может подождать, а что лучше '
                                                                             'предотвратить сейчас.',
                                                                  'faqs': [{'q': 'Замена масла на RevTech 110 такая '
                                                                                 'же, как на Harley-Davidson?',
                                                                            'a': 'По логике она может быть похожей, но '
                                                                                 'не должна считаться идентичной без '
                                                                                 'проверки двигателя, коробки и '
                                                                                 'primary-drive конфигурации '
                                                                                 'конкретного мотоцикла.'},
                                                                           {'q': 'Можно ли использовать одно масло для '
                                                                                 'двигателя, коробки и primary?',
                                                                            'a': 'Иногда продукт может быть допущен '
                                                                                 'для нескольких зон, но это не '
                                                                                 'универсальное правило. Всё зависит '
                                                                                 'от двигателя, коробки, сцепления и '
                                                                                 'primary setup.'},
                                                                           {'q': 'Зачем менять масло в коробке, если '
                                                                                 'передачи включаются нормально?',
                                                                            'a': 'Потому что износ и деградация масла '
                                                                                 'накапливаются постепенно. Свежее '
                                                                                 'правильное масло помогает защищать '
                                                                                 'шестерни и подшипники и может '
                                                                                 'улучшить ощущение переключений.'},
                                                                           {'q': 'Что будет, если в primary или зоне '
                                                                                 'привода неправильное масло?',
                                                                            'a': 'В зависимости от конструкции это '
                                                                                 'может повлиять на работу сцепления, '
                                                                                 'поиск нейтрали, смазку цепи, '
                                                                                 'уплотнения и износ деталей.'},
                                                                           {'q': 'Как часто менять масло на RevTech '
                                                                                 '110?',
                                                                            'a': 'Интервал зависит от спецификации '
                                                                                 'двигателя, конфигурации мотоцикла, '
                                                                                 'типа масла, условий езды и '
                                                                                 'рекомендаций производителя.'}]},
                                                           'pt': {'eyebrow': 'Guia da oficina · 17 de junho de 2026',
                                                                  'publishedLabel': 'Publicado em 17 de junho de 2026',
                                                                  'breadHome': 'Início',
                                                                  'breadBlog': 'Blog',
                                                                  'introTitle': 'O que este serviço inclui',
                                                                  'videoEyebrow': 'Vídeo da oficina',
                                                                  'videoTitle': 'Veja o serviço de óleo RevTech 110',
                                                                  'videoText': 'Um olhar curto sobre o serviço: óleo '
                                                                               'do motor, óleo da caixa e lubrificação '
                                                                               'da zona de transmissão verificados '
                                                                               'como sistemas mecânicos separados.',
                                                                  'videoLink': 'Abrir no YouTube',
                                                                  'faqTitle': 'FAQ sobre serviço de óleo RevTech 110',
                                                                  'ctaEyebrow': 'Precisa deste serviço?',
                                                                  'ctaTitle': 'Marque um serviço de óleo ou inspeção.',
                                                                  'btnWA': 'WhatsApp',
                                                                  'btnBack': 'Voltar ao blog',
                                                                  'imageAlt': 'Imagem de capa do serviço de óleo '
                                                                              'RevTech 110 com uma moto custom V-twin '
                                                                              'na oficina Iron Custom Motors.',
                                                                  'imageCaption': 'Serviço de óleo RevTech 110 na Iron '
                                                                                  'Custom Motors: motor, caixa e zona '
                                                                                  'de transmissão tratados como '
                                                                                  'sistemas separados.',
                                                                  'h1': 'Serviço de Óleo RevTech 110:<br/><span '
                                                                        'class="accent">Motor, Caixa de Velocidades e '
                                                                        'Transmissão.</span>',
                                                                  'h1Crumb': 'Serviço de Óleo RevTech 110: Motor, '
                                                                             'Caixa de Velocidades e Transmissão',
                                                                  'lede': 'Um grande V-twin raramente falha sem dar '
                                                                          'pequenos avisos primeiro. Às vezes os '
                                                                          'sinais são claros: mudanças mais duras, '
                                                                          'mais ruído mecânico do que o normal, uma '
                                                                          'embraiagem com sensação diferente, ou óleo '
                                                                          'que sai mais escuro e mais fino do que '
                                                                          'deveria. Outras vezes não há um sintoma '
                                                                          'evidente — apenas uma moto que rodou, '
                                                                          'aqueceu, arrefeceu, ficou parada, voltou a '
                                                                          'arrancar e continuou a trabalhar com '
                                                                          'fluidos já cansados.',
                                                                  'intro': {'title': 'O que este serviço inclui',
                                                                            'paragraphs': ['Este vídeo curto mostra um '
                                                                                           'serviço de óleo num '
                                                                                           'conjunto RevTech 110: óleo '
                                                                                           'do motor, óleo da caixa de '
                                                                                           'velocidades e lubrificação '
                                                                                           'da zona de transmissão. '
                                                                                           'Neste tipo de custom '
                                                                                           'motorcycle ao estilo '
                                                                                           'Harley, isto não é apenas '
                                                                                           '“mudar o óleo”. É uma '
                                                                                           'verificação básica da '
                                                                                           'saúde de três zonas '
                                                                                           'mecânicas diferentes, que '
                                                                                           'trabalham sob cargas muito '
                                                                                           'diferentes.',
                                                                                           'O óleo do motor lida com '
                                                                                           'calor, subprodutos da '
                                                                                           'combustão e atrito '
                                                                                           'interno. O óleo da caixa '
                                                                                           'protege engrenagens e '
                                                                                           'rolamentos sob carga. A '
                                                                                           'lubrificação da primária '
                                                                                           'ou da zona de transmissão, '
                                                                                           'dependendo da configuração '
                                                                                           'exata, pode trabalhar com '
                                                                                           'corrente, embraiagem e '
                                                                                           'componentes em rotação. '
                                                                                           'Tratar tudo como se fosse '
                                                                                           'a mesma coisa é um erro '
                                                                                           'comum.',
                                                                                           'Na Iron Custom Motors, '
                                                                                           'olhamos para este serviço '
                                                                                           'como uma verificação de '
                                                                                           'sistema — não apenas como '
                                                                                           'um simples “drenar e '
                                                                                           'encher”.']},
                                                                  'sections': [{'title': 'Porque é importante',
                                                                                'paragraphs': ['Num V-twin de grande '
                                                                                               'cilindrada, arrefecido '
                                                                                               'a ar ou a ar/óleo, o '
                                                                                               'óleo tem uma vida '
                                                                                               'difícil. O motor '
                                                                                               'trabalha com pistões '
                                                                                               'grandes, pulsações '
                                                                                               'fortes, cargas '
                                                                                               'internas elevadas e '
                                                                                               'muito calor. No '
                                                                                               'trânsito urbano de '
                                                                                               'Lisboa ou Cascais, '
                                                                                               'esse calor não '
                                                                                               'desaparece '
                                                                                               'rapidamente. Percursos '
                                                                                               'curtos, para-arranca e '
                                                                                               'humidade costeira '
                                                                                               'tornam o ambiente de '
                                                                                               'serviço mais exigente '
                                                                                               'do que parece no '
                                                                                               'papel.',
                                                                                               'O óleo novo faz mais '
                                                                                               'do que reduzir atrito. '
                                                                                               'Ajuda a remover calor '
                                                                                               'de zonas críticas, '
                                                                                               'mantém contaminantes '
                                                                                               'em suspensão, protege '
                                                                                               'superfícies metálicas '
                                                                                               'e conserva a película '
                                                                                               'lubrificante correta. '
                                                                                               'Quando o óleo está '
                                                                                               'velho, contaminado, '
                                                                                               'diluído ou '
                                                                                               'simplesmente errado '
                                                                                               'para a aplicação, a '
                                                                                               'moto pode continuar a '
                                                                                               'funcionar — mas a '
                                                                                               'margem de proteção '
                                                                                               'fica menor.',
                                                                                               'A caixa de velocidades '
                                                                                               'tem outro tipo de '
                                                                                               'esforço. Não lida com '
                                                                                               'combustão, mas lida '
                                                                                               'com alta pressão entre '
                                                                                               'dentes de engrenagens '
                                                                                               'e cargas de choque '
                                                                                               'sempre que o piloto '
                                                                                               'abre ou fecha o '
                                                                                               'acelerador. Óleo velho '
                                                                                               'ou incorreto na caixa '
                                                                                               'pode tornar as '
                                                                                               'mudanças mais pesadas, '
                                                                                               'aumentar o desgaste de '
                                                                                               'engrenagens e '
                                                                                               'rolamentos e tornar '
                                                                                               'pequenos problemas '
                                                                                               'internos mais difíceis '
                                                                                               'de detetar cedo.',
                                                                                               'A zona de transmissão '
                                                                                               'exige ainda mais '
                                                                                               'atenção. Em muitas '
                                                                                               'motos ao estilo '
                                                                                               'Harley, a transmissão '
                                                                                               'final por correia não '
                                                                                               'tem banho de óleo. '
                                                                                               'Normalmente, o serviço '
                                                                                               'de óleo refere-se à '
                                                                                               'transmissão primária '
                                                                                               'ou a zonas '
                                                                                               'lubrificadas '
                                                                                               'relacionadas com a '
                                                                                               'transmissão. Numa moto '
                                                                                               'custom, especialmente '
                                                                                               'com um motor '
                                                                                               'aftermarket como o '
                                                                                               'RevTech, a '
                                                                                               'configuração exata '
                                                                                               'deve ser confirmada '
                                                                                               'antes de escolher '
                                                                                               'óleo, quantidade ou '
                                                                                               'procedimento.']},
                                                                               {'title': 'Explicação técnica principal',
                                                                                'paragraphs': ['O óleo do motor é a '
                                                                                               'parte mais evidente do '
                                                                                               'serviço, mas também a '
                                                                                               'mais fácil de '
                                                                                               'simplificar em '
                                                                                               'excesso. Num RevTech '
                                                                                               '110 ou num V-twin '
                                                                                               'grande semelhante, o '
                                                                                               'óleo trabalha sob '
                                                                                               'elevada carga térmica '
                                                                                               'e mecânica. Tem de '
                                                                                               'proteger rolamentos, '
                                                                                               'pistões, paredes dos '
                                                                                               'cilindros, componentes '
                                                                                               'de comando e outras '
                                                                                               'peças internas, ao '
                                                                                               'mesmo tempo que '
                                                                                               'transporta '
                                                                                               'contaminantes para '
                                                                                               'longe das superfícies '
                                                                                               'de trabalho.',
                                                                                               'Com o tempo, o óleo '
                                                                                               'perde parte das suas '
                                                                                               'propriedades de '
                                                                                               'proteção. Pode oxidar, '
                                                                                               'acumular diluição por '
                                                                                               'combustível, reter '
                                                                                               'partículas metálicas '
                                                                                               'microscópicas e '
                                                                                               'tornar-se menos '
                                                                                               'estável com o calor. '
                                                                                               'Por isso, um serviço '
                                                                                               'de óleo do motor deve '
                                                                                               'incluir também a '
                                                                                               'observação do óleo '
                                                                                               'drenado, a verificação '
                                                                                               'da zona do filtro, a '
                                                                                               'inspeção de fugas e a '
                                                                                               'confirmação de que não '
                                                                                               'existem sinais de '
                                                                                               'migração de óleo, '
                                                                                               'excesso de enchimento '
                                                                                               'ou contaminação '
                                                                                               'externa.',
                                                                                               'O nível de óleo e o '
                                                                                               'procedimento de '
                                                                                               'verificação podem '
                                                                                               'mudar conforme o '
                                                                                               'depósito de óleo, '
                                                                                               'quadro, configuração '
                                                                                               'do motor e se a moto é '
                                                                                               'verificada quente, '
                                                                                               'fria, na vertical ou '
                                                                                               'apoiada no descanso '
                                                                                               'lateral. Não existe um '
                                                                                               'número universal que '
                                                                                               'deva ser seguido sem o '
                                                                                               'manual correto.',
                                                                                               'A caixa de velocidades '
                                                                                               'vive uma realidade '
                                                                                               'diferente da do motor. '
                                                                                               'Não recebe gases de '
                                                                                               'combustão, mas suporta '
                                                                                               'alta pressão entre '
                                                                                               'engrenagens e '
                                                                                               'variações de carga '
                                                                                               'sempre que o piloto '
                                                                                               'altera a entrega de '
                                                                                               'potência. Quando o '
                                                                                               'óleo da caixa '
                                                                                               'envelhece ou fica '
                                                                                               'contaminado, o piloto '
                                                                                               'pode notar mudanças '
                                                                                               'mais duras, mais ruído '
                                                                                               'mecânico, menos '
                                                                                               'precisão na alavanca '
                                                                                               'ou dificuldade em '
                                                                                               'encontrar o '
                                                                                               'ponto-morto.',
                                                                                               'A expressão '
                                                                                               '“transmissão final” '
                                                                                               'pode significar coisas '
                                                                                               'diferentes conforme a '
                                                                                               'construção da moto. Em '
                                                                                               'muitas motos ao estilo '
                                                                                               'Harley, a correia '
                                                                                               'final não é '
                                                                                               'lubrificada por óleo. '
                                                                                               'Normalmente fala-se da '
                                                                                               'primária ou de zonas '
                                                                                               'lubrificadas da '
                                                                                               'transmissão. A '
                                                                                               'configuração real tem '
                                                                                               'de ser confirmada '
                                                                                               'antes de decidir óleo, '
                                                                                               'quantidade ou '
                                                                                               'procedimento.']},
                                                                               {'title': 'Nuances de oficina que '
                                                                                         'muitos pilotos não veem',
                                                                                'bullets': ['Três zonas de óleo nem '
                                                                                            'sempre pedem o mesmo '
                                                                                            'lubrificante. Motor, '
                                                                                            'caixa e zona da '
                                                                                            'embraiagem ou primária '
                                                                                            'têm necessidades '
                                                                                            'mecânicas diferentes. A '
                                                                                            'escolha correta depende '
                                                                                            'dos componentes realmente '
                                                                                            'instalados na moto.',
                                                                                            '“Arranca e anda” não '
                                                                                            'significa que o óleo '
                                                                                            'esteja saudável. Um '
                                                                                            'grande V-twin pode '
                                                                                            'continuar a puxar bem com '
                                                                                            'óleo velho, mas a margem '
                                                                                            'de proteção pode já estar '
                                                                                            'reduzida.',
                                                                                            'Os resíduos no bujão de '
                                                                                            'drenagem são informação. '
                                                                                            'Uma pasta metálica fina '
                                                                                            'pode ser desgaste normal. '
                                                                                            'Limalhas, flocos ou '
                                                                                            'excesso de metal '
                                                                                            'significam que o serviço '
                                                                                            'deve passar a inspeção.',
                                                                                            'O clima costeiro importa. '
                                                                                            'Em Cascais e Lisboa, a '
                                                                                            'humidade e o ar marítimo '
                                                                                            'aceleram a corrosão em '
                                                                                            'parafusos, fichas '
                                                                                            'elétricas, metal exposto '
                                                                                            'e superfícies de vedação.',
                                                                                            'As motos custom precisam '
                                                                                            'de nova verificação. Uma '
                                                                                            'moto com motor RevTech '
                                                                                            'pode combinar motor, '
                                                                                            'quadro, depósito de óleo, '
                                                                                            'mangueiras, ligações, '
                                                                                            'caixa, primária e escape '
                                                                                            'aftermarket. Depois do '
                                                                                            'serviço, a moto deve ser '
                                                                                            'verificada como um '
                                                                                            'sistema completo.']},
                                                                               {'title': 'Erros comuns',
                                                                                'bullets': ['Tratar um V-twin custom '
                                                                                            'de grande cilindrada como '
                                                                                            'se fosse uma moto '
                                                                                            'genérica.',
                                                                                            'Mudar apenas o óleo do '
                                                                                            'motor e esquecer o óleo '
                                                                                            'da caixa ou da primária.',
                                                                                            'Usar números universais '
                                                                                            'encontrados na internet '
                                                                                            'em vez da documentação '
                                                                                            'correta.',
                                                                                            'Encher óleo em excesso. '
                                                                                            'Mais óleo não é '
                                                                                            'automaticamente mais '
                                                                                            'seguro e pode causar '
                                                                                            'fugas, problemas de '
                                                                                            'embraiagem ou '
                                                                                            'comportamento sujo da '
                                                                                            'ventilação.',
                                                                                            'Ignorar pequenas fugas '
                                                                                            'depois do serviço. Uma '
                                                                                            'pequena marca de óleo '
                                                                                            'pode ser apenas um '
                                                                                            'O-ring, mas também pode '
                                                                                            'indicar uma superfície de '
                                                                                            'vedação, mangueira, '
                                                                                            'ligação ou ventilação que '
                                                                                            'precisa de atenção.']},
                                                                               {'title': 'Quando visitar uma oficina',
                                                                                'paragraphs': ['Marque uma inspeção se '
                                                                                               'as mudanças ficarem '
                                                                                               'mais pesadas ou menos '
                                                                                               'precisas, se for mais '
                                                                                               'difícil encontrar '
                                                                                               'ponto-morto, se a '
                                                                                               'embraiagem começar a '
                                                                                               'arrastar, se o motor '
                                                                                               'soar mais áspero do '
                                                                                               'que o normal, se '
                                                                                               'aparecerem fugas de '
                                                                                               'óleo depois de rodar, '
                                                                                               'se o óleo cheirar a '
                                                                                               'queimado ou parecer '
                                                                                               'muito contaminado, se '
                                                                                               'houver partículas '
                                                                                               'metálicas visíveis no '
                                                                                               'bujão, ou se a moto '
                                                                                               'esteve parada durante '
                                                                                               'muito tempo.',
                                                                                               'Estes sintomas nem '
                                                                                               'sempre significam uma '
                                                                                               'avaria grave. Mas são '
                                                                                               'boas razões para '
                                                                                               'verificar a moto antes '
                                                                                               'de um pequeno problema '
                                                                                               'se tornar uma '
                                                                                               'reparação cara.']},
                                                                               {'title': 'O que verificamos na Iron '
                                                                                         'Custom Motors',
                                                                                'paragraphs': ['Na Iron Custom Motors, '
                                                                                               'um serviço de óleo num '
                                                                                               'RevTech 110 ou num '
                                                                                               'V-twin semelhante é '
                                                                                               'tratado como uma '
                                                                                               'inspeção mecânica, não '
                                                                                               'apenas como '
                                                                                               'substituição de '
                                                                                               'fluido.',
                                                                                               'Verificamos motor, '
                                                                                               'caixa e zona de '
                                                                                               'transmissão como '
                                                                                               'sistemas separados. '
                                                                                               'Confirmamos a '
                                                                                               'especificação correta '
                                                                                               'de lubrificante para a '
                                                                                               'configuração real, '
                                                                                               'inspecionamos bujões e '
                                                                                               'vedantes, procuramos '
                                                                                               'sinais de '
                                                                                               'contaminação, '
                                                                                               'verificamos fugas e '
                                                                                               'garantimos que a moto '
                                                                                               'sai limpa e segura da '
                                                                                               'oficina.',
                                                                                               'Em motos custom, '
                                                                                               'também observamos '
                                                                                               'passagem das linhas de '
                                                                                               'óleo, exposição ao '
                                                                                               'calor, pontos de '
                                                                                               'vibração, estado dos '
                                                                                               'fixadores, sinais de '
                                                                                               'corrosão e se o '
                                                                                               'conjunto faz sentido '
                                                                                               'como sistema completo. '
                                                                                               'Um bom serviço não é '
                                                                                               'só óleo novo. É uma '
                                                                                               'oportunidade para ler '
                                                                                               'a moto.']},
                                                                               {'title': 'Conclusão',
                                                                                'paragraphs': ['O serviço de óleo num '
                                                                                               'RevTech 110 ou num '
                                                                                               'V-twin ao estilo '
                                                                                               'Harley parece uma '
                                                                                               'tarefa simples por '
                                                                                               'fora, mas é uma das '
                                                                                               'rotinas mais '
                                                                                               'importantes para a '
                                                                                               'fiabilidade a longo '
                                                                                               'prazo.',
                                                                                               'Motor, caixa e zonas '
                                                                                               'de transmissão '
                                                                                               'precisam do '
                                                                                               'lubrificante certo, do '
                                                                                               'nível certo e da '
                                                                                               'abordagem correta de '
                                                                                               'inspeção. Quando feito '
                                                                                               'corretamente, este '
                                                                                               'serviço protege a '
                                                                                               'moto, melhora a '
                                                                                               'sensação de condução e '
                                                                                               'ajuda a detetar sinais '
                                                                                               'iniciais de desgaste '
                                                                                               'antes de se tornarem '
                                                                                               'problemas caros.']}],
                                                                  'ctaText': 'Se conduz uma custom com motor RevTech, '
                                                                             'uma Harley-Davidson ou outro grande '
                                                                             'V-twin em Cascais ou Lisboa, marque um '
                                                                             'serviço de óleo ou uma inspeção na Iron '
                                                                             'Custom Motors. Vamos verificar a moto '
                                                                             'como um sistema completo e explicar o '
                                                                             'que precisa de atenção, o que pode '
                                                                             'esperar e o que vale a pena prevenir '
                                                                             'agora.',
                                                                  'faqs': [{'q': 'O serviço de óleo num RevTech 110 é '
                                                                                 'igual ao de uma Harley-Davidson?',
                                                                            'a': 'Pode ser semelhante no conceito, mas '
                                                                                 'não deve ser tratado como idêntico '
                                                                                 'sem verificar motor, caixa e '
                                                                                 'configuração da primária da moto '
                                                                                 'específica.'},
                                                                           {'q': 'Pode usar-se o mesmo óleo no motor, '
                                                                                 'caixa e primária?',
                                                                            'a': 'Às vezes um lubrificante pode ser '
                                                                                 'aprovado para várias zonas, mas isso '
                                                                                 'não é uma regra universal. Depende '
                                                                                 'do motor, transmissão, embraiagem e '
                                                                                 'configuração da primária.'},
                                                                           {'q': 'Porque mudar o óleo da caixa se as '
                                                                                 'mudanças entram normalmente?',
                                                                            'a': 'Porque o desgaste e a degradação do '
                                                                                 'óleo acumulam-se gradualmente. Óleo '
                                                                                 'correto e novo ajuda a proteger '
                                                                                 'engrenagens e rolamentos e pode '
                                                                                 'melhorar a sensação das mudanças.'},
                                                                           {'q': 'O que acontece se o óleo da primária '
                                                                                 'ou da transmissão estiver errado?',
                                                                            'a': 'Dependendo da configuração, pode '
                                                                                 'afetar a embraiagem, a seleção do '
                                                                                 'ponto-morto, a lubrificação da '
                                                                                 'corrente, vedantes e desgaste de '
                                                                                 'componentes.'},
                                                                           {'q': 'Com que frequência deve ser mudado o '
                                                                                 'óleo num RevTech 110?',
                                                                            'a': 'O intervalo depende da especificação '
                                                                                 'do motor, configuração da moto, tipo '
                                                                                 'de óleo, condições de condução e '
                                                                                 'recomendações do fabricante.'}]},
                                                           'uk': {'eyebrow': 'Гайд майстерні · 17 червня 2026',
                                                                  'publishedLabel': 'Опубліковано 17 червня 2026',
                                                                  'breadHome': 'Головна',
                                                                  'breadBlog': 'Блог',
                                                                  'introTitle': 'Що входить у цей сервіс',
                                                                  'videoEyebrow': 'Відео з майстерні',
                                                                  'videoTitle': 'Дивіться сервіс оливи RevTech 110',
                                                                  'videoText': 'Короткий погляд на сервіс: моторна '
                                                                               'олива, олива коробки передач і '
                                                                               'змащення зони приводу перевіряються як '
                                                                               'окремі механічні системи.',
                                                                  'videoLink': 'Відкрити на YouTube',
                                                                  'faqTitle': 'FAQ щодо сервісу оливи RevTech 110',
                                                                  'ctaEyebrow': 'Потрібен такий сервіс?',
                                                                  'ctaTitle': 'Запишіться на сервіс оливи або '
                                                                              'інспекцію.',
                                                                  'btnWA': 'WhatsApp',
                                                                  'btnBack': 'До блогу',
                                                                  'imageAlt': 'Обкладинка сервісу оливи RevTech 110 з '
                                                                              'кастомним V-twin мотоциклом у майстерні '
                                                                              'Iron Custom Motors.',
                                                                  'imageCaption': 'Сервіс оливи RevTech 110 в Iron '
                                                                                  'Custom Motors: двигун, коробка та '
                                                                                  'зона приводу розглядаються як '
                                                                                  'окремі системи.',
                                                                  'h1': 'Сервіс оливи RevTech 110:<br/><span '
                                                                        'class="accent">двигун, коробка передач і '
                                                                        'привід.</span>',
                                                                  'h1Crumb': 'Сервіс оливи RevTech 110: двигун, '
                                                                             'коробка передач і привід',
                                                                  'lede': 'Великий V-twin рідко виходить з ладу без '
                                                                          'попереджень. Іноді ознаки очевидні: '
                                                                          'передачі вмикаються грубіше, мотор звучить '
                                                                          'механічно жорсткіше, зчеплення відчувається '
                                                                          'інакше, а злита олива темніша й рідша, ніж '
                                                                          'очікувалося. Інколи явного симптому немає — '
                                                                          'просто мотоцикл їздив, нагрівався, '
                                                                          'охолоджувався, стояв, знову запускався і '
                                                                          'поступово працював на втомлених рідинах.',
                                                                  'intro': {'title': 'Що входить у цей сервіс',
                                                                            'paragraphs': ['У цьому короткому відео '
                                                                                           'показано сервіс оливи на '
                                                                                           'RevTech 110: моторна '
                                                                                           'олива, олива коробки '
                                                                                           'передач і змащення зони '
                                                                                           'приводу. Для Harley-style '
                                                                                           'custom motorcycle це не '
                                                                                           'просто “заміна оливи”. Це '
                                                                                           'базова перевірка стану '
                                                                                           'трьох різних механічних '
                                                                                           'зон, які працюють під '
                                                                                           'різними навантаженнями.',
                                                                                           'Моторна олива працює з '
                                                                                           'температурою, продуктами '
                                                                                           'згоряння та внутрішнім '
                                                                                           'тертям. Олива в коробці '
                                                                                           'захищає навантажені '
                                                                                           'шестерні та підшипники. '
                                                                                           'Первинний привід або зона '
                                                                                           'приводу, залежно від '
                                                                                           'конкретної збірки, може '
                                                                                           'працювати з ланцюгом, '
                                                                                           'зчепленням і деталями, що '
                                                                                           'обертаються. Сприймати все '
                                                                                           'це як одну й ту саму '
                                                                                           'операцію — поширена '
                                                                                           'помилка.',
                                                                                           'В Iron Custom Motors ми '
                                                                                           'дивимося на такий сервіс '
                                                                                           'як на перевірку системи, а '
                                                                                           'не просто як на процедуру '
                                                                                           '“злив-залив”.']},
                                                                  'sections': [{'title': 'Чому це важливо',
                                                                                'paragraphs': ['У великооб’ємному '
                                                                                               'повітряному або '
                                                                                               'повітряно-оливному '
                                                                                               'V-twin олива має '
                                                                                               'непросте життя. Двигун '
                                                                                               'працює з великими '
                                                                                               'поршнями, сильними '
                                                                                               'імпульсами, високими '
                                                                                               'внутрішніми '
                                                                                               'навантаженнями та '
                                                                                               'значною температурою. '
                                                                                               'У міському трафіку '
                                                                                               'Лісабона чи Кашкайша '
                                                                                               'це тепло не зникає '
                                                                                               'швидко. Короткі '
                                                                                               'поїздки, затори та '
                                                                                               'вологість біля океану '
                                                                                               'роблять умови '
                                                                                               'експлуатації важчими, '
                                                                                               'ніж здається за '
                                                                                               'регламентом.',
                                                                                               'Свіжа олива не лише '
                                                                                               'зменшує тертя. Вона '
                                                                                               'допомагає відводити '
                                                                                               'тепло від критичних '
                                                                                               'деталей, утримує '
                                                                                               'забруднення у '
                                                                                               'зваженому стані, '
                                                                                               'захищає металеві '
                                                                                               'поверхні й підтримує '
                                                                                               'правильну оливну '
                                                                                               'плівку. Коли олива '
                                                                                               'стара, забруднена, '
                                                                                               'розбавлена або просто '
                                                                                               'не підходить для '
                                                                                               'конкретного вузла, '
                                                                                               'мотоцикл може їхати — '
                                                                                               'але запас захисту вже '
                                                                                               'менший.',
                                                                                               'Коробка передач має '
                                                                                               'інше завдання. У ній '
                                                                                               'немає продуктів '
                                                                                               'згоряння, зате є '
                                                                                               'високий тиск між '
                                                                                               'зубцями шестерень і '
                                                                                               'ударні навантаження '
                                                                                               'кожного разу, коли '
                                                                                               'райдер відкриває або '
                                                                                               'закриває газ. Стара чи '
                                                                                               'неправильна олива в '
                                                                                               'коробці може зробити '
                                                                                               'перемикання важчим, '
                                                                                               'прискорити знос '
                                                                                               'шестерень і '
                                                                                               'підшипників та '
                                                                                               'приховати дрібну '
                                                                                               'проблему до моменту, '
                                                                                               'коли вона стане '
                                                                                               'дорогою.',
                                                                                               'Зона приводу потребує '
                                                                                               'окремої уваги. На '
                                                                                               'багатьох Harley-style '
                                                                                               'мотоциклах ремінний '
                                                                                               'final drive сам по '
                                                                                               'собі не заповнений '
                                                                                               'оливою. Зазвичай '
                                                                                               'оливний сервіс '
                                                                                               'стосується primary '
                                                                                               'drive або змащуваних '
                                                                                               'зон трансмісії. На '
                                                                                               'кастомному мотоциклі, '
                                                                                               'особливо з aftermarket '
                                                                                               'engine на кшталт '
                                                                                               'RevTech, точну '
                                                                                               'конфігурацію потрібно '
                                                                                               'підтвердити до вибору '
                                                                                               'оливи, кількості та '
                                                                                               'процедури.']},
                                                                               {'title': 'Основне технічне пояснення',
                                                                                'paragraphs': ['Моторна олива — '
                                                                                               'найочевидніша частина '
                                                                                               'сервісу, але саме її '
                                                                                               'найчастіше надто '
                                                                                               'спрощують. У RevTech '
                                                                                               '110 або схожому '
                                                                                               'великому V-twin олива '
                                                                                               'працює під високим '
                                                                                               'тепловим і механічним '
                                                                                               'навантаженням. Вона '
                                                                                               'має захищати '
                                                                                               'підшипники, поршні, '
                                                                                               'стінки циліндрів, '
                                                                                               'компоненти ГРМ та інші '
                                                                                               'внутрішні деталі, '
                                                                                               'одночасно відводячи '
                                                                                               'забруднення від '
                                                                                               'робочих поверхонь.',
                                                                                               'З часом олива втрачає '
                                                                                               'частину захисних '
                                                                                               'властивостей. Вона '
                                                                                               'може окислюватися, '
                                                                                               'накопичувати сліди '
                                                                                               'палива, утримувати '
                                                                                               'мікроскопічні металеві '
                                                                                               'частинки й гірше '
                                                                                               'переносити високу '
                                                                                               'температуру. Тому '
                                                                                               'сервіс моторної оливи '
                                                                                               'має включати не тільки '
                                                                                               'заміну, а й оцінку '
                                                                                               'стану злитої оливи, '
                                                                                               'перевірку зони '
                                                                                               'фільтра, огляд на '
                                                                                               'підтікання та '
                                                                                               'підтвердження, що '
                                                                                               'немає ознак міграції '
                                                                                               'оливи, переливу або '
                                                                                               'зовнішнього '
                                                                                               'забруднення.',
                                                                                               'Рівень оливи та '
                                                                                               'процедура перевірки '
                                                                                               'можуть відрізнятися '
                                                                                               'залежно від оливного '
                                                                                               'бака, рами, '
                                                                                               'конфігурації двигуна і '
                                                                                               'навіть від того, чи '
                                                                                               'перевіряється мотоцикл '
                                                                                               'гарячим, холодним, '
                                                                                               'вертикально або на '
                                                                                               'боковій підніжці. '
                                                                                               'Універсальним цифрам '
                                                                                               'без правильного manual '
                                                                                               'довіряти не можна.',
                                                                                               'Коробка передач живе '
                                                                                               'інакше, ніж двигун. '
                                                                                               'Вона не бачить газів '
                                                                                               'згоряння, але постійно '
                                                                                               'працює з тиском між '
                                                                                               'шестернями та зміною '
                                                                                               'навантажень. Коли '
                                                                                               'олива в коробці стара '
                                                                                               'або забруднена, райдер '
                                                                                               'може відчути важче '
                                                                                               'перемикання, зайвий '
                                                                                               'механічний шум, менш '
                                                                                               'точний хід лапки або '
                                                                                               'складніший пошук '
                                                                                               'нейтралі.',
                                                                                               'Фраза “final drive” '
                                                                                               'може означати різні '
                                                                                               'речі залежно від '
                                                                                               'конструкції мотоцикла. '
                                                                                               'На багатьох '
                                                                                               'Harley-style байках '
                                                                                               'ремінний фінальний '
                                                                                               'привід не має оливної '
                                                                                               'ванни. Найчастіше '
                                                                                               'йдеться про primary '
                                                                                               'drive або окремі '
                                                                                               'змащувані зони '
                                                                                               'трансмісії. Реальну '
                                                                                               'конфігурацію потрібно '
                                                                                               'підтвердити перед '
                                                                                               'вибором оливи, '
                                                                                               'кількості чи '
                                                                                               'процедури.']},
                                                                               {'title': 'Нюанси майстерні, які часто '
                                                                                         'не помічають',
                                                                                'bullets': ['Три оливні зони не завжди '
                                                                                            'потребують однієї й тієї '
                                                                                            'самої оливи. Двигун, '
                                                                                            'коробка та зона зчеплення '
                                                                                            'або primary мають різні '
                                                                                            'механічні потреби. '
                                                                                            'Правильний вибір залежить '
                                                                                            'від фактично встановлених '
                                                                                            'компонентів.',
                                                                                            '“Заводиться і їде” не '
                                                                                            'означає, що олива '
                                                                                            'здорова. Великий V-twin '
                                                                                            'може впевнено тягнути '
                                                                                            'навіть зі старою оливою, '
                                                                                            'але запас захисту вже '
                                                                                            'може бути зменшений.',
                                                                                            'Сміття на зливній пробці '
                                                                                            '— це інформація. Легка '
                                                                                            'металева паста може бути '
                                                                                            'нормальним слідом зносу. '
                                                                                            'Стружка, пластівці або '
                                                                                            'надмірна кількість металу '
                                                                                            'означають, що сервіс має '
                                                                                            'перейти в інспекцію.',
                                                                                            'Клімат узбережжя має '
                                                                                            'значення. У Кашкайші та '
                                                                                            'Лісабоні вологість і '
                                                                                            'морське повітря '
                                                                                            'прискорюють корозію '
                                                                                            'кріплення, електричних '
                                                                                            'контактів, відкритого '
                                                                                            'металу та ущільнювальних '
                                                                                            'поверхонь.',
                                                                                            'Кастомні збірки потрібно '
                                                                                            'перевіряти повторно. '
                                                                                            'Мотоцикл із RevTech може '
                                                                                            'поєднувати aftermarket '
                                                                                            'двигун, раму, оливний '
                                                                                            'бак, шланги, фітинги, '
                                                                                            'коробку, '
                                                                                            'primary-компоненти та '
                                                                                            'нестандартний вихлоп. '
                                                                                            'Після сервісу такий байк '
                                                                                            'треба дивитися як єдину '
                                                                                            'систему.']},
                                                                               {'title': 'Типові помилки',
                                                                                'bullets': ['Ставитися до великого '
                                                                                            'кастомного V-twin як до '
                                                                                            'звичайного універсального '
                                                                                            'мотоцикла.',
                                                                                            'Міняти тільки моторну '
                                                                                            'оливу й забувати про '
                                                                                            'коробку або primary-drive '
                                                                                            'lubricant.',
                                                                                            'Використовувати '
                                                                                            'універсальні цифри з '
                                                                                            'інтернету замість '
                                                                                            'документації для '
                                                                                            'конкретного двигуна та '
                                                                                            'компонентів.',
                                                                                            'Переливати оливу. Більше '
                                                                                            'оливи — не означає '
                                                                                            'безпечніше. У деяких '
                                                                                            'вузлах це може спричинити '
                                                                                            'підтікання, проблеми зі '
                                                                                            'зчепленням або брудну '
                                                                                            'роботу вентиляції.',
                                                                                            'Ігнорувати невеликі сліди '
                                                                                            'оливи після сервісу. '
                                                                                            'Маленька пляма може бути '
                                                                                            'просто проблемою O-ring, '
                                                                                            'але також може вказувати '
                                                                                            'на ущільнювальну '
                                                                                            'поверхню, шланг, фітинг '
                                                                                            'або вентиляцію.']},
                                                                               {'title': 'Коли варто звернутися до '
                                                                                         'майстерні',
                                                                                'paragraphs': ['Запишіться на '
                                                                                               'перевірку, якщо '
                                                                                               'передачі стали '
                                                                                               'вмикатися важче або '
                                                                                               'менш точно, нейтраль '
                                                                                               'знайти складніше, '
                                                                                               'зчеплення почало '
                                                                                               '“тягнути”, двигун '
                                                                                               'звучить жорсткіше, ніж '
                                                                                               'зазвичай, після '
                                                                                               'поїздки з’явилися '
                                                                                               'підтікання, олива '
                                                                                               'пахне горілим або '
                                                                                               'виглядає надто '
                                                                                               'забрудненою, на '
                                                                                               'зливній пробці видно '
                                                                                               'металеві частинки, або '
                                                                                               'мотоцикл довго стояв '
                                                                                               'без сервісу.',
                                                                                               'Ці симптоми не завжди '
                                                                                               'означають серйозну '
                                                                                               'поломку. Але це вагомі '
                                                                                               'причини перевірити '
                                                                                               'мотоцикл до того, як '
                                                                                               'маленька проблема '
                                                                                               'перетвориться на '
                                                                                               'великий ремонт.']},
                                                                               {'title': 'Що ми перевіряємо в Iron '
                                                                                         'Custom Motors',
                                                                                'paragraphs': ['В Iron Custom Motors '
                                                                                               'сервіс оливи на '
                                                                                               'RevTech 110 або '
                                                                                               'схожому V-twin — це '
                                                                                               'механічна інспекція, а '
                                                                                               'не просто заміна '
                                                                                               'рідин.',
                                                                                               'Ми перевіряємо двигун, '
                                                                                               'коробку та зону '
                                                                                               'приводу як окремі '
                                                                                               'системи. Підтверджуємо '
                                                                                               'правильну специфікацію '
                                                                                               'оливи для конкретної '
                                                                                               'збірки, оглядаємо '
                                                                                               'зливні пробки та '
                                                                                               'ущільнення, шукаємо '
                                                                                               'ознаки забруднення, '
                                                                                               'перевіряємо підтікання '
                                                                                               'і переконуємося, що '
                                                                                               'мотоцикл чистий та '
                                                                                               'безпечний перед '
                                                                                               'видачею.',
                                                                                               'Для кастомних '
                                                                                               'мотоциклів ми також '
                                                                                               'дивимося прокладання '
                                                                                               'оливних ліній, зони '
                                                                                               'нагріву, точки '
                                                                                               'вібрації, стан '
                                                                                               'кріплення, ознаки '
                                                                                               'корозії та загальну '
                                                                                               'логіку збірки. Хороший '
                                                                                               'сервіс — це не тільки '
                                                                                               'свіжа олива. Це '
                                                                                               'можливість прочитати '
                                                                                               'мотоцикл.']},
                                                                               {'title': 'Висновок',
                                                                                'paragraphs': ['Сервіс оливи на '
                                                                                               'RevTech 110 або '
                                                                                               'схожому Harley-style '
                                                                                               'V-twin зовні виглядає '
                                                                                               'простою роботою, але '
                                                                                               'для довгої надійної '
                                                                                               'служби мотоцикла це '
                                                                                               'одна з ключових '
                                                                                               'процедур.',
                                                                                               'Двигун, коробка та '
                                                                                               'зона приводу '
                                                                                               'потребують правильної '
                                                                                               'оливи, правильного '
                                                                                               'рівня й правильного '
                                                                                               'підходу до огляду. '
                                                                                               'Якщо все зроблено '
                                                                                               'грамотно, сервіс '
                                                                                               'допомагає захистити '
                                                                                               'мотоцикл, покращити '
                                                                                               'відчуття від їзди й '
                                                                                               'упіймати ранні ознаки '
                                                                                               'зносу до дорогого '
                                                                                               'ремонту.']}],
                                                                  'ctaText': 'Якщо ви їздите на кастомному мотоциклі з '
                                                                             'RevTech, Harley-Davidson або іншому '
                                                                             'великому V-twin у районі Cascais чи '
                                                                             'Lisbon, запишіться на сервіс оливи або '
                                                                             'інспекцію в Iron Custom Motors. Ми '
                                                                             'перевіримо мотоцикл як систему й '
                                                                             'спокійно пояснимо, що потребує уваги, що '
                                                                             'може зачекати, а що краще попередити вже '
                                                                             'зараз.',
                                                                  'faqs': [{'q': 'Сервіс оливи на RevTech 110 такий '
                                                                                 'самий, як на Harley-Davidson?',
                                                                            'a': 'За логікою він може бути схожим, але '
                                                                                 'не має вважатися ідентичним без '
                                                                                 'перевірки двигуна, коробки та '
                                                                                 'primary-drive конфігурації '
                                                                                 'конкретного мотоцикла.'},
                                                                           {'q': 'Чи можна використовувати одну оливу '
                                                                                 'для двигуна, коробки та primary?',
                                                                            'a': 'Іноді мастило може бути дозволене '
                                                                                 'для кількох зон, але це не '
                                                                                 'універсальне правило. Усе залежить '
                                                                                 'від двигуна, коробки, зчеплення та '
                                                                                 'primary setup.'},
                                                                           {'q': 'Навіщо міняти оливу в коробці, якщо '
                                                                                 'передачі вмикаються нормально?',
                                                                            'a': 'Тому що знос і деградація оливи '
                                                                                 'накопичуються поступово. Свіжа '
                                                                                 'правильна олива допомагає захищати '
                                                                                 'шестерні та підшипники й може '
                                                                                 'покращити відчуття перемикання.'},
                                                                           {'q': 'Що буде, якщо в primary або зоні '
                                                                                 'приводу неправильна олива?',
                                                                            'a': 'Залежно від конструкції це може '
                                                                                 'вплинути на роботу зчеплення, пошук '
                                                                                 'нейтралі, змащення ланцюга, '
                                                                                 'ущільнення та знос компонентів.'},
                                                                           {'q': 'Як часто міняти оливу на RevTech '
                                                                                 '110?',
                                                                            'a': 'Інтервал залежить від специфікації '
                                                                                 'двигуна, конфігурації мотоцикла, '
                                                                                 'типу оливи, умов їзди та '
                                                                                 'рекомендацій виробника.'}]}},
                                                  'keywords': {'en': ['RevTech 110 oil service',
                                                                      'Harley-style V-twin maintenance',
                                                                      'engine oil',
                                                                      'gearbox oil',
                                                                      'primary drive service',
                                                                      'motorcycle service Cascais'],
                                                               'ru': ['сервис масла RevTech 110',
                                                                      'обслуживание V-twin',
                                                                      'моторное масло',
                                                                      'масло коробки передач',
                                                                      'primary drive',
                                                                      'мотосервис Кашкайш'],
                                                               'uk': ['сервіс оливи RevTech 110',
                                                                      'обслуговування V-twin',
                                                                      'моторна олива',
                                                                      'олива коробки передач',
                                                                      'primary drive',
                                                                      'мотосервіс Кашкайш'],
                                                               'pt': ['serviço de óleo RevTech 110',
                                                                      'manutenção V-twin',
                                                                      'óleo do motor',
                                                                      'óleo da caixa',
                                                                      'primária',
                                                                      'serviço de motos Cascais']}},
    'motorcycle-brake-pad-replacement-cascais': {
        'publishedISO': '2026-06-17',
        'modifiedISO': '2026-06-17',
        'imageBase': '/photos/blog/blog-motorcycle-brake-pad-replacement-cascais',
        'imageHero': 1,
        'imageCount': 1,
        'imageDims': {
            1: (1600, 900),
        },
        'youtubeUrl': 'https://www.youtube.com/shorts/mskf3enVe4M',
        'youtubeEmbed': 'https://www.youtube.com/embed/mskf3enVe4M',
        'sourceLocalizedSlugs': {
            'en': 'motorcycle-brake-pad-replacement-cascais',
            'ru': 'zamena-tormoznyh-kolodok-motocikla-cascais',
            'pt': 'substituicao-pastilhas-travao-mota-cascais',
            'uk': 'zamina-galmivnyh-kolodok-motocykla-cascais',
        },
        'meta': {
            'en': {
                'title': 'Motorcycle Brake Pad Replacement: What Riders Should Know | Iron Custom Motors',
                'description': 'Brake pads are more than a wear part. Learn how pad condition affects braking feel, safety, discs, ABS and riding confidence.',
                'excerpt': 'Brake pads are more than a wear part. Learn how pad condition affects braking feel, safety, discs, ABS and riding confidence.',
            },
            'ru': {
                'title': 'Замена тормозных колодок мотоцикла: что важно знать | Iron Custom Motors',
                'description': 'Тормозные колодки - не просто расходник. Как их состояние влияет на торможение, безопасность, диски, ABS и уверенность райдера.',
                'excerpt': 'Тормозные колодки - не просто расходник. Как их состояние влияет на торможение, безопасность, диски, ABS и уверенность райдера.',
            },
            'pt': {
                'title': 'Substituição das pastilhas de travão da moto | Iron Custom Motors',
                'description': 'As pastilhas de travão não são apenas uma peça de desgaste. Saiba como afetam a travagem, a segurança, os discos, o ABS e a confiança.',
                'excerpt': 'As pastilhas de travão não são apenas uma peça de desgaste. Saiba como afetam a travagem, a segurança, os discos, o ABS e a confiança.',
            },
            'uk': {
                'title': 'Заміна гальмівних колодок мотоцикла: що варто знати | Iron Custom Motors',
                'description': 'Гальмівні колодки - не просто витратник. Як їхній стан впливає на гальмування, безпеку, диски, ABS і впевненість райдера.',
                'excerpt': 'Гальмівні колодки - не просто витратник. Як їхній стан впливає на гальмування, безпеку, диски, ABS і впевненість райдера.',
            },
        },
        'body': {
            'en': {
                'eyebrow': 'Workshop guide · 17 June 2026',
                'publishedLabel': 'Published 17 June 2026',
                'breadHome': 'Home',
                'breadBlog': 'Blog',
                'introTitle': 'Brake service is a system',
                'videoEyebrow': 'Workshop video',
                'videoTitle': 'Watch the brake pad replacement',
                'videoText': 'A short workshop look at motorcycle brake pad replacement: pad condition, caliper inspection, disc health and the final brake-system check.',
                'videoLink': 'Open on YouTube',
                'faqTitle': 'Motorcycle brake pad replacement FAQ',
                'ctaEyebrow': 'Need brake service?',
                'ctaTitle': 'Book a brake inspection or pad replacement.',
                'btnWA': 'WhatsApp us',
                'btnBack': 'Back to blog',
                'imageAlt': 'Motorcycle brake pad replacement cover graphic showing a Brembo brake caliper and brake pads in the Iron Custom Motors workshop.',
                'imageCaption': 'Brake pad replacement at Iron Custom Motors: pad choice, caliper inspection, disc condition and final system check.',
                'h1': 'Motorcycle Brake Pad Replacement:<br/><span class="accent">What Riders Should Know.</span>',
                'h1Crumb': 'Motorcycle Brake Pad Replacement: What Riders Should Know',
                'lede': 'The brake lever does not always become dangerous in one ride. Usually, the change is quieter than that. The lever starts to feel a little softer. The bike needs slightly more distance to stop. There is a faint scraping sound when rolling slowly. The rear brake feels weak in traffic. Or the front brake still works, but it no longer gives the same confidence before a corner.',
                'intro': {
                    'title': 'Brake service is a system',
                    'paragraphs': [
                        'Brake pads are simple parts from the outside: a friction material bonded to a metal backing plate. But on the motorcycle, they are part of a much bigger system - calipers, discs, brake fluid, brake lines, ABS, tyres, suspension and rider input all work together every time you slow down.',
                        'That is why replacing brake pads is not just “putting new pads in.” A proper brake service is inspection, diagnosis, correct parts selection, careful installation, bedding-in and a final safety check.',
                        'At Iron Custom Motors, we treat brakes as a system, not as an isolated part.',
                    ],
                },
                'sections': [
                    {
                        'title': 'Why Brake Pad Condition Matters',
                        'paragraphs': [
                            'Brake pads convert motion into heat through friction. Every time you brake, the pad presses against the disc and the motorcycle’s speed is reduced. That process looks simple, but the loads are high - especially on the front brake, during downhill riding, with a passenger, on a loaded touring bike, or on a heavy Harley-Davidson or custom motorcycle.',
                            'As brake pads wear, braking feel becomes less precise, stopping distance can increase, heat management becomes worse, the disc can wear unevenly, and the brake lever or pedal may travel further than before.',
                            'The problem is not only pad thickness. A pad can still have material left, but be glazed, contaminated, cracked, overheated, unevenly worn or poorly matched to the disc. In those cases, the brake may still “work,” but not as cleanly or predictably as it should.',
                            'On a motorcycle, predictability matters. A brake that bites too suddenly, fades when hot, vibrates through the lever or feels wooden can change how the rider approaches corners, traffic and emergency stops.',
                        ],
                    },
                    {
                        'title': 'Brake Pads Are Only One Part of the System',
                        'paragraphs': [
                            'A common mistake is to assume that weak braking always means worn pads. Sometimes it does. But sometimes the real cause is somewhere else.',
                            'A proper inspection should look at pad thickness and wear pattern, disc condition and surface, caliper movement, piston condition, brake fluid age and contamination, brake hose condition, lever or pedal feel, ABS warning lights, tyre condition and suspension behavior under braking.',
                            'A motorcycle with fresh brake pads but old brake fluid can still have a soft, spongy lever. A motorcycle with new pads and a damaged disc may vibrate or make noise. A bike with sticky caliper pistons can wear one pad faster than the other. A bike with poor tyres can have strong brakes but poor stopping performance because the tyre cannot transfer the force to the road properly.',
                            'This is why brake work should never be treated as a quick cosmetic repair. It is part of the motorcycle’s safety architecture.',
                        ],
                    },
                    {
                        'title': 'Choosing the Correct Brake Pads',
                        'paragraphs': [
                            'Brake pads are not all the same. Different compounds are designed for different motorcycles, riding styles, disc materials and temperature ranges.',
                            'Some pads are built for everyday road use, with stable performance from cold and smooth control in traffic. Others are designed for heavier bikes, sport riding or higher temperatures. Some compounds may offer stronger bite but create more disc wear, more dust or a different feel at the lever.',
                            'The correct choice depends on the motorcycle, the rider and the brake system: scooter or maxi-scooter, naked bike used daily in Lisbon traffic, touring motorcycle with luggage and passenger, Harley-Davidson or heavy cruiser, adventure bike used on mixed roads, sport motorcycle with aggressive braking, or a custom bike with modified wheels, calipers or discs.',
                            'There is no universal “best brake pad.” The best pad is the one that matches the motorcycle, the brake disc, the riding conditions and the manufacturer’s specification.',
                            'For custom motorcycles, this becomes even more important. A bike may have aftermarket calipers, custom wheels, non-standard discs, a changed master cylinder or different brake lines. In that case, pad selection should be based on the actual components installed - not only on the model name.',
                        ],
                    },
                    {
                        'title': 'Bedding-In: Why New Pads Need Time',
                        'paragraphs': [
                            'New brake pads do not deliver their best performance immediately. They need to mate correctly with the brake disc. This process is usually called bedding-in.',
                            'During bedding-in, the contact surfaces adapt to each other and a proper friction layer develops on the disc. If this process is rushed, ignored or done incorrectly, the rider may experience noise, vibration, uneven braking feel or reduced performance.',
                            'This is one of the reasons why we do not like the phrase “just changed the pads, now everything is perfect.” New pads need correct installation, a suitable disc surface and a controlled bedding-in period. The brake should feel predictable, but the rider should still avoid aggressive braking until the pads and discs are properly settled, unless an emergency stop is necessary.',
                            'The exact bedding-in recommendation depends on the pad manufacturer and compound. A road pad, a sintered pad and a race compound may not require the same approach.',
                        ],
                    },
                    {
                        'title': 'What Riders Often Miss',
                        'paragraphs': [
                            'Uneven wear matters. One pad may look acceptable while the other is almost finished. This can happen because of caliper piston issues, guide pin problems, dirt, corrosion or a caliper that is not moving freely.',
                            'Brake fluid can make new pads feel bad. If the brake lever feels spongy after pad replacement, the pads may not be the problem. Old fluid, air in the system, rubber hose expansion or internal contamination can change lever feel.',
                            'Discs matter as much as pads. New pads installed on a heavily worn, grooved, warped or contaminated disc may never perform correctly. Surface condition, thickness and runout all matter, and exact limits must be checked according to the motorcycle manufacturer’s specification.',
                            'Coastal climate can affect brakes. Around Cascais and Lisbon, motorcycles live with humidity and sea air. That can accelerate corrosion on fasteners, pad pins, caliper hardware and exposed metal surfaces.',
                            'Heavy bikes are less forgiving. A touring motorcycle, cruiser or Harley-Davidson with passenger and luggage puts serious load into the braking system. Pads, discs, fluid and tyres work harder.',
                        ],
                    },
                    {
                        'title': 'Common Mistakes Owners Make',
                        'paragraphs': [
                            'The first mistake is waiting until the brake starts making metal-on-metal noise. At that point, the disc may already be damaged, and the repair can become more expensive.',
                            'The second mistake is replacing pads without inspecting the disc. If the disc surface is poor, new pads may wear badly, make noise or give weak braking feel.',
                            'The third mistake is contaminating the pads or discs during other service work. Brake pads and discs do not like oil, chain lube, fork oil, incorrectly used cleaner residue or general workshop dirt.',
                            'The fourth mistake is mixing parts without checking compatibility. Not every pad compound suits every disc or riding style.',
                            'The fifth mistake is assuming that rear brake weakness is not important. The rear brake helps with low-speed control, traffic riding, hill starts, two-up riding and stabilizing the motorcycle.',
                        ],
                    },
                    {
                        'title': 'When to Visit a Workshop',
                        'paragraphs': [
                            'Do not delay a brake inspection if you notice scraping, grinding or metallic noise, vibration through the lever or pedal, brake lever coming closer to the grip, weak bite, delayed response, burning smell after normal riding, uneven pad wear, visible cracks, missing material, glazing, brake fluid leak, ABS warning light, the bike pulling to one side under braking, or brake performance changing when hot.',
                            'These symptoms do not always mean the same fault. But with brakes, guessing is the wrong approach. The system needs to be inspected before the motorcycle is pushed harder.',
                        ],
                    },
                    {
                        'title': 'What We Check at Iron Custom Motors',
                        'paragraphs': [
                            'When we replace brake pads at Iron Custom Motors, the work does not stop at removing the old pads and fitting new ones.',
                            'We check the condition of the pads, discs, calipers, pistons, pad pins, hardware, brake fluid condition, lever or pedal feel, hose condition and visible signs of leaks or contamination. On motorcycles with ABS, we also pay attention to warning lights and system behavior.',
                            'For custom motorcycles, Harley-Davidson models, touring bikes and premium motorcycles, we also look at the bigger picture: weight, riding style, tyre condition, suspension behavior and whether the installed brake components match the motorcycle’s real use.',
                            'A proper brake service should leave the rider with more than new parts. It should leave them with a clear understanding of what was worn, what was checked and what may need attention later.',
                        ],
                    },
                    {
                        'title': 'Conclusion',
                        'paragraphs': [
                            'Brake pads are wear parts, but braking is not a small subject. A motorcycle brake system is one of the most important safety systems on the bike, and pad replacement is the right moment to inspect the system properly.',
                            'Good brakes are not only about stopping power. They are about feel, control, predictability and trust. When the lever feels right, the discs are healthy, the pads are correctly matched and the system is clean, the motorcycle gives the rider confidence.',
                            'If your brakes feel different, make noise, show uneven wear or simply have not been checked for a while, it is better to inspect them before the problem becomes expensive - or unsafe.',
                        ],
                    },
                    {
                        'title': 'Sources checked',
                        'paragraphs': [
                            'MSF T-CLOCS pre-ride inspection checklist; Brembo brake maintenance and bedding guidance; Galfer bedding-in guidance; EBC brake pad bedding guidance.',
                        ],
                    },
                ],
                'ctaText': 'If your motorcycle needs brake pad replacement or a brake system inspection, book a service at Iron Custom Motors in Cascais. We will check the system properly, explain what needs attention and make sure the bike leaves the workshop ready for the road.',
                'faqs': [
                    {
                        'q': 'How do I know when motorcycle brake pads need replacement?',
                        'a': 'Common signs include reduced braking bite, scraping noise, vibration, uneven wear, longer lever travel or visible low pad material. The exact minimum thickness depends on the motorcycle and brake manufacturer, so it should be checked against the correct specification.',
                    },
                    {
                        'q': 'Should brake discs be replaced together with pads?',
                        'a': 'Not always. But the discs must be inspected during pad replacement. If they are below the manufacturer’s limit, heavily grooved, warped, cracked or contaminated, fitting new pads alone is not enough.',
                    },
                    {
                        'q': 'Why do new brake pads sometimes make noise?',
                        'a': 'New pads can make noise if they are not bedded in correctly, if the disc surface is poor, if hardware is dirty or worn, or if the pad compound does not suit the application. Persistent noise should be checked.',
                    },
                    {
                        'q': 'Can old brake fluid affect braking even with new pads?',
                        'a': 'Yes. Old or contaminated brake fluid can make the lever feel soft or inconsistent. Pad replacement and brake fluid service are different operations, but both affect braking feel and safety.',
                    },
                    {
                        'q': 'Are sintered brake pads better than organic pads?',
                        'a': 'Not universally. Sintered pads often handle heat well and can offer strong performance, but the correct choice depends on the motorcycle, disc material, riding style and manufacturer recommendation.',
                    },
                ],
            },
            'ru': {
                'eyebrow': 'Гайд мастерской · 17 июня 2026',
                'publishedLabel': 'Опубликовано 17 июня 2026',
                'breadHome': 'Главная',
                'breadBlog': 'Блог',
                'introTitle': 'Тормозной сервис — это система',
                'videoEyebrow': 'Видео из мастерской',
                'videoTitle': 'Смотрите замену тормозных колодок',
                'videoText': 'Короткий взгляд на замену тормозных колодок: состояние колодок, осмотр суппорта, здоровье диска и финальная проверка тормозной системы.',
                'videoLink': 'Открыть на YouTube',
                'faqTitle': 'FAQ по замене тормозных колодок мотоцикла',
                'ctaEyebrow': 'Нужен сервис тормозов?',
                'ctaTitle': 'Запишитесь на проверку тормозов или замену колодок.',
                'btnWA': 'WhatsApp',
                'btnBack': 'Назад в блог',
                'imageAlt': 'Обложка статьи о замене тормозных колодок мотоцикла: суппорт Brembo и тормозные колодки в мастерской Iron Custom Motors.',
                'imageCaption': 'Замена тормозных колодок в Iron Custom Motors: подбор колодок, осмотр суппорта, состояние диска и финальная проверка системы.',
                'h1': 'Замена тормозных колодок мотоцикла:<br/><span class="accent">что важно знать.</span>',
                'h1Crumb': 'Замена тормозных колодок мотоцикла: что важно знать',
                'lede': 'Тормозная ручка редко становится опасной за одну поездку. Обычно всё меняется тише. Ручка начинает казаться немного мягче. Мотоциклу нужно чуть больше расстояния, чтобы остановиться. На малой скорости появляется лёгкий скрежет. Задний тормоз в пробке ощущается слабее. Или передний тормоз всё ещё работает, но перед поворотом уже не даёт прежней уверенности.',
                'intro': {
                    'title': 'Тормозной сервис — это система',
                    'paragraphs': [
                        'Снаружи тормозные колодки выглядят просто: фрикционный материал на металлической основе. Но на мотоцикле они работают внутри большой системы. Суппорты, диски, тормозная жидкость, шланги, ABS, шины, подвеска и действия райдера участвуют в каждом торможении.',
                        'Поэтому замена тормозных колодок - это не просто “поставить новые колодки”. Правильный тормозной сервис - это осмотр, диагностика, подбор корректных деталей, аккуратная установка, притирка и финальная проверка безопасности.',
                        'В Iron Custom Motors мы рассматриваем тормоза как систему, а не как отдельную деталь.',
                    ],
                },
                'sections': [
                    {
                        'title': 'Почему состояние тормозных колодок так важно',
                        'paragraphs': [
                            'Тормозные колодки превращают движение в тепло за счёт трения. Каждый раз, когда вы тормозите, колодка прижимается к диску, и скорость мотоцикла снижается. Процесс выглядит простым, но нагрузки высокие - особенно на переднем тормозе, на спусках, с пассажиром, с багажом, на тяжёлом touring-мотоцикле, Harley-Davidson или кастомном байке.',
                            'По мере износа колодок меняется ощущение тормоза: торможение становится менее точным, тормозной путь может увеличиваться, тепло отводится хуже, диск может изнашиваться неравномерно, а ручка или педаль тормоза могут иметь больший ход.',
                            'Проблема не только в толщине колодки. На ней ещё может оставаться материал, но она может быть застеклована, загрязнена, перегрета, потрескана, изношена неравномерно или плохо подходить к диску. В таком состоянии тормоз вроде бы “работает”, но уже не так чисто и предсказуемо.',
                            'На мотоцикле предсказуемость важна. Тормоз, который слишком резко схватывает, плывёт при нагреве, отдаёт вибрацией в ручку или кажется деревянным, меняет то, как райдер входит в повороты, едет в трафике и реагирует на экстренные ситуации.',
                        ],
                    },
                    {
                        'title': 'Колодки - только часть тормозной системы',
                        'paragraphs': [
                            'Частая ошибка - считать, что слабое торможение всегда означает изношенные колодки. Иногда это действительно так. Но иногда причина находится в другом месте.',
                            'Правильный осмотр должен включать толщину и характер износа колодок, состояние и поверхность диска, работу суппорта, состояние поршней, возраст и загрязнение тормозной жидкости, состояние тормозных шлангов, ощущение ручки или педали, предупреждения ABS, состояние шин и поведение подвески при торможении.',
                            'Мотоцикл с новыми колодками, но старой тормозной жидкостью всё равно может иметь мягкую, “ватную” ручку. Мотоцикл с новыми колодками и повреждённым диском может вибрировать или шуметь. Закисшие поршни суппорта могут съедать одну колодку быстрее другой. А плохая резина может не дать реализовать даже сильные тормоза, потому что шина не передаёт усилие на дорогу.',
                            'Именно поэтому тормозные работы нельзя воспринимать как быстрый косметический ремонт. Это часть архитектуры безопасности мотоцикла.',
                        ],
                    },
                    {
                        'title': 'Как подобрать правильные тормозные колодки',
                        'paragraphs': [
                            'Тормозные колодки не одинаковые. Разные составы рассчитаны на разные мотоциклы, стиль езды, тип дисков и температурные режимы.',
                            'Одни колодки хорошо подходят для повседневной езды: стабильно работают с холодного состояния и дают плавный контроль в городском трафике. Другие рассчитаны на тяжёлые мотоциклы, активную езду или более высокие температуры. Некоторые составы дают более сильный bite, но могут быстрее изнашивать диск, сильнее пылить или иначе ощущаться на ручке.',
                            'Правильный выбор зависит от мотоцикла, райдера и тормозной системы: scooter или maxi-scooter, naked для ежедневной езды по Лиссабону, touring-мотоцикл с багажом и пассажиром, Harley-Davidson или тяжёлый cruiser, adventure bike для mixed roads, sport bike с агрессивным торможением или custom bike с изменёнными колёсами, суппортами или дисками.',
                            'Универсальной “лучшей колодки” не существует. Лучшая колодка - та, которая подходит конкретному мотоциклу, диску, условиям езды и требованиям производителя.',
                            'Для кастомных мотоциклов это особенно важно. На байке могут стоять aftermarket-суппорты, custom wheels, нестандартные диски, другой главный тормозной цилиндр или иные тормозные шланги. В таком случае подбор должен идти от фактически установленных компонентов, а не только от названия модели.',
                        ],
                    },
                    {
                        'title': 'Притирка: почему новым колодкам нужно время',
                        'paragraphs': [
                            'Новые тормозные колодки не раскрывают свои лучшие свойства сразу. Им нужно правильно приработаться к тормозному диску. Этот процесс обычно называют bedding-in или притиркой.',
                            'Во время притирки контактные поверхности адаптируются друг к другу, а на диске формируется стабильный фрикционный слой. Если процесс торопить, игнорировать или выполнять неправильно, райдер может получить шум, вибрацию, неравномерное ощущение тормоза или сниженное тормозное усилие.',
                            'Поэтому нам не нравится фраза “колодки поменяли - теперь всё идеально”. Новым колодкам нужна правильная установка, подходящая поверхность диска и контролируемый период притирки. Тормоз должен быть предсказуемым, но райдеру всё равно стоит избегать агрессивного торможения, пока колодки и диски не приработаются, кроме случаев, когда нужно экстренно остановиться.',
                            'Точная рекомендация по притирке зависит от производителя колодок и их состава. Дорожные, sintered и гоночные составы могут требовать разного подхода.',
                        ],
                    },
                    {
                        'title': 'Что райдеры часто упускают',
                        'paragraphs': [
                            'Неравномерный износ имеет значение. Одна колодка может выглядеть нормально, а другая быть почти законченной. Это бывает из-за проблем с поршнями суппорта, направляющими, грязью, коррозией или суппортом, который не двигается свободно.',
                            'Тормозная жидкость может испортить ощущение даже с новыми колодками. Если после замены колодок ручка остаётся ватной, проблема может быть не в колодках. Старая жидкость, воздух в системе, расширение резинового шланга или внутреннее загрязнение меняют ощущение тормоза.',
                            'Диски важны не меньше колодок. Новые колодки на сильно изношенном, бороздчатом, поведённом или загрязнённом диске могут никогда не работать правильно. Поверхность, толщина и биение диска имеют значение, а точные пределы нужно проверять по спецификации производителя мотоцикла.',
                            'Морской климат влияет на тормоза. В районе Cascais и Lisbon мотоциклы живут во влажности и морском воздухе. Это ускоряет коррозию крепежа, пальцев колодок, элементов суппорта и открытого металла.',
                            'Тяжёлые мотоциклы менее прощают ошибки. Touring, cruiser или Harley-Davidson с пассажиром и багажом серьёзно нагружают тормозную систему. Колодки, диски, жидкость и шины работают тяжелее.',
                        ],
                    },
                    {
                        'title': 'Типичные ошибки владельцев',
                        'paragraphs': [
                            'Первая ошибка - ждать, пока тормоз начнёт скрежетать металлом по металлу. К этому моменту диск уже может быть повреждён, а ремонт станет дороже.',
                            'Вторая ошибка - менять колодки без осмотра диска. Если поверхность диска плохая, новые колодки могут шуметь, быстро изнашиваться или давать слабое торможение.',
                            'Третья ошибка - загрязнить колодки или диски во время других работ. Тормозные колодки и диски не любят масло, chain lube, fork oil, неправильно использованные очистители и обычную мастерскую грязь.',
                            'Четвёртая ошибка - смешивать детали без проверки совместимости. Не каждый состав колодок подходит каждому диску и стилю езды.',
                            'Пятая ошибка - считать слабый задний тормоз неважным. Задний тормоз помогает на малой скорости, в пробках, на подъёме, при езде с пассажиром и при стабилизации мотоцикла.',
                        ],
                    },
                    {
                        'title': 'Когда стоит приехать в мастерскую',
                        'paragraphs': [
                            'Не откладывайте проверку тормозов, если появились скрежет, металлический звук, вибрация в ручке или педали, ручка стала подходить ближе к грипсе, тормоз стал слабее, реакция задерживается, после обычной езды появляется запах перегрева, колодки изнашиваются неравномерно, видны трещины, сколы, застеклованная поверхность, подтёк тормозной жидкости, горит ABS, мотоцикл уводит в сторону при торможении или тормоза меняют поведение при нагреве.',
                            'Эти симптомы не всегда означают одну и ту же неисправность. Но с тормозами угадывать нельзя. Систему нужно проверить до того, как мотоцикл начнут нагружать сильнее.',
                        ],
                    },
                    {
                        'title': 'Что мы проверяем в Iron Custom Motors',
                        'paragraphs': [
                            'Когда мы меняем тормозные колодки в Iron Custom Motors, работа не заканчивается снятием старых колодок и установкой новых.',
                            'Мы проверяем состояние колодок, дисков, суппортов, поршней, пальцев, крепежа, тормозной жидкости, ощущение ручки или педали, состояние шлангов и видимые признаки подтёков или загрязнения. На мотоциклах с ABS мы также обращаем внимание на предупреждения и поведение системы.',
                            'Для custom motorcycles, Harley-Davidson, touring bikes и premium motorcycles мы смотрим шире: масса мотоцикла, стиль езды, состояние шин, работа подвески и соответствие установленных тормозных компонентов реальному использованию мотоцикла.',
                            'Правильный тормозной сервис должен дать райдеру не только новые детали. Он должен дать понимание: что было изношено, что проверено и на что стоит обратить внимание позже.',
                        ],
                    },
                    {
                        'title': 'Заключение',
                        'paragraphs': [
                            'Тормозные колодки - расходник, но тормоза не мелочь. Тормозная система мотоцикла - одна из важнейших систем безопасности, а замена колодок - правильный момент для полноценного осмотра.',
                            'Хорошие тормоза - это не только сила остановки. Это ощущение, контроль, предсказуемость и доверие. Когда ручка работает правильно, диски здоровы, колодки подобраны корректно, а система чистая, мотоцикл даёт райдеру уверенность.',
                            'Если тормоза стали ощущаться иначе, шумят, изнашиваются неравномерно или давно не проверялись, лучше осмотреть их заранее - до того, как проблема станет дорогой или небезопасной.',
                        ],
                    },
                    {
                        'title': 'Проверенные источники',
                        'paragraphs': [
                            'MSF T-CLOCS pre-ride inspection checklist; материалы Brembo по обслуживанию тормозов и притирке; рекомендации Galfer по bedding-in; рекомендации EBC по притирке тормозных колодок.',
                        ],
                    },
                ],
                'ctaText': 'Если вашему мотоциклу нужна замена тормозных колодок или проверка тормозной системы, запишитесь на сервис в Iron Custom Motors в Cascais. Мы проверим систему правильно, объясним, что требует внимания, и подготовим мотоцикл к дороге.',
                'faqs': [
                    {
                        'q': 'Как понять, что тормозные колодки мотоцикла пора менять?',
                        'a': 'Типичные признаки: слабее bite, скрежет, вибрация, неравномерный износ, увеличенный ход ручки или визуально малый остаток материала. Точная минимальная толщина зависит от мотоцикла и производителя тормозов, поэтому её нужно проверять по правильной спецификации.',
                    },
                    {
                        'q': 'Нужно ли менять тормозные диски вместе с колодками?',
                        'a': 'Не всегда. Но диски обязательно нужно осматривать при замене колодок. Если они ниже допустимой толщины, сильно изношены, имеют борозды, биение, трещины или загрязнение, одних новых колодок недостаточно.',
                    },
                    {
                        'q': 'Почему новые тормозные колодки иногда шумят?',
                        'a': 'Новые колодки могут шуметь из-за неправильной притирки, плохой поверхности диска, грязного или изношенного крепежа, либо неподходящего состава колодок. Постоянный шум стоит проверить.',
                    },
                    {
                        'q': 'Может ли старая тормозная жидкость влиять на торможение с новыми колодками?',
                        'a': 'Да. Старая или загрязнённая тормозная жидкость может делать ручку мягкой и непредсказуемой. Замена колодок и сервис тормозной жидкости - разные операции, но обе влияют на ощущение тормоза и безопасность.',
                    },
                    {
                        'q': 'Sintered колодки лучше organic?',
                        'a': 'Не универсально. Sintered-колодки часто хорошо держат нагрев и дают сильное торможение, но правильный выбор зависит от мотоцикла, материала диска, стиля езды и рекомендаций производителя.',
                    },
                ],
            },
            'pt': {
                'eyebrow': 'Guia de oficina · 17 de junho de 2026',
                'publishedLabel': 'Publicado 17 de junho de 2026',
                'breadHome': 'Início',
                'breadBlog': 'Blog',
                'introTitle': 'O serviço de travões é um sistema',
                'videoEyebrow': 'Vídeo de oficina',
                'videoTitle': 'Veja a substituição das pastilhas de travão',
                'videoText': 'Um olhar rápido de oficina sobre substituição de pastilhas: estado das pastilhas, inspeção da pinça, saúde do disco e verificação final do sistema.',
                'videoLink': 'Abrir no YouTube',
                'faqTitle': 'FAQ sobre substituição de pastilhas de travão',
                'ctaEyebrow': 'Precisa de serviço de travões?',
                'ctaTitle': 'Marque uma inspeção de travões ou substituição de pastilhas.',
                'btnWA': 'WhatsApp',
                'btnBack': 'Voltar ao blog',
                'imageAlt': 'Imagem de capa sobre substituição das pastilhas de travão da moto, com pinça Brembo e pastilhas na oficina Iron Custom Motors.',
                'imageCaption': 'Substituição de pastilhas na Iron Custom Motors: escolha correta, inspeção da pinça, estado do disco e verificação final do sistema.',
                'h1': 'Substituição das pastilhas de travão:<br/><span class="accent">o que deve saber.</span>',
                'h1Crumb': 'Substituição das pastilhas de travão da moto: o que o motociclista deve saber',
                'lede': 'A manete do travão raramente fica perigosa de um dia para o outro. Normalmente, a mudança é mais discreta. A manete começa a parecer um pouco mais esponjosa. A moto precisa de um pouco mais de distância para parar. Surge um leve som metálico a baixa velocidade. O travão traseiro parece fraco no trânsito. Ou o travão dianteiro ainda trava, mas já não transmite a mesma confiança antes de entrar numa curva.',
                'intro': {
                    'title': 'O serviço de travões é um sistema',
                    'paragraphs': [
                        'Por fora, as pastilhas de travão parecem peças simples: material de fricção ligado a uma base metálica. Mas numa moto elas fazem parte de um sistema muito maior. Pinças, discos, fluido de travão, tubos, ABS, pneus, suspensão e a ação do condutor trabalham juntos sempre que a moto desacelera.',
                        'Por isso, substituir pastilhas de travão não é apenas “montar pastilhas novas”. Um serviço de travões bem feito envolve inspeção, diagnóstico, escolha correta das peças, montagem cuidada, rodagem inicial e verificação final de segurança.',
                        'Na Iron Custom Motors, tratamos os travões como um sistema, não como uma peça isolada.',
                    ],
                },
                'sections': [
                    {
                        'title': 'Porque o estado das pastilhas é tão importante',
                        'paragraphs': [
                            'As pastilhas de travão transformam movimento em calor através da fricção. Sempre que trava, a pastilha pressiona o disco e a velocidade da moto diminui. O processo parece simples, mas as cargas são elevadas - sobretudo no travão dianteiro, em descidas, com passageiro, numa moto carregada para touring, numa Harley-Davidson pesada ou numa custom motorcycle.',
                            'À medida que as pastilhas se desgastam, a sensação de travagem pode ficar menos precisa, a distância de paragem pode aumentar, a gestão de calor piora, o disco pode desgastar-se de forma irregular e a manete ou o pedal podem ganhar mais curso.',
                            'O problema não é apenas a espessura da pastilha. Uma pastilha ainda pode ter material, mas estar vitrificada, contaminada, fissurada, sobreaquecida, gasta de forma irregular ou mal compatível com o disco. Nesses casos, o travão ainda pode “funcionar”, mas não de forma tão limpa e previsível como deveria.',
                            'Numa moto, a previsibilidade é essencial. Um travão que morde de forma brusca, perde eficácia a quente, vibra na manete ou parece “duro” e sem sensibilidade muda a forma como o motociclista aborda curvas, trânsito e travagens de emergência.',
                        ],
                    },
                    {
                        'title': 'As pastilhas são apenas uma parte do sistema',
                        'paragraphs': [
                            'Um erro comum é assumir que uma travagem fraca significa sempre pastilhas gastas. Às vezes é verdade. Mas nem sempre a causa está ali.',
                            'Uma inspeção correta deve avaliar a espessura e o padrão de desgaste das pastilhas, o estado e a superfície dos discos, o movimento da pinça, o estado dos pistões, a idade e possível contaminação do fluido de travão, o estado dos tubos, a sensação na manete ou pedal, avisos de ABS, estado dos pneus e comportamento da suspensão durante a travagem.',
                            'Uma moto com pastilhas novas, mas fluido de travão antigo, pode continuar com uma manete mole e esponjosa. Uma moto com pastilhas novas e um disco danificado pode vibrar ou fazer ruído. Pistões de pinça presos podem gastar uma pastilha mais depressa do que a outra. Pneus em mau estado podem impedir que travões fortes sejam realmente eficazes, porque o pneu não consegue transferir a força para o asfalto.',
                            'É por isso que o trabalho nos travões nunca deve ser tratado como uma reparação rápida ou cosmética. Faz parte da arquitetura de segurança da moto.',
                        ],
                    },
                    {
                        'title': 'Escolher as pastilhas de travão corretas',
                        'paragraphs': [
                            'Nem todas as pastilhas de travão são iguais. Diferentes compostos são concebidos para diferentes motos, estilos de condução, materiais de disco e faixas de temperatura.',
                            'Algumas pastilhas são feitas para uso diário, com desempenho estável a frio e bom controlo no trânsito. Outras são pensadas para motos mais pesadas, condução desportiva ou temperaturas mais elevadas. Alguns compostos oferecem uma mordida mais forte, mas podem aumentar o desgaste do disco, gerar mais pó ou alterar a sensação na manete.',
                            'A escolha correta depende da moto, do condutor e do sistema de travagem: scooter ou maxi-scooter, naked usada diariamente no trânsito de Lisboa, touring com bagagem e passageiro, Harley-Davidson ou cruiser pesado, adventure bike em estradas mistas, sport bike com travagem agressiva ou custom bike com jantes, pinças ou discos modificados.',
                            'Não existe uma “melhor pastilha” universal. A melhor pastilha é a que combina com a moto, com o disco, com as condições de utilização e com a especificação do fabricante.',
                            'Nas motos customizadas, isto é ainda mais importante. A moto pode ter pinças aftermarket, custom wheels, discos não standard, bomba de travão diferente ou tubos de travão alterados. Nesse caso, a escolha deve ser feita com base nos componentes realmente instalados - não apenas no nome do modelo.',
                        ],
                    },
                    {
                        'title': 'Bedding-in: porque as pastilhas novas precisam de tempo',
                        'paragraphs': [
                            'As pastilhas novas não entregam o seu melhor desempenho imediatamente. Precisam de assentar corretamente no disco de travão. Este processo é normalmente chamado bedding-in ou rodagem inicial das pastilhas.',
                            'Durante o bedding-in, as superfícies de contacto adaptam-se uma à outra e forma-se uma camada de fricção estável no disco. Se este processo for apressado, ignorado ou feito de forma incorreta, o motociclista pode sentir ruído, vibração, travagem irregular ou menor desempenho.',
                            'É por isso que não gostamos da frase “trocaram as pastilhas, agora está tudo perfeito”. Pastilhas novas precisam de montagem correta, superfície de disco adequada e um período controlado de rodagem. O travão deve ser previsível, mas o motociclista deve evitar travagens agressivas até pastilhas e discos assentarem corretamente, exceto em situações de emergência.',
                            'A recomendação exata de bedding-in depende do fabricante e do composto da pastilha. Uma pastilha de estrada, uma pastilha sinterizada e um composto de competição podem exigir abordagens diferentes.',
                        ],
                    },
                    {
                        'title': 'O que muitos motociclistas não veem',
                        'paragraphs': [
                            'O desgaste irregular é importante. Uma pastilha pode parecer aceitável enquanto a outra está quase no fim. Isto pode acontecer por problemas nos pistões da pinça, guias, sujidade, corrosão ou uma pinça que não se move livremente.',
                            'O fluido de travão pode fazer pastilhas novas parecerem más. Se a manete continuar esponjosa depois da substituição, o problema pode não estar nas pastilhas. Fluido antigo, ar no sistema, expansão de tubos de borracha ou contaminação interna podem alterar a sensação de travagem.',
                            'Os discos são tão importantes como as pastilhas. Pastilhas novas montadas num disco muito gasto, riscado, empenado ou contaminado podem nunca funcionar corretamente. Superfície, espessura e empeno têm importância, e os limites exatos devem ser verificados segundo a especificação do fabricante da moto.',
                            'O clima costeiro afeta os travões. Em Cascais e Lisboa, as motos vivem com humidade e ar marítimo. Isso pode acelerar a corrosão em parafusos, pinos das pastilhas, hardware da pinça e metal exposto.',
                            'Motos pesadas perdoam menos. Uma touring, cruiser ou Harley-Davidson com passageiro e bagagem coloca muita carga no sistema de travagem. Pastilhas, discos, fluido e pneus trabalham mais.',
                        ],
                    },
                    {
                        'title': 'Erros comuns dos proprietários',
                        'paragraphs': [
                            'O primeiro erro é esperar até o travão começar a fazer ruído de metal contra metal. Nessa fase, o disco pode já estar danificado e a reparação torna-se mais cara.',
                            'O segundo erro é substituir pastilhas sem inspecionar o disco. Se a superfície do disco estiver em mau estado, as pastilhas novas podem desgastar mal, fazer ruído ou travar pouco.',
                            'O terceiro erro é contaminar pastilhas ou discos durante outros trabalhos. Pastilhas e discos não gostam de óleo, lubrificante de corrente, óleo de suspensão, resíduos de produtos mal utilizados ou sujidade geral de oficina.',
                            'O quarto erro é misturar peças sem verificar compatibilidade. Nem todos os compostos de pastilha servem para todos os discos ou estilos de condução.',
                            'O quinto erro é achar que um travão traseiro fraco não importa. O travão traseiro ajuda no controlo a baixa velocidade, no trânsito, em arranques em subida, com passageiro e na estabilização da moto.',
                        ],
                    },
                    {
                        'title': 'Quando visitar uma oficina',
                        'paragraphs': [
                            'Não adie uma inspeção aos travões se notar ruído de raspagem, rangido metálico, vibração na manete ou no pedal, manete a aproximar-se mais do punho, mordida fraca, resposta atrasada, cheiro a queimado depois de uma utilização normal, desgaste irregular das pastilhas, fissuras visíveis, falta de material, vitrificação, fuga de fluido de travão, aviso de ABS, a moto a puxar para um lado ao travar ou travagem que muda quando aquece.',
                            'Estes sintomas nem sempre apontam para a mesma avaria. Mas com travões, adivinhar é a abordagem errada. O sistema deve ser inspecionado antes de a moto ser exigida com mais força.',
                        ],
                    },
                    {
                        'title': 'O que verificamos na Iron Custom Motors',
                        'paragraphs': [
                            'Quando substituímos pastilhas de travão na Iron Custom Motors, o trabalho não termina ao retirar as pastilhas antigas e montar as novas.',
                            'Verificamos o estado das pastilhas, discos, pinças, pistões, pinos, hardware, fluido de travão, sensação da manete ou pedal, estado dos tubos e sinais visíveis de fugas ou contaminação. Em motos com ABS, também observamos avisos e comportamento do sistema.',
                            'Em custom motorcycles, Harley-Davidson, touring bikes e premium motorcycles, olhamos também para o conjunto: peso, estilo de condução, estado dos pneus, comportamento da suspensão e se os componentes de travagem instalados correspondem ao uso real da moto.',
                            'Um serviço de travões bem feito deve deixar o motociclista com mais do que peças novas. Deve deixar uma explicação clara sobre o que estava gasto, o que foi verificado e o que pode precisar de atenção mais tarde.',
                        ],
                    },
                    {
                        'title': 'Conclusão',
                        'paragraphs': [
                            'As pastilhas de travão são peças de desgaste, mas travagem não é um assunto pequeno. O sistema de travagem de uma moto é um dos sistemas de segurança mais importantes, e a substituição das pastilhas é o momento certo para inspecionar tudo corretamente.',
                            'Bons travões não são apenas força de paragem. São sensação, controlo, previsibilidade e confiança. Quando a manete transmite a informação certa, os discos estão saudáveis, as pastilhas são adequadas e o sistema está limpo, a moto dá confiança ao motociclista.',
                            'Se os travões da sua moto parecem diferentes, fazem ruído, mostram desgaste irregular ou simplesmente não são verificados há algum tempo, é melhor inspecionar antes de o problema se tornar caro - ou inseguro.',
                        ],
                    },
                    {
                        'title': 'Fontes verificadas',
                        'paragraphs': [
                            'Checklist MSF T-CLOCS de inspeção antes da condução; orientações Brembo sobre manutenção de travões e bedding-in; orientação Galfer sobre bedding-in; orientação EBC sobre rodagem de pastilhas de travão.',
                        ],
                    },
                ],
                'ctaText': 'Se a sua moto precisa de substituição das pastilhas de travão ou de uma inspeção ao sistema de travagem, marque um serviço na Iron Custom Motors em Cascais. Vamos verificar o sistema corretamente, explicar o que precisa de atenção e garantir que a moto sai da oficina pronta para a estrada.',
                'faqs': [
                    {
                        'q': 'Como saber quando as pastilhas de travão da moto precisam de substituição?',
                        'a': 'Sinais comuns incluem menor força de travagem, ruído de raspagem, vibração, desgaste irregular, maior curso da manete ou pouco material visível na pastilha. A espessura mínima exata depende da moto e do fabricante do travão, por isso deve ser verificada pela especificação correta.',
                    },
                    {
                        'q': 'Os discos devem ser substituídos juntamente com as pastilhas?',
                        'a': 'Nem sempre. Mas os discos devem ser inspecionados durante a substituição das pastilhas. Se estiverem abaixo do limite do fabricante, muito riscados, empenados, fissurados ou contaminados, montar apenas pastilhas novas não é suficiente.',
                    },
                    {
                        'q': 'Porque é que pastilhas novas às vezes fazem ruído?',
                        'a': 'Pastilhas novas podem fazer ruído se não forem corretamente rodadas, se a superfície do disco estiver em mau estado, se o hardware estiver sujo ou gasto, ou se o composto não for adequado à aplicação. Ruído persistente deve ser verificado.',
                    },
                    {
                        'q': 'Fluido de travão antigo pode afetar a travagem mesmo com pastilhas novas?',
                        'a': 'Sim. Fluido antigo ou contaminado pode deixar a manete mole ou inconsistente. A substituição das pastilhas e o serviço do fluido são operações diferentes, mas ambas influenciam a sensação de travagem e a segurança.',
                    },
                    {
                        'q': 'Pastilhas sinterizadas são melhores do que orgânicas?',
                        'a': 'Não de forma universal. Pastilhas sinterizadas costumam lidar bem com calor e podem oferecer bom desempenho, mas a escolha correta depende da moto, do material do disco, do estilo de condução e da recomendação do fabricante.',
                    },
                ],
            },
            'uk': {
                'eyebrow': 'Гайд майстерні · 17 червня 2026',
                'publishedLabel': 'Опубліковано 17 червня 2026',
                'breadHome': 'Головна',
                'breadBlog': 'Блог',
                'introTitle': 'Сервіс гальм — це система',
                'videoEyebrow': 'Відео з майстерні',
                'videoTitle': 'Дивіться заміну гальмівних колодок',
                'videoText': 'Короткий погляд на заміну гальмівних колодок: стан колодок, огляд супорта, здоров’я диска та фінальна перевірка гальмівної системи.',
                'videoLink': 'Відкрити на YouTube',
                'faqTitle': 'FAQ щодо заміни гальмівних колодок мотоцикла',
                'ctaEyebrow': 'Потрібен сервіс гальм?',
                'ctaTitle': 'Запишіться на перевірку гальм або заміну колодок.',
                'btnWA': 'WhatsApp',
                'btnBack': 'Назад до блогу',
                'imageAlt': 'Обкладинка статті про заміну гальмівних колодок мотоцикла: супорт Brembo і колодки в майстерні Iron Custom Motors.',
                'imageCaption': 'Заміна гальмівних колодок в Iron Custom Motors: підбір колодок, огляд супорта, стан диска та фінальна перевірка системи.',
                'h1': 'Заміна гальмівних колодок мотоцикла:<br/><span class="accent">що варто знати.</span>',
                'h1Crumb': 'Заміна гальмівних колодок мотоцикла: що варто знати',
                'lede': 'Гальмівна ручка рідко стає небезпечною за одну поїздку. Зазвичай зміни приходять тихо. Ручка починає відчуватися трохи м’якшою. Мотоциклу потрібно трохи більше дистанції для зупинки. На малій швидкості з’являється легкий металевий звук. Заднє гальмо в трафіку здається слабшим. Або переднє гальмо все ще працює, але вже не дає тієї самої впевненості перед поворотом.',
                'intro': {
                    'title': 'Сервіс гальм — це система',
                    'paragraphs': [
                        'Ззовні гальмівні колодки виглядають просто: фрикційний матеріал на металевій основі. Але на мотоциклі вони працюють у великій системі. Супорти, диски, гальмівна рідина, шланги, ABS, шини, підвіска та дії райдера беруть участь у кожному уповільненні.',
                        'Тому заміна гальмівних колодок - це не просто “поставити нові колодки”. Правильний сервіс гальм - це огляд, діагностика, правильний підбір деталей, акуратне встановлення, притирка та фінальна перевірка безпеки.',
                        'В Iron Custom Motors ми розглядаємо гальма як систему, а не як окрему деталь.',
                    ],
                },
                'sections': [
                    {
                        'title': 'Чому стан гальмівних колодок важливий',
                        'paragraphs': [
                            'Гальмівні колодки перетворюють рух на тепло через тертя. Щоразу, коли ви гальмуєте, колодка притискається до диска, і швидкість мотоцикла зменшується. Процес виглядає простим, але навантаження високі - особливо на передньому гальмі, на спусках, з пасажиром, із багажем, на важкому touring-мотоциклі, Harley-Davidson або кастомному байку.',
                            'У міру зношення колодок відчуття гальмування може ставати менш точним, гальмівний шлях може збільшуватися, відведення тепла погіршується, диск може зношуватися нерівномірно, а ручка чи педаль можуть мати більший хід.',
                            'Проблема не лише в товщині колодки. Матеріал ще може залишатися, але колодка може бути засклована, забруднена, перегріта, потріскана, нерівномірно зношена або погано підібрана до диска. У таких випадках гальмо ще може “працювати”, але вже не так чисто й передбачувано, як має.',
                            'На мотоциклі передбачуваність критично важлива. Гальмо, яке занадто різко схоплює, втрачає ефективність при нагріванні, віддає вібрацією в ручку або здається “дерев’яним”, змінює те, як райдер заходить у повороти, рухається в трафіку та реагує на екстрені ситуації.',
                        ],
                    },
                    {
                        'title': 'Колодки - лише частина гальмівної системи',
                        'paragraphs': [
                            'Поширена помилка - вважати, що слабке гальмування завжди означає зношені колодки. Іноді так і є. Але іноді причина зовсім в іншому місці.',
                            'Правильний огляд має включати товщину й характер зношення колодок, стан і поверхню дисків, роботу супорта, стан поршнів, вік і можливе забруднення гальмівної рідини, стан шлангів, відчуття ручки чи педалі, попередження ABS, стан шин і поведінку підвіски під час гальмування.',
                            'Мотоцикл із новими колодками, але старою гальмівною рідиною, може все одно мати м’яку, “ватну” ручку. Мотоцикл із новими колодками та пошкодженим диском може вібрувати або шуміти. Підклинені поршні супорта можуть з’їдати одну колодку швидше за іншу. А погані шини можуть не дати реалізувати навіть сильні гальма, бо покришка не передає зусилля на дорогу.',
                            'Саме тому роботи з гальмами не можна сприймати як швидкий косметичний ремонт. Це частина архітектури безпеки мотоцикла.',
                        ],
                    },
                    {
                        'title': 'Як підібрати правильні гальмівні колодки',
                        'paragraphs': [
                            'Гальмівні колодки не однакові. Різні суміші розраховані на різні мотоцикли, стилі їзди, матеріали дисків і температурні режими.',
                            'Одні колодки створені для щоденної їзди: стабільно працюють з холодного стану й дають плавний контроль у трафіку. Інші розраховані на важкі мотоцикли, спортивнішу їзду або вищі температури. Деякі суміші дають сильніший bite, але можуть швидше зношувати диск, створювати більше пилу або інакше відчуватися на ручці.',
                            'Правильний вибір залежить від мотоцикла, райдера й гальмівної системи: scooter або maxi-scooter, naked для щоденної їзди Лісабоном, touring-мотоцикл із багажем і пасажиром, Harley-Davidson або важкий cruiser, adventure bike для mixed roads, sport bike з агресивним гальмуванням або custom bike зі зміненими колесами, супортами чи дисками.',
                            'Універсальної “найкращої колодки” не існує. Найкраща колодка - та, що підходить конкретному мотоциклу, диску, умовам їзди та специфікації виробника.',
                            'Для кастомних мотоциклів це особливо важливо. На байку можуть стояти aftermarket-супорти, custom wheels, нестандартні диски, інший головний гальмівний циліндр або змінені гальмівні шланги. У такому випадку підбір має базуватися на фактично встановлених компонентах, а не лише на назві моделі.',
                        ],
                    },
                    {
                        'title': 'Притирка: чому новим колодкам потрібен час',
                        'paragraphs': [
                            'Нові гальмівні колодки не показують свій найкращий результат одразу. Вони мають правильно притертися до гальмівного диска. Цей процес зазвичай називають bedding-in або притиркою.',
                            'Під час притирки контактні поверхні адаптуються одна до одної, а на диску формується стабільний фрикційний шар. Якщо цей процес поспішити, проігнорувати або виконати неправильно, райдер може отримати шум, вібрацію, нерівномірне відчуття гальма або знижену ефективність.',
                            'Саме тому нам не подобається фраза “колодки замінили - тепер усе ідеально”. Новим колодкам потрібне правильне встановлення, відповідна поверхня диска й контрольований період притирки. Гальмо має бути передбачуваним, але райдеру варто уникати агресивного гальмування, поки колодки й диски не притруться, окрім ситуацій екстреної зупинки.',
                            'Точна рекомендація щодо притирки залежить від виробника колодок і складу матеріалу. Дорожні, sintered і гоночні склади можуть вимагати різного підходу.',
                        ],
                    },
                    {
                        'title': 'Що райдери часто пропускають',
                        'paragraphs': [
                            'Нерівномірне зношення має значення. Одна колодка може виглядати нормально, а інша бути майже закінченою. Таке буває через проблеми з поршнями супорта, напрямними, брудом, корозією або супортом, який не рухається вільно.',
                            'Гальмівна рідина може зіпсувати відчуття навіть із новими колодками. Якщо після заміни колодок ручка залишається ватною, проблема може бути не в колодках. Стара рідина, повітря в системі, розширення гумового шланга або внутрішнє забруднення змінюють відчуття гальма.',
                            'Диски важливі не менше за колодки. Нові колодки на сильно зношеному, подряпаному, поведеному або забрудненому диску можуть ніколи не працювати правильно. Поверхня, товщина й биття диска мають значення, а точні межі потрібно перевіряти за специфікацією виробника мотоцикла.',
                            'Прибережний клімат впливає на гальма. У Cascais і Lisbon мотоцикли живуть у вологості та морському повітрі. Це може прискорювати корозію кріплення, пальців колодок, елементів супорта й відкритого металу.',
                            'Важкі мотоцикли менше пробачають помилки. Touring, cruiser або Harley-Davidson із пасажиром і багажем серйозно навантажують гальмівну систему. Колодки, диски, рідина й шини працюють важче.',
                        ],
                    },
                    {
                        'title': 'Типові помилки власників',
                        'paragraphs': [
                            'Перша помилка - чекати, поки гальмо почне скреготати металом по металу. На цьому етапі диск уже може бути пошкоджений, а ремонт стане дорожчим.',
                            'Друга помилка - міняти колодки без огляду диска. Якщо поверхня диска погана, нові колодки можуть неправильно зношуватися, шуміти або давати слабке гальмування.',
                            'Третя помилка - забруднити колодки чи диски під час інших робіт. Гальмівні колодки й диски не люблять оливу, мастило для ланцюга, оливу з вилки, неправильно використані очищувачі або звичайний бруд майстерні.',
                            'Четверта помилка - поєднувати деталі без перевірки сумісності. Не кожен склад колодок підходить кожному диску чи стилю їзди.',
                            'П’ята помилка - вважати слабке заднє гальмо неважливим. Заднє гальмо допомагає на малій швидкості, у трафіку, під час старту вгору, при їзді з пасажиром і для стабілізації мотоцикла.',
                        ],
                    },
                    {
                        'title': 'Коли варто звернутися до майстерні',
                        'paragraphs': [
                            'Не відкладайте перевірку гальм, якщо з’явився скрегіт, металевий звук, вібрація в ручці чи педалі, ручка підходить ближче до грипси, гальмо стало слабшим, реакція запізнюється, після звичайної їзди є запах перегріву, колодки зношуються нерівномірно, видно тріщини, відсутній матеріал, є засклована поверхня, підтікання гальмівної рідини, індикатор ABS, мотоцикл тягне вбік під час гальмування або гальма змінюють поведінку при нагріванні.',
                            'Ці симптоми не завжди означають одну й ту саму несправність. Але з гальмами вгадувати не можна. Систему потрібно оглянути до того, як мотоцикл отримуватиме більше навантаження.',
                        ],
                    },
                    {
                        'title': 'Що ми перевіряємо в Iron Custom Motors',
                        'paragraphs': [
                            'Коли ми замінюємо гальмівні колодки в Iron Custom Motors, робота не закінчується зняттям старих колодок і встановленням нових.',
                            'Ми перевіряємо стан колодок, дисків, супортів, поршнів, пальців, кріплення, гальмівної рідини, відчуття ручки чи педалі, стан шлангів і видимі ознаки підтікань або забруднення. На мотоциклах з ABS ми також звертаємо увагу на попередження та поведінку системи.',
                            'Для custom motorcycles, Harley-Davidson, touring bikes і premium motorcycles ми дивимося ширше: вага мотоцикла, стиль їзди, стан шин, робота підвіски та відповідність встановлених гальмівних компонентів реальному використанню мотоцикла.',
                            'Правильний сервіс гальм має дати райдеру більше, ніж нові деталі. Він має дати розуміння: що було зношено, що перевірено і на що варто звернути увагу пізніше.',
                        ],
                    },
                    {
                        'title': 'Висновок',
                        'paragraphs': [
                            'Гальмівні колодки - витратні деталі, але гальмування не є дрібницею. Гальмівна система мотоцикла - одна з найважливіших систем безпеки, а заміна колодок - правильний момент для повного огляду.',
                            'Хороші гальма - це не лише сила зупинки. Це відчуття, контроль, передбачуваність і довіра. Коли ручка працює правильно, диски здорові, колодки підібрані коректно, а система чиста, мотоцикл дає райдеру впевненість.',
                            'Якщо гальма відчуваються інакше, шумлять, мають нерівномірне зношення або просто давно не перевірялися, краще оглянути їх заздалегідь - до того, як проблема стане дорогою або небезпечною.',
                        ],
                    },
                    {
                        'title': 'Перевірені джерела',
                        'paragraphs': [
                            'MSF T-CLOCS pre-ride inspection checklist; матеріали Brembo щодо обслуговування гальм і bedding-in; рекомендації Galfer щодо bedding-in; рекомендації EBC щодо притирки гальмівних колодок.',
                        ],
                    },
                ],
                'ctaText': 'Якщо вашому мотоциклу потрібна заміна гальмівних колодок або перевірка гальмівної системи, запишіться на сервіс в Iron Custom Motors у Cascais. Ми правильно перевіримо систему, пояснимо, що потребує уваги, і підготуємо мотоцикл до дороги.',
                'faqs': [
                    {
                        'q': 'Як зрозуміти, що гальмівні колодки мотоцикла потрібно міняти?',
                        'a': 'Типові ознаки: слабший bite, скрегіт, вібрація, нерівномірне зношення, більший хід ручки або візуально малий залишок матеріалу. Точна мінімальна товщина залежить від мотоцикла й виробника гальм, тому її потрібно перевіряти за правильною специфікацією.',
                    },
                    {
                        'q': 'Чи потрібно міняти гальмівні диски разом із колодками?',
                        'a': 'Не завжди. Але диски обов’язково потрібно оглядати під час заміни колодок. Якщо вони нижче допустимої товщини, сильно зношені, мають борозни, биття, тріщини або забруднення, самих нових колодок недостатньо.',
                    },
                    {
                        'q': 'Чому нові гальмівні колодки іноді шумлять?',
                        'a': 'Нові колодки можуть шуміти через неправильну притирку, погану поверхню диска, брудне або зношене кріплення, або невідповідний склад колодки. Постійний шум варто перевірити.',
                    },
                    {
                        'q': 'Чи може стара гальмівна рідина впливати на гальмування з новими колодками?',
                        'a': 'Так. Стара або забруднена гальмівна рідина може робити ручку м’якою чи непередбачуваною. Заміна колодок і сервіс гальмівної рідини - різні операції, але обидві впливають на відчуття гальма й безпеку.',
                    },
                    {
                        'q': 'Sintered колодки кращі за organic?',
                        'a': 'Не універсально. Sintered-колодки часто добре витримують нагрівання й можуть давати сильне гальмування, але правильний вибір залежить від мотоцикла, матеріалу диска, стилю їзди та рекомендацій виробника.',
                    },
                ],
            },
        },
        'keywords': {
            'en': ['motorcycle brake pad replacement', 'motorcycle brake service', 'brake system inspection', 'brake pads Cascais', 'motorcycle service Lisbon', 'Iron Custom Motors brakes'],
            'ru': ['замена тормозных колодок мотоцикла', 'сервис тормозов мотоцикла', 'проверка тормозной системы', 'тормозные колодки Кашкайш', 'мотосервис Лиссабон', 'Iron Custom Motors тормоза'],
            'uk': ['заміна гальмівних колодок мотоцикла', 'сервіс гальм мотоцикла', 'перевірка гальмівної системи', 'гальмівні колодки Cascais', 'мотосервіс Lisbon', 'Iron Custom Motors гальма'],
            'pt': ['substituição pastilhas travão moto', 'serviço de travões moto', 'inspeção sistema de travagem', 'pastilhas de travão Cascais', 'oficina de motos Lisboa', 'Iron Custom Motors travões'],
        },
    }}

BLOG_POSTS['front-fork-service-motorcycle-cascais'] = {'publishedISO': '2026-06-18',
 'modifiedISO': '2026-06-18',
 'imageBase': '/photos/blog/blog-front-fork-service-motorcycle-cascais',
 'imageHero': 1,
 'imageCount': 1,
 'imageDims': {1: (1600, 900)},
 'youtubeUrl': 'https://www.youtube.com/shorts/WkXuGSn0-yw',
 'youtubeEmbed': 'https://www.youtube.com/embed/WkXuGSn0-yw',
 'sourceLocalizedSlugs': {'en': 'front-fork-service-motorcycle-cascais',
                          'ru': 'obsluzhivanie-peredney-vilki-mototsikl-cascais',
                          'pt': 'servico-forquilha-dianteira-moto-cascais',
                          'uk': 'obsluhovuvannia-perednoi-vylky-mototsykl-cascais'},
 'meta': {'en': {'title': 'Front Fork Service: Control Starts at the Front | Iron Custom Motors',
                 'description': 'Why front fork service matters: seals, bushings, clean parts, correct fork '
                                'oil viscosity and precise oil level for safer handling.',
                 'excerpt': 'Why front fork service matters: seals, bushings, clean parts, correct fork oil '
                            'viscosity and precise oil level for safer handling.'},
          'ru': {'title': 'Обслуживание передней вилки: контроль начинается спереди | Iron Custom Motors',
                 'description': 'Почему важно обслуживание вилки: сальники, направляющие, чистые детали, '
                                'правильная вязкость и точный уровень масла.',
                 'excerpt': 'Почему важно обслуживание вилки: сальники, направляющие, чистые детали, '
                            'правильная вязкость и точный уровень масла.'},
          'pt': {'title': 'Serviço da Forquilha Dianteira: Controlo à Frente | Iron Custom Motors',
                 'description': 'Porque o serviço da forquilha é importante: retentores, guias, limpeza, '
                                'óleo correto e nível preciso para melhor controlo.',
                 'excerpt': 'Porque o serviço da forquilha é importante: retentores, guias, limpeza, óleo '
                            'correto e nível preciso para melhor controlo.'},
          'uk': {'title': 'Обслуговування передньої вилки: контроль спереду | Iron Custom Motors',
                 'description': 'Чому важливе обслуговування вилки: сальники, напрямні, чисті деталі, '
                                'правильна олива і точний рівень.',
                 'excerpt': 'Чому важливе обслуговування вилки: сальники, напрямні, чисті деталі, правильна '
                            'олива і точний рівень.'}},
 'body': {'en': {'eyebrow': 'Workshop guide · 18 June 2026',
                 'publishedLabel': 'Published 18 June 2026',
                 'breadHome': 'Home',
                 'breadBlog': 'Blog',
                 'introTitle': 'Fork service is handling service',
                 'videoEyebrow': 'Workshop video',
                 'videoTitle': 'Watch the front fork service',
                 'videoText': 'A short look at front fork service: fork oil, seal inspection, internal '
                              'cleaning and precise setup checked as one handling system.',
                 'videoLink': 'Open on YouTube',
                 'faqTitle': 'Front fork service FAQ',
                 'ctaEyebrow': 'Need fork service?',
                 'ctaTitle': 'Book a front fork inspection.',
                 'btnWA': 'WhatsApp us',
                 'btnBack': 'Back to blog',
                 'imageAlt': 'Front fork service cover graphic showing fork oil service and fork tube work '
                             'in the Iron Custom Motors workshop.',
                 'imageCaption': 'Front fork service at Iron Custom Motors: seals, guides, clean internals, '
                                 'correct fork oil viscosity and precise oil level.',
                 'h1': 'Front Fork Service:<br/><span class="accent">Control Starts at the Front.</span>',
                 'h1Crumb': 'Front Fork Service: Control Starts at the Front',
                 'lede': 'A front fork rarely fails without warning. Usually, the motorcycle starts to feel '
                         'slightly different first. The front end dives more under braking. The bike feels '
                         'vague in corners. There is oil on one fork tube. The handlebar gives a small knock '
                         'over bumps. Or the front tyre no longer feels as planted as it used to. Many '
                         'riders first think about tyres, brakes or wheel balance. Sometimes they are right. '
                         'But very often, the front fork is part of the problem.',
                 'intro': {'title': 'Fork service is handling service',
                           'paragraphs': ['The fork is not just two tubes holding the front wheel. It '
                                          'controls braking stability, steering feel, tyre contact and rider '
                                          'confidence. That is why proper fork service is not just replacing '
                                          'seals. It is diagnosis, cleaning, inspection, correct parts, '
                                          'correct fork oil and precise oil level.',
                                          'At Iron Custom Motors, we treat front fork service as a handling '
                                          'and safety job.']},
                 'sections': [{'title': 'Why It Matters',
                               'paragraphs': ['The front fork supports the front of the motorcycle, absorbs '
                                              'bumps and controls how the bike behaves under braking. When '
                                              'it works properly, the motorcycle turns cleanly, brakes with '
                                              'control and holds the road with confidence.',
                                              'When the fork is tired, the symptoms can be subtle:',
                                              'In Cascais and Lisbon, motorcycles deal with city traffic, '
                                              'speed bumps, coastal roads, humidity, sea air and weekend '
                                              'rides. The fork works constantly, even when the rider does '
                                              'not think about it.'],
                               'bullets': ['excessive dive under braking;',
                                           'vague steering;',
                                           'harshness over small bumps;',
                                           'knocking or clicking from the front;',
                                           'oil around the fork seal;',
                                           'uneven front tyre wear;',
                                           'instability when braking or cornering.']},
                              {'title': 'Fork Seals Are Only the Visible Part',
                               'paragraphs': ['A leaking fork seal is easy to notice, but the seal itself is '
                                              'not always the root cause.',
                                              'Fork seals can fail because of age, dirt, dried '
                                              'contamination, corrosion, stone chips, damaged fork tubes or '
                                              'worn internal guides. If we replace only the seal and ignore '
                                              'the reason it failed, the new seal may start leaking again.',
                                              'That is why we always inspect the fork tubes, dust seals, '
                                              'retaining areas and sealing surfaces before reassembly.']},
                              {'title': 'Bushings and Guides Matter',
                               'paragraphs': ['Inside the fork, bushings and guide components control how '
                                              'smoothly the fork tubes slide. Riders do not see them, but '
                                              'they affect seal life, fork alignment, braking stability and '
                                              'suspension feel.',
                                              'If the guides are worn, the fork can develop play or '
                                              'friction. New seals fitted into a fork with worn bushings are '
                                              'not a proper repair. When needed, we replace the seals and '
                                              'guides together, because the fork must work cleanly as a '
                                              'complete sliding system.']},
                              {'title': 'Fork Oil: Correct Viscosity, Not Guesswork',
                               'paragraphs': ['Fork oil is not just fluid inside the fork. It is part of the '
                                              'damping system.',
                                              'If the oil is too thin for the motorcycle, the fork can feel '
                                              'loose, soft or underdamped. If it is too thick, the fork can '
                                              'feel harsh, slow or sticky over small bumps.',
                                              'The correct viscosity depends on the motorcycle, fork design, '
                                              'rider weight, riding style and manufacturer specification. '
                                              'That is why we do not choose fork oil “by habit.” We use the '
                                              'correct specification for the motorcycle and the actual fork '
                                              'system.']},
                              {'title': 'Oil Level Is Critical',
                               'paragraphs': ['Fork oil level is one of the most important details in this '
                                              'job.',
                                              'Many people think only oil quantity matters. In reality, the '
                                              'oil level — often measured as an air gap — changes how the '
                                              'fork behaves, especially near the end of travel.',
                                              'Too much oil can make the fork harsh and increase internal '
                                              'pressure. Too little oil can reduce support and make the fork '
                                              'dive too much or bottom too easily.',
                                              'The correct level depends on the fork design and service '
                                              'procedure. It should not be estimated by eye. Both fork legs '
                                              'must be measured and matched properly. A few millimeters can '
                                              'change how the front end feels.']},
                              {'title': 'Cleaning Is Part of the Repair',
                               'paragraphs': ['When we service a fork, we do not just drain oil and install '
                                              'new parts.',
                                              'Old fork oil can carry metal particles, seal material, '
                                              'bushing wear residue and dirt. If the fork is assembled '
                                              'dirty, the new oil becomes contaminated quickly and new parts '
                                              'wear faster.',
                                              'All internal parts must be carefully cleaned. In Portugal’s '
                                              'coastal climate, we also pay close attention to corrosion. A '
                                              'small rust mark on a fork tube can damage a new seal very '
                                              'quickly.']},
                              {'title': 'What Riders Often Miss',
                               'bullets': ['A leaking seal may be a symptom, not the cause.',
                                           'Worn bushings can destroy new seals.',
                                           'Fork oil ages even when the bike is not ridden hard.',
                                           'Oil level changes braking feel and support under deep '
                                           'compression.',
                                           'Fork service affects brakes and tyres because it changes how the '
                                           'front tyre loads the road.',
                                           'Both fork legs must work as a matched pair.']},
                              {'title': 'When to Visit a Workshop',
                               'paragraphs': ['Book a fork inspection if you notice:',
                                              'Fork oil leaks should not be ignored. Oil near the front '
                                              'wheel and brakes is a safety issue.'],
                               'bullets': ['oil on the fork tube;',
                                           'dirt stuck around the seal;',
                                           'excessive dive under braking;',
                                           'knocking or looseness at the front;',
                                           'vague steering;',
                                           'harshness over small bumps;',
                                           'unusual front tyre wear;',
                                           'instability during braking;',
                                           'oil near the brake caliper or disc.']},
                              {'title': 'What We Check at Iron Custom Motors',
                               'paragraphs': ['At Iron Custom Motors, front fork service starts with '
                                              'diagnosis.',
                                              'We inspect the fork tubes, seals, dust seals, bushings, '
                                              'guides, springs, oil condition, corrosion and front-end '
                                              'behavior. When seals or guides are worn, we replace what '
                                              'needs to be replaced. We clean all parts thoroughly before '
                                              'assembly.',
                                              'We use fork oil of the correct viscosity and set the oil '
                                              'level precisely according to the motorcycle’s specification. '
                                              'After service, we check alignment, cleanliness, leakage and '
                                              'front-end feel.',
                                              'For custom motorcycles, Harley-Davidson models, touring bikes '
                                              'and premium motorcycles, we also look at the whole system: '
                                              'rider use, tyres, brakes, rear suspension, weight, luggage '
                                              'and real riding conditions around Cascais and Lisbon.']},
                              {'title': 'Conclusion',
                               'paragraphs': ['Front fork service is not just about stopping an oil leak.',
                                              'Fresh seals matter. Good guides matter. Clean internal parts '
                                              'matter. Correct oil viscosity matters. Accurate oil level '
                                              'matters a lot.',
                                              'The front fork is where braking, steering, suspension and '
                                              'tyre grip meet. Servicing it properly gives the rider more '
                                              'control, more confidence and a motorcycle that feels right '
                                              'again.']}],
                 'ctaText': 'If your motorcycle dives too much under braking, feels vague in corners, shows '
                            'oil on the fork tubes or has not had its front fork checked for a long time, '
                            'book a front fork inspection at Iron Custom Motors in Cascais. We will diagnose '
                            'the system properly and service it with the right parts, clean assembly, '
                            'correct oil and precise oil level.',
                 'faqs': [{'q': 'How do I know if my fork seals are leaking?',
                           'a': 'Oil on the fork tube, wetness around the seal or dirt sticking to the fork '
                                'leg are common signs. If the leak gets worse, it can affect damping and '
                                'contaminate brake components.'},
                          {'q': 'Is replacing fork seals enough?',
                           'a': 'Not always. The fork tubes, guides, bushings and internal condition must '
                                'also be checked. If these parts are worn, new seals may fail again.'},
                          {'q': 'Why is fork oil viscosity important?',
                           'a': 'Fork oil controls damping. The wrong viscosity can make the fork too soft, '
                                'too harsh, too slow or inconsistent.'},
                          {'q': 'Why is fork oil level important?',
                           'a': 'Oil level changes the air chamber inside the fork. It affects support under '
                                'braking and deep compression. Incorrect level can seriously change the '
                                'front-end feel.'},
                          {'q': 'Does fork service affect braking?',
                           'a': 'Yes. The fork controls how the front tyre is loaded under braking. Poor '
                                'fork condition can make braking feel unstable or less predictable.'}]},
          'ru': {'eyebrow': 'Гайд мастерской · 18 июня 2026',
                 'publishedLabel': 'Опубликовано 18 июня 2026',
                 'breadHome': 'Главная',
                 'breadBlog': 'Блог',
                 'introTitle': 'Сервис вилки — это управляемость',
                 'videoEyebrow': 'Видео из мастерской',
                 'videoTitle': 'Смотрите обслуживание передней вилки',
                 'videoText': 'Короткий взгляд на обслуживание вилки: масло, проверка сальников, внутренняя '
                              'мойка и точная настройка как единая система управляемости.',
                 'videoLink': 'Открыть на YouTube',
                 'faqTitle': 'FAQ по обслуживанию передней вилки',
                 'ctaEyebrow': 'Нужен сервис вилки?',
                 'ctaTitle': 'Запишитесь на диагностику передней вилки.',
                 'btnWA': 'WhatsApp',
                 'btnBack': 'Назад в блог',
                 'imageAlt': 'Обложка статьи про обслуживание передней вилки: сервис масла и работа с пером '
                             'вилки в мастерской Iron Custom Motors.',
                 'imageCaption': 'Обслуживание передней вилки в Iron Custom Motors: сальники, направляющие, '
                                 'чистые внутренние детали, правильная вязкость и точный уровень масла.',
                 'h1': 'Обслуживание передней вилки:<br/><span class="accent">контроль начинается '
                       'спереди.</span>',
                 'h1Crumb': 'Обслуживание передней вилки: контроль начинается спереди',
                 'lede': 'Передняя вилка редко выходит из строя без предупреждения. Чаще мотоцикл просто '
                         'начинает ощущаться немного иначе. Перед сильнее клюёт при торможении. Мотоцикл '
                         'становится менее точным в поворотах. На одном пере появляется масляная плёнка. На '
                         'неровностях слышен лёгкий стук. Или переднее колесо уже не даёт той уверенности, '
                         'что раньше. Многие сначала думают о шинах, тормозах или балансировке. Иногда '
                         'причина действительно там. Но очень часто передняя вилка тоже участвует в '
                         'проблеме.',
                 'intro': {'title': 'Сервис вилки — это управляемость',
                           'paragraphs': ['Вилка — это не просто две трубы, которые держат колесо. Она '
                                          'отвечает за стабильность при торможении, точность руления, '
                                          'контакт шины с дорогой и уверенность райдера. Поэтому нормальное '
                                          'обслуживание вилки — это не только замена сальников. Это '
                                          'диагностика, мойка, проверка деталей, правильные сальники и '
                                          'направляющие, правильное масло и точный уровень масла.',
                                          'В Iron Custom Motors мы относимся к обслуживанию вилки как к '
                                          'работе с управляемостью и безопасностью.']},
                 'sections': [{'title': 'Почему это важно',
                               'paragraphs': ['Передняя вилка поддерживает перед мотоцикла, гасит неровности '
                                              'и контролирует поведение байка при торможении. Когда она '
                                              'работает правильно, мотоцикл охотно поворачивает, стабильно '
                                              'тормозит и уверенно держит дорогу.',
                                              'Когда вилка устала, симптомы могут быть незаметными:',
                                              'В Cascais и Lisbon мотоциклы постоянно работают в смешанных '
                                              'условиях: город, лежачие полицейские, прибрежные дороги, '
                                              'влажность, морской воздух и поездки выходного дня. Вилка '
                                              'трудится всё время, даже когда райдер об этом не думает.'],
                               'bullets': ['слишком сильный клевок при торможении;',
                                           'нечёткое руление;',
                                           'жёсткая работа на мелких неровностях;',
                                           'стук или щелчки спереди;',
                                           'масло возле сальника;',
                                           'неравномерный износ передней шины;',
                                           'нестабильность при торможении или в повороте.']},
                              {'title': 'Сальники — только видимая часть проблемы',
                               'paragraphs': ['Потёкший сальник легко заметить, но сам сальник не всегда '
                                              'является главной причиной.',
                                              'Сальники могут выходить из строя из-за возраста, грязи, '
                                              'засохшего налёта, коррозии, сколов на пере, повреждённой '
                                              'трубы или изношенных направляющих. Если просто заменить '
                                              'сальник и не найти причину, новый сальник может снова потечь.',
                                              'Поэтому перед сборкой мы проверяем перья, пыльники, '
                                              'посадочные места, стопорные зоны и рабочие поверхности.']},
                              {'title': 'Направляющие имеют значение',
                               'paragraphs': ['Внутри вилки направляющие и втулки контролируют, насколько '
                                              'ровно и плавно двигаются трубы. Снаружи их не видно, но они '
                                              'влияют на ресурс сальников, геометрию вилки, стабильность при '
                                              'торможении и работу подвески.',
                                              'Если направляющие изношены, появляется люфт или лишнее '
                                              'трение. Новые сальники в вилке с уставшими направляющими — '
                                              'это не полноценный ремонт. Когда нужно, мы меняем сальники и '
                                              'направляющие вместе, чтобы вилка работала как чистая и точная '
                                              'скользящая система.']},
                              {'title': 'Масло в вилке: правильная вязкость, а не привычка',
                               'paragraphs': ['Масло в вилке — это не просто жидкость внутри. Оно является '
                                              'частью системы демпфирования.',
                                              'Если масло слишком жидкое для конкретной вилки, перед может '
                                              'стать мягким, рыхлым и недодемпфированным. Если слишком '
                                              'густое — вилка может работать жёстко, медленно и липко на '
                                              'мелких неровностях.',
                                              'Правильная вязкость зависит от мотоцикла, конструкции вилки, '
                                              'веса райдера, стиля езды и спецификации производителя. '
                                              'Поэтому мы не выбираем масло “по привычке”. Мы используем '
                                              'спецификацию конкретного мотоцикла и фактической вилки.']},
                              {'title': 'Уровень масла критически важен',
                               'paragraphs': ['Уровень масла в вилке — один из самых важных моментов этой '
                                              'работы.',
                                              'Многие думают только об объёме масла. На практике уровень, '
                                              'часто измеряемый как воздушный зазор, меняет поведение вилки, '
                                              'особенно в конце хода.',
                                              'Слишком высокий уровень может сделать вилку жёсткой и поднять '
                                              'внутреннее давление. Слишком низкий — уменьшить поддержку, '
                                              'усилить клевок и привести к пробою.',
                                              'Правильный уровень зависит от конструкции вилки и процедуры '
                                              'обслуживания. Его нельзя выставлять “на глаз”. Оба пера '
                                              'должны быть точно измерены и согласованы между собой. Иногда '
                                              'несколько миллиметров заметно меняют ощущение передка.']},
                              {'title': 'Мойка деталей — часть ремонта',
                               'paragraphs': ['При обслуживании вилки мы не просто сливаем масло и ставим '
                                              'новые детали.',
                                              'Старое масло может содержать металлическую пыль, остатки '
                                              'сальников, продукты износа направляющих и грязь. Если собрать '
                                              'вилку грязной, новое масло быстро загрязнится, а новые детали '
                                              'будут изнашиваться быстрее.',
                                              'Все внутренние детали нужно тщательно вымыть. В прибрежном '
                                              'климате Португалии мы также внимательно смотрим на коррозию. '
                                              'Маленькая точка ржавчины на пере может быстро повредить новый '
                                              'сальник.']},
                              {'title': 'Что райдеры часто упускают',
                               'bullets': ['Потёкший сальник может быть симптомом, а не причиной.',
                                           'Изношенные направляющие могут быстро убить новые сальники.',
                                           'Масло в вилке стареет даже без агрессивной езды.',
                                           'Уровень масла меняет поддержку при торможении и глубоком ходе '
                                           'вилки.',
                                           'Обслуживание вилки влияет на тормоза и шины, потому что меняет '
                                           'загрузку переднего колеса.',
                                           'Оба пера должны работать как пара.']},
                              {'title': 'Когда ехать в мастерскую',
                               'paragraphs': ['Запишитесь на диагностику вилки, если заметили:',
                                              'Течь вилочного масла нельзя игнорировать. Масло рядом с '
                                              'передним колесом и тормозами — это вопрос безопасности.'],
                               'bullets': ['масло на пере вилки;',
                                           'грязь вокруг сальника;',
                                           'слишком сильный клевок при торможении;',
                                           'стук или люфт спереди;',
                                           'нечёткое руление;',
                                           'жёсткость на мелких неровностях;',
                                           'необычный износ передней шины;',
                                           'нестабильность при торможении;',
                                           'масло возле суппорта или тормозного диска.']},
                              {'title': 'Что мы проверяем в Iron Custom Motors',
                               'paragraphs': ['В Iron Custom Motors обслуживание передней вилки начинается с '
                                              'диагностики.',
                                              'Мы проверяем перья, сальники, пыльники, направляющие, '
                                              'пружины, состояние масла, коррозию и общее поведение передней '
                                              'части. Если сальники или направляющие изношены, мы меняем то, '
                                              'что действительно требует замены. Перед сборкой все детали '
                                              'тщательно очищаются.',
                                              'Мы используем масло нужной вязкости и точно выставляем '
                                              'уровень согласно спецификации мотоцикла. После обслуживания '
                                              'проверяем выравнивание, чистоту, отсутствие течей и ощущение '
                                              'передней части.',
                                              'Для кастомных мотоциклов, Harley-Davidson, touring и '
                                              'премиальных байков мы также смотрим на систему целиком: стиль '
                                              'езды, шины, тормоза, заднюю подвеску, вес, багаж и реальные '
                                              'условия эксплуатации в Cascais и Lisbon.']},
                              {'title': 'Вывод',
                               'paragraphs': ['Обслуживание передней вилки — это не только устранение течи '
                                              'масла.',
                                              'Свежие сальники важны. Хорошие направляющие важны. Чистые '
                                              'внутренние детали важны. Правильная вязкость масла важна. '
                                              'Точный уровень масла очень важен.',
                                              'Передняя вилка — место, где сходятся торможение, руление, '
                                              'подвеска и сцепление шины с дорогой. Правильное обслуживание '
                                              'возвращает райдеру контроль, уверенность и ощущение, что '
                                              'мотоцикл снова работает как надо.']}],
                 'ctaText': 'Если ваш мотоцикл слишком сильно клюёт при торможении, стал нечётким в '
                            'поворотах, показывает масло на перьях или давно не проходил проверку передней '
                            'вилки, запишитесь на диагностику в Iron Custom Motors в Cascais. Мы правильно '
                            'проверим систему и обслужим вилку с нужными деталями, чистой сборкой, '
                            'правильным маслом и точным уровнем.',
                 'faqs': [{'q': 'Как понять, что сальники вилки текут?',
                           'a': 'Типичные признаки — масло на пере, влажность вокруг сальника или грязь, '
                                'которая липнет к вилке. Если течь усиливается, она может повлиять на '
                                'демпфирование и загрязнить тормозные элементы.'},
                          {'q': 'Достаточно ли просто заменить сальники?',
                           'a': 'Не всегда. Нужно проверить перья, направляющие, втулки и внутреннее '
                                'состояние вилки. Если эти детали изношены, новые сальники могут снова '
                                'быстро потечь.'},
                          {'q': 'Почему важна вязкость вилочного масла?',
                           'a': 'Вилочное масло отвечает за демпфирование. Неправильная вязкость может '
                                'сделать вилку слишком мягкой, слишком жёсткой, медленной или нестабильной.'},
                          {'q': 'Почему важен уровень масла?',
                           'a': 'Уровень масла меняет воздушную камеру внутри вилки. Это влияет на поддержку '
                                'при торможении и глубоком сжатии. Неправильный уровень может серьёзно '
                                'изменить ощущение передней части.'},
                          {'q': 'Влияет ли обслуживание вилки на торможение?',
                           'a': 'Да. Вилка контролирует загрузку передней шины при торможении. Плохое '
                                'состояние вилки может сделать торможение менее стабильным и '
                                'предсказуемым.'}]},
          'pt': {'eyebrow': 'Guia de oficina · 18 junho 2026',
                 'publishedLabel': 'Publicado 18 junho 2026',
                 'breadHome': 'Início',
                 'breadBlog': 'Blog',
                 'introTitle': 'Serviço da forquilha é controlo',
                 'videoEyebrow': 'Vídeo de oficina',
                 'videoTitle': 'Veja o serviço da forquilha dianteira',
                 'videoText': 'Um olhar rápido ao serviço da forquilha: óleo, inspeção de retentores, '
                              'limpeza interna e afinação precisa como um só sistema de controlo.',
                 'videoLink': 'Abrir no YouTube',
                 'faqTitle': 'FAQ sobre serviço da forquilha dianteira',
                 'ctaEyebrow': 'Precisa de serviço da forquilha?',
                 'ctaTitle': 'Marque uma inspeção da forquilha dianteira.',
                 'btnWA': 'WhatsApp',
                 'btnBack': 'Voltar ao blog',
                 'imageAlt': 'Capa do artigo sobre serviço da forquilha dianteira: óleo de forquilha e '
                             'trabalho no tubo na oficina Iron Custom Motors.',
                 'imageCaption': 'Serviço da forquilha dianteira na Iron Custom Motors: retentores, guias, '
                                 'peças internas limpas, óleo correto e nível preciso.',
                 'h1': 'Serviço da Forquilha Dianteira:<br/><span class="accent">controlo à frente.</span>',
                 'h1Crumb': 'Serviço da Forquilha Dianteira: o Controlo Começa à Frente',
                 'lede': 'Uma forquilha dianteira raramente falha sem avisar. Normalmente, a moto começa '
                         'primeiro a sentir-se ligeiramente diferente. A frente afunda mais ao travar. A '
                         'moto fica menos precisa nas curvas. Aparece óleo num dos tubos. O guiador dá uma '
                         'pequena pancada em pisos irregulares. Ou o pneu dianteiro já não transmite a mesma '
                         'confiança. Muitos motociclistas pensam primeiro em pneus, travões ou equilibragem. '
                         'Às vezes estão certos. Mas muitas vezes a forquilha dianteira também faz parte do '
                         'problema.',
                 'intro': {'title': 'Serviço da forquilha é controlo',
                           'paragraphs': ['A forquilha não são apenas dois tubos que seguram a roda '
                                          'dianteira. Ela controla a estabilidade na travagem, a sensação de '
                                          'direção, o contacto do pneu com a estrada e a confiança do '
                                          'condutor. Por isso, um bom serviço de forquilha não é apenas '
                                          'trocar retentores. É diagnóstico, limpeza, inspeção, peças '
                                          'corretas, óleo adequado e nível de óleo preciso.',
                                          'Na Iron Custom Motors, tratamos o serviço da forquilha como um '
                                          'trabalho de segurança e comportamento dinâmico.']},
                 'sections': [{'title': 'Porque É Importante',
                               'paragraphs': ['A forquilha dianteira suporta a frente da moto, absorve '
                                              'irregularidades e controla o comportamento da moto durante a '
                                              'travagem. Quando trabalha corretamente, a moto vira com '
                                              'precisão, trava com controlo e mantém a estrada com '
                                              'confiança.',
                                              'Quando a forquilha está cansada, os sintomas podem ser '
                                              'subtis:',
                                              'Em Cascais e Lisboa, as motos vivem num ambiente exigente: '
                                              'trânsito urbano, lombas, estradas costeiras, humidade, ar '
                                              'marítimo e passeios de fim de semana. A forquilha trabalha '
                                              'constantemente, mesmo quando o condutor não pensa nisso.'],
                               'bullets': ['afundamento excessivo ao travar;',
                                           'direção pouco precisa;',
                                           'dureza em pequenas irregularidades;',
                                           'batidas ou cliques na frente;',
                                           'óleo junto ao retentor;',
                                           'desgaste irregular do pneu dianteiro;',
                                           'instabilidade ao travar ou curvar.']},
                              {'title': 'Os Retentores São Apenas a Parte Visível',
                               'paragraphs': ['Um retentor com fuga é fácil de ver, mas o retentor nem '
                                              'sempre é a causa principal.',
                                              'Os retentores podem falhar por idade, sujidade, contaminação '
                                              'seca, corrosão, marcas de pedra, tubos danificados ou guias '
                                              'internas gastas. Se trocarmos apenas o retentor e ignorarmos '
                                              'a causa, o novo retentor pode voltar a perder óleo.',
                                              'Por isso, antes da montagem verificamos os tubos, guarda-pós, '
                                              'zonas de retenção e superfícies de vedação.']},
                              {'title': 'Buchas e Guias Também Contam',
                               'paragraphs': ['Dentro da forquilha, buchas e componentes de guia controlam o '
                                              'deslizamento dos tubos. O condutor não os vê, mas eles afetam '
                                              'a vida dos retentores, o alinhamento da forquilha, a '
                                              'estabilidade na travagem e a sensação da suspensão.',
                                              'Se as guias estiverem gastas, a forquilha pode ganhar folga '
                                              'ou fricção. Montar retentores novos numa forquilha com buchas '
                                              'gastas não é um serviço completo. Quando necessário, '
                                              'substituímos retentores e guias em conjunto para que a '
                                              'forquilha trabalhe como um sistema de deslizamento limpo e '
                                              'preciso.']},
                              {'title': 'Óleo da Forquilha: Viscosidade Correta, Não Hábito',
                               'paragraphs': ['O óleo da forquilha não é apenas um fluido dentro do tubo. '
                                              'Ele faz parte do sistema de amortecimento.',
                                              'Se o óleo for demasiado fino para aquela moto, a forquilha '
                                              'pode ficar mole, solta ou com pouco amortecimento. Se for '
                                              'demasiado espesso, pode ficar dura, lenta ou presa em '
                                              'pequenas irregularidades.',
                                              'A viscosidade correta depende da moto, do desenho da '
                                              'forquilha, do peso do condutor, do estilo de condução e da '
                                              'especificação do fabricante. Por isso, não escolhemos óleo '
                                              '“por hábito”. Usamos a especificação correta para a moto e '
                                              'para o sistema real da forquilha.']},
                              {'title': 'O Nível de Óleo É Crítico',
                               'paragraphs': ['O nível do óleo da forquilha é um dos detalhes mais '
                                              'importantes deste serviço.',
                                              'Muitas pessoas pensam apenas na quantidade de óleo. Na '
                                              'prática, o nível — muitas vezes medido como air gap — altera '
                                              'o comportamento da forquilha, especialmente no fim do curso.',
                                              'Óleo a mais pode tornar a forquilha dura e aumentar a pressão '
                                              'interna. Óleo a menos pode reduzir suporte, aumentar o '
                                              'afundamento e facilitar o fim de curso.',
                                              'O nível correto depende do desenho da forquilha e do '
                                              'procedimento de serviço. Não deve ser feito “a olho”. As duas '
                                              'pernas devem ser medidas e igualadas corretamente. Alguns '
                                              'milímetros podem mudar a sensação da frente.']},
                              {'title': 'A Limpeza Faz Parte da Reparação',
                               'paragraphs': ['Ao fazer serviço de forquilha, não basta drenar óleo e montar '
                                              'peças novas.',
                                              'O óleo antigo pode transportar partículas metálicas, material '
                                              'de retentor, resíduos de desgaste das buchas e sujidade. Se a '
                                              'forquilha for montada suja, o óleo novo contamina-se '
                                              'rapidamente e as peças novas gastam-se mais cedo.',
                                              'Todas as peças internas devem ser bem limpas. No clima '
                                              'costeiro de Portugal, também prestamos atenção à corrosão. '
                                              'Uma pequena marca de ferrugem no tubo pode danificar '
                                              'rapidamente um retentor novo.']},
                              {'title': 'O Que Muitos Motociclistas Não Veem',
                               'bullets': ['Um retentor com fuga pode ser sintoma, não causa.',
                                           'Buchas gastas podem destruir retentores novos.',
                                           'O óleo da forquilha envelhece mesmo sem condução agressiva.',
                                           'O nível de óleo altera o suporte na travagem e em compressão '
                                           'profunda.',
                                           'O serviço da forquilha influencia travões e pneus, porque muda a '
                                           'carga no pneu dianteiro.',
                                           'As duas pernas da forquilha devem trabalhar como um par.']},
                              {'title': 'Quando Visitar a Oficina',
                               'paragraphs': ['Marque uma inspeção da forquilha se notar:',
                                              'Fugas de óleo da forquilha não devem ser ignoradas. Óleo '
                                              'perto da roda dianteira e dos travões é uma questão de '
                                              'segurança.'],
                               'bullets': ['óleo no tubo da forquilha;',
                                           'sujidade presa junto ao retentor;',
                                           'afundamento excessivo ao travar;',
                                           'batida ou folga na frente;',
                                           'direção pouco precisa;',
                                           'dureza em pequenas irregularidades;',
                                           'desgaste estranho do pneu dianteiro;',
                                           'instabilidade na travagem;',
                                           'óleo perto da pinça ou do disco de travão.']},
                              {'title': 'O Que Verificamos na Iron Custom Motors',
                               'paragraphs': ['Na Iron Custom Motors, o serviço da forquilha dianteira '
                                              'começa com diagnóstico.',
                                              'Verificamos tubos, retentores, guarda-pós, buchas, guias, '
                                              'molas, estado do óleo, corrosão e comportamento geral da '
                                              'frente. Quando retentores ou guias estão gastos, substituímos '
                                              'o que precisa de ser substituído. Antes da montagem, limpamos '
                                              'cuidadosamente todas as peças.',
                                              'Usamos óleo de viscosidade correta e ajustamos o nível de '
                                              'óleo com precisão, de acordo com a especificação da moto. '
                                              'Depois do serviço, verificamos alinhamento, limpeza, fugas e '
                                              'sensação da frente.',
                                              'Em motos custom, Harley-Davidson, touring e motos premium, '
                                              'olhamos também para o sistema completo: utilização do '
                                              'condutor, pneus, travões, suspensão traseira, peso, bagagem e '
                                              'condições reais de condução em Cascais e Lisboa.']},
                              {'title': 'Conclusão',
                               'paragraphs': ['O serviço da forquilha dianteira não serve apenas para parar '
                                              'uma fuga de óleo.',
                                              'Retentores novos importam. Guias em bom estado importam. '
                                              'Peças internas limpas importam. A viscosidade correta do óleo '
                                              'importa. O nível exato de óleo importa muito.',
                                              'A forquilha dianteira é onde travagem, direção, suspensão e '
                                              'aderência do pneu se encontram. Um serviço bem feito devolve '
                                              'controlo, confiança e uma moto que volta a sentir-se '
                                              'certa.']}],
                 'ctaText': 'Se a sua moto afunda demasiado ao travar, parece vaga nas curvas, mostra óleo '
                            'nos tubos da forquilha ou não faz uma verificação da frente há muito tempo, '
                            'marque uma inspeção na Iron Custom Motors em Cascais. Vamos diagnosticar o '
                            'sistema corretamente e fazer o serviço com as peças certas, montagem limpa, '
                            'óleo correto e nível preciso.',
                 'faqs': [{'q': 'Como sei se os retentores da forquilha estão a perder óleo?',
                           'a': 'Óleo no tubo, humidade junto ao retentor ou sujidade colada à perna da '
                                'forquilha são sinais comuns. Se a fuga piorar, pode afetar o amortecimento '
                                'e contaminar os travões.'},
                          {'q': 'Trocar os retentores é suficiente?',
                           'a': 'Nem sempre. Tubos, guias, buchas e estado interno da forquilha também devem '
                                'ser verificados. Se estas peças estiverem gastas, os retentores novos podem '
                                'voltar a falhar.'},
                          {'q': 'Porque é importante a viscosidade do óleo da forquilha?',
                           'a': 'O óleo controla o amortecimento. A viscosidade errada pode tornar a '
                                'forquilha demasiado mole, dura, lenta ou inconsistente.'},
                          {'q': 'Porque é importante o nível de óleo?',
                           'a': 'O nível de óleo altera a câmara de ar dentro da forquilha. Isso influencia '
                                'o suporte na travagem e em compressão profunda. Um nível incorreto pode '
                                'mudar muito a sensação da frente.'},
                          {'q': 'O serviço da forquilha afeta a travagem?',
                           'a': 'Sim. A forquilha controla a carga no pneu dianteiro durante a travagem. Uma '
                                'forquilha em mau estado pode tornar a travagem menos estável e '
                                'previsível.'}]},
          'uk': {'eyebrow': 'Гайд майстерні · 18 червня 2026',
                 'publishedLabel': 'Опубліковано 18 червня 2026',
                 'breadHome': 'Головна',
                 'breadBlog': 'Блог',
                 'introTitle': 'Сервіс вилки — це керованість',
                 'videoEyebrow': 'Відео з майстерні',
                 'videoTitle': 'Дивіться обслуговування передньої вилки',
                 'videoText': 'Короткий погляд на сервіс вилки: олива, перевірка сальників, внутрішнє '
                              'очищення і точне налаштування як єдина система керованості.',
                 'videoLink': 'Відкрити на YouTube',
                 'faqTitle': 'FAQ щодо обслуговування передньої вилки',
                 'ctaEyebrow': 'Потрібен сервіс вилки?',
                 'ctaTitle': 'Запишіться на діагностику передньої вилки.',
                 'btnWA': 'WhatsApp',
                 'btnBack': 'Назад до блогу',
                 'imageAlt': 'Обкладинка статті про обслуговування передньої вилки: сервіс оливи та робота з '
                             'пером вилки в майстерні Iron Custom Motors.',
                 'imageCaption': 'Обслуговування передньої вилки в Iron Custom Motors: сальники, напрямні, '
                                 'чисті внутрішні деталі, правильна олива і точний рівень.',
                 'h1': 'Обслуговування передньої вилки:<br/><span class="accent">контроль починається '
                       'спереду.</span>',
                 'h1Crumb': 'Обслуговування передньої вилки: контроль починається спереду',
                 'lede': 'Передня вилка рідко виходить з ладу без попередження. Зазвичай мотоцикл спочатку '
                         'просто починає відчуватися трохи інакше. Перед сильніше клює під час гальмування. '
                         'Мотоцикл стає менш точним у поворотах. На одному пері з’являється масляна плівка. '
                         'На нерівностях чути легкий стук. Або переднє колесо вже не дає тієї впевненості, '
                         'що раніше. Багато райдерів спочатку думають про шини, гальма або балансування. '
                         'Іноді причина справді там. Але дуже часто передня вилка теж є частиною проблеми.',
                 'intro': {'title': 'Сервіс вилки — це керованість',
                           'paragraphs': ['Вилка — це не просто дві труби, які тримають колесо. Вона '
                                          'відповідає за стабільність під час гальмування, точність керма, '
                                          'контакт шини з дорогою і впевненість райдера. Тому правильне '
                                          'обслуговування вилки — це не лише заміна сальників. Це '
                                          'діагностика, очищення, перевірка деталей, правильні сальники й '
                                          'напрямні, правильна олива і точний рівень оливи.',
                                          'В Iron Custom Motors ми ставимося до обслуговування передньої '
                                          'вилки як до роботи з керованістю та безпекою.']},
                 'sections': [{'title': 'Чому це важливо',
                               'paragraphs': ['Передня вилка підтримує перед мотоцикла, поглинає нерівності '
                                              'та контролює поведінку байка під час гальмування. Коли вона '
                                              'працює правильно, мотоцикл чітко повертає, стабільно гальмує '
                                              'і впевнено тримає дорогу.',
                                              'Коли вилка втомлена, симптоми можуть бути непомітними:',
                                              'У Cascais та Lisbon мотоцикли працюють у змішаних умовах: '
                                              'місто, лежачі поліцейські, прибережні дороги, вологість, '
                                              'морське повітря і поїздки на вихідних. Вилка працює постійно, '
                                              'навіть коли райдер про це не думає.'],
                               'bullets': ['надмірний клювок під час гальмування;',
                                           'нечітке кермування;',
                                           'жорстка робота на дрібних нерівностях;',
                                           'стукіт або клацання спереду;',
                                           'олива біля сальника;',
                                           'нерівномірний знос передньої шини;',
                                           'нестабільність під час гальмування або в повороті.']},
                              {'title': 'Сальники — лише видима частина проблеми',
                               'paragraphs': ['Сальник, що потік, легко помітити, але сам сальник не завжди '
                                              'є головною причиною.',
                                              'Сальники можуть виходити з ладу через вік, бруд, засохлі '
                                              'забруднення, корозію, сколи на пері, пошкоджену трубу або '
                                              'зношені внутрішні напрямні. Якщо замінити лише сальник і не '
                                              'знайти причину, новий сальник може знову потекти.',
                                              'Тому перед складанням ми перевіряємо пера, пильники, '
                                              'посадкові місця, стопорні зони та робочі поверхні.']},
                              {'title': 'Напрямні мають значення',
                               'paragraphs': ['Всередині вилки напрямні та втулки контролюють, наскільки '
                                              'рівно і плавно рухаються труби. Райдер їх не бачить, але вони '
                                              'впливають на ресурс сальників, вирівнювання вилки, '
                                              'стабільність під час гальмування і роботу підвіски.',
                                              'Якщо напрямні зношені, з’являється люфт або зайве тертя. Нові '
                                              'сальники у вилці зі зношеними напрямними — це не повноцінний '
                                              'ремонт. Коли потрібно, ми міняємо сальники й напрямні разом, '
                                              'щоб вилка працювала як чиста і точна ковзна система.']},
                              {'title': 'Олива у вилці: правильна в’язкість, а не звичка',
                               'paragraphs': ['Олива у вилці — це не просто рідина всередині. Вона є '
                                              'частиною системи демпфування.',
                                              'Якщо олива занадто рідка для конкретного мотоцикла, вилка '
                                              'може бути м’якою, розхлябаною і недостатньо демпфованою. Якщо '
                                              'занадто густа — вона може працювати жорстко, повільно або '
                                              'липко на дрібних нерівностях.',
                                              'Правильна в’язкість залежить від мотоцикла, конструкції '
                                              'вилки, ваги райдера, стилю їзди та специфікації виробника. '
                                              'Тому ми не обираємо оливу “за звичкою”. Ми використовуємо '
                                              'правильну специфікацію для конкретного мотоцикла і фактичної '
                                              'вилки.']},
                              {'title': 'Рівень оливи критично важливий',
                               'paragraphs': ['Рівень оливи у вилці — один із найважливіших моментів цієї '
                                              'роботи.',
                                              'Багато хто думає лише про кількість оливи. Насправді рівень, '
                                              'який часто вимірюється як повітряний зазор, змінює поведінку '
                                              'вилки, особливо наприкінці ходу.',
                                              'Занадто високий рівень може зробити вилку жорсткою і '
                                              'підвищити внутрішній тиск. Занадто низький — зменшити '
                                              'підтримку, посилити клювок і сприяти пробою.',
                                              'Правильний рівень залежить від конструкції вилки і процедури '
                                              'обслуговування. Його не можна виставляти “на око”. Обидва '
                                              'пера мають бути точно виміряні та узгоджені між собою. Кілька '
                                              'міліметрів можуть змінити відчуття передньої частини.']},
                              {'title': 'Очищення — частина ремонту',
                               'paragraphs': ['Під час обслуговування вилки ми не просто зливаємо оливу і '
                                              'ставимо нові деталі.',
                                              'Стара олива може містити металевий пил, залишки сальників, '
                                              'продукти зносу напрямних і бруд. Якщо зібрати вилку брудною, '
                                              'нова олива швидко забрудниться, а нові деталі зношуватимуться '
                                              'швидше.',
                                              'Усі внутрішні деталі потрібно ретельно очистити. У '
                                              'прибережному кліматі Португалії ми також уважно дивимося на '
                                              'корозію. Маленька точка іржі на пері може швидко пошкодити '
                                              'новий сальник.']},
                              {'title': 'Що райдери часто не помічають',
                               'bullets': ['Сальник, що потік, може бути симптомом, а не причиною.',
                                           'Зношені напрямні можуть швидко знищити нові сальники.',
                                           'Олива у вилці старіє навіть без агресивної їзди.',
                                           'Рівень оливи змінює підтримку під час гальмування і глибокого '
                                           'стискання.',
                                           'Обслуговування вилки впливає на гальма і шини, бо змінює '
                                           'навантаження на переднє колесо.',
                                           'Обидва пера мають працювати як пара.']},
                              {'title': 'Коли варто звернутися до майстерні',
                               'paragraphs': ['Запишіться на діагностику вилки, якщо помітили:',
                                              'Підтікання вилкової оливи не можна ігнорувати. Олива біля '
                                              'переднього колеса і гальм — це питання безпеки.'],
                               'bullets': ['оливу на пері вилки;',
                                           'бруд навколо сальника;',
                                           'надмірний клювок під час гальмування;',
                                           'стукіт або люфт спереду;',
                                           'нечітке кермування;',
                                           'жорсткість на дрібних нерівностях;',
                                           'незвичний знос передньої шини;',
                                           'нестабільність під час гальмування;',
                                           'оливу біля супорта або гальмівного диска.']},
                              {'title': 'Що ми перевіряємо в Iron Custom Motors',
                               'paragraphs': ['В Iron Custom Motors обслуговування передньої вилки '
                                              'починається з діагностики.',
                                              'Ми перевіряємо пера, сальники, пильники, напрямні, пружини, '
                                              'стан оливи, корозію і загальну поведінку передньої частини. '
                                              'Якщо сальники або напрямні зношені, ми міняємо те, що справді '
                                              'потребує заміни. Перед складанням усі деталі ретельно '
                                              'очищуються.',
                                              'Ми використовуємо оливу правильної в’язкості і точно '
                                              'виставляємо рівень відповідно до специфікації мотоцикла. '
                                              'Після обслуговування перевіряємо вирівнювання, чистоту, '
                                              'відсутність підтікань і відчуття передньої частини.',
                                              'Для кастомних мотоциклів, Harley-Davidson, touring і '
                                              'преміальних байків ми також дивимося на систему в цілому: '
                                              'стиль їзди, шини, гальма, задню підвіску, вагу, багаж і '
                                              'реальні умови експлуатації в Cascais та Lisbon.']},
                              {'title': 'Висновок',
                               'paragraphs': ['Обслуговування передньої вилки — це не лише усунення '
                                              'підтікання оливи.',
                                              'Свіжі сальники важливі. Хороші напрямні важливі. Чисті '
                                              'внутрішні деталі важливі. Правильна в’язкість оливи важлива. '
                                              'Точний рівень оливи дуже важливий.',
                                              'Передня вилка — це місце, де зустрічаються гальмування, '
                                              'кермування, підвіска і зчеплення шини з дорогою. Правильне '
                                              'обслуговування повертає райдеру контроль, впевненість і '
                                              'відчуття, що мотоцикл знову працює як треба.']}],
                 'ctaText': 'Якщо ваш мотоцикл занадто сильно клює під час гальмування, нечітко поводиться в '
                            'поворотах, має оливу на перах або давно не проходив перевірку передньої вилки, '
                            'запишіться на діагностику в Iron Custom Motors у Cascais. Ми правильно '
                            'перевіримо систему і обслужимо вилку з потрібними деталями, чистим складанням, '
                            'правильною оливою і точним рівнем.',
                 'faqs': [{'q': 'Як зрозуміти, що сальники вилки течуть?',
                           'a': 'Типові ознаки — олива на пері, вологість біля сальника або бруд, що '
                                'прилипає до вилки. Якщо підтікання посилюється, воно може вплинути на '
                                'демпфування і забруднити гальмівні елементи.'},
                          {'q': 'Чи достатньо просто замінити сальники?',
                           'a': 'Не завжди. Потрібно перевірити пера, напрямні, втулки і внутрішній стан '
                                'вилки. Якщо ці деталі зношені, нові сальники можуть знову швидко потекти.'},
                          {'q': 'Чому важлива в’язкість вилкової оливи?',
                           'a': 'Вилкова олива відповідає за демпфування. Неправильна в’язкість може зробити '
                                'вилку занадто м’якою, занадто жорсткою, повільною або нестабільною.'},
                          {'q': 'Чому важливий рівень оливи?',
                           'a': 'Рівень оливи змінює повітряну камеру всередині вилки. Це впливає на '
                                'підтримку під час гальмування і глибокого стискання. Неправильний рівень '
                                'може сильно змінити відчуття передньої частини.'},
                          {'q': 'Чи впливає обслуговування вилки на гальмування?',
                           'a': 'Так. Вилка контролює навантаження передньої шини під час гальмування. '
                                'Поганий стан вилки може зробити гальмування менш стабільним і '
                                'передбачуваним.'}]}},
 'keywords': {'en': ['front fork service',
                     'motorcycle fork seals',
                     'fork oil change',
                     'motorcycle suspension service',
                     'fork service Cascais',
                     'Iron Custom Motors fork service'],
              'ru': ['обслуживание передней вилки',
                     'сальники вилки мотоцикла',
                     'замена масла в вилке',
                     'сервис подвески мотоцикла',
                     'сервис вилки Кашкайш',
                     'Iron Custom Motors вилка'],
              'pt': ['serviço forquilha dianteira',
                     'retentores forquilha moto',
                     'troca óleo forquilha',
                     'serviço suspensão moto',
                     'forquilha Cascais',
                     'Iron Custom Motors forquilha'],
              'uk': ['обслуговування передньої вилки',
                     'сальники вилки мотоцикла',
                     'заміна оливи у вилці',
                     'сервіс підвіски мотоцикла',
                     'сервіс вилки Cascais',
                     'Iron Custom Motors вилка']}}

BLOG_POSTS["motorcycle-tyre-fitting-specialist-cascais"] = {
    "publishedISO": "2026-06-24",
    "modifiedISO": "2026-06-24",
    "imageBase": "/photos/blog/blog-motorcycle-tyre-fitting-specialist-cascais",
    "imageHero": 1,
    "imageCount": 1,
    "imageDims": {1: (1536, 1024)},
    "youtubeUrl": "https://youtube.com/shorts/KGEPaj46fBg",
    "youtubeEmbed": "https://www.youtube.com/embed/KGEPaj46fBg",
    "youtubeUploadDate": "2026-06-20T12:00:00+01:00",
    "sourceLocalizedSlugs": {
        "en": "motorcycle-tyre-fitting-specialist-cascais",
        "ru": "motoshinomontazh-spetsialist-cascais",
        "pt": "montagem-pneus-mota-especialista-cascais",
        "uk": "motoshynomontazh-spetsialist-cascais",
    },
    "meta": {
        "en": {
            "title": "Motorcycle Tyre Fitting: Why It Needs a Specialist | Iron Custom Motors",
            "description": "Motorcycle tyre fitting is not car tyre fitting. Learn why correct mounting, balancing and inspection matter for grip, stability and safety.",
            "excerpt": "Motorcycle tyre fitting is not car tyre fitting. Correct mounting, balancing and inspection change grip, stability and rider confidence.",
        },
        "ru": {
            "title": "Мотошиномонтаж: почему нужен специалист | Iron Custom Motors",
            "description": "Мотошиномонтаж — это не автомобильный шиномонтаж. Разбираем, почему монтаж, балансировка и осмотр колеса важны для управляемости и безопасности.",
            "excerpt": "Мотошиномонтаж — это не автомобильный шиномонтаж. Монтаж, балансировка и осмотр колеса напрямую влияют на управляемость и уверенность.",
        },
        "pt": {
            "title": "Montagem de Pneus de Mota: Porque Precisa de Especialista | Iron Custom Motors",
            "description": "Montagem de pneus de mota não é montagem de pneus de carro. Veja porque montagem, equilibragem e inspeção afetam segurança e confiança.",
            "excerpt": "Montagem de pneus de mota não é montagem de pneus de carro. Montagem, equilibragem e inspeção mudam segurança, estabilidade e confiança.",
        },
        "uk": {
            "title": "Мотошиномонтаж: чому потрібен спеціаліст | Iron Custom Motors",
            "description": "Мотошиномонтаж — це не автомобільний шиномонтаж. Пояснюємо, чому монтаж, балансування й огляд колеса важливі для безпеки.",
            "excerpt": "Мотошиномонтаж — це не автомобільний шиномонтаж. Монтаж, балансування й огляд колеса впливають на стабільність і впевненість.",
        },
    },
    "body": {
        "en": {
            "eyebrow": "Workshop guide · 24 June 2026",
            "publishedLabel": "Published 24 June 2026",
            "breadHome": "Home",
            "breadBlog": "Blog",
            "introTitle": "A tyre service is a handling service",
            "videoEyebrow": "Workshop video",
            "videoTitle": "Watch the motorcycle tyre fitting setup",
            "videoText": "A short look at motorcycle-specific tyre fitting equipment for wide, spoked and custom wheels.",
            "videoLink": "Open on YouTube",
            "faqTitle": "Motorcycle tyre fitting FAQ",
            "ctaEyebrow": "Need tyre fitting?",
            "ctaTitle": "Book tyre fitting or wheel balancing.",
            "btnWA": "WhatsApp us",
            "btnBack": "Back to blog",
            "imageAlt": "Motorcycle tyre service cover graphic showing tyre fitting at Iron Custom Motors.",
            "imageCaption": "Motorcycle tyre fitting and wheel balancing at Iron Custom Motors: grip, balance and control prepared on dedicated moto equipment.",
            "h1": "Motorcycle Tyre Fitting:<br/><span class=\"accent\">Why It Needs a Specialist.</span>",
            "h1Crumb": "Motorcycle Tyre Fitting: Why It Needs a Specialist",
            "lede": "A motorcycle tyre can look simple from the outside. Round, black, mounted on a rim. But the way it is fitted and balanced changes how the bike feels on the road.",
            "intro": {
                "title": "A tyre service is a handling service",
                "paragraphs": [
                    "A motorcycle tyre can look simple from the outside. Round, black, mounted on a rim. But the way it is fitted and balanced changes how the bike feels on the road.",
                    "A small vibration at speed, a front end that feels nervous, a tyre that wears unevenly, a wheel that was marked by the wrong machine — these are not rare stories. Very often, they start with one mistake: treating a motorcycle wheel like a car wheel.",
                    "Car tyre fitting is not motorcycle tyre fitting. Motorcycle wheels are lighter, more exposed, more delicate and more directly connected to the rider. The contact patch is small, the lean angle matters, and the wheel carries braking, steering and stability at the same time.",
                    "At Iron Custom Motors in Cascais, we use motorcycle-specific equipment for <a href=\"/motorcycle-tyre-service/\">tyre fitting and wheel balancing</a>. That means proper handling of spoked wheels, tube and tubeless setups, wide Harley and custom tyres, vintage rims and heavy touring wheels — not a car shop trying to adapt.",
                ],
            },
            "sections": [
                {
                    "title": "Why motorcycle tyre fitting matters",
                    "paragraphs": [
                        "Tyres are the only contact between the motorcycle and the road. Everything passes through them: braking, cornering, acceleration, ABS behaviour, suspension feel and rider confidence.",
                        "A tyre can be good on paper and still feel wrong if it is poorly mounted, incorrectly balanced, damaged during fitting, paired with the wrong valve, or installed without checking the wheel and rim condition. On a motorcycle, small errors are easier to feel because the rider is part of the chassis balance.",
                        "Correct tyre fitting is not only about getting the rubber onto the rim. It is about protecting the rim, respecting the direction of rotation, checking the valve, inspecting the wheel, seating the bead correctly, balancing the assembly and making sure the bike leaves the workshop feeling clean and stable.",
                    ],
                },
                {
                    "title": "What makes motorcycle wheels different",
                    "paragraphs": [
                        "A motorcycle wheel often carries parts that a car wheel does not: brake discs, hubs, spacers, bearings, sprocket carriers, ABS rings, delicate painted rims or polished surfaces. On spoked wheels, there can also be tube or rim-strip considerations.",
                        "That is why the machine matters. Our tyre changer is built for motorcycle wheels. We can fit tyres up to 30-inch rim size and up to 400 mm width, and we do it without removing brake discs or hubs. This protects components that car-oriented equipment often forces off the wheel.",
                        "The difference becomes obvious with Harley fat tyres, custom wheels, vintage rims, spoked wheels and large touring wheels. These are exactly the wheels that many generic tyre shops do not want to touch.",
                    ],
                },
                {
                    "title": "Balancing is not cosmetic",
                    "paragraphs": [
                        "A wheel that is not balanced properly does not just create a small vibration. It can make the handlebar buzz, send vibration through the footpegs, wear the tyre unevenly and load wheel bearings more than necessary.",
                        "At low speed, the problem may be almost invisible. At motorway speed, it becomes part of the way the motorcycle feels. A correctly balanced wheel helps the bike feel planted, smooth and predictable.",
                        "We balance motorcycle wheels up to 30 inches and 400 mm, including heavy, oversized and custom wheels. For us, balancing is part of <a href=\"/motorcycle-tyre-service/\">tyre service</a>, not an optional detail.",
                    ],
                },
                {
                    "title": "Workshop nuances riders often miss",
                    "bullets": [
                        "A new tyre still needs respect. Fresh rubber can feel different during the first rides, especially before the surface settles and the rider adapts to the new profile.",
                        "The tyre profile changes the handling. A worn tyre can make the bike turn slowly or fall into corners. A fresh tyre can bring the steering back, but it may feel sharper at first.",
                        "A tyre change is a good moment to inspect the wheel. Bearings, spacers, valves, rim condition, brake discs and ABS rings are all right there. Ignoring them is a missed opportunity.",
                        "Old tyres can still have tread. Age, cracking, hard rubber and heat cycles can reduce confidence even when the tread depth looks acceptable.",
                        "Wide custom tyres need the right equipment. Forcing them on unsuitable machinery can mark rims, stress beads or turn a simple job into damage control.",
                    ],
                },
                {
                    "title": "When to visit a workshop",
                    "paragraphs": [
                        "Book a tyre service if the tyre is worn, cracked, punctured, old, unevenly shaped, losing pressure, vibrating at speed, or if the bike no longer feels stable in corners.",
                        "Also come in if you bought tyres yourself and need professional fitting, if another shop refused your wheel, or if you ride a Harley, custom bike, chopper, touring motorcycle, spoked wheel setup or wide rear tyre that needs proper equipment.",
                        "Do not guess tyre pressure, tyre size, load rating or speed rating from the internet. These values depend on the motorcycle, tyre and manufacturer specification. For labour prices, check our <a href=\"/pricing/\">pricing page</a> before booking.",
                    ],
                },
                {
                    "title": "What we check at Iron Custom Motors",
                    "paragraphs": [
                        "At Iron Custom Motors, tyre fitting starts with the wheel, not only the tyre. We check the rim, valve, direction of rotation, visible damage, wheel bearings, spacers, brake disc area and general condition before fitting.",
                        "We work with customer-supplied tyres, and we can also <a href=\"/parts/\">order the required tyre brand and size</a>. The same specialist approach covers the full job: tyre selection, fitting, balancing and final check.",
                        "For riders around Cascais, Estoril, Oeiras and Greater Lisbon, this is the difference between a tyre mounted somehow and a wheel prepared properly for the road.",
                    ],
                },
                {
                    "title": "Conclusion",
                    "paragraphs": [
                        "Motorcycle tyre fitting is a small job only if you look at it from far away. Up close, it is one of the services that decides how the bike brakes, turns, tracks and feels at speed.",
                        "Good tyres deserve good fitting. A clean wheel, correct mounting, proper balancing and a careful inspection give the rider what matters most: confidence.",
                    ],
                },
            ],
            "ctaText": "If your motorcycle needs <a href=\"/motorcycle-tyre-service/\">tyre fitting</a>, wheel balancing or a new set of tyres, <a href=\"/contact/\">book a service</a> at Iron Custom Motors in Cascais. Bring your own tyre or tell us the brand and size you need — we will fit and balance it on motorcycle-specific equipment. You can also review the tyre labour section on our <a href=\"/pricing/\">pricing page</a>.",
            "faqs": [
                {"q": "Can a car tyre shop fit motorcycle tyres?", "a": "Sometimes they try, but car equipment is not designed for motorcycle wheels. Motorcycle rims, brake discs, hubs, spokes and wide custom tyres need proper moto-specific handling."},
                {"q": "What wheel sizes can Iron Custom Motors handle?", "a": "We fit tyres on rims up to 30 inches and up to 400 mm wide, and we service motorcycle wheels from 10 to 30 inches."},
                {"q": "Do you balance wide or heavy motorcycle wheels?", "a": "Yes. We balance motorcycle wheels up to 30 inches and 400 mm, including heavy touring, Harley, chopper and custom wheels."},
                {"q": "Can I bring my own tyre?", "a": "Yes. You can bring your own tyre, or we can order the required tyre brand and size for your motorcycle."},
                {"q": "Why is balancing important after tyre fitting?", "a": "Balancing helps reduce vibration, uneven tyre wear and unnecessary load on wheel bearings. It also makes the motorcycle feel smoother and more stable at speed."},
            ],
        },
        "ru": {
            "eyebrow": "Гид мастерской · 24 июня 2026",
            "publishedLabel": "Опубликовано 24 июня 2026",
            "breadHome": "Главная",
            "breadBlog": "Блог",
            "introTitle": "Шинный сервис — это сервис управляемости",
            "videoEyebrow": "Видео из мастерской",
            "videoTitle": "Посмотрите оборудование для мотошиномонтажа",
            "videoText": "Короткий взгляд на профильное оборудование для широких, спицованных и custom-колёс.",
            "videoLink": "Открыть на YouTube",
            "faqTitle": "FAQ по мотошиномонтажу",
            "ctaEyebrow": "Нужен шиномонтаж?",
            "ctaTitle": "Запишитесь на шиномонтаж или балансировку.",
            "btnWA": "WhatsApp",
            "btnBack": "Назад в блог",
            "imageAlt": "Обложка статьи о мотошиномонтаже Iron Custom Motors.",
            "imageCaption": "Мотошиномонтаж и балансировка в Iron Custom Motors: сцепление, баланс и контроль на профильном мотооборудовании.",
            "h1": "Мотошиномонтаж:<br/><span class=\"accent\">почему это работа для специалиста.</span>",
            "h1Crumb": "Мотошиномонтаж: почему это работа для специалиста",
            "lede": "Мотоциклетная шина снаружи выглядит простой деталью. Чёрная, круглая, стоит на диске. Но то, как она смонтирована и отбалансирована, напрямую меняет ощущение мотоцикла на дороге.",
            "intro": {
                "title": "Шинный сервис — это сервис управляемости",
                "paragraphs": [
                    "Мотоциклетная шина снаружи выглядит простой деталью. Чёрная, круглая, стоит на диске. Но то, как она смонтирована и отбалансирована, напрямую меняет ощущение мотоцикла на дороге.",
                    "Лёгкая вибрация на скорости, нервный руль, странный износ протектора, поцарапанный диск после “обычного” шиномонтажа — всё это часто начинается с одной ошибки: мотоциклетное колесо обслуживают как автомобильное.",
                    "Автомобильный шиномонтаж — это не мотошиномонтаж. У мотоцикла другая геометрия, другие риски и гораздо более прямая связь между колесом и райдером. Пятно контакта маленькое, наклон в повороте важен, а колесо одновременно отвечает за торможение, рулёжку и устойчивость.",
                    "В Iron Custom Motors в Кашкайше мы используем оборудование именно для <a href=\"/ru/shinomontazh-mototsiklov/\">мотошиномонтажа и балансировки</a>. Работаем со спицами, камерными и бескамерными колёсами, широкими Harley и custom-шинами, винтажными дисками и тяжёлыми touring-колёсами — не как автосервис, который пытается приспособиться.",
                ],
            },
            "sections": [
                {
                    "title": "Почему мотошиномонтаж важен",
                    "paragraphs": [
                        "Шины — единственная точка контакта мотоцикла с дорогой. Через них проходит всё: торможение, поворот, разгон, работа ABS, подвеска и уверенность райдера.",
                        "Даже хорошая шина может ощущаться плохо, если её неправильно посадили на диск, плохо отбалансировали, повредили при монтаже, поставили не тот вентиль или не проверили состояние колеса. На мотоцикле такие мелочи чувствуются сильнее, потому что райдер буквально живёт внутри баланса мотоцикла.",
                        "Правильный шиномонтаж — это не просто натянуть резину на диск. Это защита диска, правильное направление вращения, проверка вентиля, осмотр колеса, корректная посадка борта, балансировка и финальная проверка перед дорогой.",
                    ],
                },
                {
                    "title": "Чем мотоциклетное колесо отличается",
                    "paragraphs": [
                        "На мотоциклетном колесе часто есть то, чего нет на автомобильном: тормозные диски, ступицы, дистанционные втулки, подшипники, звёзды, ABS-кольца, окрашенные или полированные поверхности. На спицованных колёсах добавляются камера, лента обода и свои нюансы сборки.",
                        "Поэтому оборудование имеет значение. Наш станок создан под мотоколёса. Мы монтируем шины на диски до 30 дюймов и шириной до 400 мм — без снятия тормозных дисков и ступиц. Это защищает узлы, которые автомобильное оборудование часто заставляет демонтировать.",
                        "Особенно разница видна на широких Harley-шинах, кастомных колёсах, винтажных дисках, спицах и крупных touring-колёсах. Именно такие колёса часто не хотят брать универсальные шиномонтажи.",
                    ],
                },
                {
                    "title": "Балансировка — не косметика",
                    "paragraphs": [
                        "Неправильно отбалансированное колесо — это не просто небольшая вибрация. Оно может отдавать в руль и подножки, неравномерно изнашивать шину и лишний раз нагружать подшипники.",
                        "На маленькой скорости это может почти не чувствоваться. На трассе становится частью поведения мотоцикла. Хорошо отбалансированное колесо помогает мотоциклу ехать ровно, спокойно и предсказуемо.",
                        "Мы балансируем мотоциклетные колёса до 30 дюймов и 400 мм, включая тяжёлые, широкие и кастомные. Для нас балансировка — часть <a href=\"/ru/shinomontazh-mototsiklov/\">шинного сервиса</a>, а не дополнительная мелочь.",
                    ],
                },
                {
                    "title": "Нюансы, которые райдеры часто упускают",
                    "bullets": [
                        "Новая шина требует аккуратности. Первые поездки она может ощущаться иначе, пока поверхность не приработалась, а райдер не привык к новому профилю.",
                        "Профиль шины меняет рулёжку. Изношенная шина может заставлять мотоцикл лениво поворачивать или проваливаться в поворот. Новая шина возвращает остроту, но сначала может казаться непривычной.",
                        "Замена шины — хороший момент осмотреть колесо. Подшипники, втулки, вентиль, диск, тормозные диски и ABS-кольцо уже перед глазами. Игнорировать это — упускать шанс поймать проблему заранее.",
                        "Старая шина может иметь протектор. Возраст, микротрещины, задубевшая резина и тепловые циклы могут снизить уверенность даже при нормальной глубине рисунка.",
                        "Широкие custom-шины требуют правильного оборудования. Если ставить их на неподходящем станке, можно повредить диск, борт шины или превратить простую работу в ремонт последствий.",
                    ],
                },
                {
                    "title": "Когда ехать в мастерскую",
                    "paragraphs": [
                        "Записывайтесь на шиномонтаж, если шина изношена, потрескалась, проколота, старая, теряет давление, даёт вибрацию на скорости или мотоцикл стал хуже держать поворот.",
                        "Также приезжайте, если вы купили шины сами и хотите поставить их правильно, если другой сервис отказался от вашего колеса, или если у вас Harley, custom, chopper, touring, спицованное колесо или широкий задний баллон.",
                        "Не угадывайте давление, размер, индекс нагрузки и индекс скорости по интернету. Эти значения зависят от мотоцикла, конкретной шины и спецификации производителя. Стоимость работ можно посмотреть на странице <a href=\"/ru/pricing/\">цен</a>.",
                    ],
                },
                {
                    "title": "Что мы проверяем в Iron Custom Motors",
                    "paragraphs": [
                        "В Iron Custom Motors шиномонтаж начинается не с шины, а с колеса. Мы смотрим диск, вентиль, направление вращения, видимые повреждения, подшипники, втулки, зону тормозных дисков и общее состояние сборки.",
                        "Мы ставим шины клиента и можем <a href=\"/ru/parts/\">заказать нужный бренд и размер</a>. Один подход закрывает весь процесс: подбор, монтаж, балансировку и финальную проверку.",
                        "Для райдеров из Cascais, Estoril, Oeiras и Greater Lisbon это разница между “как-нибудь поставили” и колесом, подготовленным к дороге нормально.",
                    ],
                },
                {
                    "title": "Вывод",
                    "paragraphs": [
                        "Мотошиномонтаж кажется простой работой только издалека. На деле это сервис, который влияет на торможение, поворот, стабильность и ощущение мотоцикла на скорости.",
                        "Хорошая шина заслуживает правильного монтажа. Чистое колесо, аккуратная посадка, точная балансировка и внимательный осмотр дают райдеру главное — уверенность.",
                    ],
                },
            ],
            "ctaText": "Если вашему мотоциклу нужен <a href=\"/ru/shinomontazh-mototsiklov/\">шиномонтаж</a>, балансировка или новый комплект шин, <a href=\"/ru/contact/\">запишитесь</a> в Iron Custom Motors в Кашкайше. Привозите свою шину или скажите нужный бренд и размер — мы установим и отбалансируем колесо на профильном мотооборудовании. Цены на работы есть на странице <a href=\"/ru/pricing/\">прайса</a>.",
            "faqs": [
                {"q": "Можно ли ставить мотоциклетную шину в автосервисе?", "a": "Иногда автосервисы пытаются это делать, но автомобильное оборудование не рассчитано на мотоколёса. Диски, тормозные диски, ступицы, спицы и широкие custom-шины требуют профильного подхода."},
                {"q": "С какими размерами работает Iron Custom Motors?", "a": "Мы монтируем шины на диски до 30 дюймов и шириной до 400 мм, а обслуживаем мотоциклетные колёса от 10 до 30 дюймов."},
                {"q": "Балансируете ли вы широкие и тяжёлые колёса?", "a": "Да. Мы балансируем мотоциклетные колёса до 30 дюймов и 400 мм, включая тяжёлые touring, Harley, chopper и custom-колёса."},
                {"q": "Можно ли привезти свою шину?", "a": "Да. Вы можете привезти свою шину, либо мы можем заказать нужный бренд и размер под ваш мотоцикл."},
                {"q": "Зачем балансировать колесо после замены шины?", "a": "Балансировка помогает убрать вибрацию, снизить неравномерный износ шины и лишнюю нагрузку на подшипники. Мотоцикл становится ровнее и стабильнее на скорости."},
            ],
        },
        "pt": {
            "eyebrow": "Guia de oficina · 24 de junho de 2026",
            "publishedLabel": "Publicado 24 de junho de 2026",
            "breadHome": "Início",
            "breadBlog": "Blog",
            "introTitle": "Serviço de pneus é serviço de comportamento",
            "videoEyebrow": "Vídeo de oficina",
            "videoTitle": "Veja o setup para montagem de pneus de mota",
            "videoText": "Um olhar rápido ao equipamento específico para rodas largas, de raios e custom.",
            "videoLink": "Abrir no YouTube",
            "faqTitle": "FAQ sobre montagem de pneus de mota",
            "ctaEyebrow": "Precisa de pneus?",
            "ctaTitle": "Marque montagem ou equilibragem.",
            "btnWA": "WhatsApp",
            "btnBack": "Voltar ao blog",
            "imageAlt": "Imagem de capa sobre montagem de pneus de mota na Iron Custom Motors.",
            "imageCaption": "Montagem de pneus de mota e equilibragem na Iron Custom Motors: aderência, equilíbrio e controlo em equipamento dedicado.",
            "h1": "Montagem de Pneus de Mota:<br/><span class=\"accent\">Porque Precisa de um Especialista.</span>",
            "h1Crumb": "Montagem de Pneus de Mota: Porque Precisa de um Especialista",
            "lede": "Um pneu de mota parece simples visto de fora. Redondo, preto, montado numa jante. Mas a forma como é montado e equilibrado muda muito a sensação da mota na estrada.",
            "intro": {
                "title": "Serviço de pneus é serviço de comportamento",
                "paragraphs": [
                    "Um pneu de mota parece simples visto de fora. Redondo, preto, montado numa jante. Mas a forma como é montado e equilibrado muda muito a sensação da mota na estrada.",
                    "Uma pequena vibração em velocidade, a frente nervosa, desgaste estranho do pneu, uma jante marcada por uma máquina errada — isto acontece mais vezes do que devia. Muitas vezes começa com o mesmo erro: tratar uma roda de mota como se fosse uma roda de carro.",
                    "Montagem de pneus de carro não é montagem de pneus de mota. A roda da mota é mais exposta, mais delicada e está ligada diretamente ao que o condutor sente. A área de contacto é pequena, a inclinação conta, e a roda participa ao mesmo tempo na travagem, direção e estabilidade.",
                    "Na Iron Custom Motors, em Cascais, usamos equipamento específico para <a href=\"/pt/montagem-de-pneus-mota/\">montagem de pneus de mota e equilibragem</a>. Trabalhamos rodas de raios, montagens com câmara e tubeless, pneus largos Harley e custom, jantes vintage e rodas touring pesadas — não como uma oficina de carros a tentar adaptar-se.",
                ],
            },
            "sections": [
                {
                    "title": "Porque a montagem correta importa",
                    "paragraphs": [
                        "Os pneus são o único contacto entre a mota e a estrada. Tudo passa por eles: travagem, curva, aceleração, ABS, suspensão e confiança do condutor.",
                        "Um pneu pode ser bom e mesmo assim sentir-se errado se for mal montado, mal equilibrado, danificado durante a montagem, combinado com uma válvula incorreta ou instalado sem olhar para a roda. Numa mota, estes pequenos erros sentem-se mais depressa.",
                        "Uma boa montagem não é apenas colocar borracha na jante. É proteger a jante, respeitar o sentido de rotação, verificar a válvula, inspecionar a roda, assentar bem o talão, equilibrar o conjunto e confirmar que tudo sai limpo e seguro.",
                    ],
                },
                {
                    "title": "O que torna uma roda de mota diferente",
                    "paragraphs": [
                        "Uma roda de mota pode trazer discos de travão, cubos, espaçadores, rolamentos, cremalheira, anel ABS, jantes pintadas ou polidas. Nas rodas de raios ainda há câmara, fita de jante e outros detalhes.",
                        "Por isso a máquina importa. O nosso equipamento foi feito para rodas de mota. Montamos pneus em jantes até 30 polegadas e até 400 mm de largura, sem desmontar discos de travão nem cubos. Assim protegemos componentes que uma máquina de carro muitas vezes obriga a retirar.",
                        "A diferença nota-se sobretudo em pneus largos Harley, rodas custom, jantes vintage, rodas de raios e grandes rodas touring. São exatamente estas rodas que muitas oficinas genéricas preferem recusar.",
                    ],
                },
                {
                    "title": "Equilibragem não é estética",
                    "paragraphs": [
                        "Uma roda mal equilibrada não causa apenas uma pequena vibração. Pode passar vibração para o guiador e pousa-pés, gastar o pneu de forma irregular e carregar os rolamentos mais do que devia.",
                        "A baixa velocidade quase não se nota. Em autoestrada, passa a fazer parte do comportamento da mota. Uma roda bem equilibrada ajuda a mota a sentir-se mais estável, suave e previsível.",
                        "Equilibramos rodas de mota até 30 polegadas e 400 mm, incluindo rodas pesadas, largas e custom. Para nós, a equilibragem faz parte do <a href=\"/pt/montagem-de-pneus-mota/\">serviço de pneus</a>, não é um extra decorativo.",
                    ],
                },
                {
                    "title": "Detalhes que muitos motociclistas ignoram",
                    "bullets": [
                        "Um pneu novo precisa de respeito. Nos primeiros quilómetros pode sentir-se diferente, até a superfície assentar e o condutor se habituar ao novo perfil.",
                        "O perfil muda a direção. Um pneu gasto pode fazer a mota virar devagar ou cair para a curva. Um pneu novo devolve precisão, mas pode parecer mais vivo no início.",
                        "A troca de pneus é uma boa altura para olhar para a roda. Rolamentos, espaçadores, válvula, jante, discos de travão e anel ABS estão todos ali. Ignorar isso é perder uma oportunidade.",
                        "Um pneu velho pode ainda ter piso. Idade, pequenas fissuras, borracha endurecida e ciclos de calor podem reduzir a confiança mesmo com desenho visível.",
                        "Pneus largos custom precisam de equipamento certo. Forçá-los numa máquina inadequada pode marcar a jante, stressar o talão ou transformar um serviço simples num problema.",
                    ],
                },
                {
                    "title": "Quando visitar uma oficina",
                    "paragraphs": [
                        "Marque serviço se o pneu estiver gasto, rachado, furado, velho, a perder pressão, a vibrar em velocidade ou se a mota já não transmitir confiança em curva.",
                        "Venha também se comprou pneus e precisa de montagem profissional, se outra oficina recusou a roda, ou se conduz uma Harley, custom, chopper, touring, roda de raios ou pneu traseiro largo.",
                        "Não adivinhe pressão, medida, índice de carga ou índice de velocidade pela internet. Esses valores dependem da mota, do pneu e da especificação do fabricante. Para preços de mão de obra, veja a nossa página de <a href=\"/pt/pricing/\">preços</a>.",
                    ],
                },
                {
                    "title": "O que verificamos na Iron Custom Motors",
                    "paragraphs": [
                        "Na Iron Custom Motors, a montagem começa pela roda, não apenas pelo pneu. Verificamos jante, válvula, sentido de rotação, danos visíveis, rolamentos, espaçadores, zona dos discos e condição geral do conjunto.",
                        "Montamos pneus trazidos pelo cliente e também podemos <a href=\"/pt/parts/\">encomendar a marca e medida necessária</a>. O mesmo especialista acompanha o processo: escolha, montagem, equilibragem e verificação final.",
                        "Para motociclistas de Cascais, Estoril, Oeiras e Grande Lisboa, esta é a diferença entre um pneu montado de qualquer maneira e uma roda preparada corretamente para a estrada.",
                    ],
                },
                {
                    "title": "Conclusão",
                    "paragraphs": [
                        "A montagem de pneus de mota só parece simples vista de longe. De perto, é um serviço que influencia travagem, curva, estabilidade e sensação em velocidade.",
                        "Um bom pneu merece uma boa montagem. Roda limpa, montagem correta, equilibragem precisa e inspeção cuidada dão ao motociclista o que mais importa: confiança.",
                    ],
                },
            ],
            "ctaText": "Se a sua mota precisa de <a href=\"/pt/montagem-de-pneus-mota/\">montagem de pneus</a>, equilibragem ou um novo conjunto de pneus, <a href=\"/pt/contact/\">marque serviço</a> na Iron Custom Motors em Cascais. Traga o seu pneu ou diga-nos a marca e medida que precisa — montamos e equilibramos em equipamento específico para motas. A secção de pneus está também na nossa página de <a href=\"/pt/pricing/\">preços</a>.",
            "faqs": [
                {"q": "Uma oficina de carros pode montar pneus de mota?", "a": "Algumas tentam, mas o equipamento de carro não foi pensado para rodas de mota. Jantes, discos, cubos, raios e pneus custom largos precisam de tratamento específico."},
                {"q": "Que dimensões conseguem trabalhar?", "a": "Montamos pneus em jantes até 30 polegadas e até 400 mm de largura, e trabalhamos rodas de mota entre 10 e 30 polegadas."},
                {"q": "Equilibram rodas largas ou pesadas?", "a": "Sim. Equilibramos rodas de mota até 30 polegadas e 400 mm, incluindo rodas touring pesadas, Harley, chopper e custom."},
                {"q": "Posso trazer o meu próprio pneu?", "a": "Sim. Pode trazer o seu pneu, ou podemos encomendar a marca e medida certa para a sua mota."},
                {"q": "Porque é importante equilibrar depois da montagem?", "a": "A equilibragem reduz vibração, desgaste irregular do pneu e carga desnecessária nos rolamentos. A mota fica mais suave e estável em velocidade."},
            ],
        },
        "uk": {
            "eyebrow": "Гід майстерні · 24 червня 2026",
            "publishedLabel": "Опубліковано 24 червня 2026",
            "breadHome": "Головна",
            "breadBlog": "Блог",
            "introTitle": "Шинний сервіс — це сервіс керованості",
            "videoEyebrow": "Відео з майстерні",
            "videoTitle": "Подивіться обладнання для мотошиномонтажу",
            "videoText": "Короткий погляд на профільне обладнання для широких, спицованих і custom-коліс.",
            "videoLink": "Відкрити на YouTube",
            "faqTitle": "FAQ про мотошиномонтаж",
            "ctaEyebrow": "Потрібен шиномонтаж?",
            "ctaTitle": "Запишіться на шиномонтаж або балансування.",
            "btnWA": "WhatsApp",
            "btnBack": "Назад до блогу",
            "imageAlt": "Обкладинка статті про мотошиномонтаж Iron Custom Motors.",
            "imageCaption": "Мотошиномонтаж і балансування в Iron Custom Motors: зчеплення, баланс і контроль на профільному мотообладнанні.",
            "h1": "Мотошиномонтаж:<br/><span class=\"accent\">чому це робота для спеціаліста.</span>",
            "h1Crumb": "Мотошиномонтаж: чому це робота для спеціаліста",
            "lede": "Мотоциклетна шина зовні здається простою деталлю. Чорна, кругла, стоїть на диску. Але те, як її змонтували й відбалансували, дуже впливає на поведінку мотоцикла на дорозі.",
            "intro": {
                "title": "Шинний сервіс — це сервіс керованості",
                "paragraphs": [
                    "Мотоциклетна шина зовні здається простою деталлю. Чорна, кругла, стоїть на диску. Але те, як її змонтували й відбалансували, дуже впливає на поведінку мотоцикла на дорозі.",
                    "Легка вібрація на швидкості, нервова передня частина, дивний знос протектора, подряпаний диск після “звичайного” шиномонтажу — усе це часто починається з однієї помилки: мотоциклетне колесо обслуговують як автомобільне.",
                    "Автомобільний шиномонтаж — це не мотошиномонтаж. У мотоцикла інша геометрія, інші ризики й набагато пряміший зв’язок між колесом і райдером. Пляма контакту маленька, нахил у повороті має значення, а колесо одночасно відповідає за гальмування, керування й стабільність.",
                    "В Iron Custom Motors у Кашкайші ми використовуємо обладнання саме для <a href=\"/uk/shynomontazh-mototsykliv/\">мотошиномонтажу та балансування</a>. Працюємо зі спицями, камерними й безкамерними колесами, широкими Harley та custom-шинами, вінтажними дисками й важкими touring-колесами — не як автосервіс, що намагається пристосуватися.",
                ],
            },
            "sections": [
                {
                    "title": "Чому правильний мотошиномонтаж важливий",
                    "paragraphs": [
                        "Шини — це єдиний контакт мотоцикла з дорогою. Через них проходить усе: гальмування, поворот, розгін, робота ABS, підвіска й упевненість райдера.",
                        "Навіть хороша шина може відчуватися неправильно, якщо її погано посадили на диск, неточно відбалансували, пошкодили під час монтажу, поставили не той вентиль або не перевірили саме колесо. На мотоциклі такі дрібниці відчуваються швидше.",
                        "Правильний шиномонтаж — це не просто натягнути гуму на диск. Це захист диска, правильний напрямок обертання, перевірка вентиля, огляд колеса, коректна посадка борта, балансування й фінальна перевірка перед дорогою.",
                    ],
                },
                {
                    "title": "Чим мотоциклетне колесо відрізняється",
                    "paragraphs": [
                        "На мотоциклетному колесі часто є те, чого немає на автомобільному: гальмівні диски, маточини, дистанційні втулки, підшипники, зірки, ABS-кільця, фарбовані або поліровані поверхні. На спицях додаються камера, стрічка обода й свої нюанси складання.",
                        "Тому обладнання має значення. Наш верстат створений під мотоколеса. Ми монтуємо шини на диски до 30 дюймів і завширшки до 400 мм — без зняття гальмівних дисків і маточин. Це зберігає вузли, які автомобільне обладнання часто змушує демонтувати.",
                        "Особливо різниця помітна на широких Harley-шинах, custom-колесах, вінтажних дисках, спицях і великих touring-колесах. Саме такі колеса часто не хочуть брати універсальні шиномонтажі.",
                    ],
                },
                {
                    "title": "Балансування — не косметика",
                    "paragraphs": [
                        "Погано збалансоване колесо — це не просто легка вібрація. Воно може віддавати в кермо й підніжки, нерівномірно зношувати шину й зайвий раз навантажувати підшипники.",
                        "На малій швидкості це може майже не відчуватися. На трасі стає частиною поведінки мотоцикла. Добре збалансоване колесо допомагає мотоциклу їхати рівно, спокійно й передбачувано.",
                        "Ми балансуємо мотоциклетні колеса до 30 дюймів і 400 мм, включно з важкими, широкими та custom. Для нас балансування — частина <a href=\"/uk/shynomontazh-mototsykliv/\">шинного сервісу</a>, а не додаткова дрібниця.",
                    ],
                },
                {
                    "title": "Нюанси, які райдери часто пропускають",
                    "bullets": [
                        "Нова шина потребує обережності. Перші поїздки вона може відчуватися інакше, поки поверхня не приживеться, а райдер не звикне до нового профілю.",
                        "Профіль шини змінює керованість. Зношена шина може робити мотоцикл млявим у повороті або, навпаки, змушувати його провалюватися. Нова шина повертає точність, але спочатку може здаватися гострішою.",
                        "Заміна шини — гарний момент оглянути колесо. Підшипники, втулки, вентиль, диск, гальмівні диски й ABS-кільце вже перед очима. Ігнорувати це — втратити шанс знайти проблему раніше.",
                        "Стара шина може ще мати протектор. Вік, мікротріщини, задубіла гума й теплові цикли можуть знизити впевненість навіть при нормальному малюнку.",
                        "Широкі custom-шини потребують правильного обладнання. Якщо ставити їх на невідповідному верстаті, можна пошкодити диск, борт шини або перетворити просту роботу на ремонт наслідків.",
                    ],
                },
                {
                    "title": "Коли їхати в майстерню",
                    "paragraphs": [
                        "Записуйтеся на шиномонтаж, якщо шина зношена, потріскана, проколота, стара, втрачає тиск, дає вібрацію на швидкості або мотоцикл гірше тримає поворот.",
                        "Також приїжджайте, якщо ви купили шини самостійно й хочете встановити їх правильно, якщо інший сервіс відмовився від вашого колеса, або якщо у вас Harley, custom, chopper, touring, спицоване колесо чи широкий задній балон.",
                        "Не вгадуйте тиск, розмір, індекс навантаження чи індекс швидкості з інтернету. Ці значення залежать від мотоцикла, конкретної шини й специфікації виробника. Вартість робіт є на сторінці <a href=\"/uk/pricing/\">цін</a>.",
                    ],
                },
                {
                    "title": "Що ми перевіряємо в Iron Custom Motors",
                    "paragraphs": [
                        "В Iron Custom Motors шиномонтаж починається не з шини, а з колеса. Ми перевіряємо диск, вентиль, напрямок обертання, видимі пошкодження, підшипники, втулки, зону гальмівних дисків і загальний стан вузла.",
                        "Ми встановлюємо шини клієнта й можемо <a href=\"/uk/parts/\">замовити потрібний бренд і розмір</a>. Один підхід закриває весь процес: підбір, монтаж, балансування й фінальну перевірку.",
                        "Для райдерів із Cascais, Estoril, Oeiras і Greater Lisbon це різниця між “якось поставили” і колесом, нормально підготовленим до дороги.",
                    ],
                },
                {
                    "title": "Висновок",
                    "paragraphs": [
                        "Мотошиномонтаж здається простою роботою тільки здалеку. Насправді це сервіс, який впливає на гальмування, поворот, стабільність і відчуття мотоцикла на швидкості.",
                        "Хороша шина заслуговує правильного монтажу. Чисте колесо, акуратна посадка, точне балансування й уважний огляд дають райдеру головне — впевненість.",
                    ],
                },
            ],
            "ctaText": "Якщо вашому мотоциклу потрібен <a href=\"/uk/shynomontazh-mototsykliv/\">шиномонтаж</a>, балансування або новий комплект шин, <a href=\"/uk/contact/\">запишіться</a> в Iron Custom Motors у Кашкайші. Привозьте свою шину або скажіть потрібний бренд і розмір — ми встановимо й відбалансуємо колесо на профільному мотообладнанні. Ціни на роботи є на сторінці <a href=\"/uk/pricing/\">прайса</a>.",
            "faqs": [
                {"q": "Чи можна ставити мотоциклетну шину в автосервісі?", "a": "Іноді автосервіси намагаються це робити, але автомобільне обладнання не розраховане на мотоколеса. Диски, гальмівні диски, маточини, спиці й широкі custom-шини потребують профільного підходу."},
                {"q": "З якими розмірами працює Iron Custom Motors?", "a": "Ми монтуємо шини на диски до 30 дюймів і завширшки до 400 мм, а обслуговуємо мотоциклетні колеса від 10 до 30 дюймів."},
                {"q": "Чи балансуєте ви широкі й важкі колеса?", "a": "Так. Ми балансуємо мотоциклетні колеса до 30 дюймів і 400 мм, включно з важкими touring, Harley, chopper і custom-колесами."},
                {"q": "Чи можна привезти свою шину?", "a": "Так. Ви можете привезти свою шину, або ми можемо замовити потрібний бренд і розмір під ваш мотоцикл."},
                {"q": "Навіщо балансувати колесо після заміни шини?", "a": "Балансування допомагає прибрати вібрацію, зменшити нерівномірний знос шини й зайве навантаження на підшипники. Мотоцикл стає рівнішим і стабільнішим на швидкості."},
            ],
        },
    },
    "keywords": {
        "en": ["motorcycle tyre fitting", "motorcycle wheel balancing", "tyre service Cascais", "wide motorcycle tyres", "Iron Custom Motors tyre service"],
        "ru": ["мотошиномонтаж", "балансировка мотоциклетных колес", "шиномонтаж Кашкайш", "широкие мото шины", "Iron Custom Motors шиномонтаж"],
        "pt": ["montagem pneus mota", "equilibragem rodas mota", "serviço pneus Cascais", "pneus largos mota", "Iron Custom Motors pneus"],
        "uk": ["мотошиномонтаж", "балансування мотоциклетних коліс", "шиномонтаж Cascais", "широкі мото шини", "Iron Custom Motors шиномонтаж"],
    },
}

BLOG_POSTS[_BEAR650_SLUG] = _load_bear650_post()
BLOG_POSTS[_HARLEY_SERVICE_SLUG] = _load_harley_service_post()
BLOG_POSTS[_BEAR650_BUILD_SLUG] = _load_bear650_build_post()
