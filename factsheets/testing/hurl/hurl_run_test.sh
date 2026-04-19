#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

hurl --version
# hurl examples/test.hurl # External dependency
