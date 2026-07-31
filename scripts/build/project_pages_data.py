"""Structured source data for generated project pages."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path


SITE_ROOT = Path(__file__).resolve().parents[2]

LANGUAGE_SECTIONS = {
    "ENGLISH": "en",
    "PORTUGUÊS (pt-PT)": "pt",
    "РУССКИЙ": "ru",
    "УКРАЇНСЬКА": "uk",
}

_FIGHTER_CONFIGS = {
    "fighter": {
        "source": SITE_ROOT / "content/projects/fighter_4lang.md",
        "year": "2014",
        "published_iso": "2026-07-27T12:00:00+01:00",
        "hero_base": "/photos/projects/fighter",
        "hero_source": "Fighter_HERO.jpg",
        "gallery_base": "/photos/projects/gallery/fighter/fighter",
        "gallery_sources": [
            "134632_000_3727.jpg",
            "141001_000_3785.jpg",
            "135441_000_3736.jpg",
            "142638_000_3830.jpg",
            "142159_000_3819.jpg",
            "135357_000_3732.jpg",
            "135823_000_3753.jpg",
            "142952_000_3842.jpg",
            "135340_000_3729.jpg",
            "135727_000_3748.jpg",
            "141201_000_3792.jpg",
        ],
        "ui": {
            "en": {
                "home": "Home",
                "projects": "Projects",
                "badge": "Long Chopper · Full Custom",
                "year_label": "Year",
                "category_label": "Category",
                "category": "Long Chopper · Full Custom",
                "where_label": "Where",
                "where": "Built in Kharkiv, Ukraine",
                "gallery": "Gallery",
                "gallery_title": "<em>Fighter</em> — in detail.",
            },
            "pt": {
                "home": "Início",
                "projects": "Projetos",
                "badge": "Long Chopper · Full Custom",
                "year_label": "Ano",
                "category_label": "Categoria",
                "category": "Long Chopper · Full Custom",
                "where_label": "Local",
                "where": "Construído em Kharkiv, Ucrânia",
                "gallery": "Galeria",
                "gallery_title": "<em>Fighter</em> — em detalhe.",
            },
            "ru": {
                "home": "Главная",
                "projects": "Проекты",
                "badge": "Лонг-чоппер · Full Custom",
                "year_label": "Год",
                "category_label": "Категория",
                "category": "Лонг-чоппер · Full Custom",
                "where_label": "Где",
                "where": "Построен в Харькове, Украина",
                "gallery": "Галерея",
                "gallery_title": "<em>Fighter</em> — в деталях.",
            },
            "uk": {
                "home": "Головна",
                "projects": "Проєкти",
                "badge": "Лонг-чопер · Full Custom",
                "year_label": "Рік",
                "category_label": "Категорія",
                "category": "Лонг-чопер · Full Custom",
                "where_label": "Де",
                "where": "Збудовано у Харкові, Україна",
                "gallery": "Галерея",
                "gallery_title": "<em>Fighter</em> — у деталях.",
            },
        },
        "gallery_alts": {
            "en": [
                "Fighter long chopper rear fender and custom taillight detail",
                "Fighter long chopper passenger seat and Green Plazma paint detail",
                "Fighter long chopper RevTech engine and Samson exhaust detail",
                "Fighter long chopper Spyke ignition and engine detail",
                "Fighter long chopper BDL open primary drive detail",
                "Fighter long chopper RevTech 110 engine detail",
                "Fighter long chopper fuel tank and cockpit detail",
                "Fighter long chopper Wicked Image wheel and brake detail",
                "Fighter long chopper Green Plazma fuel tank and fork detail",
                "Fighter long chopper full side view",
                "Fighter long chopper with rider outdoors",
            ],
            "pt": [
                "Fighter long chopper, detalhe do guarda-lamas traseiro e farolim custom",
                "Fighter long chopper, detalhe do lugar de pendura e pintura Green Plazma",
                "Fighter long chopper, detalhe do motor RevTech e escape Samson",
                "Fighter long chopper, detalhe da ignição Spyke e do motor",
                "Fighter long chopper, detalhe da primária aberta BDL",
                "Fighter long chopper, detalhe do motor RevTech 110",
                "Fighter long chopper, detalhe do depósito e posto de condução",
                "Fighter long chopper, detalhe da roda Wicked Image e travão",
                "Fighter long chopper, detalhe do depósito Green Plazma e forquilha",
                "Fighter long chopper, vista lateral completa",
                "Fighter long chopper com piloto no exterior",
            ],
            "ru": [
                "Fighter лонг-чоппер — заднее крыло и кастомный фонарь",
                "Fighter лонг-чоппер — пассажирское сиденье и краска Green Plazma",
                "Fighter лонг-чоппер — мотор RevTech и выхлоп Samson",
                "Fighter лонг-чоппер — зажигание Spyke и детали мотора",
                "Fighter лонг-чоппер — открытая первичная передача BDL",
                "Fighter лонг-чоппер — мотор RevTech 110",
                "Fighter лонг-чоппер — бак и кокпит",
                "Fighter лонг-чоппер — колесо Wicked Image и тормоз",
                "Fighter лонг-чоппер — бак Green Plazma и вилка",
                "Fighter лонг-чоппер — полный вид сбоку",
                "Fighter лонг-чоппер с пилотом",
            ],
            "uk": [
                "Fighter лонг-чопер — заднє крило та кастомний ліхтар",
                "Fighter лонг-чопер — пасажирське сидіння та фарба Green Plazma",
                "Fighter лонг-чопер — мотор RevTech і вихлоп Samson",
                "Fighter лонг-чопер — запалювання Spyke та деталі мотора",
                "Fighter лонг-чопер — відкрита первинна передача BDL",
                "Fighter лонг-чопер — мотор RevTech 110",
                "Fighter лонг-чопер — бак і кокпіт",
                "Fighter лонг-чопер — колесо Wicked Image і гальмо",
                "Fighter лонг-чопер — бак Green Plazma та вилка",
                "Fighter лонг-чопер — повний вигляд збоку",
                "Fighter лонг-чопер із пілотом",
            ],
        },
    },
}

LEGACY_PROJECT_DATA_PATH = SITE_ROOT / "content/projects/legacy_projects_4lang.json"
LEGACY_PROJECT_ORDER = [
    "inspirium",
    "beckman",
    "unbreakable",
    "quanta-r",
    "burly",
    "sturmvogel",
    "geometric",
    "joker",
    "hellboy",
    "true-religion",
]

# The publication timestamp is the first Git commit that introduced the
# legacy project pages. Modified timestamps are the already-published sitemap
# content dates and remain language-specific where Git history differs.
LEGACY_PROJECT_DATES = {
    "inspirium": "2026-06-20T11:33:40+01:00",
    "beckman": "2026-06-20T11:33:40+01:00",
    "unbreakable": {
        "en": "2026-07-24T20:10:52+01:00",
        "ru": "2026-07-24T20:10:52+01:00",
        "uk": "2026-07-24T20:10:53+01:00",
        "pt": "2026-07-24T20:10:52+01:00",
    },
    "quanta-r": "2026-06-20T11:33:40+01:00",
    "burly": "2026-06-20T11:33:40+01:00",
    "sturmvogel": "2026-07-24T20:24:26+01:00",
    "geometric": "2026-06-20T11:33:40+01:00",
    "joker": "2026-06-20T11:33:40+01:00",
    "hellboy": "2026-06-20T11:33:40+01:00",
    "true-religion": "2026-06-20T11:33:40+01:00",
}

_LEGACY_PROJECT_DATA = json.loads(
    LEGACY_PROJECT_DATA_PATH.read_text(encoding="utf-8")
)

PROJECT_CONFIGS = {
    slug: {
        "source": LEGACY_PROJECT_DATA_PATH,
        "source_format": "localized_html",
        "published_iso": "2026-05-05T21:37:36+02:00",
        "modified_iso": LEGACY_PROJECT_DATES[slug],
    }
    for slug in LEGACY_PROJECT_ORDER
}
PROJECT_CONFIGS.update(_FIGHTER_CONFIGS)
PROJECT_CONFIGS["fighter"]["source_format"] = "markdown"
PROJECT_CONFIGS["fighter"]["modified_iso"] = PROJECT_CONFIGS["fighter"][
    "published_iso"
]
PROJECT_CONFIGS["fighter"]["visible_text_sha256"] = {
    "en": "3a105c2135bad232b2d6e01b8cdb83686f7c87b1a4fefcf3e69b74d899bc9395",
    "ru": "725b26e490480f786b929fc893853f41ad33b6642aca888af32231db2f543b53",
    "uk": "d5e061959c0d98b0e59681f50a53fdcbaf64aa2f621ef17b634ebbbf32df9d78",
    "pt": "3f8cc1b58b14eea3dd0155cb717dd5a61b473e3e451b2a4ff0103a66fef21f6c",
}

REDIRECT_CONFIGS = {
    "nezlamniy": {
        "target": "unbreakable",
        "labels": {
            "en": {
                "title": "Redirecting to Unbreakable | Iron Custom Motors",
                "message": "Redirecting to",
                "target_name": "Unbreakable",
            },
            "ru": {
                "title": "Переход на Unbreakable | Iron Custom Motors",
                "message": "Переход на",
                "target_name": "Unbreakable",
            },
            "uk": {
                "title": "Перехід на Unbreakable | Iron Custom Motors",
                "message": "Перехід на",
                "target_name": "Unbreakable",
            },
            "pt": {
                "title": "A redirecionar para Unbreakable | Iron Custom Motors",
                "message": "A redirecionar para",
                "target_name": "Unbreakable",
            },
        },
    },
    "quanta": {
        "target": "quanta-r",
        "labels": {
            "en": {
                "title": "Redirecting to Quanta R | Iron Custom Motors",
                "message": "Redirecting to",
                "target_name": "Quanta R",
            },
            "ru": {
                "title": "Переход на Quanta R | Iron Custom Motors",
                "message": "Переход на",
                "target_name": "Quanta R",
            },
            "uk": {
                "title": "Перехід на Quanta R | Iron Custom Motors",
                "message": "Перехід на",
                "target_name": "Quanta R",
            },
            "pt": {
                "title": "A redirecionar para Quanta R | Iron Custom Motors",
                "message": "A redirecionar para",
                "target_name": "Quanta R",
            },
        },
    },
}


def inline_markdown(value: str) -> str:
    """Render the limited inline Markdown used by project copy."""
    rendered = html.escape(value, quote=False)
    rendered = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda match: f'<a href="{html.escape(match.group(2), quote=True)}">{match.group(1)}</a>',
        rendered,
    )
    rendered = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", rendered)
    return rendered


def parse_body_blocks(raw_body: str) -> list[dict[str, str]]:
    blocks: list[dict[str, str]] = []
    paragraph: list[str] = []

    def flush_paragraph():
        if paragraph:
            blocks.append({"type": "p", "text": " ".join(paragraph)})
            paragraph.clear()

    for line in raw_body.splitlines():
        stripped = line.strip()
        if not stripped:
            flush_paragraph()
            continue
        if stripped.startswith("## "):
            flush_paragraph()
            blocks.append({"type": "h2", "text": stripped[3:]})
            continue
        paragraph.append(stripped)
    flush_paragraph()
    return blocks


def blocks_to_html(blocks: list[dict[str, str]]) -> str:
    output = []
    for block in blocks:
        if block["type"] == "h2":
            output.append(f"<h2>{html.escape(block['text'])}</h2>")
        else:
            output.append(f"<p>{inline_markdown(block['text'])}</p>")
    return "\n".join(output)


def parse_project_source(source_path: Path) -> dict[str, dict]:
    text = source_path.read_text(encoding="utf-8")
    matches = list(
        re.finditer(
            r"^## (ENGLISH|PORTUGUÊS \(pt-PT\)|РУССКИЙ|УКРАЇНСЬКА)\s*$",
            text,
            flags=re.MULTILINE,
        )
    )
    parsed: dict[str, dict] = {}

    for index, match in enumerate(matches):
        lang = LANGUAGE_SECTIONS[match.group(1)]
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        section = text[match.end():end].strip()
        section = re.sub(r"\n---\s*$", "", section).strip()

        title_match = re.search(r"^\*\*SEO Title:\*\* (.+)$", section, flags=re.MULTILINE)
        meta_match = re.search(r"^\*\*Meta Description:\*\* (.+)$", section, flags=re.MULTILINE)
        slug_match = re.search(r"^\*\*Slug:\*\* (.+)$", section, flags=re.MULTILINE)
        h1_match = re.search(r"^# (.+)$", section, flags=re.MULTILINE)
        subtitle_match = re.search(r"^\*(.+)\*$", section, flags=re.MULTILINE)
        image_match = re.search(r"^\[IMAGE:.*\| ALT: (.+)\]$", section, flags=re.MULTILINE)

        required = [title_match, meta_match, slug_match, h1_match, subtitle_match, image_match]
        if any(item is None for item in required):
            raise ValueError(f"Incomplete project source section: {match.group(1)}")

        body_start = image_match.end()
        raw_body = section[body_start:].strip()
        blocks = parse_body_blocks(raw_body)
        if not blocks or blocks[-1]["type"] != "p":
            raise ValueError(f"Project closing paragraph missing: {match.group(1)}")
        closing = blocks.pop()

        parsed[lang] = {
            "title": title_match.group(1),
            "description": meta_match.group(1),
            "slug": slug_match.group(1),
            "h1": h1_match.group(1),
            "subtitle": subtitle_match.group(1),
            "hero_alt": image_match.group(1),
            "body_html": blocks_to_html(blocks),
            "closing_html": blocks_to_html([closing]),
        }

    if set(parsed) != {"en", "pt", "ru", "uk"}:
        raise ValueError(f"Expected four languages in {source_path}")
    return parsed


def load_project(slug: str) -> dict:
    config = PROJECT_CONFIGS[slug]
    if config["source_format"] == "localized_html":
        content = _LEGACY_PROJECT_DATA[slug]["languages"]
    else:
        content = parse_project_source(config["source"])
    return {**config, "slug": slug, "content": content}


def project_modified_iso(project: dict, lang: str) -> str:
    value = project["modified_iso"]
    if isinstance(value, dict):
        return value[lang]
    return value


PROJECT_PAGE_META = {
    slug: {
        lang: {
            "title": values["title"],
            "description": values["description"],
        }
        for lang, values in load_project(slug)["content"].items()
    }
    for slug in PROJECT_CONFIGS
}
