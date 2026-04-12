#!/bin/bash
set -e
cd "$(dirname "$0")"

schemathesis run examples/api.yaml
