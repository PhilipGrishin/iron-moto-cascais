# Repository Self-Audit

Audit date: 2026-07-31

This report records the repository and documentation audit requested in the
FINAL consolidation task. It deliberately does not duplicate live inventory
counts or cache-bust values. Those facts have one canonical home:
`docs/PROJECT_STATE.md`.

## Evidence Standard

- **Confirmed** means verified directly from the repository, Git, generated
  output, or a cache-bypassed production response.
- **Data-backed** means derived from a maintained source registry or a recorded
  measurement with its method stated nearby.
- **Assumption** means plausible but not verified.
- **Unknown** means the repository does not contain enough evidence.
- **Access required** means an external account or owner action is needed.

The audit used Git status and worktree inspection, repository-wide `rg`
searches, Python imports of maintained registries, direct source review of all
scripts under `scripts/build/`, sitemap/HTML parsing, validator source review,
and cache-bypassed HTTP requests where production behavior was relevant.

## Repository Identity And Copies

**Confirmed:** the active checkout is
`/Users/philipgrishin/Documents/ICM_Website`, on branch `main`, with remote
`https://github.com/dreamcarua/iron-moto-cascais.git`. At audit start the local
branch and `origin/main` had no divergence.

**Resolved, 2026-07-31:** temporary Git worktrees from the C6 reproducibility
work were found under `/private/tmp` during the audit. After explicit owner
authorization, their state was checked against canonical commit `fc25c4a4`,
then the obsolete worktrees were removed and the worktree registry was pruned.

**Confirmed:** a scan of Git roots under the owner's `Documents`, `Desktop`,
and `Downloads` directories found no second checkout using the website remote.
An empty non-Git directory named `ICM WebSite` exists under the owner's Claude
projects directory; it contains no repository files. Other Git roots found in
the scan belong to ERP, SEO monitoring, finance, marketplace, and unrelated
projects and were not modified.

**Limitation:** paths outside the scanned owner directories and temporary
worktrees were not exhaustively searched across the entire machine.

## Documentation Authority Audit

The durable documentation model is now explicit in the first section of
`AGENTS.md`:

| Information | Canonical home |
| --- | --- |
| Current inventory, counts, versions, and deployment state | `docs/PROJECT_STATE.md` |
| Repeatable content workflows and page-family ownership | `docs/CONTENT_TYPES.md` |
| Active operating rules | `AGENTS.md` |
| Open risks, external dependencies, and required access | `docs/OPEN_TASKS.md` |
| Historical chronology | `docs/CODEX_CHANGELOG.md` |
| Executable build and validation commands | `scripts/build/README.md` |

### Mismatches Found And Reconciled

| Previous mismatch | Evidence | Resolution |
| --- | --- | --- |
| Setup and build commands were duplicated across top-level documents | Command blocks in `README.md`, `AGENTS.md`, and the build README had drifted | Commands now live only in `scripts/build/README.md`; other documents link to named workflows |
| `README.md` declared an older Python floor | Build scripts use PEP 604 union syntax | The build README now states the source-backed minimum runtime |
| Documentation implied a path-portable full build | Pricing PDF generation uses macOS system font paths | The platform limitation is explicit in `PROJECT_STATE`, `OPEN_TASKS`, and the build README |
| Current site counts and cache values were repeated in multiple documents | Repository-wide search found conflicting copies | Current quantitative state is consolidated in `PROJECT_STATE`; active docs reference it |
| Content-family rules existed only in historical changelog entries | Changelog review found rules without a durable process home | Stable rules were promoted to `CONTENT_TYPES`; chronology remains in the changelog |
| Review refresh timing and service details were repeated | Workflow and Worker source are stronger evidence | Top-level documents now point to the workflow, Worker source, and project state instead of copying values |
| `HANDOFF.md` behaved like a current source of truth | Its page counts and process notes lagged behind generators | It is explicitly historical and points to the current read order |
| A task/report term implied an `EN_PAGES` registry | Source search found no such registry | `PROJECT_STATE` identifies `PAGES` as the canonical English sitemap registry; the historical report carries an explicit correction |
| A preliminary C7 note generalized a high-density article finding to project pages | Follow-up browser evidence confirms the current scope is Blog and News articles | The original report is preserved with a dated correction; the actionable finding is in `OPEN_TASKS` |
| `.env.example` cited a historical file for repository identity | Git remote is authoritative | The comment now points to `PROJECT_STATE` |

