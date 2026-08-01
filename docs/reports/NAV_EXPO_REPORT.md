# NAV+EXPO Final Report

Date: 2026-08-01 (Europe/Lisbon)

Status: **confirmed complete**

Implementation commit: `6a2bdff72ba36b34906571d33f7a14c83f0c419a`

Production deployment:

- GitHub Pages workflow:
  `https://github.com/dreamcarua/iron-moto-cascais/actions/runs/30710734079`
- Result: success, deploy job completed in 41 seconds.
- Production cache-bypass token: `?navexpo=6a2bdff7`.
- Rich Results Test:
  `https://search.google.com/test/rich-results/result?id=t7AO4jGtQjTcFgYkw3MtpQ`

## Requested Scope

1. Add Cocktail to the desktop and mobile Projects menus on all 216 sitemap
   pages, with localized URLs and the same order as `/projects/`.
2. Remove the duplicate hard-coded menu inventory by deriving both menus from
   `new_pages_data.py` `PROJECT_TILES`.
3. Add a sitemap-wide validator assertion that fails on the prior output and
   passes after regeneration.
4. Apply the approved 36 exact replacements for Sturmvogel, Beckman and Hell
   Boy in four languages, rebuild the 12 details, and move only their 12
   sitemap dates.

## Confirmed Inputs

- Approved external source:
  `/Users/philipgrishin/Documents/Co-Work SEO/2026-08-01_exhibition-updates_3-projects_4lang.md`
- Source SHA-256:
  `58dd5215e299c2a111cb18f5149e2517b05d99b7ed394e2993cdbbb41ea55972`
- Source filesystem creation/modification timestamp:
  `2026-08-01T17:04:58+01:00`.
- Owner-confirmed fact: Sturmvogel, Beckman and Hell Boy are in the permanent
  exhibition beside the rider lounge at the Iron Custom Motors workshop.
- The approved file explicitly required 36 `CURRENT` to `REPLACE WITH`
  operations: 3 projects x 4 languages x 3 edits.

## Root Cause And Systemic Fix

`/projects/` already rendered 12 entries from `PROJECT_TILES`, including
Cocktail. `site_chrome.py` maintained a separate hard-coded list with only the
previous 11 projects. Desktop and mobile both consumed that stale list, so the
same omission propagated consistently to every page.

The fix makes `PROJECT_NAV_LINKS` derive slug, label and order from
`PROJECT_TILES`. There is now one project-listing registry for the portfolio
and both menu variants. `validate_seo.py --check-project-navigation` compares
the exact expected registry sequence, including the language-local URL, on
every sitemap page.

The same task exposed an incompatible sitemap rule: `/projects/` inherited the
maximum modification date of any detail page even when the listing itself did
not change. That rule was removed. The listing now follows semantic history of
its own `<main>` content, while each project detail continues to use its
explicit source-backed date.

## Required Red And Green Assertion Evidence

The first attempted invocation with the system interpreter stopped before the
assertion because that interpreter did not contain `beautifulsoup4`. It is not
counted as red evidence. The repository virtual environment from
`requirements.txt` was then used for both recorded runs.

Before the menu fix, against the HTML at prior `HEAD` `31f66728`:

```text
Project navigation validation failed: 216 page mismatch(es) across 216 sitemap page(s); 12 registered project(s) expected
  - https://ironcustommotors.com/: project navigation registry mismatch: desktop has 12 link(s), expected 13; mobile has 12 link(s), expected 13
  - https://ironcustommotors.com/ru/: project navigation registry mismatch: desktop has 12 link(s), expected 13; mobile has 12 link(s), expected 13
  - https://ironcustommotors.com/uk/: project navigation registry mismatch: desktop has 12 link(s), expected 13; mobile has 12 link(s), expected 13
  - https://ironcustommotors.com/pt/: project navigation registry mismatch: desktop has 12 link(s), expected 13; mobile has 12 link(s), expected 13
  - https://ironcustommotors.com/motorcycle-service/: project navigation registry mismatch: desktop has 12 link(s), expected 13; mobile has 12 link(s), expected 13
  - https://ironcustommotors.com/ru/motorcycle-service/: project navigation registry mismatch: desktop has 12 link(s), expected 13; mobile has 12 link(s), expected 13
  - https://ironcustommotors.com/uk/motorcycle-service/: project navigation registry mismatch: desktop has 12 link(s), expected 13; mobile has 12 link(s), expected 13
  - https://ironcustommotors.com/pt/motorcycle-service/: project navigation registry mismatch: desktop has 12 link(s), expected 13; mobile has 12 link(s), expected 13
  - ... 208 more page mismatch(es)
```

