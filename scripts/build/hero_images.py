#!/usr/bin/env python3
"""Shared helpers for optimized hero background images."""

from __future__ import annotations

import re
from pathlib import Path

HERO_IMAGE_WIDTHS = (768, 1280, 1920)
HERO_IMAGE_FORMATS = ("avif", "webp", "jpg")
HERO_OPTIMIZED_URL_PREFIX = "/photos/optimized"


def hero_image_slug(source_url: str) -> str:
    """Return the stable optimized-image slug for a local hero source path."""
    path = source_url.split("?", 1)[0].lstrip("/")
    stem = Path(path).with_suffix("").as_posix()
    if stem.startswith("photos/"):
        stem = stem[len("photos/"):]
    stem = re.sub(r"-(?:800|1200|1600|1920|2400)$", "", stem)
    return re.sub(r"[^a-zA-Z0-9]+", "-", stem).strip("-").lower()


def optimized_hero_url(source_url: str, width: int, ext: str) -> str:
    if ext not in HERO_IMAGE_FORMATS:
        raise ValueError(f"Unsupported hero image format: {ext}")
    return f"{HERO_OPTIMIZED_URL_PREFIX}/{hero_image_slug(source_url)}-{width}.{ext}"


def hero_image_set(source_url: str, width: int = 1280) -> str:
    """Return a CSS image-set() value with AVIF, WebP and JPEG fallback."""
    avif = optimized_hero_url(source_url, width, "avif")
    webp = optimized_hero_url(source_url, width, "webp")
    jpg = optimized_hero_url(source_url, width, "jpg")
    return (
        "image-set("
        f"url('{avif}') type('image/avif'), "
        f"url('{webp}') type('image/webp'), "
        f"url('{jpg}') type('image/jpeg')"
        ")"
    )


def hero_background_css(source_url: str, width: int = 1280) -> str:
    """Return CSS declarations for an optimized background with JPEG fallback."""
    fallback = optimized_hero_url(source_url, width, "jpg")
    return f"background-image:url('{fallback}');background-image:{hero_image_set(source_url, width)}"


def hero_preload_links(source_url: str) -> str:
    """Return AVIF preload links for the homepage hero breakpoints."""
    return "\n".join(
        [
            (
                f'<link rel="preload" as="image" href="{optimized_hero_url(source_url, 768, "avif")}" '
                'type="image/avif" media="(max-width: 767px)" fetchpriority="high"/>'
            ),
            (
                f'<link rel="preload" as="image" href="{optimized_hero_url(source_url, 1280, "avif")}" '
                'type="image/avif" media="(min-width: 768px) and (max-width: 1279px)" fetchpriority="high"/>'
            ),
            (
                f'<link rel="preload" as="image" href="{optimized_hero_url(source_url, 1920, "avif")}" '
                'type="image/avif" media="(min-width: 1280px)" fetchpriority="high"/>'
            ),
        ]
    )
