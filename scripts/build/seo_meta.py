#!/usr/bin/env python3
"""Shared SEO meta helpers for generated static pages."""

from __future__ import annotations

ROBOTS_IMAGE_PREVIEW = "max-image-preview:large"


def _robots_meta_tags(soup):
    if soup.head is None:
        return []
    return [
        meta
        for meta in soup.head.find_all("meta")
        if str(meta.get("name", "")).lower() == "robots"
    ]


def robots_content_with_large_image_preview(content: str) -> str:
    """Return robots content with max-image-preview:large merged in."""
    directives = [part.strip() for part in (content or "").split(",") if part.strip()]
    next_directives = []
    found = False
    for directive in directives:
        if directive.lower().startswith("max-image-preview:"):
            if not found:
                next_directives.append(ROBOTS_IMAGE_PREVIEW)
                found = True
            continue
        next_directives.append(directive)
    if not found:
        next_directives.append(ROBOTS_IMAGE_PREVIEW)
    return ", ".join(next_directives)


def robots_has_large_image_preview(soup) -> bool:
    return any(
        ROBOTS_IMAGE_PREVIEW in meta.get("content", "").lower()
        for meta in _robots_meta_tags(soup)
    )


def upsert_robots_image_preview(soup) -> bool:
    """Ensure the page allows large Google image previews.

    Existing robots directives such as noindex/follow are preserved.
    Returns True when the soup was changed.
    """
    if soup.head is None:
        return False

    metas = _robots_meta_tags(soup)
    if metas:
        changed = False
        primary = metas[0]
        next_content = robots_content_with_large_image_preview(primary.get("content", ""))
        if primary.get("content") != next_content:
            primary["content"] = next_content
            changed = True
        for duplicate in metas[1:]:
            duplicate.decompose()
            changed = True
        return changed

    meta = soup.new_tag("meta")
    meta["name"] = "robots"
    meta["content"] = ROBOTS_IMAGE_PREVIEW

    anchor = soup.head.find("meta", attrs={"name": "theme-color"})
    if anchor is None:
        anchor = soup.head.find("meta", attrs={"name": "viewport"})
    if anchor is not None:
        anchor.insert_after(meta)
    else:
        soup.head.insert(0, meta)
    return True
