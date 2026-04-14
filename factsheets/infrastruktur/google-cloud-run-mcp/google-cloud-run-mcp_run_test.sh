#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

npx -y @google-cloud/cloud-run-mcp --help
