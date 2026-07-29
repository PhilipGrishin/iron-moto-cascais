# Iron Custom Motors - Agent Context

Read `AGENTS.md` before making changes. It defines the operating rules for
this repository and applies to every coding agent.

## Source Of Truth

Use repository sources in this order:

1. `AGENTS.md` for operating rules and non-negotiables.
2. `docs/PROJECT_STATE.md` for the current site inventory, supported languages,
   active page families, and current cache-bust value.
3. `docs/CONTENT_TYPES.md` for page-family ownership and repeatable workflows.
4. `docs/OPEN_TASKS.md` for temporary risks and unresolved follow-ups.
5. `scripts/build/README.md` for canonical generator and validator order.
6. Source data and generators under `scripts/build/`.
7. Generated HTML as output and verification evidence.

Do not rely on external local files or paths that are not committed to this
repository. When required business or content requirements are missing from
the sources above, state the gap and ask the owner before making an
irreversible decision.

## Project Purpose

Iron Custom Motors uses this static multilingual website for marketing,
local search, AI-citation readiness, and service lead generation. The site is
served from the repository root by GitHub Pages.

The implementation is plain HTML, CSS, and JavaScript. Python and Node helpers
under `scripts/build/` generate and validate checked-in output; there is no
server-side application framework or CMS.

## Working Rules

- Preserve multilingual parity and same-language internal links.
- Keep asset paths absolute.
- Treat generated page data and shared renderers as the source of truth.
- Preserve canonical, hreflang, JSON-LD, image dimensions, and sitemap
  consistency.
- Use real content dates for sitemap and structured-data dates.
- Follow the end-to-end delivery rule in `AGENTS.md`.
- Keep site copy premium, restrained, and engineering-driven.
- Do not describe independent motorcycle-brand service pages as authorized
  dealer pages. The relevant brands are those registered in `BRAND_ORDER`.
- Keep the Authorized Dealer family separate from independent brand service
  pages.
- Never expose secrets in client files, documentation, commits, or logs.

## Reviews

Google rating and total review count come from the Cloudflare Worker response
stored in `assets/reviews-snapshot.json`. The Worker uses a twenty-four-hour
edge cache.

Visible review cards are selected from `assets/reviews-curated.json` according
to its `displayCount`. The generated JSON-LD `review[]` entries must match
those visible cards exactly, while `AggregateRating.reviewCount` remains the
live total from the Worker snapshot.

The current refresh implementation is
`scripts/build/build_reviews_schema.py`. Follow the Reviews workflow in
`docs/CONTENT_TYPES.md` and the command order in `scripts/build/README.md`.

## Verification

Run the focused validators named by the relevant page-family workflow, then
run the broad SEO validator and `git diff --check`. Do not claim completion
without checking the intended output and likely regressions.
