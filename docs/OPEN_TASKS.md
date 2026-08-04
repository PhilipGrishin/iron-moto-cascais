# Open Tasks, Risks And Watchlist

Last updated: 2026-08-04

This file owns unresolved work, external dependencies and access requirements.
Statuses use the labels defined in the `AGENTS.md` documentation protocol.

## Active Implementation

No active implementation task is recorded after P-THE-FIRST delivery.

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
| FormSubmit | **confirmed** | contact form delivery can fail; WhatsApp remains a separate lead path | inbox activation/account access required |
| Google Analytics and Meta Pixel | **confirmed** | attribution/analytics fail without blocking core page rendering | analytics/business account access required |
| Google Fonts | **confirmed** | remote font failure causes fallback typography and possible layout variation | external network dependency |
| Google Search Console / Rich Results UI | **access required** | live indexing and Google UI status cannot be certified locally | owner/browser account access required |

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
- Context: the current lead path is WhatsApp plus FormSubmit.
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
