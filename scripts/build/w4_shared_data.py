#!/usr/bin/env python3
"""Checksum-backed routing copy introduced by S-REBUILD Wave 4."""

from __future__ import annotations

import hashlib
import re
from html import escape
from pathlib import Path

from w3_shared_data import RELATED_DESCRIPTIONS as W3_RELATED_DESCRIPTIONS


BUILD_DIR = Path(__file__).resolve().parent
SOURCE_FILE = BUILD_DIR / "content" / "w4_routing_copy_4lang.md"
EXPECTED_SOURCE_SHA256 = "0fe5adbd58e585c1292768cd93bb39de9a4e494e04381a29f347aaee8e079438"
LANG_MAP = {"EN": "en", "PT": "pt", "RU": "ru", "UK": "uk"}


def _approved_source() -> str:
    source = SOURCE_FILE.read_bytes()
    actual = hashlib.sha256(source).hexdigest()
    if actual != EXPECTED_SOURCE_SHA256:
        raise ValueError(
            f"{SOURCE_FILE.name}: SHA-256 {actual} != approved {EXPECTED_SOURCE_SHA256}"
        )
    return source.decode("utf-8")


def _section(source: str, start: str, end: str | None) -> str:
    start_match = re.search(start, source, flags=re.MULTILINE)
    if not start_match:
        raise ValueError(f"Wave 4 source section missing: {start}")
    tail = source[start_match.end():]
    if end is None:
        return tail
    end_match = re.search(end, tail, flags=re.MULTILINE)
    if not end_match:
        raise ValueError(f"Wave 4 source section end missing: {end}")
    return tail[:end_match.start()]


def _strip_count(value: str) -> str:
    return re.sub(r"\s+\(\d+\)$", "", value.strip())


def _parse_home_links(source: str) -> dict[str, dict[str, str]]:
    body = _section(source, r"^## A\.", r"^## B\.")
    result = {lang: {} for lang in LANG_MAP.values()}
    rows = re.finditer(
        r"^\| `([^`]+)` \| .*? \| (.*?) \| (.*?) \| (.*?) \| (.*?) \|$",
        body,
        flags=re.MULTILINE,
    )
    for match in rows:
        key = match.group(1)
        values = {
            "en": _strip_count(match.group(2)),
            "pt": _strip_count(match.group(3)),
            "ru": _strip_count(match.group(4)),
            "uk": _strip_count(match.group(5)),
        }
        output_key = f"{key}.link" if key.startswith("services.s") else key
        for lang, value in values.items():
            result[lang][output_key] = value
    expected_keys = {
        "services.s1.link",
        "services.s2.link",
        "services.s3.link",
        "services.s4.link",
        "services.cta5",
        "services.cta6",
        "pricing.cta",
    }
    if any(set(values) != expected_keys for values in result.values()):
        raise ValueError("Wave 4 homepage anchor inventory differs from approved Part A")
    return result


def _parse_registry_additions(source: str) -> dict[str, dict[str, str]]:
    body = _section(source, r"^## B\.", r"^## C\.")
    headings = list(
        re.finditer(r"^### .+? — `(/[^`]+/)`\s*$", body, flags=re.MULTILINE)
    )
    result: dict[str, dict[str, str]] = {}
    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(body)
        block = body[heading.end():end]
        values = {
            LANG_MAP[match.group(1)]: match.group(2)
            for match in re.finditer(
                r"^\| (EN|PT|RU|UK) \| (.*?) \| \d+ \|$",
                block,
                flags=re.MULTILINE,
            )
        }
        if set(values) != set(LANG_MAP.values()):
            raise ValueError(f"{heading.group(1)}: expected four Wave 4 descriptions")
        result[heading.group(1)] = values
    if set(result) != {"/projects/", "/contact/"}:
        raise ValueError("Wave 4 registry additions differ from approved Part B")
    return result


def _parse_blog_related(
    source: str,
) -> tuple[dict[str, dict[str, str]], dict[str, tuple[str, str, str]]]:
    body = _section(source, r"^## C\.", r"^## D\.")
    copy = {lang: {} for lang in LANG_MAP.values()}
    for match in re.finditer(
        r"^\| (EN|PT|RU|UK) \| (.*?) \| \d+ \| (.*?) \| \d+ \|$",
        body,
        flags=re.MULTILINE,
    ):
        copy[LANG_MAP[match.group(1)]] = {
            "heading": match.group(2),
            "lead": match.group(3),
        }
    if any(set(values) != {"heading", "lead"} for values in copy.values()):
        raise ValueError("Wave 4 blog-related heading copy is incomplete")

    mapping: dict[str, tuple[str, str, str]] = {}
    for match in re.finditer(
        r"^\| `([^`]+)` \| (.*?) \|$", body, flags=re.MULTILINE
    ):
        targets = []
        for item in match.group(2).split(", "):
            cleaned = item.strip().strip("`")
            if cleaned == "tyre page":
                cleaned = "/motorcycle-tyre-service/"
            targets.append(cleaned)
        if len(targets) != 3:
            raise ValueError(f"{match.group(1)}: expected exactly three related targets")
        mapping[match.group(1)] = tuple(targets)
    if len(mapping) != 9:
        raise ValueError(f"Expected 9 Wave 4 blog mappings, got {len(mapping)}")
    return copy, mapping


