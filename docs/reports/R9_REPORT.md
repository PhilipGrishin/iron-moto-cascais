# R9 Delivery Report

Date: 2026-08-10 (Europe/Lisbon)  
Status: **confirmed**  
Implementation commit: `800c4c68`  
GitHub Pages workflow: `31390002213` (`success`)

## Source Integrity

- Approved input:
  `/Users/philipgrishin/Documents/Co-Work SEO/2026-08-10_reviews-curated-9.json`
- Repository target: `assets/reviews-curated.json`
- SHA-256 of both files:
  `aaad7c6c40839b4174653524fcc7749e17714792b033b861e011d57cdf708190`
- Result: byte-for-byte identical, including the absence of a trailing
  newline.
- The six original review objects are unchanged and retain their mutual order.

Exact rendered order and dates:

| Position | Author | Published date |
|---:|---|---|
| 1 | Eugene Tkachevsky | 2026-06-25 |
| 2 | Vladimir Beck | 2026-08-07 |
| 3 | Volodymyr Chyrva | 2026-08-07 |
| 4 | Graeme Gilbertson | 2026-06-21 |
| 5 | Yurii Adam | 2026-06-21 |
| 6 | Алексей Бегунов | 2026-08-03 |
| 7 | Dmytro Zhuk | 2026-06-22 |
| 8 | Александр Рыбалко | 2026-05-31 |
| 9 | Марія Легкун | 2026-05-02 |

## Canonical Reviews Workflow

Commands:

```bash
python3 scripts/build/build_reviews_schema.py
python3 scripts/build/validate_seo.py
```

Verbatim output:

```text
Fetching https://icm-reviews.vg-ab6.workers.dev/ ...
  rating=5 count=22 reviews=5
  curated source: assets/reviews-curated.json (9 records, displayCount=9)
  snapshot unchanged: assets/reviews-snapshot.json
  patched: index.html (9 curated reviews)
  patched: ru/index.html (9 curated reviews)
  patched: uk/index.html (9 curated reviews)
  patched: pt/index.html (9 curated reviews)

Done. Aggregate 5★ from 22 reviews, 9 curated Review items injected into 4 home pages.
SEO validation passed: 228 sitemap URL(s)
```

The snapshot remains the aggregate source of truth. No rating or total was
derived from the number of curated cards.

## Focused Acceptance Verification

Static parsing of each generated home page confirmed:

- exactly 9 visible `.review` cards;
- exact author order, full text and date parity with the curated source;
- exactly 9 JSON-LD `Review` items;
- JSON-LD `Review` objects match the visible curated records one-for-one;
- `AggregateRating.ratingValue = 5` and `reviewCount = 22`.

Results:

```text
index.html: cards=9 schemaReviews=9 aggregate=5.0/22 order/date/text parity passed
pt/index.html: cards=9 schemaReviews=9 aggregate=5.0/22 order/date/text parity passed
ru/index.html: cards=9 schemaReviews=9 aggregate=5.0/22 order/date/text parity passed
uk/index.html: cards=9 schemaReviews=9 aggregate=5.0/22 order/date/text parity passed
```

Responsive browser verification:

- 1440 x 1000: 9 cards, 1205 px review-grid width, no document overflow;
- 390 x 844: 9 cards in a single-column stack, 340 px review-grid width, no
  document overflow;
- both viewports displayed the `5.0 / 22` summary and the exact nine-author
  order.

## Sitemap Discipline

The URL set remains byte-for-byte equivalent. Exactly four `lastmod` values
changed:

| URL | Previous | R9 |
|---|---|---|
| `https://ironcustommotors.com/` | `2026-07-27T13:09:58+01:00` | `2026-08-10T13:39:27+01:00` |
| `https://ironcustommotors.com/pt/` | `2026-07-27T16:33:36+01:00` | `2026-08-10T13:39:27+01:00` |
| `https://ironcustommotors.com/ru/` | `2026-07-27T16:33:34+01:00` | `2026-08-10T13:39:27+01:00` |
| `https://ironcustommotors.com/uk/` | `2026-07-27T16:33:35+01:00` | `2026-08-10T13:39:27+01:00` |

The resulting sitemap SHA-256 is
`4ff1085cda49c0a631899e876f82ee4b81c93eb83ca4b8e9b8c9f2500a16e427`.

## Repository Validators

```text
SEO validation passed: 228 sitemap URL(s)
Brand page validation passed: 7 brand page set(s).
Harley Hub validation passed: 12 pages and all required integrations
OK: all 14 registered project slugs passed multilingual copy, media, schema, cache-bust, redirect and integration checks
```

`node --check` for both maintained site scripts and the Worker, Python compile
checks and `git diff --check` also passed.

## Reproducibility

The documented Full Safe Rebuild was executed on a separate clean clone at
commit `800c4c68`, including all generators, four pricing PDFs and all four
validator groups. The final `git status --short` output was empty.

The Full Safe Rebuild intentionally excludes the network-backed Reviews
Workflow; the already generated review output remained stable throughout the
rebuild, as required by the documented process.

## Production Verification

GitHub Pages workflow `31390002213` completed successfully. Cache-bypass URLs
using `?r9=800c4c68` returned HTTP 200 for `/`, `/pt/`, `/ru/` and `/uk/`.
Each production page passed the same 9-card, 9-schema-item, exact
order/date/text and `5/22` aggregate assertions.

Production artifact hashes:

```text
assets/reviews-curated.json  aaad7c6c40839b4174653524fcc7749e17714792b033b861e011d57cdf708190
sitemap.xml                  4ff1085cda49c0a631899e876f82ee4b81c93eb83ca4b8e9b8c9f2500a16e427
```

Both are byte-for-byte identical to the repository versions.

## Final Scope

Implementation output:

- `assets/reviews-curated.json`;
- `index.html`, `pt/index.html`, `ru/index.html`, `uk/index.html`;
- `sitemap.xml`, required solely for the four honest home-page `lastmod`
  updates.

Required durable documentation:

- `docs/PROJECT_STATE.md`;
- `docs/CODEX_CHANGELOG.md`;
- `docs/reports/R9_REPORT.md`.

`assets/reviews-snapshot.json`, CSS, JavaScript and cache-bust values are
unchanged. No other served pages or assets changed.
