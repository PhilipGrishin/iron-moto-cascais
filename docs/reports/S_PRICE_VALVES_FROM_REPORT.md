# S-PRICE-VALVES-FROM

Date: 2026-09-18. Status: implemented, deployed and production-verified.

Implementation commit: `108684b3e8b43bc8c9a77b970f1332b298adbb58`.

## Scope and approved input

The owner approved starting-price notation for valve-clearance work, with
unchanged amounts: `+` in tables and localized `from` wording in prose.
Scope: Pricing, Motorcycle Service and six brand families, in EN/PT/RU/UK,
plus the four existing downloadable PDFs. GBP is outside this implementation.

The exact delivery is preserved at
`scripts/build/content/2026-09-18_valve-prices-from_4lang.md`.
Confirmed SHA-256:
`2b7cf8ef0a529e930b821d65af54b54ac8bba82fb6d27ab61d6e28da3d130212`.
Parts A-C drive the implementation; Part D records exclusions; Part E remains
an external handoff only. No prices, forms, Workers, secrets, homepages or
shared runtime assets are changed by this task.

## Baseline correction

The supplied task names `7d9e482d`, but implementation starts from clean
`main` at `77a89916` after the owner's completed stabilization. That work
already synchronized every trust strip to the review snapshot. Therefore the
expected sitemap change is 32 content URLs, rather than the old task's 56.
The 24 former strip-only URLs should retain their content and dates. No date
will be forced forward to satisfy an obsolete count.

## Implementation

- Updated only the six valve rows and four notes in `pricing_data.py`.
- Applied the four approved whole-line hub replacements and 32 brand-copy
  replacements, plus the non-rendered Rules header.
- Updated the existing checksum pins. Existing HTML/PDF/table-splitting
  renderers require no logic changes.
- Aligned four canonical key-price labels in `docs/BUSINESS_FACTS.md`, which
  also supplies the generated `llms.txt`; the amounts remain unchanged.
- Preserved existing PDF filenames and shared asset cache versions.

New source SHA-256 values:

| Source | SHA-256 |
|---|---|
| `service_hub_copy_4lang.md` | `08627850a90a2307a8e78ccae7ba85141911bb6919ebc0dc324e84af1d6e522a` |
| `brand_pages_w2_copy_4lang.md` | `f08554168fddc38d43c0aad73917a3342d4f317b402381571d808cf57b8ed2d2` |

## Acceptance

Confirmed locally on 2026-09-18:

- Full Safe Rebuild passed, including every documented validator. Repeating it
  in a fresh full-history clone of the implementation commit left empty
  `git status --short`, including all four PDF binaries.
- `verify_site.sh` passed: all site validator families, all 14 project checks,
  JavaScript/Python syntax and the five existing Leads Worker tests.
- Approved CURRENT/NEW whole-line comparisons passed: four service lines,
  32 brand lines and the Rules header only. Both new source pins match their
  files. In the isolated clone, appending one byte separately to each source
  stopped its real builder with a SHA-256 error. Each original was restored;
  final clone status was empty.
- Exact raw-HTML comparison against the baseline, masking only the valve table
  and its note, confirmed that every other byte of all four Pricing pages is
  unchanged. Each Service page differs by its one approved paragraph only.
- All six brand tables in all four languages contain the approved `+ €`
  amounts, including the split Honda/Suzuki rows. The 24 price answers equal
  the approved source. Every visible FAQ matches its FAQPage question/answer
  sequence. The existing monetary whitelist passed.
- BMW metadata lengths (EN/PT/RU/UK): 155/153/151/153. Ducati: 155/146/150/150.
  Each description, Open Graph description and Twitter description equals
  the approved string.
- All four PDFs retain seven pages and their original filenames. Extracted
  text from all 28 pages is unchanged outside the approved table cells and
  notes on page 5. Rendered page 5 was visually inspected in each language:
  no clipping, overlapping text or missing glyphs; the table, full note and
  following tyre table fit. Renderer code and fonts are unchanged.
- Local browser checks: Portuguese Pricing at 390 and 1440 CSS px, and the
  expanded Portuguese BMW price FAQ at 390 px. No document overflow; prices,
  table layout and FAQ interaction work.
- Checked 32,341 internal anchor destinations across all 253 tracked HTML
  files against local served files: zero missing targets. This is a local
  destination check, not an audit of all external sites.

PDF filenames (unchanged despite the historical `2025` filename suffix):

- `pricing/files/ICM_price-list_2025_EN.pdf`
- `pricing/files/ICM_tabela-precos_2025_PT.pdf`
- `pricing/files/ICM_прайс-лист_2025_RU.pdf`
- `pricing/files/ICM_прайс-лист_2025_UA.pdf`

## Sitemap and unchanged scope

Confirmed by parsing baseline and new sitemap XML: 236 URLs; exactly 32
changed dates and 204 unchanged dates. HTML file membership matches the same
32 paths. Dates come from the existing content-history process; no generator
or timestamp override was introduced.

The following 32 URLs moved, grouped by task scope. Every path uses
`https://ironcustommotors.com`.

