# Project instructions for AI agents

This file is read by AI coding agents (Codex, Cursor, Cline, Claude Code,
and others) before work begins.

## START HERE: Documentation Protocol

The repository is the sole durable source of project truth. Nothing important
may exist only in chat, an external local file, or one agent's memory. The
acceptance question at every handoff is: **would a new session, with no chat
history, know what is true, what is open, and how to continue safely?**

### Canonical Home For Each Kind Of Information

| Information | Canonical home |
|---|---|
| Current state, inventories, counts, deployed identifiers and cache-bust values | `docs/PROJECT_STATE.md` |
| Canonical business identity, NAP, hours, founder, profiles and published key prices | `docs/BUSINESS_FACTS.md` |
| Repeatable processes, page-family ownership and stable implementation patterns | `docs/CONTENT_TYPES.md` |
| Active operating rules and non-negotiables | `AGENTS.md` |
| Open risks, external dependencies, access requirements and unresolved work | `docs/OPEN_TASKS.md` |
| Chronology of completed work | `docs/CODEX_CHANGELOG.md` |
| Build and verification commands | `scripts/build/README.md` |
| Large-task intake shape | `docs/TASK_BRIEF_TEMPLATE.md` |

One fact gets one canonical home. Other documents link to that home instead of
copying the fact. The changelog records history; it is not a rulebook. When a
completed task establishes a reusable norm, promote that norm immediately to
`AGENTS.md` or `docs/CONTENT_TYPES.md`.

### Required Reading Order

At every session start and after context compaction:

1. Read `AGENTS.md` fully.
2. Run `git status --short` and inspect the current branch and worktree before
   editing.
3. Read `docs/PROJECT_STATE.md`.
4. Read `docs/BUSINESS_FACTS.md` when business identity, contact, hours,
   origin, service languages, profiles or published prices are relevant.
5. Read `docs/CONTENT_TYPES.md` for the affected page family.
6. Read `docs/OPEN_TASKS.md`.
7. Read `docs/TASK_BRIEF_TEMPLATE.md` when shaping a large task.
8. Read `scripts/build/README.md` before running any build or validator.
9. Read relevant source data and generators.
10. Use `docs/CODEX_CHANGELOG.md` only for chronology and prior evidence.

`CLAUDE.md`, `README.md` and `HANDOFF.md` are entry points, not competing
sources of truth. Do not rely on chat memory when repository evidence exists.

### Recording Standard

- Record decisions immediately, including the reason and date.
- Mark canceled work `CANCELED`; do not silently delete it.
- Record scope limits, failed approaches and why they failed.
- For deployed work, record the commit, what was verified, and what was not
  verified.
- Keep measured values beside their method and date. Never present an
  unmeasured assumption as a result.
- Label material claims as `confirmed`, `data-backed`, `assumption`, `unknown`,
  or `access required`. Put the verification method beside the claim.
- Correct false documentation explicitly. State what was wrong, the corrected
  fact and its evidence; do not silently erase meaningful history.
- Never overwrite an unread file. Read it, compare it with the intended change,
  and merge deliberately.

At the end of meaningful or long-running work, update
`docs/PROJECT_STATE.md` when current state changed and `docs/OPEN_TASKS.md`
when risks or follow-ups changed. Add implementation chronology to
`docs/CODEX_CHANGELOG.md`. Run the documented verification before handoff.

## Scalability and handoff rule

- Every site change must leave the project easier for the next
  developer or the next AI session to understand. Prefer clear
  source data, shared helpers, and documented build flows over
  one-off manual edits.
- Keep the site scalable. Do not introduce a separate generator,
  compiler, or editing path for each individual page when an
  existing generic page family or shared renderer can be extended.
  Typical repeated work belongs in reusable data structures,
  reusable build scripts, or documented shared utilities.
- When a change creates or modifies a repeatable pattern, update
  the relevant documentation (`AGENTS.md`, `README.md`,
  `docs/PROJECT_STATE.md`, `docs/CONTENT_TYPES.md`,
  `docs/CODEX_CHANGELOG.md`, `docs/OPEN_TASKS.md`,
  `scripts/build/README.md`, or an adjacent source comment) so a
  developer can quickly find where the data lives, which generator
  owns it, and which verification commands protect it.
- Keep stable rules in `AGENTS.md`; keep temporary follow-ups,
  external-account risks and unresolved items in `docs/OPEN_TASKS.md`.
  Do not let `AGENTS.md` become a task backlog.
