#!/usr/bin/env python3
"""Checksum-backed shared copy introduced by S-REBUILD Wave 3."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path


BUILD_DIR = Path(__file__).resolve().parent
SOURCE_FILE = BUILD_DIR / "content" / "w3_anchors_heads_strip.md"
EXPECTED_SOURCE_SHA256 = "9822c913f8e70d8edc9ed3e9806afd1e6525f4b193c44b1a05ecf5043efe4d13"
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
        raise ValueError(f"Wave 3 source section missing: {start}")
    if end is None:
        return source[start_match.end():]
    end_match = re.search(end, source[start_match.end():], flags=re.MULTILINE)
    if not end_match:
        raise ValueError(f"Wave 3 source section end missing: {end}")
    return source[start_match.end():start_match.end() + end_match.start()]


def _parse_related(source: str) -> dict[str, dict[str, str]]:
    body = _section(source, r"^## A\.", r"^## B\.")
    headings = list(re.finditer(r"^### .+? — `(/[^`]+/)`\s*$", body, flags=re.MULTILINE))
    related: dict[str, dict[str, str]] = {}
    for index, heading in enumerate(headings):
        path = heading.group(1)
        end = headings[index + 1].start() if index + 1 < len(headings) else len(body)
        block = body[heading.end():end]
        values: dict[str, str] = {}
        for match in re.finditer(
            r"^\| (EN|PT|RU|UK) \| (.*?) \| \d+ \|\s*$",
            block,
            flags=re.MULTILINE,
        ):
            values[LANG_MAP[match.group(1)]] = match.group(2)
        if set(values) != set(LANG_MAP.values()):
            raise ValueError(f"{path}: expected four Wave 3 related descriptions")
        related[path] = values
    if len(related) != 17:
        raise ValueError(f"Expected 17 related-description targets, got {len(related)}")
    return related


def _parse_head_trims(source: str) -> dict[str, dict[str, dict[str, str]]]:
    body = _section(source, r"^## B\.", r"^## C\.")
    headings = list(re.finditer(r"^### `(/[^`]+/)`\s*$", body, flags=re.MULTILINE))
    trims: dict[str, dict[str, dict[str, str]]] = {}
    for index, heading in enumerate(headings):
        path = heading.group(1)
        end = headings[index + 1].start() if index + 1 < len(headings) else len(body)
        block = body[heading.end():end]
        fields: dict[str, dict[str, str]] = {}
        markers = list(re.finditer(r"^\*\*(Title|Meta)\*\*", block, flags=re.MULTILINE))
        for marker_index, marker in enumerate(markers):
            field_end = markers[marker_index + 1].start() if marker_index + 1 < len(markers) else len(block)
            field_block = block[marker.end():field_end]
            values: dict[str, str] = {}
            for match in re.finditer(
                r"^\| (EN|PT|RU|UK) \| .*? \(\d+\) \| (.*?) \(\d+\) \|\s*$",
                field_block,
                flags=re.MULTILINE,
            ):
                values[LANG_MAP[match.group(1)]] = match.group(2)
            if values:
                if set(values) != set(LANG_MAP.values()):
                    raise ValueError(f"{path} {marker.group(1)}: expected four head trims")
                fields[marker.group(1).lower()] = values
        trims[path] = fields
    expected = {
        "/pre-purchase-inspection/": {"meta"},
        "/contact/": {"title", "meta"},
        "/services/": {"title", "meta"},
        "/english-speaking-motorcycle-workshop/": {"meta"},
    }
    if {path: set(fields) for path, fields in trims.items()} != expected:
        raise ValueError("Wave 3 head-trim inventory differs from the approved source")
    return trims


def _parse_trust_labels(source: str) -> dict[str, list[str]]:
    body = _section(source, r"^## C\.", r"^## Self-check")
    labels = {lang: [] for lang in LANG_MAP.values()}
    row_pattern = re.compile(
        r"^\| (.*?) \(\d+\) \| (.*?) \(\d+\) \| (.*?) \(\d+\) \| (.*?) \(\d+\) \|\s*$",
        flags=re.MULTILINE,
    )
    for match in row_pattern.finditer(body):
        row = {"pt": match.group(1), "en": match.group(2), "ru": match.group(3), "uk": match.group(4)}
        for lang, value in row.items():
            labels[lang].append(value)
    if any(len(values) != 5 for values in labels.values()):
        raise ValueError("Expected five Wave 3 trust-strip labels in each language")
    for lang, values in labels.items():
        number = "5.0" if lang == "en" else "5,0"
        if number not in values[0]:
            raise ValueError(f"{lang}: trust rating label has no approved decimal value")
        values[0] = values[0].replace(number, "{rating}", 1)
    return labels


_SOURCE = _approved_source()
RELATED_DESCRIPTIONS = _parse_related(_SOURCE)
HEAD_TRIMS = _parse_head_trims(_SOURCE)
TRUST_LABELS = _parse_trust_labels(_SOURCE)


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
