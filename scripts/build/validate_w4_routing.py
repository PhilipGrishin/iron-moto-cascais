#!/usr/bin/env python3
"""Validate the checksum-backed S-REBUILD Wave 4 routing contract."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup

from blog_data import BLOG_POSTS
from project_pages_data import LEGACY_PROJECT_ORDER, PROJECT_CONFIGS, project_modified_iso
from site_chrome import localized_href
from w4_shared_data import (
    BLOG_RELATED_COPY,
    BLOG_RELATED_TARGETS,
    EXPECTED_SOURCE_SHA256,
    HOME_LINK_COPY,
    ORPHAN_SENTENCES,
    RELATED_DESCRIPTIONS,
    RELATED_TITLE_KEYS,
    SOURCE_FILE,
)


SITE_ROOT = Path(__file__).resolve().parents[2]
LANGS = ("en", "pt", "ru", "uk")
CHANGE_DATE = "2026-09-07T10:00:00+01:00"
HOME_TARGETS = (
    ("services.s1.link", "/motorcycle-service/"),
    ("services.s2.link", "/parts/"),
    ("services.s3.link", "/upgrades-tuning/"),
    ("services.s4.link", "/custom/"),
    ("services.cta5", "/motorcycle-tyre-service/"),
    ("services.cta6", "/pre-purchase-inspection/"),
    ("pricing.cta", "/pricing/"),
)


def page_path(path: str, lang: str) -> Path:
    prefix = Path() if lang == "en" else Path(lang)
    return SITE_ROOT / prefix / path.strip("/") / "index.html"


def text_of(node) -> str:
    return " ".join(node.get_text(" ", strip=True).split()) if node else ""


def inline_text_of(node) -> str:
    return " ".join("".join(node.strings).split()) if node else ""


def markdown_visible(value: str) -> str:
    return re.sub(r"\[([^]]+)]\([^)]+\)", r"\1", value)


def validate_home(issues: list[str]) -> None:
    i18n = json.loads((SITE_ROOT / "scripts/build/i18n.json").read_text(encoding="utf-8"))
    for lang in LANGS:
        path = SITE_ROOT / ("index.html" if lang == "en" else f"{lang}/index.html")
        soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
        label = path.relative_to(SITE_ROOT).as_posix()
        for key, source_target in HOME_TARGETS:
            target = localized_href(source_target, lang)
            value = soup.find(attrs={"data-i18n": key})
            anchor = value.find_parent("a") if value else None
            if value is None or text_of(value) != HOME_LINK_COPY[lang][key]:
                issues.append(f"{label}: Wave 4 homepage anchor {key} mismatch")
            elif anchor is None or anchor.get("href") != target:
                issues.append(f"{label}: Wave 4 homepage anchor {key} target mismatch")
            if i18n[lang].get(key) != HOME_LINK_COPY[lang][key]:
                issues.append(f"i18n.json {lang}: Wave 4 homepage key {key} mismatch")
        service_cards = soup.select("#services article.service")[:4]
        if len(service_cards) != 4:
            issues.append(f"{label}: expected four primary service cards")
        else:
            keys = [card.select_one(".arrow-link [data-i18n]") for card in service_cards]
            if any(node is None or node.get("data-i18n") == "services.learn" for node in keys):
                issues.append(f"{label}: shared services.learn remains on a primary service card")
            elif len({text_of(node) for node in keys}) != 4:
                issues.append(f"{label}: primary service-card anchors are not distinct")
        pricing_sub = soup.find(attrs={"data-i18n": "pricing.sub"})
        if pricing_sub is None or "2026" not in text_of(pricing_sub) or "2025" in text_of(pricing_sub):
            issues.append(f"{label}: pricing.sub year is not 2026-only")


def validate_blog(issues: list[str]) -> None:
    if set(BLOG_RELATED_TARGETS) != set(BLOG_POSTS):
        issues.append("blog_data.py: Wave 4 mapping does not cover all posts")
        return
    global_i18n = json.loads(
        (SITE_ROOT / "scripts/build/i18n.json").read_text(encoding="utf-8")
    )
    for slug, targets in BLOG_RELATED_TARGETS.items():
        if BLOG_POSTS[slug].get("modifiedISO") != CHANGE_DATE:
            issues.append(f"blog_data.py: {slug} modifiedISO is not the Wave 4 date")
        if tuple(BLOG_POSTS[slug].get("relatedTargets", ())) != targets:
            issues.append(f"blog_data.py: {slug} related target order mismatch")
        for lang in LANGS:
            path = page_path(f"blog/{slug}", lang)
            soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
            label = path.relative_to(SITE_ROOT).as_posix()
            related = soup.select_one("section[data-w4-related]")
            if related is None:
                issues.append(f"{label}: Wave 4 related block missing")
                continue
            heading = related.find("h2")
            lead = related.select_one("p.lead")
            if text_of(heading) != BLOG_RELATED_COPY[lang]["heading"]:
                issues.append(f"{label}: related heading mismatch")
            if text_of(lead) != BLOG_RELATED_COPY[lang]["lead"]:
                issues.append(f"{label}: related lead mismatch")
            cards = related.select("a.blog-related-card")
            expected_hrefs = [localized_href(target, lang) for target in targets]
            if [card.get("href") for card in cards] != expected_hrefs:
                issues.append(f"{label}: related card target order mismatch")
            for card, target in zip(cards, targets):
                expected_title = global_i18n[lang][RELATED_TITLE_KEYS[target]]
                if text_of(card.select_one(".blog-related-label")) != expected_title:
                    issues.append(f"{label}: {target} related title mismatch")
                if text_of(card.select_one(".blog-related-text")) != RELATED_DESCRIPTIONS[target][lang]:
                    issues.append(f"{label}: {target} related description mismatch")
            faq = related.find_previous_sibling("section")
            cta = related.find_next_sibling("section")
            if faq is None or faq.select_one(".blog-faq") is None:
                issues.append(f"{label}: related block is not immediately after FAQ")
            if cta is None or "blog-cta-box" not in cta.get("class", []):
                issues.append(f"{label}: related block is not immediately before CTA")
            posting_dates = []
            for script in soup.select('script[type="application/ld+json"]'):
                try:
                    graph = json.loads(script.string or "null")
                except json.JSONDecodeError:
                    continue
                nodes = graph.get("@graph", []) if isinstance(graph, dict) else []
                nodes = [graph, *nodes] if isinstance(graph, dict) else []
                posting_dates.extend(
                    node.get("dateModified")
                    for node in nodes
                    if isinstance(node, dict)
                    and node.get("@type") in {"BlogPosting", "Article"}
                )
            if posting_dates != [CHANGE_DATE]:
                issues.append(f"{label}: BlogPosting dateModified differs from Wave 4")

    for slug, localized in ORPHAN_SENTENCES.items():
        for lang, approved in localized.items():
            path = page_path(f"blog/{slug}", lang)
            soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
            label = path.relative_to(SITE_ROOT).as_posix()
            expected = markdown_visible(approved["markdown"])
            matches = [
                p
                for p in soup.select(".blog-article-body section p")
                if inline_text_of(p) == expected
            ]
            if len(matches) != 1:
                issues.append(f"{label}: expected one exact orphan-post anchor sentence")
                continue
            link = matches[0].find("a")
            expected_href = re.search(r"\]\((/[^)]+)\)", approved["markdown"]).group(1)
            if link is None or link.get("href") != expected_href:
                issues.append(f"{label}: orphan-post internal href mismatch")
            section = matches[0].find_parent("section")
            if section is None or section.find_next_sibling("section") is None:
                issues.append(f"{label}: orphan sentence section placement is incomplete")
            elif matches[0] is not section.find_all("p", recursive=False)[-1]:
                issues.append(f"{label}: orphan sentence is not the section's last paragraph")


def validate_projects(issues: list[str]) -> None:
    generic_targets = ("/projects/", "/custom/", "/community/", "/contact/")
    for slug in LEGACY_PROJECT_ORDER:
        project = PROJECT_CONFIGS[slug]
        for lang in LANGS:
            if project_modified_iso(project, lang) != CHANGE_DATE:
                issues.append(f"project_pages_data.py: {slug} {lang} modified date mismatch")
            path = page_path(f"projects/{slug}", lang)
            soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
            label = path.relative_to(SITE_ROOT).as_posix()
            section = soup.select_one('section[data-enhancement="project-related"]')
            rows = []
            for row in section.select("article.project-enhance-row") if section else []:
                link = row.select_one("h4 a[href]")
                paragraph = row.find("p")
                if link is None or paragraph is None:
                    continue
                for target in generic_targets:
                    if link.get("href") == localized_href(target, lang):
                        rows.append((target, text_of(paragraph)))
                        break
            expected = [(target, RELATED_DESCRIPTIONS[target][lang]) for target in generic_targets]
            if rows != expected:
                issues.append(f"{label}: four generic project rows differ from Wave 4 registry")


def main() -> int:
    issues: list[str] = []
    if not SOURCE_FILE.exists():
        issues.append("Wave 4 source file missing")
    validate_home(issues)
    validate_blog(issues)
    validate_projects(issues)
    if len(RELATED_DESCRIPTIONS) != 19:
        issues.append("Wave 4 combined registry does not contain 19 targets")
    if issues:
        print("S-REBUILD Wave 4 validation failed:")
        for issue in issues:
            print(f"  - {issue}")
        return 1
    print(
        "S-REBUILD Wave 4 validation passed: approved source "
        f"{EXPECTED_SOURCE_SHA256}, 4 homes, 19 registry targets, "
        "36 blog related blocks and 40 legacy-project row sets."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
