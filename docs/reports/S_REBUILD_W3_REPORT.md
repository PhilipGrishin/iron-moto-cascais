# S-REBUILD-W3 Delivery Report

Date: 2026-09-07 (Europe/Lisbon)

Baseline commit: `fcaf3a2858440335ca819a6e2fb0994acced1204`

Implementation commit: `49e80dfcb8a400a0481ca2638ae1b63551da98c8`

Documentation commit: `207e063890fc394de08393d8585b459ec0d73be1`

## Delivered Scope

The three owner-approved Wave 3 inputs were copied byte-for-byte to the
repository and verified with these SHA-256 values:

| Repository source | SHA-256 |
|---|---|
| `scripts/build/content/parts_hub_copy_4lang.md` | `86687081e07eb74377e9d15aa0c81aca3a2beec138dfc7677ebb4ace5272538e` |
| `scripts/build/content/upgrades_hub_copy_4lang.md` | `1385731f4051d2d1bf32885f5c9decdc802f602b90de507189d7883d07c7ebfc` |
| `scripts/build/content/w3_anchors_heads_strip.md` | `9822c913f8e70d8edc9ed3e9806afd1e6525f4b193c44b1a05ecf5043efe4d13` |

Parts and Upgrades are now registered beside Service and Custom in the shared
copy-driven commercial-hub generator. All eight new language variants have one
H1, five numbered sections, six source-identical visible FAQ items and six
matching `FAQPage` questions, localized `Service` and `BreadcrumbList` data,
same-language related links, localized WhatsApp prefill, telephone and lead-form
CTAs, self-canonical URLs and complete hreflang clusters. Whole-page source
comparison is part of `validate_service_custom_hubs.py` and passed for all four
hubs in all four languages.

The legacy generic-i18n path no longer owns Parts or Upgrades. Their retired
page-specific prefixes are `pp.*` and `up.*`; neither remains in generated HTML
or the maintained i18n runtime. `build_i18n.py` excludes both pages and
`enhance_money_pages.py` has an empty compatibility page map.

The checked Wave 3 registry supplies the localized text for all 17 related
targets. Brand related and other-brand cards resolve descriptions through this
registry instead of the former `seo.relatedText` and `seo.otherBrandText`
fillers. A rendered-HTML sweep found zero old filler sentences in all four
languages, and the focused validator checks every card against its target.

## Trust Strip And Rating Lifecycle

One shared trust-strip component is rendered directly after the hero on the
four commercial hubs, seven brand-service families, tyre service and
pre-purchase inspection: 13 families x four languages, exactly 52 pages. It has
the five owner-approved localized items, no review count and no schema change.
The homepage has no trust strip.

The no-JavaScript rating is read from `assets/reviews-snapshot.json` at build
time and formatted as `5.0` in English and `5,0` in Portuguese, Russian and
Ukrainian. A local mutation test changed the snapshot rating to `4.9`, rebuilt
the 52 pages and observed `4.9` / `4,9` in every expected variant. The original
snapshot was then restored byte-for-byte. In the browser, the
`data-icm-rating` hook is refreshed through the existing Reviews Worker request
and 12-hour cache; the static snapshot remains the failure/no-JavaScript
fallback.

All 52 local pages were checked at 390 x 844 and 1440 x 900. Each contained one
strip and five items, none caused document-level horizontal overflow, and all
five items stayed on one row at 1440 pixels. Production checks on Portuguese
Parts and English Upgrades repeated the 390/1440 layout checks: the strip wrapped
inside its container on mobile and stayed on one row on desktop. The hero
resource inventory contained exactly one responsive AVIF candidate per test:

| Page | 390 px | 1440 px |
|---|---|---|
| PT Parts | `parts-shelf-768.avif` | `parts-shelf-1920.avif` |
| EN Upgrades | `mechanic-768.avif` | `mechanic-1920.avif` |

## Approved Head Trims

The exact Wave 3 title/meta replacements were applied to Contact, Services,
pre-purchase inspection and the English-speaking workshop hub. The eight new
Contact/Services titles are at most 60 characters and all 16 metadata
descriptions are 140-155 characters. Derived Open Graph and Twitter values
match the canonical head values.

Contact, Services and the English-speaking hub are head-only changes, so their
12 sitemap dates did not move. Pre-purchase inspection also received the visible
trust strip, so its four dates correctly belong to the 52 content changes.