After the generator fix and full regeneration:

```text
Project navigation validation passed: 216 sitemap page(s); 12 registered project(s); desktop and mobile order match
```

## Exact Exhibition Replacement Evidence

The source file was parsed by project and language. Before mutation, every
`CURRENT` block occurred exactly once in its target `main_html`. The JSON was
loaded with `json.load`, changed with one bounded `str.replace` per approved
pair, and serialized with `json.dump(..., ensure_ascii=False, indent=2)`.
The 12 visible-text hashes were then regenerated.

Each current `main_html` was compared with the prior committed JSON after
applying only its three approved replacements:

| Project/language | Approved replacements | Exact transformed HTML | Visible hash |
|---|---:|---|---|
| Beckman EN | 3 | match | match |
| Beckman PT | 3 | match | match |
| Beckman RU | 3 | match | match |
| Beckman UK | 3 | match | match |
| Hell Boy EN | 3 | match | match |
| Hell Boy PT | 3 | match | match |
| Hell Boy RU | 3 | match | match |
| Hell Boy UK | 3 | match | match |
| Sturmvogel EN | 3 | match | match |
| Sturmvogel PT | 3 | match | match |
| Sturmvogel RU | 3 | match | match |
| Sturmvogel UK | 3 | match | match |

The generated HTML comparison reported:

```text
changed_html=216
main_markup_changed=12 exact_expected=True
main_text_changed=12 exact_expected=True
unexpected_main_markup=[]
missing_expo_main_markup=[]
```

For all 12 target pages, the `<main>` differences are limited to the approved
new exhibition section, Context card 03, and CTA subline. Hell Boy's first
replacement also contains the approved corrected final history paragraph.
Full-page visible text additionally gains the two required Cocktail menu
labels, once in desktop chrome and once in mobile chrome. The other 204 page
`<main>` elements are byte-equivalent after parsing and have identical visible
text.

## Sitemap And Scope Evidence

- Changed sitemap HTML files: exactly 216, which is the complete sitemap
  inventory.
- Changed visible `<main>` content: exactly the 12 exhibition pages.
- Sitemap URL sets before and after: identical, 216 URLs.
- Changed `lastmod` values: exactly 12, all moved to
  `2026-08-01T17:04:58+01:00`.
- The four `/projects/` listing dates remained unchanged because its visible
  listing did not change.
- `llms.txt` remained byte-identical.
- `assets/main.css`, `assets/main.js` and all cache-bust values remained
  unchanged.
- `assets/main.css` SHA-256:
  `672913fd3bc5f04ed52a4770b43c34e5b4e9bb202c0462ce7e45bf0449ca590c`.
- `assets/main.js` SHA-256:
  `6ce25247ca13a5e2c2d1764a9755775ae5c9d2dce5c69e0bd0e98bfd0922bf61`.
- New sitemap SHA-256:
  `cc093c122b6225d2ec39a286cf9164ec614bac910ae6a95d87bb06b7ab2f935c`.

The 12 changed sitemap entries were EN/PT/RU/UK variants of:

- `/projects/sturmvogel/`
- `/projects/beckman/`
- `/projects/hellboy/`

No non-HTML runtime asset changed. Some generated HTML also has canonical
attribute ordering or line serialization inside shared chrome/head output;
this is non-visible serialization from the documented full build. The strict
`<main>` and visible-text comparisons above protect the requested content
scope.

## Changed Maintained Files

Implementation commit `6a2bdff7` changed:

- all 216 sitemap HTML files for shared project navigation;
- the 12 target project HTML files additionally for approved visible content;
- `content/projects/legacy_projects_4lang.json`;
- `scripts/build/site_chrome.py`;
- `scripts/build/validate_seo.py`;
- `scripts/build/project_pages_data.py`;
- `scripts/build/build_sitemap.py`;
- `scripts/build/validate_project_pages.py`;
- `scripts/build/README.md`;
- `docs/CONTENT_TYPES.md`;
- `sitemap.xml`.

The final evidence follow-up adds this report plus current-state and changelog
documentation. No CSS, JavaScript, image, PDF, cache-bust or discovery-index
file changed.

## Repository Validation

The four validator groups produced:

```text
SEO validation passed: 216 sitemap URL(s)
Brand page validation passed: 7 brand page set(s).
Harley Hub validation passed: 12 pages and all required integrations
OK: beckman project page passed multilingual copy, media, schema, cache-bust, redirect and integration checks
OK: burly project page passed multilingual copy, media, schema, cache-bust, redirect and integration checks
OK: cocktail project page passed multilingual copy, media, schema, cache-bust, redirect and integration checks
OK: fighter project page passed multilingual copy, media, schema, cache-bust, redirect and integration checks
OK: geometric project page passed multilingual copy, media, schema, cache-bust, redirect and integration checks
OK: hellboy project page passed multilingual copy, media, schema, cache-bust, redirect and integration checks
OK: inspirium project page passed multilingual copy, media, schema, cache-bust, redirect and integration checks
OK: joker project page passed multilingual copy, media, schema, cache-bust, redirect and integration checks
OK: quanta-r project page passed multilingual copy, media, schema, cache-bust, redirect and integration checks
OK: sturmvogel project page passed multilingual copy, media, schema, cache-bust, redirect and integration checks
OK: true-religion project page passed multilingual copy, media, schema, cache-bust, redirect and integration checks
OK: unbreakable project page passed multilingual copy, media, schema, cache-bust, redirect and integration checks
```

JavaScript syntax checks, Python compilation and `git diff --check` also
passed. Two consecutive complete rebuilds in the implementation worktree
produced the same binary diff SHA-256:
`7be63602947706071860c7e7c3b03110358fc43eeb841305b25bc83d6a84180b`.

A separate no-hardlink clone of `6a2bdff7` ran the documented Full Safe
Rebuild and all four validator groups. Its final `git status --short` was
empty.

## Production And Rich Results Evidence

After successful workflow `30710734079`, a concurrent cache-bypass check read
all 216 production URLs:

```text
production_urls_checked=216
status_200=216
desktop_registry_match=216
mobile_registry_match=216
bad=[]
exhibition_pages_checked=12
exact_exhibition_heading=12
failures=[]
```

The production sitemap returned 200 and was byte-identical to the committed
sitemap.

Google Rich Results Test result `t7AO4jGtQjTcFgYkw3MtpQ` crawled
`/projects/beckman/?navexpo=6a2bdff7` successfully on 2026-08-01 at 18:40:02
and reported four valid items. Separate type views confirmed:

| Type | Valid | Warnings | Errors |
|---|---:|---:|---:|
| Article | 1 | 0 | 0 |
| Breadcrumbs | 1 | 0 | 0 |
| LocalBusiness | 1 | 0 | 0 |
| Organization | 1 | 0 | 0 |

## Acceptance Conclusion

1. **Passed:** Cocktail and all 12 registered projects appear in localized,
   ordered desktop and mobile menus on 216/216 production pages.
2. **Passed:** the new assertion has both required red and green evidence.
3. **Passed:** all 36 approved replacements are exact; only the intended 12
   project `<main>` elements changed.
4. **Passed:** sitemap membership is unchanged and only 12 target dates moved.
5. **Passed:** chrome parity, all four validator groups and external Rich
   Results validation are clean.
6. **Passed:** changed files stay inside HTML/shared navigation/project source,
   sitemap/validators and documentation; CSS/JS/cache-bust are unchanged.
7. **Passed:** the complete documented rebuild leaves a clean clone.
