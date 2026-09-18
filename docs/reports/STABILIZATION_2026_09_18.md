# Maintenance Stabilization — 18 September 2026

## Scope and delivery

The owner authorized immediate website stabilization and data consistency,
explicitly deferring the dyno topic. Implementation commit: `67a014f6`.
Production verification is pending publication at the time of this entry.

The earlier [readiness audit](MAINTENANCE_READINESS_2026_09_18.md) describes
conditions before these fixes. Current inventories belong to
[Project State](../PROJECT_STATE.md), and unresolved business/account matters
to [Open Tasks](../OPEN_TASKS.md).

## Changes

- Reconciled local main with upstream review refresh `7d9e482d`. Preserved all
  original uncommitted intake documents privately before any edit. The public
  SEO handoff deliberately excludes private account tables and commercial
  estimates; the original report remains intact in the ignored intake archive.
- Updated the review renderer to refresh home aggregates/cards/schema and all
  commercial trust hooks/runtime translations together. Added offline snapshot
  rendering, invalid-aggregate rejection and required-output failures. Updated
  the scheduled workflow to include sitemap dates and validate before commit.
- Added a shared validation entry point used by Pages and Reviews. Pages
  checks out the exact triggering/passed commit and full history, validates,
  then packages the existing public allowlist. No server-side site build,
  framework, CMS or new external integration was introduced.
- Retired the destructive repository-bootstrap script as a non-mutating notice.
- Localized form placeholders through the maintained global dictionary and
  shared form normalization. Fixed mobile contact-card wrapping/spacing and
  rendered existing approved homepage counter targets in initial HTML. Changed
  the time-sensitive duration subtitle to the established founding year.
- Aligned Privacy/Cookies with the actual Cloudflare analytics, anonymous lead
  counters, browser storage and external services in all four languages.
  Existing business retention/Terms provisions were outside this factual
  runtime correction. This does not establish comprehensive legal compliance.
- Added all-language noindex aliases from `proekty/first` to The First through
  the existing project registry/renderer/validator, and included the new root
  directory in the public artifact. These are static meta-refresh/JavaScript
  redirects with a fallback link, not server-side 301 rules.
- Removed the unsupported robots directive while retaining the generated
  discovery index. Corrected Reviews Worker documentation: cache expiry does
  not guarantee API volume, redeploy is not a purge, and cache-miss errors do
  not implement stale-body recovery. Worker behavior and secrets are unchanged.

## Verification

**Confirmed**, 2026-09-18:

- Live Reviews Worker returned 4.9 from 29 reviews, matching the checked-in
  snapshot. The refresh preserved timestamp-only snapshot stability. Editorial
  cards remain the approved curated set; no reviewer wording was invented.
- Full Safe Rebuild completed in the working repository, including all four
  PDFs and every validator. The PDFs remained byte-identical to the baseline.
- A fresh full-history clone of `67a014f6` completed the entire documented
  rebuild with an empty `git status --short`. This closes the audit's
  reproducibility failure; intermediate generator messages are not evidence
  of final repository drift.
- The common validation gate passed: all sitemap URLs, brands, Harley family,
  commercial hubs/trust strips, Wave 4 routing, all registered project
  validators, JavaScript/Python syntax and all five existing Leads Worker tests.
- An isolated synthetic snapshot change to rating 4.8 / count 30 updated
  exactly 56 HTML consumers plus snapshot and sitemap. Broad and commercial
  validation passed; a second refresh was byte-idempotent. Five invalid
  response cases (out-of-range/NaN/bool rating and negative/bool total) aborted
  without modifying the valid output. Synthetic data never entered production.
- Only 64 sitemap dates changed: commercial trust content, four homes and
  eight Privacy/Cookies pages. All other 172 dates were preserved. Main-text
  comparison, excluding rating hooks, found changes only on homes and those
  legal pages. Dyno copy and unrelated public claims remain unchanged.
- Browser checks covered forms in all four languages, mobile contacts at
  390 px, desktop contacts and PT BMW at 1440 px, PT Privacy and the legacy
  RU project redirect. No horizontal overflow was measured. Contact-card text
  fits its container; field hints are translated; redirect reaches The First.
  Sampled browser warnings/errors were empty. No enquiry was sent.
- Shell syntax and the retired deploy notice were checked. Active documentation
  relative links resolved; whitespace checks passed. Changed text was scanned
  for Google/GitHub credential and private-key patterns with no matches.
- Google Cloud's website project listed one available key created after the
  historical exposure, restricted to Places API (New). Its value was never
  revealed. Historical revocation in every possible project is still unknown.

## Sources and limits

Runtime disclosure was checked against local client/Worker code and
[Cloudflare's Web Analytics description](https://www.cloudflare.com/web-analytics/).
Legacy mapping follows the existing Pages pattern and
[Google's redirect guidance](https://developers.google.com/search/docs/crawling-indexing/301-redirects).
These sources support implementation choices, not ranking or compliance claims.

The two unmatched historical URLs, old-domain control, historical credential
revocation, actual FormSubmit inbox delivery, private customer attribution and
business-profile scope require evidence outside the completed website changes.
Dyno work remains owner-deferred. This is representative browser verification,
not a full accessibility certification or new performance benchmark.

Temporary build/crawl/regression logs live under `/tmp/icm-stabilization-*` and
`/tmp/icm-review-regression*`; durable conclusions are recorded here. Private
intake originals remain in `.secrets/maintenance-intake-2026-09-18/`.
