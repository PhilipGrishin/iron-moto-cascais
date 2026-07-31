# C8-FIX Report: Project Chrome Localization

Date: 2026-07-31

## Root Cause

- Status: **confirmed** by source inspection and a 33-page rendered-text diff.
- C8 changed project ownership from the generic `build_i18n.py` flow to direct
  rendering by `build_project_pages.py`.
- The direct renderer starts from the English Joker page and called
  `patch_navigation_footer()`. That helper rebuilt navigation lists and
  localized chrome links, but it did not replace the remaining `data-i18n`
  text in the cookie banner, sticky CTA, header/mobile CTAs or footer.
- `build_i18n.py` previously applied those strings through the shared
  translation dictionary. The replacement path omitted the equivalent call.
- The fix imports and calls `site_chrome.apply_global_i18n(soup, lang)` in the
  project generator before replacing the project-specific `<main>`. It uses
  the existing `scripts/build/i18n.json` source and adds no translations.

## Full Visible-Text Comparison

Method: for each of the 33 PT/RU/UK project pages, load the page at `affa9121`
with `git show`, remove non-rendered `script`, `style`, `template` and
`noscript` elements, collapse body-text whitespace, and compare the complete
result with the regenerated page. `<main>` was also compared independently.

Before the fix at `619d288d`:

- complete rendered body match: 0/33;
- rendered `<main>` match: 33/33;
- every project in one language had the same chrome-only difference pattern;
- affected maintained keys included `cookie.text`, `cookie.reject`,
  `cookie.accept`, `cta.bookService`, `cta.bookHeader`, `cta.whatsapp`,
  `footer.tagline`, `footer.col1`, `footer.col2`, `footer.col3`, `footer.hours`
  and `footer.rights`.

After the fix:

- complete rendered body match: 33/33;
- rendered `<main>` match: 33/33;
- intentional visible C8 differences remaining against `affa9121`: none;
- C8 head/schema changes and removal of inline translation payloads remain
  non-visible implementation differences.

The 11 English project pages already matched `affa9121` before the fix and
remain byte-identical to `619d288d`. All 8 noindex redirect stubs also remain
byte-identical to `619d288d`.

## Regression Assertion

`validate_seo.py` now collects every `data-i18n` string from the canonical
cookie banner, sticky CTA, WhatsApp action, desktop header, mobile drawer and
footer on every indexable page. It compares the ordered text signature with
the homepage of the same language. Required baseline keys explicitly include
cookie text/buttons, booking and WhatsApp CTAs, footer tagline and both main
footer group headings.

Negative run: validator code applied to the unchanged `619d288d` HTML before
the generator fix:

```text
SEO validation failed: 33 issue(s)
NEGATIVE_ASSERTION_EXIT=1
```

The 33 reported URLs were exactly 11 project slugs under each of `/ru/`,
`/uk/` and `/pt/`; no other page was reported.

Positive run after regeneration:

```text
SEO validation passed: 212 sitemap URL(s)
```

## Scope And Immutable Output

- Implementation commit: `52316a26`.
- Changed HTML: exactly 33 localized project details.
- Changed source: `build_project_pages.py` and `validate_seo.py`.
- Changed English project HTML: zero.
- Changed redirect stubs: zero.
- Changed other sitemap HTML: zero across the other 168 URLs.
- `sitemap.xml` and all 212 lastmod values are byte-identical; SHA-256:
  `4910de2803fdd535c37198cf27ed541c23e66be8bd53afe80466881261e54971`.
- `assets/main.css`, `assets/main.js`, `assets/projects.css` and
  `assets/projects.js` are unchanged. Their cache-bust values remain
  `20260724a` for main assets and `20260710b` for project assets.

## Local Verification

- SEO validation passed: 212 sitemap URLs, including the new chrome assertion.
- Brand page validation passed: 7 brand page sets.
- Harley Hub validation passed: 12 pages and all required integrations.
- Project validation passed for all 11 slugs in four languages.
- Maintained JavaScript syntax checks, Python compilation and
  `git diff --check` passed.
- The complete Full Safe Rebuild from `scripts/build/README.md` left a clean
  clone of `52316a26` with empty `git status --short`.

## Production Verification

Pending publication. Record the GitHub Pages workflow, cache-bypass query and
all 33 live chrome comparisons here after deployment.