- After each meaningful implementation, add a short entry to
  `docs/CODEX_CHANGELOG.md` with the commit, what changed, what
  was verified and any handoff notes.
- For large content tasks, prefer a short task brief plus attached
  files. Do not duplicate long multilingual copy in chat when the
  source file can be read from disk.
- Stability comes first. Design changes must be implemented in a
  way that future generated pages inherit safely, and verification
  must check that previous page families still render and link
  correctly.

## How to operate in this repo

- Project-boundary confirmation is mandatory. If the owner submits a task in
  this chat that does not directly concern `ICM_Website` or its deployment,
  do not inspect, modify, deploy, or otherwise act on another project. First
  ask the owner whether the task should be executed and which project it
  belongs to, and proceed only after explicit confirmation.
- The repo is a static site (HTML, CSS, JS). There is no
  framework, no build step on the server side, no test suite.
  GitHub Pages serves files in `main` branch root as-is.
- Editing work may be a direct source edit, a generated page-family update, or
  a combination. Inspect ownership in `docs/CONTENT_TYPES.md` before choosing.
- After any change to `assets/main.css` or `assets/main.js`,
  bump the cache-bust query (`?v=...`) on every HTML file. The
  convention is `?v=YYYYMMDD<letter>`. Read the current value from
  `docs/PROJECT_STATE.md`.
- When the project owner asks Codex to do implementation work,
  treat the request as an end-to-end delivery by default: make
  the change, run the relevant verification, commit, push, and
  verify the result after the push. Do not stop at a proposal or
  an unpushed working tree unless the owner explicitly says
  "no commit", "no push", "analysis only", "draft", or gives
  another limiting instruction.
- Verification does not stop at `git push`. After every push,
  automatically verify the exact work that was pushed. For site
  changes, check the public production URLs after deployment
  whenever possible, confirm the relevant pages/assets/schema are
  live, and report any external checks that cannot be performed
  without account access.
- Do not commit Python bytecode, `__pycache__`, local virtual environments, or
  build scratch files. Keep generated output reproducible from tracked sources.

## File-by-file routing

- Site-wide copy → look first in `assets/main.js` (`I18N` object,
  keys like `nav.services`, `cta.bookHeader` etc.). If the copy
  appears in pre-rendered HTML, it must be updated in BOTH
  `main.js` AND every language's pre-rendered HTML — running
  `scripts/build/build_i18n.py` keeps them in sync.
- Per-page copy that is specific to one page (e.g. the
  `/bmw-service/` body text) lives in
  `scripts/build/<feature>_data.py`. Editing the data file and
  re-running the matching `build_*.py` script regenerates the
  HTML.
- All project detail pages are registered in
  `scripts/build/project_pages_data.py`, rendered directly in four languages
  by `scripts/build/build_project_pages.py`, and checked by
  `scripts/build/validate_project_pages.py`. Migrated copy lives in the
  registered project data files, never only in generated HTML or an inline
  `window.ICM_I18N_PAGE` block. Read the Projects section in
  `docs/CONTENT_TYPES.md` before editing this family.
- News articles live in `scripts/build/news_data.py`. To add
  one, add an entry to `NEWS_ARTICLES`, then run
  `build_news.py`.
- Blog articles live in `scripts/build/blog_data.py`. The
  `/blog/` hub and `/blog/<slug>/` articles are generated by
  `build_blog.py`; posts should be added to `BLOG_POSTS` and then
  wired into the same multilingual build flow as news articles.
- Brand service pages are registered in
  `scripts/build/brand_pages_data.py`. Add new brands to
  `BRAND_CONFIG` / `BRAND_ORDER`, then add `BRAND_HEAD` and
  `PAGE_I18N` content for every supported language. Follow the
  Brand Pages workflow in `docs/CONTENT_TYPES.md`.
- The Authorized Dealer hub lives in
  `scripts/build/authorized_dealer_data.py` and is generated by
  `scripts/build/build_authorized_dealer.py`. Future official
  dealer partner cards belong in `AUTHORIZED_DEALER_BRANDS`; keep
  this as the single source of truth for the hub and future
  `/authorized-dealer/<brand>/` subpage cards.
- Pricing tables are in `scripts/build/pricing_data.py`. Edit
  and re-run `build_pricing.py`.
- Legal pages (Privacy, Cookies, Terms) are in
  `scripts/build/legal_pages_data.py`.
