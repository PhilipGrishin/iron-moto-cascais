#!/usr/bin/env python3
"""
Fetch fresh Google reviews from the Cloudflare Worker and inject them as
JSON-LD AggregateRating + Review schema into the LocalBusiness graph
on every home page (en/ru/uk/pt). This makes the reviews visible to Google
and AI engines without JS execution — and enables review stars in SERPs.

Run locally:  python3 build_reviews_schema.py
(Sandbox in Cowork has no outbound network, so this MUST be run on the
local machine where push happens.)

Idempotent: re-running with no changes leaves files identical.
"""

import json
import re
import sys
import urllib.request
from html import escape
from pathlib import Path
from bs4 import BeautifulSoup

SITE_ROOT = Path(__file__).resolve().parents[2]

WORKER_URL = "https://icm-reviews.vg-ab6.workers.dev/"
N_REVIEWS_IN_SCHEMA = 8       # how many reviews to include in JSON-LD
MIN_REVIEW_RATING = 4         # surface only 4★+ reviews
MIN_TEXT_LEN = 20             # skip 1-2 word reviews
BUSINESS_ID = "https://ironcustommotors.com/#business"
ORG_NAME = "Iron Custom Motors"
STAR_PATH = "M12 2l3 7h7l-5.5 4.5L18 21l-6-4-6 4 1.5-7.5L2 9h7z"


def fetch_reviews():
    """Get reviews JSON from the Cloudflare Worker."""
    print(f"Fetching {WORKER_URL} ...")
    req = urllib.request.Request(WORKER_URL, headers={"User-Agent": "ICM-build-script/1.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    print(f"  rating={data.get('rating')} count={data.get('total')} reviews={len(data.get('reviews', []))}")
    return data


def build_aggregate_rating(data):
    return {
        "@type": "AggregateRating",
        "ratingValue": data.get("rating"),
        "reviewCount": data.get("total"),
        "bestRating": 5,
        "worstRating": 1,
    }


def _extract_text(v):
    """Handle both shapes: plain string OR Google Places {text, languageCode}."""
    if not v:
        return ""
    if isinstance(v, str):
        return v
    if isinstance(v, dict):
        return v.get("text") or ""
    return ""


def _extract_author(v):
    if not v:
        return ""
    if isinstance(v, str):
        return v
    if isinstance(v, dict):
        return v.get("displayName") or v.get("name") or ""
    return ""


def build_review_items(data):
    """Filter and convert reviews → Review schema items."""
    items = []
    for r in data.get("reviews", []):
        rating = r.get("rating")
        if not rating or rating < MIN_REVIEW_RATING:
            continue
        # Prefer original text (author's language) over machine-translated text.
        body = _extract_text(r.get("originalText")) or _extract_text(r.get("text"))
        body = body.strip()
        if len(body) < MIN_TEXT_LEN:
            continue
        author = _extract_author(r.get("authorAttribution")) or r.get("author") or "Google user"
        author = (author or "").strip() or "Google user"
        published = r.get("publishTime") or r.get("publishedAt") or ""
        items.append({
            "@type": "Review",
            "reviewRating": {
                "@type": "Rating",
                "ratingValue": rating,
                "bestRating": 5,
                "worstRating": 1,
            },
            "author": {"@type": "Person", "name": author},
            "reviewBody": body[:1200],   # truncate if super long
            "datePublished": published[:10] if published else None,
            "publisher": {"@type": "Organization", "name": "Google"},
        })
        if len(items) >= N_REVIEWS_IN_SCHEMA:
            break
    return items


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


def _static_review_cards(data):
    reviews = []
    for review in data.get("reviews", []):
        text = (_extract_text(review.get("originalText")) or _extract_text(review.get("text"))).strip()
        if len(text) < MIN_TEXT_LEN:
            continue
        reviews.append({
            "author": _extract_author(review.get("authorAttribution")) or review.get("author") or "Google user",
            "rating": review.get("rating") or 5,
            "text": text,
            "when": review.get("when") or "Google review",
        })

    reviews.sort(key=lambda r: (-(r["rating"] or 0), -len(r["text"])))
    cards = []
    for review in reviews[:3]:
        author = (review["author"] or "Google user").strip()
        text = _truncate(review["text"], 380)
        role = f"Google review · {review['when']}" if review.get("when") else "Google review"
        cards.append(f'''<article class="review">
<div class="stars">{_stars_svg(review["rating"])}</div>
<p>&ldquo;{escape(text)}&rdquo;</p>
<div class="author"><div class="avatar">{escape(_initials(author))}</div><div class="author-info"><span class="name">{escape(author)}</span><span class="role">{escape(role)}</span></div></div>
</article>''')
    return "\n".join(cards)


def inject_static_review_fallback(html: str, data: dict) -> tuple[str, bool]:
    """Patch the no-network HTML fallback so raw HTML and no-JS views do not
       show placeholder review data."""
    rating = data.get("rating")
    total = data.get("total")
    cards = _static_review_cards(data)
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

    agg = build_aggregate_rating(data)
    reviews = build_review_items(data)
    print(f"  using {len(reviews)} reviews for schema (≥{MIN_REVIEW_RATING}★, ≥{MIN_TEXT_LEN} chars)")

    # Also persist the reviews JSON as a snapshot the JS widget can fall back to
    snapshot_path = SITE_ROOT / "assets" / "reviews-snapshot.json"
    snapshot_path.parent.mkdir(exist_ok=True)
    snapshot_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  snapshot → {snapshot_path.relative_to(SITE_ROOT)}")

    # Inject into home pages of all 4 languages
    pages = [
        SITE_ROOT / "index.html",
        SITE_ROOT / "ru" / "index.html",
        SITE_ROOT / "uk" / "index.html",
        SITE_ROOT / "pt" / "index.html",
    ]
    patched = 0
    for p in pages:
        if not p.exists():
            print(f"  SKIP missing: {p}")
            continue
        html = p.read_text(encoding="utf-8")
        new_html, ok = inject_into_business_graph(html, agg, reviews)
        new_html, fallback_ok = inject_static_review_fallback(new_html, data)
        if (ok or fallback_ok) and new_html != html:
            p.write_text(new_html, encoding="utf-8")
            patched += 1
            print(f"  patched: {p.relative_to(SITE_ROOT)}")
        elif ok:
            print(f"  unchanged: {p.relative_to(SITE_ROOT)}")
        else:
            print(f"  no LocalBusiness graph found in {p.relative_to(SITE_ROOT)} — SKIP")

    print(f"\nDone. Aggregate {agg['ratingValue']}★ from {agg['reviewCount']} reviews, "
          f"{len(reviews)} Review items injected into {patched} home pages.")


if __name__ == "__main__":
    main()