## Sitemap

The sitemap retains 236 URLs with an unchanged URL key set. Baseline SHA-256:
`cbf40099d3ab4b0502bf678d4c65f01ec71b807eea9abad215faf39e0a87b52f`.
Wave 3 SHA-256:
`d8a1e6f48f55c699123fe4286f381f3326c6f6b604897457690e72299d5ad2e6`.
Exactly these 52 visible-content URLs received a new `lastmod`:

| URL | Previous `lastmod` | New `lastmod` |
|---|---|---|
| `https://ironcustommotors.com/bmw-service/` | `2026-09-07T08:07:06+01:00` | `2026-09-07T09:29:17+01:00` |
| `https://ironcustommotors.com/custom/` | `2026-09-06T22:09:32+01:00` | `2026-09-07T09:26:03+01:00` |
| `https://ironcustommotors.com/ducati-service/` | `2026-09-07T08:07:06+01:00` | `2026-09-07T09:29:17+01:00` |
| `https://ironcustommotors.com/harley-service/` | `2026-09-07T08:07:06+01:00` | `2026-09-07T09:29:18+01:00` |
| `https://ironcustommotors.com/honda-service/` | `2026-09-07T08:07:07+01:00` | `2026-09-07T09:29:18+01:00` |
| `https://ironcustommotors.com/motorcycle-service/` | `2026-09-06T22:09:31+01:00` | `2026-09-07T09:26:02+01:00` |
| `https://ironcustommotors.com/motorcycle-tyre-service/` | `2026-08-09T10:02:41+01:00` | `2026-09-07T09:29:18+01:00` |
| `https://ironcustommotors.com/parts/` | `2026-06-29T16:43:22+01:00` | `2026-09-07T09:26:03+01:00` |
| `https://ironcustommotors.com/pre-purchase-inspection/` | `2026-07-31T14:26:11+01:00` | `2026-09-07T09:29:18+01:00` |
| `https://ironcustommotors.com/pt/bmw-service/` | `2026-09-07T08:07:09+01:00` | `2026-09-07T09:29:20+01:00` |
| `https://ironcustommotors.com/pt/custom/` | `2026-09-06T22:09:32+01:00` | `2026-09-07T09:26:03+01:00` |
| `https://ironcustommotors.com/pt/ducati-service/` | `2026-09-07T08:07:09+01:00` | `2026-09-07T09:29:20+01:00` |
| `https://ironcustommotors.com/pt/harley-service/` | `2026-09-07T08:07:10+01:00` | `2026-09-07T09:29:20+01:00` |
| `https://ironcustommotors.com/pt/honda-service/` | `2026-09-07T08:07:10+01:00` | `2026-09-07T09:29:21+01:00` |
| `https://ironcustommotors.com/pt/montagem-de-pneus-mota/` | `2026-08-09T10:02:43+01:00` | `2026-09-07T09:29:21+01:00` |
| `https://ironcustommotors.com/pt/motorcycle-service/` | `2026-09-06T22:09:32+01:00` | `2026-09-07T09:26:02+01:00` |
| `https://ironcustommotors.com/pt/parts/` | `2026-06-29T16:43:22+01:00` | `2026-09-07T09:26:03+01:00` |
| `https://ironcustommotors.com/pt/pre-purchase-inspection/` | `2026-07-31T14:26:11+01:00` | `2026-09-07T09:29:21+01:00` |
| `https://ironcustommotors.com/pt/royal-enfield-service/` | `2026-09-07T08:07:13+01:00` | `2026-09-07T09:29:22+01:00` |
| `https://ironcustommotors.com/pt/suzuki-service/` | `2026-09-07T08:07:13+01:00` | `2026-09-07T09:29:23+01:00` |
| `https://ironcustommotors.com/pt/triumph-service/` | `2026-09-07T08:07:14+01:00` | `2026-09-07T09:29:23+01:00` |
| `https://ironcustommotors.com/pt/upgrades-tuning/` | `2026-06-29T16:43:22+01:00` | `2026-09-07T09:26:04+01:00` |
| `https://ironcustommotors.com/royal-enfield-service/` | `2026-09-07T08:07:14+01:00` | `2026-09-07T09:29:23+01:00` |
| `https://ironcustommotors.com/ru/bmw-service/` | `2026-09-07T08:07:15+01:00` | `2026-09-07T09:29:24+01:00` |
| `https://ironcustommotors.com/ru/custom/` | `2026-09-06T22:09:32+01:00` | `2026-09-07T09:26:03+01:00` |
| `https://ironcustommotors.com/ru/ducati-service/` | `2026-09-07T08:07:16+01:00` | `2026-09-07T09:29:24+01:00` |
| `https://ironcustommotors.com/ru/harley-service/` | `2026-09-07T08:07:16+01:00` | `2026-09-07T09:29:24+01:00` |
| `https://ironcustommotors.com/ru/honda-service/` | `2026-09-07T08:07:16+01:00` | `2026-09-07T09:29:25+01:00` |
| `https://ironcustommotors.com/ru/motorcycle-service/` | `2026-09-06T22:09:31+01:00` | `2026-09-07T09:26:02+01:00` |
| `https://ironcustommotors.com/ru/parts/` | `2026-06-29T16:43:22+01:00` | `2026-09-07T09:26:03+01:00` |
| `https://ironcustommotors.com/ru/pre-purchase-inspection/` | `2026-07-31T14:26:11+01:00` | `2026-09-07T09:29:25+01:00` |
| `https://ironcustommotors.com/ru/royal-enfield-service/` | `2026-09-07T08:07:18+01:00` | `2026-09-07T09:29:26+01:00` |
| `https://ironcustommotors.com/ru/shinomontazh-mototsiklov/` | `2026-08-09T10:02:47+01:00` | `2026-09-07T09:29:26+01:00` |
| `https://ironcustommotors.com/ru/suzuki-service/` | `2026-09-07T08:07:19+01:00` | `2026-09-07T09:29:26+01:00` |
| `https://ironcustommotors.com/ru/triumph-service/` | `2026-09-07T08:07:19+01:00` | `2026-09-07T09:29:26+01:00` |
| `https://ironcustommotors.com/ru/upgrades-tuning/` | `2026-06-29T16:43:22+01:00` | `2026-09-07T09:26:04+01:00` |
| `https://ironcustommotors.com/suzuki-service/` | `2026-09-07T08:07:20+01:00` | `2026-09-07T09:29:27+01:00` |
| `https://ironcustommotors.com/triumph-service/` | `2026-09-07T08:07:20+01:00` | `2026-09-07T09:29:27+01:00` |
| `https://ironcustommotors.com/uk/bmw-service/` | `2026-09-07T08:07:21+01:00` | `2026-09-07T09:29:28+01:00` |
| `https://ironcustommotors.com/uk/custom/` | `2026-09-06T22:09:32+01:00` | `2026-09-07T09:26:03+01:00` |
| `https://ironcustommotors.com/uk/ducati-service/` | `2026-09-07T08:07:22+01:00` | `2026-09-07T09:29:29+01:00` |
| `https://ironcustommotors.com/uk/harley-service/` | `2026-09-07T08:07:22+01:00` | `2026-09-07T09:29:29+01:00` |
| `https://ironcustommotors.com/uk/honda-service/` | `2026-09-07T08:07:22+01:00` | `2026-09-07T09:29:29+01:00` |
| `https://ironcustommotors.com/uk/motorcycle-service/` | `2026-09-06T22:09:32+01:00` | `2026-09-07T09:26:02+01:00` |
| `https://ironcustommotors.com/uk/parts/` | `2026-06-29T16:43:22+01:00` | `2026-09-07T09:26:03+01:00` |
| `https://ironcustommotors.com/uk/pre-purchase-inspection/` | `2026-07-31T14:26:11+01:00` | `2026-09-07T09:29:30+01:00` |
| `https://ironcustommotors.com/uk/royal-enfield-service/` | `2026-09-07T08:07:24+01:00` | `2026-09-07T09:29:31+01:00` |
| `https://ironcustommotors.com/uk/shynomontazh-mototsykliv/` | `2026-08-09T10:02:50+01:00` | `2026-09-07T09:29:31+01:00` |
| `https://ironcustommotors.com/uk/suzuki-service/` | `2026-09-07T08:07:24+01:00` | `2026-09-07T09:29:31+01:00` |
| `https://ironcustommotors.com/uk/triumph-service/` | `2026-09-07T08:07:24+01:00` | `2026-09-07T09:29:31+01:00` |
| `https://ironcustommotors.com/uk/upgrades-tuning/` | `2026-06-29T16:43:22+01:00` | `2026-09-07T09:26:04+01:00` |
| `https://ironcustommotors.com/upgrades-tuning/` | `2026-06-29T16:43:22+01:00` | `2026-09-07T09:26:04+01:00` |

