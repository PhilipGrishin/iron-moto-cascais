# Iron Custom Motors - Agent Context

Read `AGENTS.md` before making changes. It defines the operating rules for
this repository and applies to every coding agent.

## Source Of Truth

Follow the `START HERE: Documentation Protocol` section in `AGENTS.md`. It is
the canonical reading order and the ownership map for project facts, business
facts, workflows, open risks, chronology and build commands. Do not reproduce
that order here.

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
stored in `assets/reviews-snapshot.json`. The cache policy is owned by
`worker/reviews.js` and documented beside it in `worker/README.md`.

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