def _inline_markdown_link(value: str) -> str:
    match = re.search(r"\[([^]]+)]\((/[^)]+)\)", value)
    if not match:
        raise ValueError(f"Wave 4 orphan sentence has no internal markdown link: {value}")
    return (
        escape(value[:match.start()])
        + f'<a href="{escape(match.group(2), quote=True)}">{escape(match.group(1))}</a>'
        + escape(value[match.end():])
    )


def _parse_orphan_sentences(source: str) -> dict[str, dict[str, dict[str, str]]]:
    body = _section(source, r"^## D\.", r"^## E\.")
    headings = list(
        re.finditer(r"^### `/blog/([^/]+)/`.*$", body, flags=re.MULTILINE)
    )
    result: dict[str, dict[str, dict[str, str]]] = {}
    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(body)
        block = body[heading.end():end]
        values = {}
        for match in re.finditer(
            r"^\| (EN|PT|RU|UK) \| (.*?) \| \d+ \|$",
            block,
            flags=re.MULTILINE,
        ):
            markdown = match.group(2)
            values[LANG_MAP[match.group(1)]] = {
                "markdown": markdown,
                "html": _inline_markdown_link(markdown),
            }
        if set(values) != set(LANG_MAP.values()):
            raise ValueError(f"{heading.group(1)}: expected four orphan-post anchors")
        result[heading.group(1)] = values
    if len(result) != 3:
        raise ValueError(f"Expected 3 Wave 4 orphan posts, got {len(result)}")
    return result


_SOURCE = _approved_source()
HOME_LINK_COPY = _parse_home_links(_SOURCE)
W4_RELATED_DESCRIPTIONS = _parse_registry_additions(_SOURCE)
RELATED_DESCRIPTIONS = {**W3_RELATED_DESCRIPTIONS, **W4_RELATED_DESCRIPTIONS}
BLOG_RELATED_COPY, BLOG_RELATED_TARGETS = _parse_blog_related(_SOURCE)
ORPHAN_SENTENCES = _parse_orphan_sentences(_SOURCE)

RELATED_TITLE_KEYS = {
    "/motorcycle-service/": "services.s1.title",
    "/upgrades-tuning/": "services.s3.title",
    "/parts/": "services.s2.title",
    "/custom/": "services.s4.title",
    "/motorcycle-tyre-service/": "nav.tyreServ",
    "/pricing/": "nav.pricing",
    "/community/": "nav.community",
    "/pre-purchase-inspection/": "nav.preInsp",
    "/authorized-dealer/": "nav.authorizedDealerHub",
    "/harley-tuning/": "nav.harleyTuning",
    "/harley-service/": "nav.hdServ",
    "/bmw-service/": "nav.bmwServ",
    "/ducati-service/": "nav.ducServ",
    "/suzuki-service/": "nav.suzukiServ",
    "/honda-service/": "nav.hondaServ",
    "/royal-enfield-service/": "nav.brandRoyalEnfield",
    "/triumph-service/": "nav.brandTriumph",
    "/projects/": "nav.projects",
    "/contact/": "nav.contact",
}

if len(RELATED_DESCRIPTIONS) != 19:
    raise ValueError(f"Expected 19 combined routing targets, got {len(RELATED_DESCRIPTIONS)}")
if set(RELATED_TITLE_KEYS) != set(RELATED_DESCRIPTIONS):
    raise ValueError("Wave 4 title-key registry differs from the 19 routing targets")
for slug, targets in BLOG_RELATED_TARGETS.items():
    unknown = set(targets) - set(RELATED_DESCRIPTIONS)
    if unknown:
        raise ValueError(f"{slug}: unknown related targets: {sorted(unknown)}")


def related_description_key(path: str) -> str:
    """Return the stable i18n key used by related-card description elements."""
    slug = path.strip("/").replace("/", ".")
    return f"related.description.{slug}"


def related_source_path(path: str, lang: str) -> str:
    """Resolve a localized related href back to the English registry key."""
    from site_chrome import localized_href

    for source_path in RELATED_DESCRIPTIONS:
        if path in {source_path, localized_href(source_path, lang)}:
            return source_path
    raise KeyError(f"No related-description target for {path} ({lang})")