No other sitemap member or date changed.

## Verification And Deployment

The canonical local gates report:

```text
SEO validation passed: 236 sitemap URL(s)
Brand page validation passed: 7 brand page set(s).
Harley Hub validation passed: 12 pages and all required integrations
Commercial hub validation passed: 16 hub pages, 52 trust strips, related descriptions and head trims.
```

All 14 registered project validators also pass. The sitemap-wide SEO validator
confirms zero broken internal links and intact canonical, hreflang, localized
chrome and cache-bust contracts. `node --check assets/main.js` and
`git diff --check` pass.

A fresh clone from
`https://github.com/PhilipGrishin/iron-moto-cascais.git` at documentation
commit `207e063890fc394de08393d8585b459ec0d73be1` completed the documented Full
Safe Rebuild, including the pricing-PDF step and every focused/project
validator, with empty `git status --short` afterward.

GitHub Pages workflow
[`34102070677`](https://github.com/PhilipGrishin/iron-moto-cascais/actions/runs/34102070677)
completed successfully. Cache-bypass checks returned HTTP 200 for all 52
commercial pages and found exactly one trust strip, the correct fallback rating
and repository-identical semantic `<main>` content on every page. Production
`sitemap.xml`, `llms.txt` and `assets/main.js` are byte-identical to the
repository, with SHA-256 values
`d8a1e6f48f55c699123fe4286f381f3326c6f6b604897457690e72299d5ad2e6`,
`590d13f8acb21c4505deb0c358bc66b80c9bb99aa0ec0ec79a8a13501979ca0b`
and `d80d016da2ad2859f2d5d6dbe433d6df2a7a31ce9f67516ddc44bf6a66602cae`
respectively. All 16 approved production head trims match their maintained
sources exactly.

Google Rich Results Test crawled both requested production pages successfully:

- PT `/pt/parts/`: result
  [`4IymClRwww4t0XIblH-KhA`](https://search.google.com/test/rich-results/result?id=4IymClRwww4t0XIblH-KhA),
  three valid supported items and no errors: Breadcrumb, Local business and
  Organization.
- EN `/upgrades-tuning/`: result
  [`_KC6wtVpYg5Rtd3WR7WZzg`](https://search.google.com/test/rich-results/result?id=_KC6wtVpYg5Rtd3WR7WZzg),
  three valid supported items and no errors: Breadcrumb, Local business and
  Organization.

The repository parser additionally validates the `Service` and `FAQPage`
graphs. Google currently does not expose those two schema types as rich-result
enhancements in this test UI; their absence from the supported-item summary is
not an error.

## Diff Scope, Deviations And Rollback

The implementation commit changes 263 files: all 240 tracked HTML files for the
required common JavaScript cache-bust, plus `assets/main.js`, `sitemap.xml`,
`llms.txt` and 20 build/data/source/validator files. Semantic comparison against
the baseline classifies the HTML precisely: 52 visible-body changes, 12 head-only changes
(Contact, Services and the English-speaking hub), and 176 cache-bust/generator
serialization-only changes. The homepage's visible body is unchanged. The
cumulative implementation-and-documentation diff before this report contains
268 unique files; this report is the only additional file.

No pricing data or PDFs, forms, FormSubmit settings, Workers, secrets, CI,
schema contracts, sitemap membership or common CSS changed. The common
JavaScript cache key moved to `20260907a` because the shared runtime gained only
the approved rating refresh hook; lead-beacon and WhatsApp-prefill logic is
unchanged.

There are no functional deviations from the brief. Copy-driven hub related
cards retain the exact labels and text present in each approved hub source;
brand related/other-brand cards consume the shared 17-target description
registry. Injecting registry prose into the owner-approved hub body would have
broken the required whole-page 1:1 contract, so the two renderer paths use their
respective explicit owner sources.

Rollback is the normal Git revert of the Wave 3 task commits. No external
Worker, account, secret or infrastructure state was changed.
