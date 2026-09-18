# Open Tasks, Risks And Watchlist

Last updated: 2026-09-18

This file owns unresolved work, external dependencies and access requirements.
Statuses use the labels defined in the `AGENTS.md` documentation protocol.

## Active Implementation

None.

## Maintenance Readiness Follow-Up

Status: **implemented and locally verified**, 2026-09-18; publication and
clean-clone verification are being recorded in the stabilization report.
The preceding [readiness audit](reports/MAINTENANCE_READINESS_2026_09_18.md)
is historical evidence from before these fixes.

- **Resolved:** local main was fast-forwarded to the review refresh without
  losing the existing audit. Complete private intake documents are preserved
  under `.secrets/maintenance-intake-2026-09-18/`; the public SEO audit is an
  explicit publication-safe handoff summary. Analysis-only changelog notes
  use a distinct heading and do not invent implementation commit hashes.
- **Resolved:** review refresh updates every snapshot consumer, including
  commercial trust ratings and inline translations, before sitemap generation
  and validation. Both publication workflows run the common release gate.
- **Resolved:** `deploy.sh` is a non-mutating retirement notice. Mobile contact
  cards wrap correctly, form placeholders are localized, and homepage counters
  have their existing approved values in static HTML. Worker cache/failure
  documentation now matches the implementation.
- **Confirmed current key restrictions; historical revocation unknown:** on
  2026-09-18 the signed-in Google Cloud project for this website listed one
  available API key, created on 2026-06-02, restricted to Places API (New).
  This is later than the exposed literal committed on 2026-05-05. No older
  active key appeared in that project's list. The key value was not revealed,
  compared, tested or copied; deletion of the historical key in every possible
  project remains unproven. Preserve that distinction. No credential change
  was made, and the Reviews Worker remains operational.
- **Access confirmed:** GitHub/Actions, the configured Cloudflare Worker
  account, authenticated lead stats, GSC, GBP manager and Google Cloud's
  website project. Sessions can expire. FormSubmit inbox delivery, media
  upload administration and old-domain registrar control were not retested.

## SEO And Local Search Audit Follow-Up

The original private analysis remains preserved; the
[public handoff](reports/SEO_GEO_AUDIT_2026_09_08.md) contains no internal
commercial estimates or account-performance tables.

- **DEFERRED by owner, 2026-09-18:** dyno availability and associated website /
  GBP wording. No availability date is inferred and no dyno copy was changed.
- **Unknown:** acquisition sources and completed-job attribution. Existing
  anonymous counters measure contact intent, not unique clients or revenue.
  Accurate outcomes require a private workshop register and real job data.
- **Business scope confirmation required:** GBP's mechanic-category list
  includes automobile-oriented services. Verify actual scope before removing
  entries or changing categories; do not infer workshop capabilities from
  generated service suggestions. The YouTube handle discrepancy also remains
  an identity-verification follow-up.
- **Unknown:** the earlier Portugal-filtered GSC page table did not reconcile
  with the chart/country/device totals. Private figures and exports remain in
  the private intake archive. Use an independent export or authorized API
  comparison before drawing page-level traffic conclusions.
- **Partly resolved:** the legacy `proekty/first` path now has a matching
  localized redirect to The First, generated through the existing project
  registry. The old domain's forwarding rules and renewal remain outside
  verified account control. `proekty/ducati-9991` and
  `photogallery/events/amd2014` have no confirmed equivalent in the current
  content registry; retain honest 404 responses until historical material or
  an exact mapping is recovered. Do not send unrelated historical URLs to a
  generic service page merely to suppress a 404 report.
- **Resolved:** static homepage counters and retired tracking disclosures.
  Privacy/Cookies now describe the observed runtime in all four languages;
  this factual correction is not a comprehensive legal review. Existing
  business retention and Terms clauses were not independently audited.
- **Data-backed performance watch:** the previous mobile lab run indicated
  room to improve the font/CSS critical path. No new Core Web Vitals field
  dataset or controlled before/after performance benchmark is available.
- **Indexing watch:** the priority Portuguese service URLs were indexed in the
  prior account inspection. Individual recrawl timing is external to the
  deployment and does not by itself indicate a broken sitemap.

The prior strategy-workspace boundary remains in force for other projects.
This audit was explicitly requested in `ICM_Website`; its presence here does
not authorize inspection or copying of another strategy workspace.

## Performance Follow-Up

The duplicate Blog `<picture>` hero candidate issue is resolved by C7-FIX2.
The earlier affected-family statement incorrectly included 12 News articles;
repository source and rendered output confirm that those articles already use
the C7-FIX CSS-background contract. The correction and evidence are retained
in `docs/reports/C7_FIX2_REPORT.md` rather than as active work here.

### C7 LCP measurement record

- Status: **data-backed**, historical evidence retained for future decisions.
- Method: local Chromium through Playwright, viewport 390 x 844 CSS pixels,
  device pixel ratio 3, network 1.6 Mbps / 170 ms latency, CPU throttling 4x,
  median of 3 runs. Measured 2026-07-31.

| Page | Before C7 | After C7 | After C7-FIX |
|---|---:|---:|---:|
| `/bmw-service/` | 2292 ms | 2600 ms | 1472 ms |
| `/faq/` | 1432 ms | 1508 ms | 900 ms |
| `/motorcycle-service/` | 1116 ms | 720 ms | 744 ms |
| `/projects/beckman/` | 1480 ms | not separately retained | 892 ms |
| `/blog/front-fork-service-motorcycle-cascais/` | 1328 ms | 1376 ms | 1388 ms |

