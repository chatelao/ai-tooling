#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

git clone https://github.com/jango-blockchained/mcp-freecad.git
cd mcp-freecad && pip install -r requirements.txt
