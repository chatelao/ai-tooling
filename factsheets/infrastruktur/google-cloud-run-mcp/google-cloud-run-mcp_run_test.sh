#!/bin/bash
set -e
cd "$(dirname "$0")"

npx -y @google-cloud/cloud-run-mcp --help
