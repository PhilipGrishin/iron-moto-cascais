#!/usr/bin/env bash
# Validate checked-in output without regenerating or fetching external data.
set -euo pipefail
cd "$(dirname "$0")/../.."

node --check assets/main.js
node --check assets/projects.js
node --check worker/reviews.js
node --check worker/leads/worker.mjs
node --test worker/leads/worker.test.mjs
python3 -m py_compile scripts/build/*.py
python3 scripts/build/validate_seo.py
python3 scripts/build/validate_brand_pages.py
python3 scripts/build/validate_harley_hub.py
python3 scripts/build/validate_service_custom_hubs.py
python3 scripts/build/validate_w4_routing.py
for slug in $(python3 -c "import sys; sys.path.insert(0, 'scripts/build'); from project_pages_data import PROJECT_CONFIGS; print(' '.join(sorted(PROJECT_CONFIGS)))"); do
  python3 scripts/build/validate_project_pages.py "$slug"
done
git diff --check
