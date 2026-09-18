# S-PRICE-VALVES-FROM

Date: 2026-09-18. Status: implementation and verification in progress.

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

Pending: full rebuild, exact-copy/scope comparison, PDF rendering, checksum
failure test, clean-clone reproducibility, publication and production checks.