| Group | EN | PT | RU | UK |
|---|---|---|---|---|

| Pricing | `/pricing/` | `/pt/pricing/` | `/ru/pricing/` | `/uk/pricing/` |
| Service hub | `/motorcycle-service/` | `/pt/motorcycle-service/` | `/ru/motorcycle-service/` | `/uk/motorcycle-service/` |
| BMW | `/bmw-service/` | `/pt/bmw-service/` | `/ru/bmw-service/` | `/uk/bmw-service/` |
| Ducati | `/ducati-service/` | `/pt/ducati-service/` | `/ru/ducati-service/` | `/uk/ducati-service/` |
| Honda | `/honda-service/` | `/pt/honda-service/` | `/ru/honda-service/` | `/uk/honda-service/` |
| Suzuki | `/suzuki-service/` | `/pt/suzuki-service/` | `/ru/suzuki-service/` | `/uk/suzuki-service/` |
| Triumph | `/triumph-service/` | `/pt/triumph-service/` | `/ru/triumph-service/` | `/uk/triumph-service/` |
| Royal Enfield | `/royal-enfield-service/` | `/pt/royal-enfield-service/` | `/ru/royal-enfield-service/` | `/uk/royal-enfield-service/` |

The old task's 24 extra strip-only URLs did **not** move; their HTML remains
byte-identical to the stabilized baseline and their sitemap dates are retained:

| Family | EN | PT | RU | UK |
|---|---|---|---|---|
| custom | `/custom/` | `/pt/custom/` | `/ru/custom/` | `/uk/custom/` |
| parts | `/parts/` | `/pt/parts/` | `/ru/parts/` | `/uk/parts/` |
| upgrades-tuning | `/upgrades-tuning/` | `/pt/upgrades-tuning/` | `/ru/upgrades-tuning/` | `/uk/upgrades-tuning/` |
| harley-service | `/harley-service/` | `/pt/harley-service/` | `/ru/harley-service/` | `/uk/harley-service/` |
| motorcycle-tyre-service | `/motorcycle-tyre-service/` | `/pt/montagem-de-pneus-mota/` | `/ru/shinomontazh-mototsiklov/` | `/uk/shynomontazh-mototsykliv/` |
| pre-purchase-inspection | `/pre-purchase-inspection/` | `/pt/pre-purchase-inspection/` | `/ru/pre-purchase-inspection/` | `/uk/pre-purchase-inspection/` |

Other exclusions are unchanged: homepages, shared assets/cache values, forms,
Workers, review sources, tyre prices, scheduled-service groups, full-service
brand cards and unused legacy Honda/Suzuki FAQ strings. GBP and the deferred
dyno decision were not acted on.

## Production verification

Confirmed on 2026-09-18:

- [Pages run 35333451302](https://github.com/PhilipGrishin/iron-moto-cascais/actions/runs/35333451302)
  succeeded and published exact commit `108684b3e8b43bc8c9a77b970f1332b298adbb58`.
- At 10:14:24 UTC, cache-bypassed HTTP checks passed on all 236 sitemap URLs:
  HTTP 200, one H1, matching title and three description tags,
  canonical/hreflang, all JSON-LD, main text and shared cache references.
  Only Cloudflare's contact-email obfuscation was normalized.
- Ten public files returned HTTP 200 and matched repository bytes: the four
  PDFs, shared CSS/JS, review snapshot, sitemap, robots and `llms.txt`.
- Live Portuguese Pricing at 1440 px and the expanded Portuguese BMW price
  FAQ at 390 px show the new copy with no document overflow. The live browser
  warning/error log was empty.
- [PT BMW Rich Results](https://search.google.com/test/rich-results/result?id=nhrVk4OotX0d8cTMcYRqRw)
  and [PT Pricing Rich Results](https://search.google.com/test/rich-results/result?id=v6EgCdjUup8CbCWTtT4hoA)
  each reported one valid Breadcrumb item and no errors, crawled at 11:14:09
  and 11:14:12 Lisbon time. The BMW tested-HTML panel contains the new approved
  description, including `válvulas Boxer desde 150 / 300 €`.
- These are successful supported-item tests, **not** Google FAQPage validation:
  Google retired FAQ rich results on 2026-05-07 and removed the documentation
  in June. The requested FAQPage-specific RRT result is therefore unavailable.
  Exact FAQPage/visible parity was checked separately and the deployed graphs
  match locally validated output. Evidence:
  [official Google documentation updates](https://developers.google.com/search/updates).


## Deviations and limits

- The task's 56-URL expectation was based on a superseded baseline. The 32-URL
  outcome is correct for the owner's stabilized current site, as detailed above.
- Four key-price labels in canonical Business Facts and generated `llms.txt`
  were also aligned so machine-readable discovery does not retain fixed-price
  wording. This is the same approved pricing decision, with no amount changes.
- No cache-bust bump: `main.css` and `main.js` are unchanged, so their current
  version is preserved as required by repository policy.
- PDF build portability remains a pre-existing macOS-font dependency.
- Rollback: revert this task's implementation and documentation commits only.
  No external business-profile, Worker or account configuration was modified.
