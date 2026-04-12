#!/bin/bash
set -e
cd "$(dirname "$0")"

uvx awslabs.aws-api-mcp-server@latest --help
