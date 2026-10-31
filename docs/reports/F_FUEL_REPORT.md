# F-FUEL delivery record

Date: 2026-10-31. Status: deployed and production-verified; all requested acceptance checks passed.

## Scope and implementation plan

- Confirmed baseline: `acc06dce942cfe8d89d6310ec3a449d816b6c04b`; local main and
  origin/main match. The worktree was clean at intake.
- Add the approved fuel-system service page in four languages through the
  existing copy-driven hub renderer. Preserve all supplied copy bytes and pin
  SHA-256 `0981b316c80d262e51bd806a99497e969eeeb210265b27f3b2bd8757037a315c`.
- Share the existing Blog deferred native-video renderer/script. Add optional
  video metadata and a block after section 04; keep old Blog output unchanged.
- Add only the approved footer and two contextual links. Preserve header
  navigation, existing page bodies outside the eight approved integration
  URLs, every amount, all PDFs, forms, Workers and reviews.
- Register discovery/deployment paths, validate exact copy and scope, test
  responsive pages/video, commit, clean-clone rebuild, push and verify public
  pages, media and Google Rich Results.

## Media decisions and access

- Confirmed: no files are supplied in `_media/fuel/`. Use the approved fallback
  hero `/photos/service-action-1600.jpg`; no new hero image is generated.
- The owner explicitly authorized Codex to upload the supplied Downloads MP4,
  superseding the attachment's owner-upload assumption. Do not commit the MP4
  or poster to Git. Upload only the two new fuel-system objects to the existing
  media host; do not modify existing objects, bucket access or Workers.
- Initial public checks: both intended media URLs returned 404.
- Resolved access interruption: Wrangler OAuth and browser login had expired.
  The owner signed into the existing account in Chrome; the upload succeeded
  through that authenticated browser session.
- Confirmed by FFmpeg: input is 720 × 1280, 30 fps, H.264 High 4:4:4 / yuv444p,
  HLG / BT.2020, with AAC at 96 kHz. Prepare a compatible H.264 High / yuv420p,
  SDR BT.709 / AAC 48 kHz web copy with fast-start metadata, retaining the
  original file. Derive a poster frame from the converted video.

## Known implementation differences from the brief

- `assets/main.js` is the maintained source of global translations;
  `extract_i18n.js` writes `i18n.json`, not the reverse. Add the approved key to
  the runtime source and regenerate JSON to keep Full Safe Rebuild stable.
- The footer is shared chrome, so other pages receive the footer addition and
  the required cache-bust; neither causes a content-date change.
- The current visible hub breadcrumb includes Services, but its JSON-LD omits
  that level. Make the new page's breadcrumb match the requested visible path
  without changing the four existing hubs' schema.

## Verification and deployment

Local and production acceptance passed; detailed evidence follows below.

## Upload evidence

- Confirmed: existing `icm-media` R2 bucket has the active custom domain
  `media.ironcustommotors.com`. The owner signed in; exactly two new objects
  were uploaded through the Cloudflare UI. Browser-extension direct upload
  required additional file-URL access, so the standard macOS file chooser was
  used instead; no new extension permissions were granted.
- MP4: HTTP 200, `video/mp4`, 19,682,121 bytes, SHA-256
  `45175aa9af5002866c9fba51c90dde50c03a893f5d0fcba0ad8a530a41775de3`.
  R2/public Last-Modified: `2026-10-31T20:03:29+00:00` (Lisbon offset).
- Poster: HTTP 200, `image/jpeg`, 118,777 bytes, SHA-256
  `bee8ba36eca72e21699cb9224ac9967beea67552abe101ba2affd1d2cb044137`.
  R2/public Last-Modified: `2026-10-31T20:03:26+00:00`.
- Downloaded bytes equal the prepared local objects; MP4 byte range 0–1023
  returns HTTP 206 and exactly 1,024 bytes. Actual media: 720 × 1280,
  49.942 seconds, H.264 High/yuv420p SDR BT.709, AAC 48 kHz, fast-start.
  Poster is frame 10 seconds. Original owner input remains unchanged:
  SHA-256 `8dceaa1c8c3daa4d0a91cbf4e00457f53e58ffd349da642797362dfb85fc73ac`.
- Additional scope clarification: the four noindex thank-you pages are omitted
  from the sitemap navigation patcher and preserve their body shells. The
  shared patcher now refreshes their managed footer columns only; headers,
  forms and body copy remain unchanged.
- Rollback: reverting site commits removes page links and media references.
  The two uploaded R2 objects remain external assets; no existing object or
  bucket setting was modified.

## Local acceptance

- Full Safe Rebuild passed on macOS, including all four PDF outputs and all
  validator families. The common read-only release gate passed separately,
  including JavaScript syntax and all five existing Leads Worker tests.
- Four new language variants match the complete approved hero, sections,
  CTA, related links and six FAQ answers; visible FAQ and JSON-LD match.
  Optional video metadata is localized, real dimensions and duration are used,
  no `inLanguage` is inferred, and the block sits between sections 04 and 05.
- Both one-byte copy-checksum failure tests rejected modified input; exact
  original bytes were restored. Service source differs in exactly four lines.
