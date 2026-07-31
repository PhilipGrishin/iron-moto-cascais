# FINAL Repository Self-Audit Report

Date: 2026-07-31

Documentation implementation commit: `d08a3297`

The durable audit inventory is `docs/REPOSITORY_AUDIT.md`. This closeout report
records the changes and acceptance evidence without becoming a second source
for current inventory. Live counts and cache-bust values remain owned only by
`docs/PROJECT_STATE.md`.

## Audit Scope And Method

The audit compared Git, filesystem output, sitemap entries, source registries,
every top-level Python/JavaScript source under `scripts/build/`, all active
validators, managed documentation, and cache-bypassed production discovery
responses. It also scanned the owner's normal project directories for another
checkout using the same remote.

The task was documentation-only. No page copy, navigation, schema, media,
inventory, `llms.txt`, `robots.txt`, HTML, or sitemap content was changed.

## Documentation Mismatches And Actions

| Mismatch found | Evidence | Action |
| --- | --- | --- |
| Build/setup/validation sequences were duplicated across active documents | Command blocks had different scopes and had historically drifted | Made `scripts/build/README.md` the only owner of build and validator commands; replaced duplicates with named workflow references |
| Current inventory and cache values appeared in multiple places | Repository-wide search and C1 history | Consolidated current quantitative state in `docs/PROJECT_STATE.md`; other active docs now link to it |
| Active rules existed only in historical changelog entries | Changelog-to-code/process review | Promoted repeatable norms into `AGENTS.md` and `docs/CONTENT_TYPES.md` |
| The documentation start order was duplicated and differed by entry point | `AGENTS.md`, `CLAUDE.md`, and `HANDOFF.md` review | Added the controlling protocol as the first section of `AGENTS.md`; entry points link to it |
| Changelog history could be mistaken for current rules | Existing handoff language | Protocol now states that chronology is not a rulebook and requires promotion of reusable norms |
| The previous environment claim was too old and too portable | PEP 604 syntax and hardcoded macOS Arial paths | Documented the source-backed Python floor and the macOS-only literal full build; added the portability risk to `OPEN_TASKS` |
| The review cache duration and schedule were copied into higher-level docs | Worker/workflow source is authoritative | Removed copied timing values; active docs point to source and workflow |
| Review card count and aggregate review total were easy to conflate | Curated JSON, snapshot, and generator review | Documented `displayCount` ownership for visible cards and live Worker snapshot ownership for aggregate totals |
| `HANDOFF.md` could be read as current inventory/process authority | Stale historical role | Kept it as a thin historical entry point and linked it to the protocol |
| `.env.example` cited the historical handoff for repository identity | Git remote and project state are stronger sources | Pointed the comment to `docs/PROJECT_STATE.md` |
| Project reports used the task term `EN_PAGES`, but no registry exists | Source search | Recorded the correction: `PAGES` is the English sitemap registry |
| C7's preliminary high-density note used DPR 2 and generalized the observation to project pages | Current DPR 3 browser evidence | Preserved the original report, added a dated correction, and placed the confirmed Blog/News follow-up in `OPEN_TASKS` |
| `OPEN_TASKS` did not contain all current chat-only performance and operational findings | Comparison with task evidence | Added the duplicate article-hero transfer, measured LCP series/method, PDF portability, CDN bypass, urllib denial, temporary worktrees, and account boundaries |
| The external strategy/copy workspace boundary was not durable | Owner workflow known from task history | Added one boundary statement to `OPEN_TASKS` without copying external strategy content |
| Generator/data/validator ownership was not exhaustive | Direct inspection of every top-level build source | Replaced the build README inventory with an exhaustive source/input/output/protection map and explicit validation gaps |
| Validator documentation overstated what passing checks prove | Validator source review and C7 regression history | Documented exclusions for visual quality, measured performance, external RRT, external services, semantic lastmod truth, and high-density `<picture>` transfer |

## Changed Files

Documentation implementation commit `d08a3297`:

- `.env.example`
- `AGENTS.md`
- `CLAUDE.md`
- `HANDOFF.md`
- `README.md`
- `docs/CONTENT_TYPES.md`
- `docs/OPEN_TASKS.md`
- `docs/PROJECT_STATE.md`
- `docs/REPOSITORY_AUDIT.md`
- `docs/TASK_BRIEF_TEMPLATE.md`
- `docs/reports/C7_FIX_REPORT.md`
- `scripts/build/README.md`

Closeout documentation added after the clean-clone gate:

- `docs/CODEX_CHANGELOG.md`
- `docs/reports/FINAL_SELF_AUDIT_REPORT.md`

No `.html` file, `sitemap.xml`, `llms.txt`, or `robots.txt` changed.

## Implementation Diff Stat

Exact `git show --stat --oneline --summary d08a3297` output:

```text
d08a3297 docs: consolidate repository operating knowledge
 .env.example                  |   3 +-
 AGENTS.md                     | 125 +++---
 CLAUDE.md                     |  18 +-
 HANDOFF.md                    |  11 +-
 README.md                     |  61 +--
 docs/CONTENT_TYPES.md         | 891 +++++++++++++-----------------------------
 docs/OPEN_TASKS.md            | 206 ++++++----
 docs/PROJECT_STATE.md         | 462 +++++++++-------------
 docs/REPOSITORY_AUDIT.md      | 229 +++++++++++
 docs/TASK_BRIEF_TEMPLATE.md   |   7 +-
 docs/reports/C7_FIX_REPORT.md |  16 +
 scripts/build/README.md       | 645 +++++++++++++-----------------
 12 files changed, 1186 insertions(+), 1488 deletions(-)
 create mode 100644 docs/REPOSITORY_AUDIT.md
```

## Validation Evidence

The first attempt used the unprepared system Python and failed before project
validation because `bs4` was not installed. No project file was changed. The
successful run used `/private/tmp/icm-final-venv`, installed from the root
`requirements.txt`.

Exact focused validator output before the documentation commit and again from
the clean clone after the full rebuild:

```text
SEO validation passed: 212 sitemap URL(s)
Brand page validation passed: 7 brand page set(s).
Harley Hub validation passed: 12 pages and all required integrations
OK: fighter project page passed multilingual, media, schema and integration checks
```

The Broad Verification sequence produced the same exact validator output.
JavaScript syntax checks, Python compilation, and `git diff --check` emitted no
errors.

## Clean-Clone Reproducibility

Clean clone:
`/private/tmp/icm-final-clean.IYacsC`

Checked commit:
`d08a32977b745bc83228788944e2e3af328ff654`

The literal **Full Safe Rebuild** from `scripts/build/README.md` completed,
including pricing PDFs, shared post-processors, discovery files, and all
focused validators. The literal **Broad Verification** also completed.

Exact status transcript after the full rebuild:

```text
POST_STATUS_START
POST_STATUS_END
```

Exact status transcript after Broad Verification:

```text
BROAD_STATUS_START
BROAD_STATUS_END
```

Both empty sections mean `git status --short` produced no output.

## Sitemap And Lastmod Integrity

Repository sitemap SHA-256 before and after the clean-clone rebuild:

```text
4910de2803fdd535c37198cf27ed541c23e66be8bd53afe80466881261e54971
```

SHA-256 of the ordered `<lastmod>` value sequence before and after:

```text
54b263ecb9b2bb7fa349ab466e72735e95d879c67d7235b3c22a27ab0abb178e
```

The hashes are identical. No per-page lastmod changed.

## Production Discovery Checks

- **Confirmed, 2026-07-31:** cache-bypassed production `robots.txt` returned
  HTTP 200 and advertised both sitemap and `LLMs-Txt`.
- **Confirmed, 2026-07-31:** cache-bypassed production `llms.txt` returned
  HTTP 200.
- **Confirmed, 2026-07-31:** cache-bypassed production sitemap returned HTTP
  200 and matched the repository sitemap SHA-256.
- **Confirmed, 2026-07-31:** default `urllib.request.urlopen` received HTTP
  403 for the live sitemap. This remains an open operational compatibility
  item, not a site change in this task.

## Resume Test: Repository Documents Only

The test followed the reading order at the top of `AGENTS.md` and did not use
chat history.

### What is this project?

It is the checked-in production source and generated output for the static,
multilingual Iron Custom Motors marketing and lead-generation website. GitHub
Pages serves the repository root and Cloudflare fronts the public domain.

### What state is it in?

The maintained registries, sitemap, localized output, schema baseline, asset
stamps, and discovery files are aligned. Exact inventory and current public
identifiers are in `docs/PROJECT_STATE.md`. The documented full build is
reproducible on the stated macOS environment, and the focused validators pass.

### What is currently in progress?

No active implementation is recorded after this audit. Open performance,
portability, CDN, monitoring, and account-access items are explicitly listed
in `docs/OPEN_TASKS.md` with evidence and status.

### What should happen next?

For a new owner-approved task, read the relevant family in
`docs/CONTENT_TYPES.md`, then execute the named workflow from
`scripts/build/README.md`. Among already recorded follow-ups, the concrete
performance candidate is eliminating duplicate high-density Blog/News article
hero downloads while preserving visual output and measuring before/after.
PDF portability and external CDN/account items remain separate scopes.

All four questions are answerable from repository documentation alone.

## Knowledge Previously Available Only In Task History

The following items were transferred into durable repository documentation:

- exact Blog/News high-density duplicate-hero behavior, affected output,
  transfer sizes, test profile, and candidate remedies;
- the complete C7/C7-FIX LCP measurement series and the conclusion that passing
  structural checks does not demonstrate a performance benefit;
- the macOS Arial dependency of pricing PDF generation;
- the requirement to bypass Cloudflare cache when verifying discovery files;
- the default urllib sitemap denial;
- the existence and role boundary of the owner's separate strategy/copy/SEO
  workspace.

Temporary C6 worktrees found outside the active checkout were also recorded as
an open cleanup decision. No other checkout using the production website
remote was found in the scanned owner project directories.

## Residual Limits

- Account-only Search Console, Cloudflare, analytics, FormSubmit, and Rich
  Results UI state cannot be certified from repository access alone.
- The external strategy workspace was intentionally not copied into this
  repository.
- The clean-clone full build is currently proven on macOS with the required
  fonts, not on another operating system.