No current process relies on `HANDOFF.md` or `CHANGELOG.md` as its sole source.
They remain historical references.

### Post-Audit Corrections

- **Previous statement:** `nav_renderer.py`, `seo_metadata.py`, and
  `business_facts.py` were named as current shared modules.
  **Correction (2026-07-31):** those files do not exist. The current shared
  implementation modules are `build_output.py`, `hero_images.py`,
  `seo_meta.py`, and `site_chrome.py`; `build_llms.py` reads canonical business
  facts directly from `docs/BUSINESS_FACTS.md`. Evidence: tracked source files,
  imports, and the exhaustive inventory in `scripts/build/README.md`.
- **Previous statement:** Node.js was described as required for the navigation
  patch.
  **Correction (2026-07-31):** `nav_patch.py` is a Python script. Node.js is
  required for `extract_i18n.js` and JavaScript syntax checks. Evidence:
  script source and the Environment section of `scripts/build/README.md`.

## Site Structure Audit

**Confirmed:** the sitemap registry, localized-path registry, source data, and
served files agree. The exact current inventory by family and language is
recorded in `docs/PROJECT_STATE.md`, with the extraction method and source
registry named beside each fact.

**Confirmed:** sitemap entries resolve to served HTML, canonical and hreflang
contracts pass the active validator, and no separate `EN_PAGES` inventory
exists. `PAGES` in `scripts/build/build_sitemap.py` is the canonical English
discovery inventory; `LOCALIZED_PATHS` owns internal-link localization.

**Confirmed:** non-indexable utility HTML exists outside the sitemap. It is
listed in `PROJECT_STATE` so filesystem HTML totals are not mistaken for public
URL inventory.

## Build Script Ownership Audit

Every Python and JavaScript file directly under `scripts/build/` was reviewed.
The exhaustive filename-by-filename ownership map is maintained in
`scripts/build/README.md`, grouped as page generators, post-processors and
media tools, data/shared modules, and validators. Each executable entry states
what it builds, its maintained input, and the validator that protects its
output where one exists.

The audit found these important ownership boundaries:

- `build_sitemap.py` owns discovery inventory and sitemap output.
- `localize_internal_links.py`, `build_i18n.py`, `apply_seo_meta.py`, and
  `nav_patch.py` are shared post-processors and must remain in the documented
  full-build order.
- Page-family generators own their generated HTML; source data must be edited
  instead of generated files.
- `build_output.py`, `hero_images.py`, `seo_meta.py`, and `site_chrome.py` are
  shared modules rather than standalone build steps.
- Media-conversion scripts are intentionally excluded from the routine full
  build because they require task-specific source assets.
- Pricing PDF generation has content checks in `validate_seo.py`, but no
  dedicated PDF layout validator.
- Shared post-processors do not have one validator per script; their contracts
  are covered across `validate_seo.py` and the family validators.
- Data modules without a dedicated validator are identified explicitly in the
  build README rather than being presented as fully protected.

No script or data module was found without a documented owner after the README
rewrite.

## Validator Coverage Audit

### `validate_seo.py`

Checks sitemap-to-file resolution, essential metadata, canonical and hreflang
contracts, JSON-LD parsing and Breadcrumb presence, localized URL locality,
asset existence and cache-bust consistency, hero preload contracts, English
LLM discovery coverage, and shared navigation/footer consistency.

It does **not** prove Rich Results Test warning-free status, visible FAQ/schema
parity for every family, external endpoint availability, visual layout,
real-user LCP improvement, sitemap lastmod truthfulness, PDF visual quality,
or the absence of duplicate high-density `<picture>` candidate downloads.

### `validate_brand_pages.py`