- The generated hub pages (`/services/`, `/projects/`, `/about/`,
  `/community/`, `/contact/`, `/faq/`) are in
  `scripts/build/new_pages_data.py` and are rendered by
  `scripts/build/build_new_pages.py`.

## Non-negotiables

- Multilingual parity. Every public page must exist in every supported
  language. Read the current language inventory from
  `docs/PROJECT_STATE.md`; do not introduce an English-only public page.
- Internal link locality. A page under `/ru/` must link to other
  `/ru/` pages, not to the English root. `localize_internal_links.py`
  enforces this; run it after generating HTML.
- Absolute asset paths. Use `/photos/...` and `/assets/...`, not
  relative `../`. Relative paths break inside language subtrees.
- Schema.org JSON-LD on every indexable page. At minimum a
  `BreadcrumbList`. The site relies on this for both Google and
  AI engine citation.
- Cache-bust. Every change to `assets/main.css` or `assets/main.js`
  must come with a cache-bust bump across every HTML file.
- Sitemap and `hreflang` consistency. New pages go into
  `scripts/build/build_sitemap.py` PAGES list AND get hreflang
  alternates on every language variant. New page paths also go
  into `scripts/build/localize_internal_links.py` LOCALIZED_PATHS.
- Sitemap `<lastmod>` must reflect each page's real last-content-change
  date from Git history of that page's source/served HTML, per language,
  in ISO-8601 with timezone. Never stamp all URLs with the build/deploy
  time. An unchanged page must keep the same `lastmod` across deploys.
- Structured-data `datePublished` and `dateModified` must use real
  content dates with timezone, not deploy time.

## Conventions

- Cache-bust query string format: `?v=YYYYMMDD<letter>`.
- Localized subtrees: `/ru/`, `/uk/`, `/pt/` (lowercase ISO 639-1).
- Default language is English at `/`.
- Tone of copy: premium, restrained, engineering-driven. No
  emojis in copy. Brand names of motorcycles are kept in their
  original spelling across every supported language.
- The project owner asked that the brand stay "independent" —
  do not call the workshop an authorized motorcycle-brand dealer.
  This applies to the brands registered in `BRAND_ORDER`; preserve
  the approved independent-workshop wording in their source data.
- The Authorized Dealer section is a separate parts/accessories
  supply channel. Do not imply authorized motorcycle-brand dealer
  status unless an official partner page and approved wording have
  been provided.
- "Iron Custom Motors" is the brand name and stays untranslated.
- All Google review surfacing goes through the Cloudflare Worker
  at `https://icm-reviews.vg-ab6.workers.dev/`. Do not put the
  Google Places API key in the client-side site.

## Common task workflows

Do not duplicate generator sequences here. They drift when a shared SEO or
validation stage changes.

- Use `docs/CONTENT_TYPES.md` for translation, hub, Authorized Dealer, brand,
  news, blog, project, pricing, Harley Hub, tyre-service, and review workflows.
- Use `scripts/build/README.md` for the canonical command order and script
  ownership.
- Keep the homepage brand strip synchronized with the brands registered in
  `BRAND_ORDER`; `validate_brand_pages.py` checks this contract.

### Update Google reviews snapshot and curated cards

This workflow requires outbound network access. Follow the canonical Reviews
commands in `scripts/build/README.md` and the ownership rules in
`docs/CONTENT_TYPES.md`.

The script fetches `https://icm-reviews.vg-ab6.workers.dev/`,
writes the live rating/count to `assets/reviews-snapshot.json`,
reads editorial cards from `assets/reviews-curated.json`, and
injects static home-page review cards plus LocalBusiness
`AggregateRating`/`Review` JSON-LD on the supported home pages.

`AggregateRating.ratingValue` and `reviewCount` must come from the
Worker/snapshot total. Visible cards and JSON-LD `review[]` items
must come from the curated file and match 1:1. Do not set
`reviewCount` to the number of curated cards.

The scheduled automation lives in `.github/workflows/reviews-refresh.yml`; its
cron and manual trigger are defined only in that workflow.

## What this site does NOT have (do not assume)

- No build step on GitHub side.
- No CMS.
- No test suite.
- No type checking.
- No backend other than FormSubmit and the Cloudflare Worker.
- No Google Tag Manager container (events go to `dataLayer`
  via `gtag` directly; no GTM loader).
- No admin UI.

If a task seems to require any of the above, stop and ask the
project owner before introducing one.
