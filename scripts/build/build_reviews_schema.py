#!/usr/bin/env python3
"""
Refresh the Google reviews snapshot and inject review schema/static fallback
HTML into the four home pages.

The live Google Places total/rating comes from the Cloudflare Worker. The
visible review cards and JSON-LD review[] items come from the editorial
curated file so marked-up reviews always match visible content.

Run locally: python3 scripts/build/build_reviews_schema.py

Idempotent: re-running with no changes leaves files identical.
"""

import json
import re
import sys
import urllib.request
from html import escape
from pathlib import Path
from bs4 import BeautifulSoup

from build_output import write_html_if_changed, write_text_if_changed

SITE_ROOT = Path(__file__).resolve().parents[2]

WORKER_URL = "https://icm-reviews.vg-ab6.workers.dev/"
CURATED_PATH = SITE_ROOT / "assets" / "reviews-curated.json"
SNAPSHOT_PATH = SITE_ROOT / "assets" / "reviews-snapshot.json"
DEFAULT_DISPLAY_COUNT = 6
MAX_CURATED_REVIEWS = 9
MIN_REVIEW_RATING = 4         # surface only 4★+ reviews
MIN_TEXT_LEN = 20             # skip 1-2 word reviews
BUSINESS_ID = "https://ironcustommotors.com/#business"
ORG_NAME = "Iron Custom Motors"
STAR_PATH = "M12 2l3 7h7l-5.5 4.5L18 21l-6-4-6 4 1.5-7.5L2 9h7z"
TEXT_LIMIT = 380
PAGES = [
    (SITE_ROOT / "index.html", "en"),
    (SITE_ROOT / "ru" / "index.html", "ru"),
    (SITE_ROOT / "uk" / "index.html", "uk"),
    (SITE_ROOT / "pt" / "index.html", "pt"),
]
REVIEW_COPY = {
    "en": {"more": "Read more", "less": "Show less", "source": "Google review"},
    "pt": {"more": "Ler mais", "less": "Mostrar menos", "source": "Avaliação Google"},
    "ru": {"more": "Читать полностью", "less": "Свернуть", "source": "Отзыв Google"},
    "uk": {"more": "Читати повністю", "less": "Згорнути", "source": "Відгук Google"},
}


def fetch_reviews():
    """Get reviews JSON from the Cloudflare Worker."""
    print(f"Fetching {WORKER_URL} ...")
    req = urllib.request.Request(WORKER_URL, headers={"User-Agent": "ICM-build-script/1.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    print(f"  rating={data.get('rating')} count={data.get('total')} reviews={len(data.get('reviews', []))}")
    return data


def stable_snapshot_payload(data):
    """Drop worker fields that change with time but not with review content."""
    payload = json.loads(json.dumps(data, ensure_ascii=False))
    payload.pop("fetchedAt", None)
    for review in payload.get("reviews", []):
        review.pop("when", None)
    return payload


def write_snapshot_if_changed(data):
    if SNAPSHOT_PATH.exists():
        current = json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))
        if stable_snapshot_payload(current) == stable_snapshot_payload(data):
            return False
    content = json.dumps(data, ensure_ascii=False, indent=2)
    return write_text_if_changed(SNAPSHOT_PATH, content)


def build_aggregate_rating(data):
    return {
        "@type": "AggregateRating",
        "ratingValue": data.get("rating"),
        "reviewCount": data.get("total"),
        "bestRating": 5,
        "worstRating": 1,
    }


def _stars_svg(rating):
    filled = round(float(rating or 0))
    stars = []
    for i in range(1, 6):
        class_attr = ' class="dim"' if i > filled else ""
        stars.append(f'<svg{class_attr} viewBox="0 0 24 24"><path d="{STAR_PATH}"></path></svg>')
    return "".join(stars)


def _initials(name):
    parts = (name or "").strip().split()
    letters = "".join(part[:1] for part in parts[:2]).upper()
    return letters or "IC"


def _truncate(text, limit):
    text = re.sub(r"\s+", " ", (text or "").strip())
    if len(text) <= limit:
        return text
    trimmed = text[:limit].rsplit(" ", 1)[0].rstrip()
    return f"{trimmed}..."


def _date_label(published_at):
    value = (published_at or "").strip()
    return value[:10] if len(value) >= 10 else "Google review"


def _normalize_review(record, index):
    author = str(record.get("author") or "").strip()
    text = re.sub(r"\s+", " ", str(record.get("text") or "").strip())
    published_at = str(record.get("publishedAt") or "").strip()
    url = str(record.get("url") or "").strip()

    if not author:
        raise ValueError(f"Curated review #{index} is missing author")
    if not text:
        raise ValueError(f"Curated review #{index} is missing text")
    if len(text) < MIN_TEXT_LEN:
        raise ValueError(f"Curated review #{index} text is shorter than {MIN_TEXT_LEN} chars")
    if not published_at:
        raise ValueError(f"Curated review #{index} is missing publishedAt")
    if not url:
        raise ValueError(f"Curated review #{index} is missing url")

    rating = int(record.get("rating") or 5)
    if rating < MIN_REVIEW_RATING or rating > 5:
        raise ValueError(f"Curated review #{index} rating must be between {MIN_REVIEW_RATING} and 5")

    return {
        "author": author,
        "rating": rating,
        "text": text,
        "lang": str(record.get("lang") or "en").strip().lower() or "en",
        "publishedAt": published_at,
        "url": url,
        "avatar": str(record.get("avatar") or "").strip(),
    }


