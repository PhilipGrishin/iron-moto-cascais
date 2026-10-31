# F-FUEL-FIX delivery record

Date: 2026-10-31. Status: implementation in progress; deployment pending.

## Scope and decisions

- Confirmed baseline and first parent: `8c07ec88c513d89d1adeaa4f512ee72671e049c3`.
  Local main and origin/main match; the intake worktree was clean.
- Apply owner-approved revision 3 byte-for-byte, update its existing checksum
  pin, and rebuild the five-hub family through the documented shared workflow.
- The input differs in exactly 17 lines: one unrendered facts line and four
  lines per language (section 01 introduction, item 4, related price-list
  anchor and FAQ answer 1). No hourly rate remains on Fuel System pages.
- Preserve all other site content, prices, assets, video/player/schema,
  navigation, footer, integrations, PDFs, Workers and external accounts.
- Verify complete approved copy and FAQ parity, exact four-page/sitemap scope,
  the common release gate and Full Safe Rebuild in a fresh full-history clone.
  Commit, push, and verify the four public pages before closing the task.
- Use the explicitly attached Desktop file; the brief's Documents input path
  is superseded by the attachment location. Its required checksum matches.

## Local verification

- Confirmed by the input hash and line-by-line comparison: exactly 17 source
  lines changed. The supplied file is preserved byte-for-byte and its existing
  checksum pin and build README table are updated. Current revision and SHA
  are recorded in PROJECT_STATE.md.
- The documented hub/downstream workflow and `verify_site.sh` passed: all
  validator families, every registered project, JavaScript syntax and five
  existing Leads Worker tests. Complete four-language copy and FAQ parity
  passed through the existing commercial-hub validator.
- Independent [scope audit](F_FUEL_FIX_SCOPE.json) compares against the exact
  baseline: only four HTML files changed; the other 261 are byte-identical.
  After masking the four approved visible units and FAQ answer 1 in JSON-LD,
  the complete page DOM matches baseline. This includes the player,
  VideoObject, all remaining schema, metadata, header, footer, scripts and form.
- Each page has one H1, five hreflang alternates, its canonical and og:image,
  six FAQ entries and five related cards. Hourly-rate occurrences are zero;
  euro amounts are exactly the allowed set. No cache-bust change was needed.
- `llms.txt`, shared assets, other source copy, pricing data, PDFs, Workers and
  all other tracked files outside the declared change are byte-identical.
- [Browser checks](F_FUEL_FIX_BROWSER_LOCAL.json): installed Chrome through
  Playwright, all four languages at 390 and 1440 px. The revised introduction,
  item 4 and FAQ answer render; the first FAQ opens. Zero horizontal overflow,
  JavaScript errors or HTTP failures. PT mobile and RU desktop section captures
  were visually inspected; lead events were intercepted and no form submitted.
- `git diff --check` passed. Clean-clone rebuild and deployment are pending.

## Exact sitemap accounting

All 248 URLs are unchanged. Exactly these four content dates move; the other
244 dates remain unchanged. Before/after timestamps are in the scope audit.

- `https://ironcustommotors.com/fuel-system-service/`
- `https://ironcustommotors.com/pt/fuel-system-service/`
- `https://ironcustommotors.com/ru/fuel-system-service/`
- `https://ironcustommotors.com/uk/fuel-system-service/`

## Deviations and limits

- No implementation deviation. The only input-location difference is noted
  above. No external account, media object or business listing was modified.
- Google Rich Results was not rerun for this text-only revision. Visible FAQ
  and FAQPage parity were verified directly; the prior F-FUEL test remains
  historical evidence and is not claimed as a fresh test.
