# Maintenance Readiness Audit — 18 September 2026

This report describes the **pre-fix audit baseline**. Subsequent owner-authorized
stabilization is recorded in Project State and the
[stabilization report](STABILIZATION_2026_09_18.md); the
audit findings below remain dated evidence rather than current open status.

## Decision and scope

**Confirmed:** the project can be maintained with the available local runtime,
repository access, browser sessions and Cloudflare credentials. No additional
plugin is needed for routine website work. **Not confirmed:** a clean release
baseline. The current upstream output has a reproducibility defect, and the
working checkout contains unfinished documentation from the preceding audit.

This was an onboarding and maintenance audit, not a request to change public
copy, deploy software or edit account settings. No website implementation,
commit, push, branch change, form submission or account configuration change
was performed. `git fetch` updated remote-tracking information only. Existing
uncommitted work was preserved. Temporary rebuilds ran outside the checkout.

Current inventories and deployed identifiers belong to
[Project State](../PROJECT_STATE.md); unresolved actions belong to
[Open Tasks](../OPEN_TASKS.md#maintenance-readiness-follow-up).

## Evidence boundaries

Measured on 2026-09-18 in Europe/Lisbon:

- Local baseline: `67d27b24`, branch `main`, one registered worktree.
- Upstream baseline: `7d9e482d`, the automated review refresh of 14 September.
  Its Actions run `34846035990` completed both refresh and reusable deployment.
- Git history: 250 commits reachable from upstream, beginning 4 May 2026.
  Instructions, canonical documents, implementation chronology, recent reports,
  source ownership, generators, runtime and both workflows were inspected.
- All 1,687 tracked files were readable and hashed. Header verification of
  1,292 tracked raster images found no errors. This is not a visual review of
  every image or an exhaustive line-by-line security review of every source.
- The 249 HTML files had 36,872 checked local link/asset references and zero
  missing file targets. Fragment targets and every external website link were
  not exhaustively checked. Relative links in the active documentation and
  reports resolved.
- Ignored credentials, prior account evidence and operational lead reports
  were kept private. Dependency environments and Git internals were not treated
  as website source files. No credential value is included in this report.

## Validation results

| Check | Result and limitation |
|---|---|
| Local Python environment | Existing `.venv`, Python 3.14.6; `pip check` passed; required packages and macOS Arial fonts available. System Python lacks the project packages, so activate `.venv` first. |
| JavaScript and Python syntax | Shared JS, project JS, both Workers and all maintained Python source files passed syntax checks. |
| Leads Worker tests | All 5 existing Node tests passed. The site has validators rather than a general application test suite, but a Worker test suite does exist. |
| Local broad SEO validator | Failed only on the pre-existing 8 September changelog entry, which has no commit hash. This is a documentation gate, not an observed HTML failure. |
| Local focused validators | Brand, Harley Hub, commercial hubs, Wave 4 and all 14 project validators passed against the older local snapshot. |
| Untouched upstream commercial validator | Failed on all 52 trust strips after the automated rating change. |
| Other untouched upstream validators | Broad SEO, brands, Harley Hub and Wave 4 passed before any regeneration. |
| Full Safe Rebuild of upstream | Every command completed, including all four PDFs and all validator families. It left 52 changed HTML files plus `sitemap.xml`; therefore the clean-checkout reproducibility requirement failed. PDFs were byte-identical. |
| Git integrity / whitespace | Connectivity check completed without corruption errors; dangling historical commits were reported, not deleted. `git diff --check` passed. |

The canonical executable commands remain in
[the build README](../../scripts/build/README.md). The rebuild used a fresh
full-history local clone checked out at the exact upstream commit and the
existing project virtual environment. Network review refresh and image
re-encoding were excluded, as required by the Full Safe Rebuild workflow.

### Confirmed cause of the rebuild drift

The review workflow commits only the snapshot and four homepages. The shared
commercial trust strip also consumes the snapshot, but those 52 outputs are
not refreshed by that workflow. Their deployed initial HTML still contains
5.0 (5,0 in localized output), whereas the snapshot and live Worker now return
4.9 from 29 reviews. Runtime JavaScript can correct the displayed rating after
the request completes; the desktop tyre-page browser check observed 4,9.

Rebuilding changes only the visible rating on those 52 pages; the brand pages
also update the corresponding inline translation data. It moves 52 sitemap
dates using the working-file timestamp fallback. No other visible text change
was found in those files. Fix the complete snapshot-consumer publication path
and verify date semantics before publishing a broad regeneration.

## Production verification

- All 236 sitemap URLs returned HTTP 200 with one H1, matching canonical,
  source-matching language alternates and parseable JSON-LD. Portuguese
  alternates intentionally use `pt-PT`; treating them as missing `pt` would be
  an audit error.
- Titles and H1s matched upstream on every URL. Main-text comparison matched
  on 232 pages after decoding Cloudflare email protection. The four Privacy
  pages differed only by two spaces around the protected email, not content.
- Public `sitemap.xml`, `robots.txt`, `llms.txt`, shared CSS/JS and the review
  snapshot were byte-identical to upstream using a unique query and no-cache
  headers. This is deployed-output evidence, separate from rebuild correctness.
- All 12 unique `media.ironcustommotors.com` video/poster endpoints found in
  served HTML returned HTTP 200 to HEAD requests. Full playback and media
  account administration were not re-audited.
- HTTP apex and HTTPS `www` resolved to the HTTPS apex. The three previously
  documented legacy deep links still finish at HTTP 404; see Open Tasks.
- Browser checks covered PT home, PT contact and modal, PT BMW service and EN
  Beckman at 390 px, plus PT tyre service at 1440 px. No document-level
  horizontal overflow was measured on those pages. The contact modal opened
  and closed, mobile navigation exposed the registered sections, and switching
  Beckman from EN to PT displayed Portuguese content. Sampled browser logs
  contained no warnings/errors. This is a representative sample, not a
  236-page visual or accessibility certification.
- The homepage email card was visibly clipped at 390 px; PT modal placeholders
  still include English text. These are small UI follow-ups, separate from
  document-level overflow.
- The form was inspected without sending an enquiry. Its private FormSubmit
  alias is present. Browser checks used `icm-leads-test=1` when opening the
  form so any form-view event uses the reserved acceptance partition. Inbox
  delivery was not retested.

## Access and integration readiness

| Service | Confirmed access or health | Remaining boundary |
|---|---|---|
| GitHub repository and Actions | Authenticated `gh` account has pull/push/admin permissions; remote fetch and workflow/job inspection worked. | Push dry-run was rejected as non-fast-forward because local `main` is behind. No forced push or real write was attempted. |
| GitHub Pages / Cloudflare edge | Latest review deployment succeeded; live content matches upstream. | Origin settings and all CDN rules were not audited. GitHub's `https_enforced` flag alone does not describe the working Cloudflare HTTP redirect. |
| Cloudflare Workers | Existing Wrangler OAuth reaches the configured account; deployment histories for both Workers are readable. | No deployment, token creation, new integration or permission expansion was performed. |
| Reviews / Google Places | HTTP 200 and correct production CORS; current aggregate matches deployed snapshot. | Google Cloud key restrictions, billing and revocation of the historical key were not verified. |
| Leads / KV | Authenticated 7-day stats response has the expected contract and excludes tests. No-token request returned 401; apex/www preflights returned 204; foreign-origin preflight returned 403 without allow-origin. | This verifies access and the response contract, not unique clients, appointments or revenue. |
| Google Search Console | Current signed-in session accesses the correct domain property. Sitemap processed successfully on 16 September with 236 discovered pages. Manual actions and security reports both say no problems. | No fresh full performance export, URL-by-URL index audit, Rich Results test or PageSpeed benchmark was run. |
| Google Business Profile | Current signed-in manager lists the verified Iron Custom Motors business. | Services, new reviews, performance and pending edits were not exhaustively re-audited. |
| FormSubmit | Source and modal route use the maintained private alias. | Current inbox receipt remains untested; a deliberate delivery test requires an explicitly authorized message. |
| Media hosting | All referenced endpoints available. | Upload/admin access and storage policy not tested. |
| Legacy domain | Redirect behavior observable publicly. | Registrar/DNS recovery remains unresolved. |

Existing browser sessions and OAuth can expire. Their success today is not a
promise of permanent access. No new connector is required to continue routine
code/content work.

## Other confirmed findings

1. `deploy.sh` is an obsolete bootstrap script that deletes `.git`, initializes
   a new repository and tries to create a GitHub repository. It must not be
   used for maintenance. Current publication is the tracked Pages workflow.
2. A Google API-key-shaped literal remains in the historical version of
   `worker/README.md` at `185d3607`; its removal appears in `7ea6b1b1`. The
   current tracked-text scan found no Google/GitHub/private-key pattern match.
   A later Worker secret update is visible, but it does not establish that
   the exposed historical key was revoked. The literal was not tested or
   reproduced in audit output.
3. Pages and review-refresh workflows do not run the repository validators
   before deployment. This explains how a successful deployment can coexist
   with the confirmed trust-strip failure.
4. `worker/README.md` claims a stale-body fallback on upstream failure, but
   `worker/reviews.js` returns 502 after a cache miss followed by a fetch/API
   error. The static site fallback is separate. The README's cache-refresh and
   API-call-budget claims should be reviewed against the actual implementation.
5. Current brand copy still advertises in-house dyno capability, contrary to
   the last owner-confirmed availability boundary. The previous audit also
   records stale legal tracking disclosures and incomplete customer attribution.
   No new equipment availability or business outcome was assumed.
6. Previous current-state documentation had stale sitemap hash/unique-date
   values as well as the superseded review aggregate. The dated corrections
   in Project State describe measured production, not changes to public files.

## Handoff and next implementation

Start the next implementation by preserving and deliberately reconciling the
existing audit documents, then fast-forwarding local `main` to upstream. Do
not use `git add .`: the preceding SEO report contains internal account and
commercial analysis and must not accidentally enter the public repository.

The first technical task should repair review-refresh propagation, restore
clean-rebuild and validation gates, and retire the destructive bootstrap entry
point. Correct dyno availability in the maintained multilingual sources as a
separate factual-content task. Historical key revocation should be confirmed
in Google Cloud without exposing or testing the old credential.

New work should continue through the existing shared generators, four-language
parity, family validators, cache-bust rules and post-deployment verification.
No CMS, replacement framework or new service is needed for this handoff.

## Audit artifacts

Only this report and the canonical state/risk/chronology notes were changed by
the audit. Raw command logs, crawl JSON and isolated clones are temporary under
`/tmp/icm-readiness-20260918/`; they are not durable prerequisites for a future
session. The decisive findings and verification limits are recorded above.
No audit documents were committed or pushed during this analysis task.
