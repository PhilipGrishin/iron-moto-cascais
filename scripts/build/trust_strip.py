#!/usr/bin/env python3
"""Shared visible trust strip for commercial page families."""

from __future__ import annotations

import html
import json
from pathlib import Path

from w3_shared_data import TRUST_LABELS


SITE_ROOT = Path(__file__).resolve().parents[2]
SNAPSHOT = SITE_ROOT / "assets" / "reviews-snapshot.json"


def snapshot_rating() -> float:
    data = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    rating = data.get("rating")
    if not isinstance(rating, (int, float)):
        raise ValueError("reviews-snapshot.json has no numeric rating")
    return float(rating)


def format_rating(rating: float, lang: str) -> str:
    value = f"{rating:.1f}"
    return value if lang == "en" else value.replace(".", ",")


def trust_i18n(lang: str) -> dict[str, str]:
    rating = format_rating(snapshot_rating(), lang)
    values = TRUST_LABELS[lang]
    return {
        "trust.ratingPrefix": values[0].split("{rating}", 1)[0],
        "trust.rating": rating,
        "trust.ratingSuffix": values[0].split("{rating}", 1)[1],
        **{f"trust.item{index}": value for index, value in enumerate(values[1:], start=2)},
    }


def render_trust_strip(lang: str, *, i18n: bool = False) -> str:
    values = trust_i18n(lang)
    key = (lambda name: f' data-i18n="{name}"') if i18n else (lambda name: "")
    items = [
        '<li class="icm-trust-item icm-trust-rating">'
        '<span aria-hidden="true" class="icm-trust-star">★</span>'
        f'<span{key("trust.ratingPrefix")}>{html.escape(values["trust.ratingPrefix"])}</span>'
        f'<span data-icm-rating=""{key("trust.rating")}>{html.escape(values["trust.rating"])}</span>'
        f'<span{key("trust.ratingSuffix")}>{html.escape(values["trust.ratingSuffix"])}</span>'
        "</li>"
    ]
    items.extend(
        f'<li class="icm-trust-item"{key(f"trust.item{index}")}>{html.escape(values[f"trust.item{index}"])}</li>'
        for index in range(2, 6)
    )
    return (
        '<div class="icm-trust-strip" data-icm-trust-strip="">'
        '<div class="container"><ul>' + "".join(items) + "</ul></div></div>"
    )


TRUST_STRIP_CSS = """
.icm-trust-strip{padding:15px 0;background:#0a0a0a;border-top:1px solid var(--border);border-bottom:1px solid var(--border)}
.icm-trust-strip ul{display:flex;align-items:center;justify-content:center;flex-wrap:wrap;gap:10px 22px;margin:0;padding:0;list-style:none}
.icm-trust-item{display:inline-flex;align-items:center;gap:0;white-space:nowrap;font-family:var(--font-ui);font-size:12px;font-weight:700;line-height:1.25;letter-spacing:.075em;text-transform:uppercase;color:var(--text-dim)}
.icm-trust-item+.icm-trust-item::before{content:"·";margin-right:22px;color:var(--accent)}
.icm-trust-rating{color:#fff}.icm-trust-star{margin-right:6px;color:var(--accent)}
@media (max-width:760px){.icm-trust-strip{padding:14px 0}.icm-trust-strip ul{justify-content:flex-start;gap:9px 16px}.icm-trust-item{white-space:normal;font-size:11px}.icm-trust-item+.icm-trust-item::before{margin-right:16px}}
"""
