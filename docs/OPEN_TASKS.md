# Open Tasks, Risks And Watchlist

Last updated: 2026-07-31

This file owns unresolved work, external dependencies and access requirements.
Statuses use the labels defined in the `AGENTS.md` documentation protocol.

## Active Implementation

No active implementation task is recorded after the FINAL documentation audit.

## Performance Follow-Up

### Responsive `<picture>` hero downloads two candidates

- Status: **data-backed**, open; explicitly outside C7-FIX.
- Affected output: 28 blog article pages and 12 news article pages.
- Method: local Chromium through Playwright, viewport 390 x 844 CSS pixels,
  device pixel ratio 3, network 1.6 Mbps / 170 ms latency, CPU throttling 4x.
  Evidence collected 2026-07-31.
- Observation: the preload requests the 768px AVIF while `<picture>` `srcset`
  selects the 1280px AVIF for the same hero. Both are transferred. In the
  measured case the transfers were 26,494 bytes plus 50,467 bytes, while only
  the latter candidate was rendered.
- Impact: extra hero bytes and connection competition on constrained networks.
  Laboratory LCP is noisy, so the transfer duplication is the stronger finding.
- Next action: in a separately approved performance task, test preload
  `imagesrcset`/`imagesizes` or align candidate choice with device pixels. Keep
  visual output unchanged and measure before and after.

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

### Old temporary worktrees outside the primary checkout

- Status: **confirmed**, cleanup decision required.
- Evidence: `git worktree list`, 2026-07-31.
- Paths: `/private/tmp/icm-c6-audit.SYgMIB`,
  `/private/tmp/icm-c6-before.ISW2xQ`, and
  `/private/tmp/icm-c6-fulltest.vfneog`.
- Impact: they are detached historical C6 verification copies, not production
  sources, but can confuse future repository discovery while they exist.
- Next action: owner may authorize `git worktree remove`/`prune`; do not delete
  them implicitly during documentation work.

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

### Pre-purchase description in `llms.txt`

- Status: **confirmed**, deferred by the C6 scope boundary.
- Context: the published inspection page and metadata state the fixed EUR 150
  price, while the generated AI discovery description retains earlier
  starting-price wording through `LLMS_DESCRIPTION_EN`.
- Next action: update the maintained discovery source in an approved GEO task,
  regenerate `llms.txt`, and preserve complete English sitemap coverage.

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
