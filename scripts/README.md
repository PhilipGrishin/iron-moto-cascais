# Build scripts

Local helper scripts that touch live data (Google reviews API via the
Cloudflare Worker, etc). Run from this folder on your machine — the
sandbox session can't reach external services.

## `build_reviews_schema.py`

Fetches the latest reviews from
`https://icm-reviews.vg-ab6.workers.dev/`, then injects an
`AggregateRating` + up to 8 `Review` items into the LocalBusiness
JSON-LD on the home page (all four languages).

Result: Google and AI engines see real review data without running JS,
which enables ⭐ star snippets in SERPs and lets AI assistants cite
specific customer feedback.

Also writes a snapshot of the worker response to
`assets/reviews-snapshot.json` (small, can be committed — useful as a
JS fallback if the worker is ever down).

### How to run

```bash
# from the repo root
python3 scripts/build_reviews_schema.py
```

Requires: Python 3.8+, `beautifulsoup4` installed (`pip install beautifulsoup4`).

### How often

Reviews change slowly. A weekly cron is plenty. Manual run when:
- new reviews come in and you want them surfaced fast
- before submitting the site for re-indexing in Search Console
- before a paid ad campaign (so the ad copy reflects current rating)

### What gets edited

After a run, you'll see modifications in:

- `index.html`, `ru/index.html`, `uk/index.html`, `pt/index.html` —
  the LocalBusiness JSON-LD now contains `aggregateRating` + `review[]`
- `assets/reviews-snapshot.json` — fresh worker dump

Commit these and push as usual.

### Safety

The script is idempotent — re-running with no changes leaves files
identical. It only touches the one JSON-LD `<script>` tag that contains
the LocalBusiness graph; it doesn't touch any other markup.
