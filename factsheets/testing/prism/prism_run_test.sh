#!/bin/bash
set -e
cd "$(dirname "$0")"

npx prism mock examples/api.yaml
