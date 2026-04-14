#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

uvx awslabs.aws-api-mcp-server@latest
