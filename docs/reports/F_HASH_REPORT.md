# F-HASH Delivery Report

Date: 2026-08-22 (Europe/Lisbon)  
Status: **confirmed**  
Implementation commit: `5c010b49dea6d0b81742a5f63993e8ebe947c815`  
GitHub Pages workflow: `32566489805` (`success`)

## Requested Fix And Confirmed Scope

Every existing lead form now submits to the activated FormSubmit privacy
alias:

```text
https://formsubmit.co/c29ab5a6818b2926388e8978888304a2
```

Repository inspection corrected one premise of the task: the lead form does
not exist on every built page. It exists on exactly 120 of 241 tracked HTML
files: 30 route shapes in each of the four supported languages. Every one of
those 120 instances previously exposed the recipient email in its `action`,
and every one was changed. No other HTML contained a FormSubmit action.

The modal source is not a separate template, partial, data record or
JavaScript string. The checked-in HTML owns the form markup. Page-family
generators either preserve an existing modal or copy the language page chrome;
`assets/main.js` only attaches behavior to `#leadForm`. Repository-wide
case-insensitive searches found no recipient action in `scripts/build/`,
`content/`, JavaScript or other non-HTML source files. This ownership is now
documented in `scripts/build/README.md`.

The real delivery inbox remains unchanged in visible contact information,
`mailto` links, schema and canonical business facts. Only the FormSubmit
`action` value changed.

## Changed Files

The implementation commit changed exactly 123 files:

- 120 generated/served HTML files, each with one exact action-value
  substitution;
- `scripts/build/validate_seo.py`;
- `AGENTS.md`;
- `scripts/build/README.md`.

The 120 HTML files are the following 30 route shapes at the English root and
under each of `/pt/`, `/ru/` and `/uk/`:

```text
/
/about/
/authorized-dealer/
/authorized-dealer/c-way/
/blog/
/blog/front-fork-service-motorcycle-cascais/
/blog/harley-davidson-full-service-done-right/
/blog/motorcycle-brake-pad-replacement-cascais/
/blog/motorcycle-tyre-fitting-specialist-cascais/
/blog/revtech-110-oil-service-engine-gearbox-drive/
/blog/royal-enfield-bear-650-fork-oil-case-study/
/blog/royal-enfield-bear-650-scrambler-build/
/blog/tubeless-conversion-spoked-wheels/
/blog/tubeless-sealing-tape-failure/
/bmw-service/
/community/
/contact/
/ducati-service/
/faq/
/harley-service/
/honda-service/
/news/
/news/ericeira-kustom-fest-2026/
/news/lisbon-motorcycle-film-fest-2026-beckman/
/news/opens-new-workshop-in-cascais/
/projects/
/royal-enfield-service/
/services/
/suzuki-service/
/triumph-service/
```

Required delivery documentation adds `docs/PROJECT_STATE.md`,
`docs/CODEX_CHANGELOG.md` and this report after the implementation commit.
The final task therefore touches 126 unique files across its implementation
and documentation commits.

No CSS, JavaScript, cache-bust value, visible copy, schema, hidden form field,
`llms.txt`, sitemap URL or sitemap `lastmod` changed.

## Permanent Regression Assertion

`validate_seo.py` now enumerates every built `*.html` file, including HTML
outside the sitemap, parses every form action and rejects a FormSubmit action
containing `@`. The failure includes the offending repository-relative file.

The required break test temporarily restored the email action in
`index.html`. The validator failed with exit code 1 and this exact output:

```text
SEO validation failed: 1 issue(s)
  - index.html: FormSubmit form action exposes an email address; use the activated private alias
```

The alias was restored immediately. The subsequent green run reported:

```text
SEO validation passed: 232 sitemap URL(s)
```

## Form, Content And Search Evidence

Repository-wide checks after the complete Full Safe Rebuild reported:

```text
exposed recipient-action matches:     0
form pages:                            120
alias occurrences:                    120
maximum alias occurrences per page:   1
exact action-only HTML changes:        120/120
visible text identical:               241/241 HTML files
normalized forms identical:           120/120
```

The normalized form comparison replaced only the action value with a neutral
placeholder before byte comparison. It therefore also protects `_subject`,
`_template`, `_captcha`, `_honey` and the remaining form markup from accidental
changes.

Legitimate occurrences of the business email remain elsewhere by design. The
zero-match requirement applies to the exposed FormSubmit recipient URL, not to
visible business identity data.

## Sitemap Discipline

The markup-only change did not move any `lastmod`. `sitemap.xml` remained
byte-identical before the change, after the Full Safe Rebuild, in the clean
clone and in production:

```text
before      d0c0d98dc180f44a3d13cadc859c7f1c355c8999557c2a232b84855d87d22b82
after       d0c0d98dc180f44a3d13cadc859c7f1c355c8999557c2a232b84855d87d22b82
production  d0c0d98dc180f44a3d13cadc859c7f1c355c8999557c2a232b84855d87d22b82
```

## Repository Validators

The canonical Full Safe Rebuild and the separate Broad Verification both
completed successfully:

```text
SEO validation passed: 232 sitemap URL(s)
Brand page validation passed: 7 brand page set(s).
Harley Hub validation passed: 12 pages and all required integrations
OK: all 14 registered project slugs passed multilingual copy, media, schema, cache-bust, redirect and integration checks
```

JavaScript syntax checks, Python compilation and `git diff --check` also
passed.

## Reproducibility

A separate clean clone of implementation commit `5c010b49` ran the complete
documented Full Safe Rebuild, including all generated page families and the
four pricing PDFs. All four validator groups passed and the final
`git status --short` was empty.

## Production Verification

GitHub Pages workflow `32566489805` deployed the implementation commit
successfully. Unique cache-bypass requests then parsed all 120 production form
pages and confirmed:

```text
production form pages checked: 120
production form errors:        0
actions equal private alias:   120/120
actions containing @:          0
normalized form mismatches:    0
production sitemap identical:  True
```

The production check compared each complete normalized form with the local
repository version, not only the action string. This confirms that the hidden
fields and the rest of the form remained unchanged after deployment.
