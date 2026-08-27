# M-REPO Delivery Report

Date: 2026-08-27 (Europe/Lisbon)

Status: **implementation and CI gating confirmed; final Pages retry pending**

## Repository Transfer

- The owner transferred the repository on 2026-08-24 to
  `https://github.com/PhilipGrishin/iron-moto-cascais`.
- Local `origin` now uses
  `https://github.com/PhilipGrishin/iron-moto-cascais.git` for fetch and push.
- `git fetch origin` and `git push --dry-run origin main` both succeeded.
- The owner confirmed that the domain, DNS and GitHub Pages settings were
  reconfigured and verified after the transfer. The former URL redirects but
  is not treated as canonical.
- A direct HTTP check on 2026-08-27 returned `301` from the former URL with a
  `Location` header pointing to the new canonical repository; the new URL
  returned `200`.

## Repository Reference Audit

Repository-wide case-insensitive search, excluding `.git`, found no remaining
literal reference to the former owner name after the update. There were no
such references in `docs/CODEX_CHANGELOG.md`, so no historical changelog entry
was rewritten. Three historical Actions links retained their run IDs while
their repository owner segment was changed to the canonical owner. The
historical repository audit now explicitly records that its original remote
evidence predates the transfer.

The only executable/configuration reference was the GitHub Pages preview host
in `worker/reviews.js`; it now allows `https://philipgrishin.github.io`.
Deployment of this Worker source is separately marked **access required** in
`docs/OPEN_TASKS.md` because Wrangler has no Cloudflare API token in this
environment. The production custom-domain origin remains allowed.

## CI Design And Verification

- `.github/workflows/pages.yml` uses `cancel-in-progress: true` for the shared
  `pages` concurrency group. Pushes during this delivery cancelled superseded
  runs `33098540463` and `33099198727`, confirming the behavior.
- `pages.yml` is also a reusable `workflow_call` workflow.
- `.github/workflows/reviews-refresh.yml` exposes the commit step's
  `committed` output and calls the reusable Pages workflow only when that
  output is `true`.
- Changed-path evidence: manually dispatched Reviews run `33098885793`
  refreshed the Worker snapshot and pushed bot commit `6f28a412`. This exposed
  the GitHub security behavior that a `GITHUB_TOKEN` push does not start a new
  push workflow, and motivated the explicit reusable-workflow call.
- No-change evidence: a second manual dispatch, run `33099517887`, logged
  `No review changes to commit.`, completed successfully, and skipped its
  `deploy` job. It created neither a new commit nor a Pages workflow run and
  did not cancel the in-progress direct deployment.
- Both workflow files parsed as YAML; all embedded Bash blocks passed
  `bash -n`. GitHub accepted and displayed the final workflow definitions.
- Direct Pages run `33099469591` and fresh workflow-dispatch run `33100602162`
  both completed checkout, artifact preparation and artifact upload, then the
  GitHub Pages backend remained at `updating_pages` until the action's
  10-minute timeout. Retrying the same run was not used as evidence because it
  correctly encountered two same-name artifacts from the two attempts. The
  official GitHub status API reported both Actions and Pages operational, so a
  fresh final deployment is required after a cooldown; no green result is
  claimed from these attempts.

## Build And Scope Evidence

- All four validator groups passed: SEO for 236 sitemap URLs, 7 Brand page
  sets, 12 Harley Hub pages, and every registered project slug.
- The documented Full Safe Rebuild changed no generated output.
- `sitemap.xml` remained byte-identical with SHA-256
  `4ef974f467c30c2e67efe7e276dbb6b03f93efd87959a3e72d7178673a9c31ae`.
- M-REPO source scope is limited to both workflows, current repository docs,
  three historical report URLs, the repository audit note, the Reviews Worker
  preview allowlist, and workflow documentation. The manual acceptance run
  separately produced the expected automated review snapshot commit touching
  `assets/reviews-snapshot.json` and the four home pages; it raised the live
  aggregate review count from 24 to 25. No other site HTML changed.

Exact M-REPO source/documentation files:

- `.github/workflows/pages.yml`
- `.github/workflows/reviews-refresh.yml`
- `README.md`
- `docs/CODEX_CHANGELOG.md`
- `docs/OPEN_TASKS.md`
- `docs/PROJECT_STATE.md`
- `docs/REPOSITORY_AUDIT.md`
- `docs/reports/C8_FIX_REPORT.md`
- `docs/reports/C8_PROJECT_MIGRATION_REPORT.md`
- `docs/reports/M_REPO_REPORT.md`
- `docs/reports/NAV_EXPO_REPORT.md`
- `scripts/build/README.md`
- `worker/reviews.js`

Separate automated Reviews run `6f28a412` changed exactly:

- `assets/reviews-snapshot.json`
- `index.html`
- `pt/index.html`
- `ru/index.html`
- `uk/index.html`
