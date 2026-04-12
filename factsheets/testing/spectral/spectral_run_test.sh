#!/bin/bash
set -e
cd "$(dirname "$0")"

npx spectral lint examples/api.yaml --ruleset examples/.spectral.yaml