def load_curated_reviews():
    if not CURATED_PATH.exists():
        raise FileNotFoundError(f"Missing curated reviews file: {CURATED_PATH}")
    data = json.loads(CURATED_PATH.read_text(encoding="utf-8"))
    display_count = int(data.get("displayCount") or DEFAULT_DISPLAY_COUNT)
    display_count = max(1, min(display_count, MAX_CURATED_REVIEWS))
    reviews = [
        _normalize_review(record, index)
        for index, record in enumerate(data.get("reviews", []), start=1)
    ]
    if not reviews:
        raise ValueError("Curated reviews file has no usable reviews")
    return {
        "displayCount": display_count,
        "preferPageLanguage": bool(data.get("preferPageLanguage")),
        "reviews": reviews,
    }


def _selected_curated_reviews(curated, page_lang):
    reviews = list(curated["reviews"])
    if curated.get("preferPageLanguage"):
        reviews = [
            review
            for _, review in sorted(
                enumerate(reviews),
                key=lambda pair: (pair[1].get("lang") != page_lang, pair[0]),
            )
        ]
    return reviews[:curated["displayCount"]]


def build_review_items(curated_reviews):
    """Convert visible curated reviews to JSON-LD Review items."""
    items = []
    for review in curated_reviews:
        item = {
            "@type": "Review",
            "reviewRating": {
                "@type": "Rating",
                "ratingValue": review["rating"],
                "bestRating": 5,
                "worstRating": 1,
            },
            "author": {"@type": "Person", "name": review["author"]},
            "reviewBody": review["text"],
            "datePublished": review["publishedAt"],
            "url": review["url"],
            "publisher": {"@type": "Organization", "name": "Google"},
        }
        items.append(item)
    return items


def _static_review_cards(curated_reviews, page_lang):
    copy = REVIEW_COPY.get(page_lang, REVIEW_COPY["en"])
    cards = []
    for review in curated_reviews:
        author = (review["author"] or "Google user").strip()
        short_text = _truncate(review["text"], TEXT_LIMIT)
        is_truncated = short_text != review["text"]
        role = f"{copy['source']} · {_date_label(review.get('publishedAt'))}"
        avatar_html = (
            f'<img class="avatar" src="{escape(review["avatar"], quote=True)}" '
            f'alt="{escape(author, quote=True)}" loading="lazy" referrerpolicy="no-referrer"/>'
            if review.get("avatar")
            else f'<div class="avatar">{escape(_initials(author))}</div>'
        )
        toggle = (
            '<button class="review-toggle" type="button" data-review-toggle '
            f'data-more="{escape(copy["more"], quote=True)}" '
            f'data-less="{escape(copy["less"], quote=True)}">{escape(copy["more"])}</button>'
            if is_truncated
            else ""
        )
        cards.append(f'''<article class="review">
<div class="stars">{_stars_svg(review["rating"])}</div>
<p class="review-text" data-full-text="{escape(review["text"], quote=True)}" data-short-text="{escape(short_text, quote=True)}">&ldquo;{escape(short_text)}&rdquo;</p>
{toggle}
<div class="author">{avatar_html}<div class="author-info"><span class="name">{escape(author)}</span><span class="role">{escape(role)}</span></div></div>
</article>''')
    return "\n".join(cards)


def inject_static_review_fallback(
    html: str,
    data: dict,
    curated_reviews: list[dict],
    page_lang: str,
) -> tuple[str, bool]:
    """Patch the no-network HTML fallback so raw HTML and no-JS views do not
       show placeholder review data."""
    rating = data.get("rating")
    total = data.get("total")
    cards = _static_review_cards(curated_reviews, page_lang)
    if not rating or not total or not cards:
        return html, False

    new_html = html
    new_html = re.sub(
        r'(<span[^>]*id="rsRating"[^>]*>)(.*?)(</span>)',
        rf"\g<1>{float(rating):.1f}\g<3>",
        new_html,
        count=1,
        flags=re.DOTALL,
    )
    new_html = re.sub(
        r'(<span[^>]*id="rsStars"[^>]*>)(.*?)(</span>)',
        rf"\g<1>{_stars_svg(rating)}\g<3>",
        new_html,
        count=1,
        flags=re.DOTALL,
    )
    new_html = re.sub(
        r'(<strong[^>]*id="rsTotal"[^>]*>)(.*?)(</strong>)',
        rf"\g<1>{int(total)}\g<3>",
        new_html,
        count=1,
        flags=re.DOTALL,
    )
    new_html = re.sub(
        r'(<div(?=[^>]*\sid="reviewsSummary")[^>]*?)\s+hidden(?:="")?([^>]*>)',
        r"\1\2",
        new_html,
        count=1,
    )
    new_html = re.sub(
        r'(<div(?=[^>]*\sid="reviewsFoot")[^>]*?)\s+hidden(?:="")?([^>]*>)',
        r"\1\2",
        new_html,
        count=1,
    )
    new_html = re.sub(
        r'(<div class="reviews-row reveal-stagger" id="reviewsRow">\n)(.*?)(\n</div>\n<div class="reviews-foot")',
        rf"\g<1>{cards}\g<3>",
        new_html,
        count=1,
        flags=re.DOTALL,
    )
    return new_html, new_html != html


