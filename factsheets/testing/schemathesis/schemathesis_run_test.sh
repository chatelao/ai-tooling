#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

/usr/bin/python3 -m http.server 8080 > /dev/null 2>&1 & sleep 2; schemathesis run examples/api.yaml --url http://localhost:8080 || true; kill $! 2>/dev/null || true
