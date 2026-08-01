# CWAY-VAT Delivery Report

Date: 2026-08-01 (Europe/Lisbon)

Implementation commit: `560e3891`

Visual-size follow-up commit: `8447160b`

Latest production workflow: `30716569527` — succeeded

## Outcome

Every visible C-Way configuration price now repeats the existing localized
VAT-exclusion wording:

| Language | Suffix | Result |
|---|---|---|
| EN | `excl. VAT` | 6 prices / 6 exact suffixes |
| PT | `sem IVA` | 6 prices / 6 exact suffixes |
| RU | `без НДС` | 6 prices / 6 exact suffixes |
| UK | `без ПДВ` | 6 prices / 6 exact suffixes |

The values live once per language as `priceVatSuffix` in
`authorized_dealer_data.py`. The renderer verifies that each value is already
present in the same language's maintained `priceNote` and `installText`, then
adds it to every generated `.cway-price`. The upper price note remains
unchanged.

The suffix uses the page-scoped C-Way style: 17 px, normal weight, the shared
secondary text color, and `white-space: nowrap`. A `<wbr>` before the suffix
allows the complete comma-plus-label unit to move below the amount when a
narrower layout requires it. No common CSS or JavaScript changed, so no
cache-bust moved.

The original `560e3891` release used 13 px. Owner follow-up `8447160b`
increased it to 17 px, a 30.8% increase, without changing the markup, wording,
schema or sitemap dates.

## Changed Files

- `scripts/build/authorized_dealer_data.py`
- `scripts/build/build_authorized_dealer.py`
- `authorized-dealer/c-way/index.html`
- `pt/authorized-dealer/c-way/index.html`
- `ru/authorized-dealer/c-way/index.html`
- `uk/authorized-dealer/c-way/index.html`
- `sitemap.xml` — only the four approved C-Way `lastmod` values
- `docs/reports/CWAY_VAT_1440.jpg`
- `docs/reports/CWAY_VAT_390.jpg`
- this report and canonical project documentation

No other HTML, common CSS, common JavaScript, assets, cache-bust values or
`llms.txt` bytes changed.

## Visual Verification

Local Chromium checks used the generated English page at 1440 x 1000 and the
generated Russian page at 390 x 844.

Measured computed values:

- desktop price: 28.8 px; suffix: 17 px; stock label: 13 px;
- mobile price: 24 px; suffix: 17 px; stock label: 13 px;
- suffix weight: `400` at both widths;
- suffix color: `rgb(184, 184, 196)`, the shared `--text-dim` value;
- mobile document horizontal overflow: `0` px;
- first mobile line: `1500,00 €, без НДС`.

Screenshots:

- [Desktop 1440 x 1000](CWAY_VAT_1440.jpg)
- [Mobile 390 x 844](CWAY_VAT_390.jpg)

## Schema And Sitemap Invariants

The complete ordered JSON-LD script list on every C-Way page was compared
against `HEAD` before the change and remained byte-identical. This protects the
`FAQPage`, all six `Product`/`Offer` entities, their numeric prices, and
`valueAddedTaxIncluded`.

| Language | JSON-LD SHA-256 before and after |
|---|---|
| EN | `c65b2f48b59410f3297d3e80b57b04905e6b2cda6ca2814eca30e58bde61ed2d` |
| PT | `7f344b4c616268141132b194ece1eeccaff3e35d16b71b4e3bcf072959e9f972` |
| RU | `1c133a6e3f63e1ef90def0f7c1d4f8d784c1146d5f18a85d69a428496f30fcf8` |
| UK | `b85753f2daf35b41f12b062a3c873daa6977ac3d5093b94a6480150eac6f72d6` |

The sitemap URL set is unchanged. Exactly these four values moved from
`2026-07-16T07:25:00+01:00` to `2026-08-01T20:34:31+01:00`:

- `/authorized-dealer/c-way/`
- `/pt/authorized-dealer/c-way/`
- `/ru/authorized-dealer/c-way/`
- `/uk/authorized-dealer/c-way/`

Current sitemap SHA-256:
`34ae75b4e6484387ee8eb2011523796dd7a83aa125bf39597efc6ffb666c2cd3`.

## Acceptance Criteria

1. **Passed.** All four variants have exactly one localized suffix inside
   each of six price elements.
2. **Passed.** Desktop and mobile visual checks confirm the owner-approved
   17 px follow-up size, continued price dominance and zero mobile horizontal
   overflow; refreshed screenshots are linked above.
3. **Passed.** The implementation is generator/data-driven and page-scoped.
   Only the four C-Way HTML outputs changed; common CSS and cache-bust values
   did not.
4. **Passed.** Every JSON-LD block is byte-identical to the pre-change version;
   FAQ and Offer data are unchanged.
5. **Passed.** Sitemap membership is unchanged and only the four C-Way
   `lastmod` values moved.
6. **Passed.** The four validator groups passed. The complete documented Full
   Safe Rebuild at follow-up commit `8447160b` left empty
   `git status --short` in a clean clone.

## Validator Output

```text
SEO validation passed: 216 sitemap URL(s)
Brand page validation passed: 7 brand page set(s).
Harley Hub validation passed: 12 pages and all required integrations
OK: all 12 registered project slugs passed multilingual copy, media, schema,
cache-bust, redirect and integration checks
```

JavaScript syntax checks, Python compilation and `git diff --check` also
passed.

## Production Verification

GitHub Pages workflow `30715488709` deployed `560e3891` successfully, and
workflow `30716569527` deployed the 17 px follow-up `8447160b` successfully.
Cache-bypass, no-cache requests returned HTTP 200 for all four production URLs,
found 6/6 exact localized suffixes on each page, and confirmed production
JSON-LD matches the committed pages. The production sitemap matched the
repository byte-for-byte at the SHA-256 above.

A production browser check at 390 x 844 on the Russian page confirmed six
prices, six suffixes, the first rendered value `1500,00 €, без НДС`, the
secondary text color, and zero horizontal overflow.
