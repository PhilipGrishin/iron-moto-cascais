# S-REBUILD-W4b Completion Report

Date: 2026-09-07 (Europe/Lisbon)

## Delivery

- Baseline: `ab62874a`
- Implementation commit: `ff7c7e11e85fc4aa312471af3d868d36ca22d025`
- GitHub Pages workflow: `34163554738` (`success`)
- Cache key: `20260907b` -> `20260907c`
- Rollback: `git revert ff7c7e11e85fc4aa312471af3d868d36ca22d025`

The `pricing.eyebrow` year is now 2026 in the maintained `assets/main.js`
I18N map, generated `scripts/build/i18n.json`, and the four pre-rendered home
pages. The wording and middle-dot separator are otherwise unchanged.

## Public URLs

- `https://ironcustommotors.com/` — `Pricing · 2026`
- `https://ironcustommotors.com/pt/` — `Tabela de preços · 2026`
- `https://ironcustommotors.com/ru/` — `Прайс-лист · 2026`
- `https://ironcustommotors.com/uk/` — `Прайс-лист · 2026`

All four returned HTTP 200 after deployment. An interactive browser check
used the site's language control in the order EN -> PT -> RU -> UK -> EN; the
rendered eyebrow matched the approved 2026 string after every switch.

## Exact Scope

The implementation commit changes 253 files:

- 240 HTML files: four home pages contain the approved visible year change;
  the other 236 HTML files contain only the required shared cache-key bump.
- `assets/main.js` and extracted `scripts/build/i18n.json`.
- Seven existing generator cache-key sources and
  `scripts/build/validate_w4_routing.py`.
- `sitemap.xml`, `docs/OPEN_TASKS.md`, and `docs/PROJECT_STATE.md`.

An exact byte comparison against the baseline normalized only
`20260907c` -> `20260907b` in all 240 HTML files and the approved eyebrow
2026 -> 2025 substitution in the four homes. All 240 normalized files were
byte-identical; there were zero unexpected HTML differences. The completed
watchlist item was removed from `docs/OPEN_TASKS.md` and recorded in the
changelog.

## Required 2025 Grep

```text
index.html 1
pt/index.html 1
ru/index.html 1
uk/index.html 1
```

The sole match in each file is the factual 2025 workshop-move sentence in
`story.p3`:

```text
index.html:487: In 2025 we brought the workshop to Cascais...
pt/index.html:487: Em 2025 trouxemos o workshop para Cascais...
ru/index.html:487: В 2025 мы привезли мастерскую в Кашкайш...
uk/index.html:487: У 2025 ми привезли майстерню до Кашкайша...
```

## Sitemap Accounting

- URL count: 236
- Previous SHA-256: `d307cbc83053f44b22875d42362796d91d85c8a582fc9467c462574bf6c8d406`
- New SHA-256: `3d5e96e1f0cbf94c2cb44c05d92db04e8acbb6a4b73a873d9841a1a287d7796f`
- Exact `lastmod` changes: 4

```text
https://ironcustommotors.com/     2026-09-07T10:00:00+01:00 -> 2026-09-07T22:25:25+01:00
https://ironcustommotors.com/ru/  2026-09-07T10:00:00+01:00 -> 2026-09-07T22:26:19+01:00
https://ironcustommotors.com/uk/  2026-09-07T10:00:00+01:00 -> 2026-09-07T22:26:19+01:00
https://ironcustommotors.com/pt/  2026-09-07T10:00:00+01:00 -> 2026-09-07T22:26:19+01:00
```

The deployed sitemap is byte-identical to the committed file.

## Verification

- Full Safe Rebuild: passed locally.
- Clean-clone Full Safe Rebuild at the implementation commit: passed with an
  empty `git status --short`.
- `validate_seo.py`: passed, 236 sitemap URLs.
- `validate_brand_pages.py`: passed, seven brand sets.
- `validate_harley_hub.py`: passed, 12 pages.
- `validate_service_custom_hubs.py`: passed, 16 hubs and 52 trust strips.
- `validate_w4_routing.py`: passed, including the new exact localized eyebrow
  assertions.
- `validate_project_pages.py`: passed for all 14 project sets.
- JavaScript syntax and Python compilation checks: passed.
- `git diff --check`: passed.

The focused break test temporarily restored the Portuguese eyebrow to 2025.
The validator exited 1 with
`pt/index.html: pricing.eyebrow is not the approved 2026 copy`. The test
mutation was reverted and the validator then passed.

Production asset checks:

- `assets/main.js` SHA-256:
  `46dba812885c6617fc5b83625d0f6ed94e9a08a1ad7af92f32d2e179a21a6580`
  locally and on production.
- `sitemap.xml` SHA-256:
  `3d5e96e1f0cbf94c2cb44c05d92db04e8acbb6a4b73a873d9841a1a287d7796f`
  locally and on production.
