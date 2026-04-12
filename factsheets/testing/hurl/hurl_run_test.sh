#!/bin/bash
set -e
cd "$(dirname "$0")"

hurl examples/test.hurl
