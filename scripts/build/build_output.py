#!/usr/bin/env python3
"""Stable output helpers for repository build scripts.

Generated HTML is occasionally formatted by different parsers during the
build pipeline.  Preserve the tracked representation when the generated DOM
is equivalent, so an idle build does not hide real changes in serialization
noise.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from bs4 import BeautifulSoup, Comment, NavigableString, Tag


I18N_ASSIGNMENT = re.compile(
    r"^\s*window\.ICM_I18N_PAGE\s*=\s*(\{.*\})\s*;\s*$",
    re.DOTALL,
)
BODY_ELEMENT = re.compile(r"<body\b[^>]*>.*?</body>", re.DOTALL | re.IGNORECASE)
MAIN_ELEMENT = re.compile(r"<main\b[^>]*>.*?</main>", re.DOTALL | re.IGNORECASE)
PAGE_I18N_SCRIPT = re.compile(
    r"<script\b[^>]*>\s*window\.ICM_I18N_PAGE\s*=.*?</script>",
    re.DOTALL | re.IGNORECASE,
)
JSON_LD_SCRIPT = re.compile(
    r"<script\b(?=[^>]*type=[\"']application/ld\+json[\"'])[^>]*>.*?</script>",
    re.DOTALL | re.IGNORECASE,
)
HREFLANG_LINK = re.compile(
    r"<link\b(?=[^>]*hreflang=)[^>]*?/?>",
    re.DOTALL | re.IGNORECASE,
)


def _script_value(tag: Tag) -> object:
    value = tag.string or tag.get_text()
    if tag.get("type") == "application/ld+json":
        try:
            return ("json-ld", json.dumps(json.loads(value), ensure_ascii=False, sort_keys=True))
        except json.JSONDecodeError:
            return ("script", value.strip())
    match = I18N_ASSIGNMENT.match(value)
    if match:
        try:
            payload = json.loads(match.group(1))
            return ("i18n", json.dumps(payload, ensure_ascii=False, sort_keys=True))
        except json.JSONDecodeError:
            pass
    return ("script", value.strip())


def _node_value(node) -> object | None:
    if isinstance(node, Comment):
        return ("comment", str(node).strip())
    if isinstance(node, NavigableString):
        value = re.sub(r"\s+", " ", str(node))
        return None if not value.strip() else ("text", value.strip())
    if not isinstance(node, Tag):
        return None

    attrs = []
    for key, value in sorted(node.attrs.items()):
        if isinstance(value, list):
            value = tuple(value)
        attrs.append((key, value))

    if node.name == "script":
        children = (_script_value(node),)
    elif node.name in {"style", "pre", "textarea"}:
        children = (("raw", node.get_text().strip()),)
    else:
        children = tuple(
            child_value
            for child in node.children
            if (child_value := _node_value(child)) is not None
        )
    return (node.name, tuple(attrs), children)


def html_semantically_equal(current: str, generated: str) -> bool:
    """Compare HTML structure while ignoring formatting and attribute order."""
    current_soup = BeautifulSoup(current, "html.parser")
    generated_soup = BeautifulSoup(generated, "html.parser")
    return _node_value(current_soup) == _node_value(generated_soup)


def _preserve_body_shell(current: str, generated: str) -> str:
    """Keep tracked site chrome while replacing the generator-owned main."""
    current_body_match = BODY_ELEMENT.search(current)
    generated_body_match = BODY_ELEMENT.search(generated)
    if current_body_match is None or generated_body_match is None:
        return generated

    current_body = current_body_match.group(0)
    generated_body = generated_body_match.group(0)
    current_main_match = MAIN_ELEMENT.search(current_body)
    generated_main_match = MAIN_ELEMENT.search(generated_body)
    if current_main_match is None or generated_main_match is None:
        return generated

    current_main = current_main_match.group(0)
    generated_main = generated_main_match.group(0)
    replacement_main = (
        current_main
        if html_semantically_equal(current_main, generated_main)
        else generated_main
    )
    merged_body = (
        current_body[: current_main_match.start()]
        + replacement_main
        + current_body[current_main_match.end() :]
    )
    return (
        generated[: generated_body_match.start()]
        + merged_body
        + generated[generated_body_match.end() :]
    )


def _preserve_page_i18n(current: str, generated: str) -> str:
    """Keep the page-specific inline dictionary already owned by the output."""
    current_match = PAGE_I18N_SCRIPT.search(current)
    generated_match = PAGE_I18N_SCRIPT.search(generated)
    if current_match is None or generated_match is None:
        return generated
    return (
        generated[: generated_match.start()]
        + current_match.group(0)
        + generated[generated_match.end() :]
    )


def _page_i18n_payload(script: str) -> dict | None:
    opening_end = script.find(">")
    closing_start = script.lower().rfind("</script>")
    if opening_end < 0 or closing_start < 0:
        return None
    match = I18N_ASSIGNMENT.match(script[opening_end + 1 : closing_start])
    if match is None:
        return None
    try:
        return json.loads(match.group(1))
    except json.JSONDecodeError:
        return None


def _merge_page_i18n(current: str, generated: str) -> str:
    """Retain downstream keys while updating keys owned by the generator."""
    current_match = PAGE_I18N_SCRIPT.search(current)
    generated_match = PAGE_I18N_SCRIPT.search(generated)
    if current_match is None or generated_match is None:
        return generated

    current_payload = _page_i18n_payload(current_match.group(0))
    generated_payload = _page_i18n_payload(generated_match.group(0))
    if current_payload is None or generated_payload is None:
        return generated

    merged = {
        lang: dict(values) if isinstance(values, dict) else values
        for lang, values in current_payload.items()
    }
    for lang, values in generated_payload.items():
        if isinstance(values, dict) and isinstance(merged.get(lang), dict):
            merged[lang].update(values)
        else:
            merged[lang] = values

    if merged == current_payload:
        replacement = current_match.group(0)
    else:
        replacement = (
            "<script>window.ICM_I18N_PAGE = "
            + json.dumps(merged, ensure_ascii=False)
            + ";</script>"
        )
    return (
        generated[: generated_match.start()]
        + replacement
        + generated[generated_match.end() :]
    )


def _json_script_payload(script: str) -> object | None:
    opening_end = script.find(">")
    closing_start = script.lower().rfind("</script>")
    if opening_end < 0 or closing_start < 0:
        return None
    try:
        return json.loads(script[opening_end + 1 : closing_start])
    except json.JSONDecodeError:
        return None


def _json_is_subset(generated: object, current: object) -> bool:
    if isinstance(generated, dict) and isinstance(current, dict):
        return all(
            key in current and _json_is_subset(value, current[key])
            for key, value in generated.items()
        )
    if isinstance(generated, list) and isinstance(current, list):
        return len(generated) == len(current) and all(
            _json_is_subset(generated_item, current_item)
            for generated_item, current_item in zip(generated, current)
        )
    return generated == current


def _link_identity(link: str) -> tuple[str, str] | None:
    soup = BeautifulSoup(link, "html.parser")
    tag = soup.find("link")
    if tag is None:
        return None
    hreflang = str(tag.get("hreflang", ""))
    if hreflang == "pt":
        hreflang = "pt-PT"
    return hreflang, str(tag.get("href", ""))


def _preserve_downstream_head(current: str, generated: str) -> str:
    """Keep validated downstream head enrichment during an early build stage."""
    current_json = list(JSON_LD_SCRIPT.finditer(current))
    generated_json = list(JSON_LD_SCRIPT.finditer(generated))
    if len(current_json) == len(generated_json):
        replacements = []
        for current_match, generated_match in zip(current_json, generated_json):
            current_payload = _json_script_payload(current_match.group(0))
            generated_payload = _json_script_payload(generated_match.group(0))
            if (
                current_payload is not None
                and generated_payload is not None
                and _json_is_subset(generated_payload, current_payload)
            ):
                replacements.append((generated_match.start(), generated_match.end(), current_match.group(0)))
        for start, end, replacement in reversed(replacements):
            generated = generated[:start] + replacement + generated[end:]

    current_links = list(HREFLANG_LINK.finditer(current))
    generated_links = list(HREFLANG_LINK.finditer(generated))
    if (
        len(current_links) == len(generated_links)
        and [_link_identity(match.group(0)) for match in current_links]
        == [_link_identity(match.group(0)) for match in generated_links]
    ):
        replacements = [
            (generated_match.start(), generated_match.end(), current_match.group(0))
            for current_match, generated_match in zip(current_links, generated_links)
        ]
        for start, end, replacement in reversed(replacements):
            generated = generated[:start] + replacement + generated[end:]
    return generated


def write_html_if_changed(
    path: Path,
    generated: str,
    *,
    preserve_body_shell: bool = False,
    preserve_page_i18n: bool = False,
    merge_page_i18n: bool = False,
    preserve_downstream_head: bool = False,
) -> bool:
    """Write generated HTML only when its DOM differs from the tracked file."""
    if path.exists():
        current = path.read_text(encoding="utf-8")
        if preserve_body_shell:
            generated = _preserve_body_shell(current, generated)
        if preserve_page_i18n:
            generated = _preserve_page_i18n(current, generated)
        elif merge_page_i18n:
            generated = _merge_page_i18n(current, generated)
        if preserve_downstream_head:
            generated = _preserve_downstream_head(current, generated)
        if current == generated or html_semantically_equal(current, generated):
            return False
    path.write_text(generated, encoding="utf-8")
    return True


def write_text_if_changed(path: Path, generated: str) -> bool:
    """Write text only when its bytes differ from the tracked file."""
    if path.exists() and path.read_text(encoding="utf-8") == generated:
        return False
    path.write_text(generated, encoding="utf-8")
    return True
