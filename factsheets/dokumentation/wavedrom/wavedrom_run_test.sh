#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"
npx wavedrom-cli -i examples/test.json -s examples/test.svg
