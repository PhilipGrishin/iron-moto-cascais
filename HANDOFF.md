# Iron Custom Motors - Historical Handoff

This file is retained as a stable top-level entry point for older tooling and
bookmarks. It does not own the current site inventory or build workflow.

## Resume Here

Start with the `START HERE: Documentation Protocol` in `AGENTS.md`. It owns
the required reading order and the location of every durable project fact.

`docs/PROJECT_STATE.md` is the only documentation source for current URL,
HTML, page-family, language, project, article, brand, and cache-bust
quantities. Do not copy those values into this file.

## Project Summary

Iron Custom Motors is a static multilingual marketing and lead-generation
website for a motorcycle workshop in Cascais, Greater Lisbon. GitHub Pages
serves the checked-in HTML from the repository root.

The project uses plain HTML, CSS, and JavaScript. Python and Node helpers in
`scripts/build/` regenerate and validate static output. Page-family ownership
and canonical command sequences are documented in `docs/CONTENT_TYPES.md` and
`scripts/build/README.md`.

Brand service pages are independent workshop pages. Their active inventory is
defined by the brands registered in `BRAND_ORDER`. The Authorized Dealer
family is a separate parts and accessories channel and must not be used to
imply authorized motorcycle-brand dealer status.

## Reviews

The current reviews implementation is
`scripts/build/build_reviews_schema.py`.

- Live rating and total review count come from the Cloudflare Worker response
  stored in `assets/reviews-snapshot.json`.
- Visible review cards come from `assets/reviews-curated.json` according to
  its `displayCount`.
- Generated JSON-LD `review[]` entries mirror the visible curated cards.
- `AggregateRating.reviewCount` remains the live total from the Worker
  snapshot, not the number of visible cards.

See the Reviews section in `docs/CONTENT_TYPES.md` for the maintained workflow.

## Delivery

Follow the end-to-end delivery and verification rules in `AGENTS.md`.
GitHub Pages deploys the `main` branch, and deployment verification is part of
the task unless the owner explicitly limits the scope.

Never expose secrets in documentation, commits, logs, or screenshots. Secret
variable names and ownership notes live in `.env.example`.