Checks the brand registry contract, required brand content groups, localized
variants, hero assets, service/FAQ/Breadcrumb schema types, reciprocal links,
homepage brand integration, sitemap inclusion, and forbidden terminology.

It does **not** replace browser checks, external Rich Results Test execution,
performance measurement, or editorial review of every translation.

### `validate_harley_hub.py`

Checks source copy contracts, required page and integration structure, hero
assets, schema families, FAQ parity, forbidden terms, local links, navigation,
feed/portfolio integration, homepage integration, and sitemap inclusion.

It does **not** prove visual parity at every viewport, production cache state,
or external Rich Results Test behavior.

### `validate_project_pages.py`

Checks registered data-driven project pages for multilingual copy, media,
schema, listings, menu integration, sitemap/lastmod behavior, and prohibited
Harley Hub leakage.

It does **not** fully validate legacy hand-authored project copy, browser
layout, measured LCP, or external Rich Results Test output.

## External Dependencies And Failure Modes

The current dependency and access matrix lives in `docs/OPEN_TASKS.md` so
operational risks remain visible. Confirmed dependencies include GitHub Pages,
Cloudflare edge delivery, the reviews Worker and Google Places upstream,
FormSubmit, analytics and advertising endpoints, Google Fonts, WhatsApp, and
social profile links.

Key failure behavior:

- A failed Pages deployment leaves production on the previously deployed
  revision.
- Cloudflare can serve stale discovery files after deployment unless checks
  bypass edge cache.
- Worker or upstream review failure can make live review refresh unavailable;
  the repository snapshot remains the static fallback.
- FormSubmit failure prevents contact-form delivery and requires external
  service access to diagnose.
- Analytics, advertising, fonts, WhatsApp, and social endpoints can fail
  independently without preventing the static HTML from loading.

Account-level configuration cannot be proven from repository contents alone
and is marked **Access required** in `OPEN_TASKS`.

## Environment Audit

**Confirmed:** the documented build requires a Python runtime compatible with
the syntax used by the scripts, Node.js for `extract_i18n.js` and JavaScript
syntax checks, and the Python packages in the root `requirements.txt`.

**Confirmed:** the full build is currently macOS-specific because
`build_pricing_pdfs.py` loads Arial from hardcoded `/System/Library/Fonts`
paths. A non-macOS clean clone cannot execute that step literally without a
font strategy change. The limitation is documented as an active risk rather
than hidden behind a portability claim.

**Confirmed:** generated Python bytecode and local scratch output are not
project artifacts and must not be introduced by normal verification.

## Previously Chat-Only Knowledge

The following important facts were not durably recoverable from the repository
before this task and are now recorded:

| Knowledge | Durable location |
| --- | --- |
| High-density Blog article `<picture>` heroes previously transferred both preload and selected candidates; the old News inclusion was incorrect | `docs/reports/C7_FIX2_REPORT.md` |
| C7/C7-FIX local LCP measurements, exact method, and the conclusion that structural validation did not guarantee performance | `docs/OPEN_TASKS.md` |
| Cloudflare discovery-file verification must bypass edge cache | `docs/OPEN_TASKS.md` and `scripts/build/README.md` |
| Default Python urllib requests can receive a production sitemap denial | `docs/OPEN_TASKS.md` |
| Pricing PDF generation makes the literal full build macOS-only | `docs/PROJECT_STATE.md`, `docs/OPEN_TASKS.md`, and `scripts/build/README.md` |
| Site strategy and copy decisions live in a separate owner workspace and arrive here as approved tasks | `docs/OPEN_TASKS.md` |

The separate strategy workspace is intentionally not copied into this
repository. This repository owns approved site source and delivery behavior,
not the owner's broader strategy documents.

## Scope Confirmation

This consolidation changes documentation and one environment example comment
only. It does not change page text, navigation, schema, images, page inventory,
`llms.txt`, `robots.txt`, HTML, or `sitemap.xml`. Site defects observed during
the audit were documented in `OPEN_TASKS` and were not repaired outside the
requested scope.
