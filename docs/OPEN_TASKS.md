# Open Tasks, Risks And Watchlist

This file keeps temporary context out of `AGENTS.md`. Update it when a task is
resolved or a new follow-up appears.

Last updated: 2026-07-31

## Active Implementation Tasks

No active implementation task is pending at the time of this update.

## Pending Content Follow-up

### High-DPR `<picture>` preload candidate selection

- Status: Observed during C7-FIX; outside that block's CSS-background scope.
- Context: At a 390px viewport with device pixel ratio 2, a blog article
  preloads its 768px AVIF hero while responsive `srcset` selects the 1280px
  AVIF of the same hero. The preload is the correct article hero, not a card
  image, but both width candidates are observed as resources. Project detail
  pages use the same `<picture>` family and were explicitly protected from
  C7-FIX changes after their measured LCP improvement.
- Next action: In a separate approved performance task, decide whether preload
  `imagesrcset`/`imagesizes` should replace breakpoint-specific links for
  `<picture>` heroes, then measure projects and articles before changing them.

### Pre-purchase description in `llms.txt`

- Status: Deferred by the C6 scope boundary.
- Context: The published inspection page and metadata now state the fixed
  EUR 150 price, while the committed AI discovery summary still carries the
  earlier starting-price wording. C6 explicitly requires `llms.txt` to remain
  unchanged.
- Next action: In the next approved GEO content task, update the maintained
  discovery source and regenerate `llms.txt` together.

## Standing Watchlist

### Google Rich Results UI

- Status: External browser/account check.
- Context: Local/source JSON-LD validation is usually available, but the actual
  Google Rich Results Test UI is external and can be rate-limited or require
  manual browser work.
- Rule: Do not claim the Google UI passed unless it was actually run. Report
  local/schema/source validation separately.

### Google Search Console

- Status: External account.
- Context: Manual indexing requests and coverage reports require user account
  access.
- Rule: Provide exact URLs and instructions when account access is not available.

### Cloudflare

- Status: External account.
- Context: DNS, cache purge, Workers and Worker secrets live in Cloudflare.
- Rule: Do not expose secrets. For review-worker checks, verify the public
  Worker endpoint and document any account-only actions.

### Google Places API Key Rotation

- Status: Operational watch item.
- Context: Reviews use the Cloudflare Worker secret, not a client-side key.
- Rule: Rotate through Google Cloud + Cloudflare Worker secret when requested,
  then verify the Worker and site review widget.

### CMS

- Status: Not implemented.
- Context: All content publishing is currently developer-driven through the
  repository and generators.
- Recommendation: Add a CMS only if non-developers need to publish frequently.

### Advanced Lead Form

- Status: Future enhancement.
- Context: Current lead path is WhatsApp + FormSubmit.
- Possible future fields: brand, model, year, urgency, preferred date, photo
  upload, anti-spam and thank-you URL.

## Documentation Update Checklist

When any item above changes:

1. Move resolved items out of this file or mark them resolved with date.
2. Add a short entry to `docs/CODEX_CHANGELOG.md` if code/site changed.
3. Update `docs/PROJECT_STATE.md` if the site structure changed.
4. Update `docs/CONTENT_TYPES.md` if the implementation pattern changed.
