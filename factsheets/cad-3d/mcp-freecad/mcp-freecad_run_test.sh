#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

cd mcp-freecad && /usr/bin/python3 mcp_server.py --help
