"""Load the owner-approved Wave 2 brand copy from its checked Markdown source."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path


CONTENT_PATH = Path(__file__).with_name("content") / "brand_pages_w2_copy_4lang.md"
EXPECTED_SHA256 = "a53853ed90ce9317dc61adb13cf8178ae6fad81e341d3769204453c604eb8af6"
SLUGS = (
    "harley-service",
    "bmw-service",
    "ducati-service",
    "honda-service",
    "suzuki-service",
    "triumph-service",
    "royal-enfield-service",
)
LANG_HEADING_TO_CODE = {"EN": "en", "PT (pt-PT)": "pt", "RU": "ru", "UK": "uk"}


def _required(pattern: str, text: str, label: str) -> str:
    match = re.search(pattern, text, flags=re.MULTILINE)
    if not match:
        raise ValueError(f"Missing {label} in {CONTENT_PATH}")
    return match.group(1)


def load_w2_brand_copy() -> dict[str, dict[str, dict[str, str]]]:
    raw = CONTENT_PATH.read_bytes()
    actual = hashlib.sha256(raw).hexdigest()
    if actual != EXPECTED_SHA256:
        raise ValueError(
            f"Unexpected W2 brand-copy SHA-256: {actual}; expected {EXPECTED_SHA256}"
        )
    text = raw.decode("utf-8")
    result: dict[str, dict[str, dict[str, str]]] = {}

    for slug in SLUGS:
        brand_match = re.search(
            rf"^## {re.escape(slug)}\n(?P<body>.*?)(?=^## (?:{'|'.join(map(re.escape, SLUGS))}|Implementer mapping)|\Z)",
            text,
            flags=re.MULTILINE | re.DOTALL,
        )
        if not brand_match:
            raise ValueError(f"Missing brand section {slug} in {CONTENT_PATH}")
        brand_body = brand_match.group("body")
        result[slug] = {}

        headings = list(re.finditer(r"^### (EN|PT \(pt-PT\)|RU|UK)\n", brand_body, re.MULTILINE))
        if len(headings) != 4:
            raise ValueError(f"Expected four language sections for {slug}, found {len(headings)}")
        for index, heading in enumerate(headings):
            lang = LANG_HEADING_TO_CODE[heading.group(1)]
            end = headings[index + 1].start() if index + 1 < len(headings) else len(brand_body)
            section = brand_body[heading.end():end]
            result[slug][lang] = {
                "title": _required(r"^\*\*Title \(\d+\):\*\* (.+)$", section, f"{slug}/{lang} title"),
                "description": _required(r"^\*\*Meta \(\d+\):\*\* (.+)$", section, f"{slug}/{lang} meta"),
                "section_intro": _required(r"^\*\*Section intro:\*\* (.+)$", section, f"{slug}/{lang} section intro"),
                "price_faq_q": _required(r"^\*\*Price FAQ — Q:\*\* (.+?) \*\*A:\*\*", section, f"{slug}/{lang} price FAQ question"),
                "price_faq_a": _required(r"^\*\*Price FAQ — Q:\*\* .+? \*\*A:\*\* (.+)$", section, f"{slug}/{lang} price FAQ answer"),
                "faq_1_q": _required(r"^\*\*FAQ \+1 — Q:\*\* (.+?) \*\*A:\*\*", section, f"{slug}/{lang} FAQ +1 question"),
                "faq_1_a": _required(r"^\*\*FAQ \+1 — Q:\*\* .+? \*\*A:\*\* (.+)$", section, f"{slug}/{lang} FAQ +1 answer"),
                "faq_2_q": _required(r"^\*\*FAQ \+2 — Q:\*\* (.+?) \*\*A:\*\*", section, f"{slug}/{lang} FAQ +2 question"),
                "faq_2_a": _required(r"^\*\*FAQ \+2 — Q:\*\* .+? \*\*A:\*\* (.+)$", section, f"{slug}/{lang} FAQ +2 answer"),
            }
    return result


W2_BRAND_COPY = load_w2_brand_copy()
