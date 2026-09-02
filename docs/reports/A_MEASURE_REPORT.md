# A-MEASURE Delivery Report

Date: 2026-09-02 (Europe/Lisbon)  
Status: **complete and production-verified**  
Implementation commits: `fae3a7cec8a17bd663d055282b7d1f184beb3669`,
`173d62e1a28c81c42e6f7515b865ff650fee8cef`,
`a286b68ae8dc00d94a22cf6aa8296754005b2b09`

## Delivered Architecture

The static site now sends four anonymous lead-intent event types to the
first-party operational Worker endpoint:

```text
https://icm-leads.vg-ab6.workers.dev/
```

The deployed Reviews Worker was also synchronized with its current repository
source during the same owner-authorized Wrangler session:

```text
https://icm-reviews.vg-ab6.workers.dev/
```

`icm-leads` stores only daily KV counters by event type, language and page. It
does not read or retain IP addresses, user-agent strings, form field values or
raw events. The accepted referrer value is normalized by the browser, validated
and then discarded by the Worker. Responses set no cookies. Counters expire
after 400 days, and an anonymous per-isolate limit accepts at most 120 event
requests per minute.

The browser sends `whatsapp`, `tel`, `form_view` and `form_submit` through
`navigator.sendBeacon`, with a `fetch(..., keepalive: true)` fallback. The
handler is delegated and does not delay link navigation. WhatsApp links gain a
localized page-title message at click time; checked-in link URLs remain
unchanged.

Cloudflare Web Analytics remains owner-managed edge injection. No Google,
Meta or other third-party analytics runtime was added.

## Worker Deployment And Security

The owner completed Wrangler OAuth in the browser for the Vg account. No
credential, OAuth token or stats token was printed into chat or committed.

- `icm-leads` final deployed version:
  `cf3c9c68-187a-49b6-907c-47185f1187bf`.
- `icm-reviews` final deployed version:
  `1f83be4d-1114-4b87-92bf-cb06d11a098e`.
- The lead KV namespace identifier is checked into the Worker configuration;
  the private `STATS_TOKEN` is not.
- The token is stored as a Cloudflare Worker secret and locally in
  `.secrets/leads.env` with mode `0600`.
- `.secrets/` and `.wrangler/` are gitignored and absent from `git status`.
- A fixed-string scan using the local secret found zero matches in tracked
  files. This report intentionally records no secret value.

Production endpoint checks returned:

```text
POST /event, each supported type      202
GET /stats without token              401
OPTIONS, production apex origin       204 + exact allow-origin
OPTIONS, production www origin        204 + exact allow-origin
POST/OPTIONS, foreign origin           403 + no allow-origin
Set-Cookie on checked responses        absent
```

The deployed Reviews Worker returned HTTP 200 and the exact CORS origin for
both `https://ironcustommotors.com` and
`https://philipgrishin.github.io`. Its response contained rating 5, total 26
and five API review records. The production page continued to render its
checked-in snapshot value of 25 and all nine curated cards; client pages do not
fetch the Reviews Worker at runtime, so changing the visible aggregate remains
owned by the scheduled Reviews Workflow rather than this markup-only task.

## Acceptance-Traffic Isolation

Synthetic and browser acceptance events use page `/**test**/`. The Worker
writes those counters under `test:d:` instead of the operational `d:` prefix.
Normal `/stats` responses exclude them. `tools/leads_report.py` explicitly
requests `includeTests=0`; an auditor can inspect acceptance data only with
`includeTests=1`.

The production client uses the same isolation when a page is opened with
`?icm-leads-test=1`. The query is never sent as `page`; the payload remains the
query-free reserved path and uses language `en`, satisfying the normal Worker
contract.

Final one-day acceptance totals were:

| Type | `includeTests=0` | `includeTests=1` | Acceptance sources |
|---|---:|---:|---|
| `whatsapp` | 0 | 5 | one API event plus EN/PT/RU/UK production clicks |
| `tel` | 0 | 2 | one API event plus one production click |
| `form_submit` | 0 | 2 | one API event plus one production form submission |
| `form_view` | 0 | 3 | one API event plus two production modal openings |

The reserved test page therefore contained 12 events, while the ordinary
baseline and both generated 7/28-day reports contained zero test events.

## Production Browser Verification

The in-app browser loaded the deployed shared JavaScript from
`/assets/main.js?v=20260902b`. Its resource inventory observed the lead endpoint
as `other`, with `beacon` as the request source. The telephone navigation was
blocked by the browser's external-protocol safety policy after the delegated
handler ran; the persisted `tel` increment and resource entry confirmed that
the beacon had already completed without delaying the attempted transition.