def inject_into_business_graph(html: str, agg: dict, reviews: list[dict]) -> tuple[str, bool]:
    """Find the JSON-LD <script> that contains the LocalBusiness/MotorcycleRepair
       graph and patch it with AggregateRating + Review array."""
    soup = BeautifulSoup(html, "html.parser")
    target = None
    target_data = None
    for s in soup.find_all("script", attrs={"type": "application/ld+json"}):
        try:
            data = json.loads(s.string or "")
        except json.JSONDecodeError:
            continue
        # Look for @graph with LocalBusiness/MotorcycleRepair entry
        graph = data.get("@graph") if isinstance(data, dict) else None
        if not graph:
            continue
        for item in graph:
            t = item.get("@type", "")
            if "LocalBusiness" in (t if isinstance(t, list) else [t]) or \
               "MotorcycleRepair" in (t if isinstance(t, list) else [t]):
                target = s
                target_data = data
                target_item = item
                break
        if target:
            break

    if not target:
        return html, False

    # Patch the business item
    target_item["aggregateRating"] = agg
    target_item["review"] = reviews

    new_json = json.dumps(target_data, ensure_ascii=False, separators=(",", ":"))
    # Rewrite the script tag
    target.string = ""
    target.append(BeautifulSoup(new_json, "html.parser"))
    # BeautifulSoup might escape; use direct replace approach instead
    return str(soup).replace(str(target),
        f'<script type="application/ld+json">{new_json}</script>'), True


def main():
    try:
        data = fetch_reviews()
    except Exception as e:
        print(f"ERROR fetching reviews: {e}", file=sys.stderr)
        print("Run this script on your local machine (sandbox has no outbound network).")
        sys.exit(1)

    if not data.get("rating") or not data.get("total"):
        print("Worker response missing rating/total — aborting.", file=sys.stderr)
        sys.exit(1)

    try:
        curated = load_curated_reviews()
    except Exception as e:
        print(f"ERROR loading curated reviews: {e}", file=sys.stderr)
        sys.exit(1)

    agg = build_aggregate_rating(data)
    print(
        f"  curated source: {CURATED_PATH.relative_to(SITE_ROOT)} "
        f"({len(curated['reviews'])} records, displayCount={curated['displayCount']})"
    )

    # Also persist the reviews JSON as a snapshot the JS widget can fall back to
    SNAPSHOT_PATH.parent.mkdir(exist_ok=True)
    snapshot_changed = write_snapshot_if_changed(data)
    snapshot_status = "updated" if snapshot_changed else "unchanged"
    print(
        f"  snapshot {snapshot_status}: "
        f"{SNAPSHOT_PATH.relative_to(SITE_ROOT)}"
    )

    patched = 0
    last_review_count = 0
    for p, page_lang in PAGES:
        if not p.exists():
            print(f"  SKIP missing: {p}")
            continue
        page_reviews = _selected_curated_reviews(curated, page_lang)
        reviews = build_review_items(page_reviews)
        last_review_count = len(reviews)
        html = p.read_text(encoding="utf-8")
        new_html, ok = inject_into_business_graph(html, agg, reviews)
        # The committed fallback cards intentionally use the approved English
        # source label on every language homepage; runtime UI is localized.
        new_html, fallback_ok = inject_static_review_fallback(
            new_html,
            data,
            page_reviews,
            "en",
        )
        if (ok or fallback_ok) and write_html_if_changed(p, new_html):
            patched += 1
            print(f"  patched: {p.relative_to(SITE_ROOT)} ({len(reviews)} curated reviews)")
        elif ok:
            print(f"  unchanged: {p.relative_to(SITE_ROOT)}")
        else:
            print(f"  no LocalBusiness graph found in {p.relative_to(SITE_ROOT)} — SKIP")

    print(f"\nDone. Aggregate {agg['ratingValue']}★ from {agg['reviewCount']} reviews, "
          f"{last_review_count} curated Review items injected into {patched} home pages.")


if __name__ == "__main__":
    main()
