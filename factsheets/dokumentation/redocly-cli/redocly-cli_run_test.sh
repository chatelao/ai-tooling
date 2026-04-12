#!/bin/bash
set -e
cd "$(dirname "$0")"

npx @redocly/cli lint examples/api.yaml