WhatsApp clicks produced exactly one `text` parameter with the page title and
the correct language prefix:

- EN: `Hi Iron Custom Motors! I'm writing from the page: ...`
- PT: `Olá Iron Custom Motors! Escrevo a partir da página: ...`
- RU: `Здравствуйте, Iron Custom Motors! Пишу со страницы: ...`
- UK: `Вітаю, Iron Custom Motors! Пишу зі сторінки: ...`

After explicit action-time confirmation from the owner, one production form
was submitted with the visible label `TEST A-MEASURE — ignore`. FormSubmit
redirected directly to `https://ironcustommotors.com/thank-you/`, whose
confirmation heading and response-hours text rendered correctly.

## Thank-You Pages And Forms

The four deployed utility pages are:

- `https://ironcustommotors.com/thank-you/`
- `https://ironcustommotors.com/pt/thank-you/`
- `https://ironcustommotors.com/ru/thank-you/`
- `https://ironcustommotors.com/uk/thank-you/`

All four returned HTTP 200, use a self-canonical URL, carry
`noindex, follow, max-image-preview:large`, and are absent from `sitemap.xml`.
The English page had to be added to the explicit Pages artifact directory
allowlist; the first successful run exposed its omission, commit `a286b68a`
fixed the source, and the subsequent deployment confirmed HTTP 200.

Browser layout checks on the English page at 390 x 844 and 1440 x 900 found no
horizontal overflow. The page and its Worker responses set no cookies.

All 128 built pages containing `#leadForm` retain the activated private
FormSubmit alias and existing hidden fields. Their `_next` values point to the
absolute thank-you URL in the page language. The alias itself was not changed.

## Reporting Tool

`tools/leads_report.py` reads its token from `ICM_LEADS_STATS_TOKEN` or the
gitignored `.secrets/leads.env`, fetches 7-day and 28-day statistics, prints
type, page and language tables, and writes the local ignored snapshot
`data/leads/<date>_leads.json`. A live run completed successfully and excluded
all acceptance counters.

## Sitemap, Content And Scope

The production and repository sitemap remained byte-identical throughout the
task:

```text
SHA-256  4ef974f467c30c2e67efe7e276dbb6b03f93efd87959a3e72d7178673a9c31ae
URLs     236
```

The four thank-you pages are intentionally outside the sitemap. No `lastmod`
moved. Visible text on all 245 pre-existing HTML files was unchanged; the only
new visible text belongs to the four requested utility pages.

Before final delivery documentation, the implementation changed 266 unique
files:

- 236 existing sitemap HTML files for the shared asset cache-bust and, where a
  form exists, localized `_next` markup;
- four new localized `thank-you/index.html` files;
- `assets/main.js`;
- `.github/workflows/pages.yml`;
- `.env.example`, `.gitignore`, `data/leads/.gitignore` and `AGENTS.md`;
- the ten owning build modules or validators under `scripts/build/` plus
  `scripts/build/README.md`;
- `tools/leads_report.py`;
- four `worker/leads/` files and `worker/wrangler.toml`;
- `docs/CONTENT_TYPES.md`, `docs/OPEN_TASKS.md` and
  `docs/PROJECT_STATE.md`.

This report and `docs/CODEX_CHANGELOG.md` bring the final unique task scope to
268 files. No CSS, image, video, PDF, review snapshot, visible pre-existing
copy, sitemap content or page `lastmod` changed.

## Validation And Reproducibility

Local verification completed successfully:

```text
Lead Worker tests                   5/5 passed
SEO validator                      236 sitemap URLs passed
Brand validator                    7 page sets passed
Harley Hub validator               12 pages passed
Project validators                 all 14 registered projects passed
JavaScript syntax / Python compile passed
git diff --check                   passed
```

The required privacy assertion was break-tested before delivery: a temporary
Google Analytics runtime reference caused `validate_seo.py` to fail with the
file-specific cookie-free-measurement error, and the restored source passed.

The complete Full Safe Rebuild, including all page families and four pricing
PDFs, passed in the working repository. A separate full-history clone from
`https://github.com/PhilipGrishin/iron-moto-cascais.git` at `a286b68a` ran the
same workflow and all four validator groups, then reported zero
`git status --short` lines. A shallow-clone trial was intentionally not used as
validator evidence because the changelog validator correctly requires older
commit history.

GitHub Pages run `33665877221` successfully deployed the implementation. The
missing English artifact-directory finding was fixed by `a286b68a`; final
Pages run `33666134112` completed successfully and served all four utility
pages.
