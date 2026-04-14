#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

npx spectral lint examples/api.yaml --ruleset examples/.spectral.yaml
