# S-REBUILD-W2 Delivery Report

Date: 2026-09-07 (Europe/Lisbon)

Baseline commit: `5b1f08d928c1bf9576d5873b50843207b49b7671`

Implementation commit: `5074ef713133d43028bba2a83346d96f73ff14eb`

## Delivered Scope

The owner-approved Wave 2 source was copied byte-for-byte to
`scripts/build/content/brand_pages_w2_copy_4lang.md`. Both the supplied source
and repository copy have SHA-256:

```text
a53853ed90ce9317dc61adb13cf8178ae6fad81e341d3769204453c604eb8af6
```

All seven brand families in English, Portuguese, Russian and Ukrainian now
have the approved title, meta description, pricing introduction, rewritten
price FAQ and two appended FAQ pairs. A programmatic comparison of 252 source
fields against the 28 generated pages reported zero mismatches, including the
PT Honda title, RU Ducati price answer and UK Triumph second FAQ requested as
spot checks.

Each brand page has one pricing section directly after its services section
and before known failure patterns. `BRAND_PRICING` resolves the scheduled
maintenance group, localized checklist, valve rows, brand-specific cards and
five universal workshop prices from stable records in `pricing_data.py`. The
same-language complete-price-list link is generated in every variant.

The four Pricing pages and their `OfferCatalog` graphs contain the renamed
Triumph/Royal Enfield group, the extended air-filter exception in all three
locations, the new twin-valve row and four localized brand-specific cards. All
four downloadable PDFs were regenerated with their existing names.

## Construction And Regression Tests

The brand validator now rejects any rendered euro amount absent from
`pricing_data.py`, exact group-price drift, an incorrect `from` marker, a
checklist mismatch, missing brand-specific cards, an incorrect section
position or non-local Pricing link. It also protects the approved copy SHA,
title/meta limits and visible/schema FAQ parity.

The amount assertion was break-tested by temporarily changing Honda's
generated scheduled-service amount from `150 €` to `999 €`. Validation failed
with `visible price amount(s) absent from pricing_data.py: ['999']`; the test
mutation was restored. Construction was tested in the opposite direction by
changing the canonical group amount from `150` to `151`, rebuilding and
observing the generated Honda price change; the canonical value was then
restored and rebuilt. The final 28-page amount sweep reports zero values
outside the canonical registry and no prohibited 30–40 percent comparison.

The Service/Custom validator's numeric-source parser was made tolerant of
grouped values such as `25 000`; this is the only supporting validator change
outside the brand-family validator.

## Responsive And PDF Checks

At 390×844 and 1440×1000, browser checks found no page-level horizontal
overflow. The section appeared once in the required position; the compact
checklist and horizontally contained valve table rendered inside their
section, and localized Pricing links were correct. Common CSS/JavaScript and
their cache-bust values did not change.

All four PDFs contain seven pages. Text extraction across every page confirms
the new heading, four service cards, the Triumph/Royal Enfield valve row and
the `750–1 500+ EUR` Ducati value. The affected section page in all four PDFs
was rendered to images and inspected for clipping, overlap and missing glyphs.
A second PDF build produced byte-identical files.

## Sitemap

The sitemap stays at 236 URLs with an unchanged URL key set. Baseline SHA-256:
`52aead525994703b941a5cca0f5dd94bc9589b651267a500fda767bf7e331956`.
W2 SHA-256: `cbf40099d3ab4b0502bf678d4c65f01ec71b807eea9abad215faf39e0a87b52f`.
Exactly these 32 visible-content URLs received a new `lastmod`:

| URL | New `lastmod` |
|---|---|
| `https://ironcustommotors.com/pricing/` | `2026-09-07T08:03:25+01:00` |
| `https://ironcustommotors.com/ru/pricing/` | `2026-09-07T08:03:33+01:00` |
| `https://ironcustommotors.com/uk/pricing/` | `2026-09-07T08:03:38+01:00` |
| `https://ironcustommotors.com/pt/pricing/` | `2026-09-07T08:03:29+01:00` |
| `https://ironcustommotors.com/harley-service/` | `2026-09-07T08:07:06+01:00` |
| `https://ironcustommotors.com/ru/harley-service/` | `2026-09-07T08:07:16+01:00` |
| `https://ironcustommotors.com/uk/harley-service/` | `2026-09-07T08:07:22+01:00` |
| `https://ironcustommotors.com/pt/harley-service/` | `2026-09-07T08:07:10+01:00` |
| `https://ironcustommotors.com/bmw-service/` | `2026-09-07T08:07:06+01:00` |
| `https://ironcustommotors.com/ru/bmw-service/` | `2026-09-07T08:07:15+01:00` |
| `https://ironcustommotors.com/uk/bmw-service/` | `2026-09-07T08:07:21+01:00` |
| `https://ironcustommotors.com/pt/bmw-service/` | `2026-09-07T08:07:09+01:00` |
| `https://ironcustommotors.com/ducati-service/` | `2026-09-07T08:07:06+01:00` |
| `https://ironcustommotors.com/ru/ducati-service/` | `2026-09-07T08:07:16+01:00` |
| `https://ironcustommotors.com/uk/ducati-service/` | `2026-09-07T08:07:22+01:00` |
| `https://ironcustommotors.com/pt/ducati-service/` | `2026-09-07T08:07:09+01:00` |
| `https://ironcustommotors.com/suzuki-service/` | `2026-09-07T08:07:20+01:00` |
| `https://ironcustommotors.com/ru/suzuki-service/` | `2026-09-07T08:07:19+01:00` |
| `https://ironcustommotors.com/uk/suzuki-service/` | `2026-09-07T08:07:24+01:00` |
| `https://ironcustommotors.com/pt/suzuki-service/` | `2026-09-07T08:07:13+01:00` |
| `https://ironcustommotors.com/honda-service/` | `2026-09-07T08:07:07+01:00` |
| `https://ironcustommotors.com/ru/honda-service/` | `2026-09-07T08:07:16+01:00` |
| `https://ironcustommotors.com/uk/honda-service/` | `2026-09-07T08:07:22+01:00` |
| `https://ironcustommotors.com/pt/honda-service/` | `2026-09-07T08:07:10+01:00` |
| `https://ironcustommotors.com/royal-enfield-service/` | `2026-09-07T08:07:14+01:00` |
| `https://ironcustommotors.com/ru/royal-enfield-service/` | `2026-09-07T08:07:18+01:00` |
| `https://ironcustommotors.com/uk/royal-enfield-service/` | `2026-09-07T08:07:24+01:00` |
| `https://ironcustommotors.com/pt/royal-enfield-service/` | `2026-09-07T08:07:13+01:00` |
| `https://ironcustommotors.com/triumph-service/` | `2026-09-07T08:07:20+01:00` |
| `https://ironcustommotors.com/ru/triumph-service/` | `2026-09-07T08:07:19+01:00` |
| `https://ironcustommotors.com/uk/triumph-service/` | `2026-09-07T08:07:24+01:00` |
| `https://ironcustommotors.com/pt/triumph-service/` | `2026-09-07T08:07:14+01:00` |

No other sitemap member or date changed.

## Verification And Deployment

The local canonical gates report:

```text
SEO validation passed: 236 sitemap URL(s)
Brand page validation passed: 7 brand page set(s).
Harley Hub validation passed: 12 pages and all required integrations
Service/Custom hub validation passed: 8 hubs, 4 pricing pages, 4 tyre metas.
```

All 14 registered project validators also pass. The sitemap-wide SEO pass
confirms zero broken internal links and the maintained hreflang/chrome
contracts. A fresh clone from
`https://github.com/PhilipGrishin/iron-moto-cascais.git` at documentation
commit `27a6b375ea4185791e67b7f4a6c9666a43c53cdd` completed the documented Full
Safe Rebuild, including the PDF step and every project validator, with empty
`git status --short` afterward.

GitHub Pages workflow
[`34094429593`](https://github.com/PhilipGrishin/iron-moto-cascais/actions/runs/34094429593)
completed successfully. All 32 affected production URLs returned HTTP 200.
Production `sitemap.xml` and `llms.txt` are byte-identical to the repository,
with SHA-256 values `cbf40099d3ab4b0502bf678d4c65f01ec71b807eea9abad215faf39e0a87b52f`
and `fb90fcdeb2f37b907178136406ba76fe09f081357c90a2ede47f94631e8c123f`
respectively. Cloudflare's email-obfuscation layer rewrites the visible contact
email and injects its decoder script in production HTML; after normalizing that
documented edge transformation, no other source difference remained.

Production browser inspection of `/pt/honda-service/` confirmed the approved
title, self-canonical, one pricing section, `150 €` source-group value,
same-language `/pt/pricing/` link, 8 visible FAQs and 8 matching schema FAQs.
Google Rich Results Test crawled both requested language variants successfully:

- EN `/harley-service/`: result `edxtmTQwzBGiuqLZrCBsPA`, one valid Breadcrumb
  item, no errors.
- PT `/pt/honda-service/`: result `1RENYeQWSHdJdTHDuVFNTA`, one valid Breadcrumb
  item, no errors.

## Diff Scope And Deviations

The implementation commit changes exactly 52 files. The cumulative
baseline-to-final task diff contains 54 unique files: 28 generated brand HTML
pages, four Pricing HTML pages, four Pricing PDFs, `sitemap.xml`, `llms.txt`,
10 build/data/source/validator files and six documentation/report files.
Homepage, hubs, tyre pages, PPI, contact, forms, Workers, secrets, CI, common
CSS/JavaScript and sitemap membership are unchanged.

The only implementation deviation is the one-line whitespace normalization in
`validate_service_custom_hubs.py`, required because the new approved localized
major-service name contains grouped `25 000`. No external system is touched
except the normal Git push, GitHub Pages deployment and requested Rich Results
tests.
