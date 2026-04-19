#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

# Playwright-Test ausführen.
npx playwright --version
# npx playwright test examples/test.spec.js # might be too heavy/require browser
