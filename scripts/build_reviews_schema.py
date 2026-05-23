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
from pathlib import Path
from bs4 import BeautifulSoup

SITE_ROOT = Path(__file__).resolve().parents[2] / "ICM WebSite"
# Adjust path if you run this from a different location:
if not SITE_ROOT.exists():
    # Try sandbox path
    SITE_ROOT = Path("/sessions/gracious-confident-meitner/mnt/ICM WebSite")

WORKER_URL = "https://icm-reviews.vg-ab6.workers.dev/"
N_REVIEWS_IN_SCHEMA = 8       # how many reviews to include in JSON-LD
MIN_REVIEW_RATING = 4         # surface only 4★+ reviews
MIN_TEXT_LEN = 20             # skip 1-2 word reviews
BUSINESS_ID = "https://ironcustommotors.com/#business"
ORG_NAME = "Iron Custom Motors"


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


def build_review_items(data):
    """Filter and convert reviews → Review schema items."""
    items = []
    for r in data.get("reviews", []):
        rating = r.get("rating")
        if not rating or rating < MIN_REVIEW_RATING:
            continue
        # Prefer original text (in the language the author wrote it in)
        body = (r.get("originalText") or {}).get("text") or (r.get("text") or {}).get("text") or ""
        body = body.strip()
        if len(body) < MIN_TEXT_LEN:
            continue
        author = ((r.get("authorAttribution") or {}).get("displayName") or "Google user").strip()
        published = r.get("publishTime") or ""
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
        if ok and new_html != html:
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