- Independent [scope audit](F_FUEL_SCOPE.json): all 244 old page schemas and
  all 261 existing header/mobile/form regions are unchanged. Exactly eight
  old main-content pages changed. All 252 shared footers contain one localized
  Fuel System link immediately after pre-purchase inspection. No new incoming
  header/home/service-card/related-card integration was added.
- All four PDFs, shared CSS, project assets and review files are byte-identical
  to baseline. Runtime JavaScript changes only add the four approved labels.
- Checked 42,956 local link/asset references and 588 static fragment targets
  with zero missing destinations. The other 44 fragment links are existing
  booking-modal actions, each with the matching modal.
- [Browser evidence](F_FUEL_BROWSER_LOCAL.json): installed Chrome through
  Playwright at 390 × 844 / DPR 2 and 1440 × 1000 / DPR 1; zero horizontal
  overflow, JavaScript errors or failed HTTP responses. No MP4 request before
  click; after click the real remote video plays at 720 × 1280. FAQ expands and
  the localized lead modal opens. No lead form was submitted; lead-event
  requests were intercepted locally. All four language titles/footer routes
  were checked. Screenshots were visually inspected after the existing loader
  disappeared. Browser duration is 49.941 s; MP4 movie header is 49.942 s.
- Initial checks caught mixed generator cache stamps, a comparison-only space
  around inline links in parentheses, and missing utility-page footer updates.
  These were corrected before acceptance; no approved prose was changed.

## Exact sitemap accounting

Baseline 244 → 248 URLs. The following existing URLs receive content dates for
Service section 01 item 8's approved appended link:

- `/motorcycle-service/`
- `/pt/motorcycle-service/`
- `/ru/motorcycle-service/`
- `/uk/motorcycle-service/`

These existing URLs receive content dates for the approved web-only pricing note:

- `/pricing/`
- `/pt/pricing/`
- `/ru/pricing/`
- `/uk/pricing/`

New publication URLs:

- `/fuel-system-service/`
- `/pt/fuel-system-service/`
- `/ru/fuel-system-service/`
- `/uk/fuel-system-service/`

All other 236 existing dates stay unchanged. Exact before/after timestamps and
reasons are preserved in `F_FUEL_SCOPE.json`; shared-footer/cache-only changes
never advance those dates. Main assets use the canonical stamp recorded in
`PROJECT_STATE.md`; project asset stamps remain unchanged.

## Reproducibility and implementation identity

- Implementation/artifact commit: `3d89015758fd25ea5c40077909252d7879f7dcc8`.
- Exact first parent: `acc06dce942cfe8d89d6310ec3a449d816b6c04b`; upstream had
  not moved from the requested baseline.
- The canonical Full Safe Rebuild passed in a fresh full-history local clone
  of this commit, including PDFs and every registered project validator;
  `git status --short` was empty. Evidence: `F_FUEL_REBUILD.json`.
- Push confirmed to `origin/main`; Pages workflow `41237540946` succeeded.
  The connected GitHub tool returned no runs, so the existing authenticated
  GitHub CLI supplied the exact commit/run status.

## Production acceptance

- Pages [run 41237540946](https://github.com/PhilipGrishin/iron-moto-cascais/actions/runs/41237540946)
  deployed the exact implementation commit and completed successfully at
  `2026-10-31T20:10:52Z`.
- [Production audit](F_FUEL_PRODUCTION.json): all 248 sitemap URLs and four
  noindex thank-you pages returned HTTP 200 and matched repository main text,
  JSON-LD, title/description, canonical/hreflang, hero/video references, asset
  cache keys and the new footer route. Cloudflare email obfuscation was decoded
  before comparison. Twelve public files (discovery/shared assets and all four
  pricing PDFs) matched repository bytes through cache-bypass requests.
- [Live browser evidence](F_FUEL_BROWSER_PRODUCTION.json): the PT page passed
  both 390/1440 profiles with zero overflow, JavaScript errors or HTTP failures;
  no MP4 before click and actual playback after click. All four language page
  titles and footer routes were checked. No lead form was submitted.
- [Google Rich Results](https://search.google.com/test/rich-results/result?id=SlWCPwScILmbIJkGpBgfRQ)
  crawled the public PT URL at `2026-10-31T20:11:07+00:00`, detecting four
  valid supported items: Breadcrumb, LocalBusiness, Organization and Video.
  No errors or warnings were shown. The Video detail confirms localized copy,
  both public URLs, actual upload time and `PT49.942S`. Machine-readable
  evidence: `F_FUEL_RICH_RESULTS.json`. FAQ parity was checked directly; Google
  no longer supports FAQ rich results, as recorded in `OPEN_TASKS.md`.
- No task blocker remains. The supplied hero was absent, so the explicitly
  allowed service-photo fallback is used. Video is published and enabled;
  no later enablement step is needed. Existing account/runtime maintenance
  notices remain separately recorded in `OPEN_TASKS.md`.

## Media preparation method

FFmpeg 7.1 converted the owner file using libx264 High / level 4.0, CRF 20,
medium preset, yuv420p, AAC 48 kHz / 128 kbit/s, stripped metadata and
`+faststart`. HLG/BT.2020 → SDR BT.709 used
`zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p`.
The MP4 movie-header timescale supplied exact duration; a frame at 10 seconds
supplied the JPEG poster. Temporary codec tooling was installed outside the
repository; no project or runtime dependency was introduced.