For `/projects/beckman/`, the rendered hero transfer changed from 68,544 bytes
to 16,708 bytes. Conclusion: C7 passed all structural validators but still made
some brand pages slower. Resource hints are not proof of a performance benefit;
measure representative page families under a stated profile.

## Build And Environment Risks

### Pricing PDF generator is macOS-only

- Status: **confirmed**, open.
- Evidence: `scripts/build/build_pricing_pdfs.py` hardcodes Arial files under
  `/System/Library/Fonts/Supplemental/`; source inspection 2026-07-31.
- Current artifact status: **confirmed current** for S-REBUILD-W2 on
  2026-09-07. All four PDFs were regenerated from the extended
  `pricing_data.py`, remained byte-idempotent on a second run, contained the
  new brand-specific cards and Triumph / Royal Enfield valve row, and passed
  text extraction across all seven pages plus visual inspection of the new
  section in all four files. This does not resolve portability.
- Impact: the documented full build currently succeeds only on macOS with those
  fonts installed. HTML-only generators are not blocked by this specific issue.
- Next action: in a separately scoped build-portability task, vendor approved
  fonts or implement a deterministic cross-platform font lookup, then compare
  generated PDF content and layout before changing the canonical build claim.

## Discovery And CDN Risks

### Cloudflare may serve stale discovery files after deployment

- Status: **confirmed**, operational watch item.
- Evidence: production is fronted by Cloudflare and response headers expose
  edge caching. Cache-bypass requests on 2026-07-31 returned the current
  `robots.txt` and `llms.txt`; `robots.txt` included `LLMs-Txt`.
- Impact: ordinary post-deploy requests can report an old discovery file and
  produce a false verification result.
- Rule: verify `robots.txt`, `llms.txt` and other cached static output with a
  unique query string plus no-cache request headers. Purging Cloudflare cache
  is **access required** and belongs to the owner when bypass still shows old
  content.

### Default Python urllib receives 403 for live sitemap

- Status: **confirmed**, open operational compatibility issue.
- Method: `urllib.request.urlopen` with its default user agent against the live
  `sitemap.xml`, 2026-07-31, returned HTTP 403. A cache-bypass `curl` request
  returned HTTP 200 and bytes identical to the repository file.
- Impact: simplistic external monitoring based on default urllib may falsely
  report that the sitemap is unavailable.
- Next action: use an explicit normal user agent for monitoring or review the
  Cloudflare rule with account access. Do not weaken edge protection without
  owner approval.

## External Services And Access

| Dependency | Status | Failure impact | Access boundary |
|---|---|---|---|
| GitHub Pages / Actions | **confirmed** | deploys stop; checked-in production output remains served | repository/account access required for workflow administration |
| Cloudflare DNS/CDN | **confirmed** | DNS, TLS, cache or routing can obscure a valid GitHub Pages deploy | account access required |
| Reviews Worker and Google Places | **confirmed** | live review widget/snapshot refresh can fail; existing static curated fallback remains | Worker and Google Cloud access required; secret must stay server-side |
| Leads Worker / KV | **confirmed** | lead-intent beacons and private reports fail if the Worker or KV binding is unavailable | stats secret stays server-side and in gitignored `.secrets/` |
| FormSubmit | **confirmed** | contact form delivery can fail; WhatsApp remains a separate lead path | inbox activation/account access required |
| Cloudflare Web Analytics | **owner-managed** | pageview/referrer/CWV reporting is independent of repository lead counters | owner enables edge injection; no HTML snippet is maintained here |
| Google Fonts | **confirmed** | remote font failure causes fallback typography and possible layout variation | external network dependency |
| Google Search Console / Rich Results UI | **GSC read access confirmed 2026-09-18; session-dependent** | local validators cannot replace live account evidence | owner/browser account access required; the audit records the exact reports inspected |

Do not claim an account-only verification passed unless it was actually run.
Local JSON-LD parsing and repository validators are separate evidence.

## Product And Publishing Watchlist

### The First historical result and current whereabouts

- Status: **unknown**, non-blocking publication follow-up.
- Confirmed boundary: the approved source does not establish the motorcycle's
  current whereabouts or a verified Motobike 2012 award/result. The published
  project page therefore makes no current-location or award claim.
- Next action: add either fact only when the owner supplies an authoritative
  source. Do not infer a result from the motorcycle's exhibition history.

### Fetish historical result and current whereabouts

- Status: **unknown**, non-blocking publication follow-up.
- Confirmed boundary: the approved source identifies Fetish as the first
  Ukrainian custom entered in the 2013 AMD World Championship, but does not
  provide a verified competition result or the motorcycle's current
  whereabouts. The published project page therefore states participation only
  and makes no current-location claim.
- Next action: add either fact only when the owner supplies an authoritative
  source. Do not infer the result or location from unrelated exhibition copy.

### CMS

- Status: **unknown need**, not implemented.
- Context: publishing is developer-driven through repository sources and
  generators.
- Decision gate: introduce a CMS only if non-developers need frequent direct
  publishing and the operational cost is accepted.

### Advanced lead form

- Status: **assumption**, future enhancement only.
- Context: the current lead path is WhatsApp plus FormSubmit; A-MEASURE adds
  anonymous intent counters without changing form fields.
- Candidate scope: structured motorcycle/request fields, anti-spam, media
  intake and a measurable success state. Requirements need owner approval.

## External Strategy Workspace Boundary

- Status: **confirmed owner workflow**.
- Business strategy, SEO planning and approved multilingual copy are maintained
  in a separate owner workspace and arrive here as explicit tasks or committed
  source files.
- This repository owns the website implementation and durable implementation
  facts. Do not copy an external strategy workspace wholesale into the repo;
  commit only approved inputs needed to reproduce the site.
