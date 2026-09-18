#!/usr/bin/env bash
# Retained as a safe notice for old bookmarks and local command history.
set -euo pipefail
cat >&2 <<'NOTICE'
The initial repository bootstrap has been retired.
This script makes no changes. Do not reinitialize the existing repository.

Follow scripts/build/README.md: build locally, validate, review the diff,
commit and push to main. The Deploy GitHub Pages workflow publishes the
validated, checked-in public files. Verify the production URLs afterward.
NOTICE
exit 1
