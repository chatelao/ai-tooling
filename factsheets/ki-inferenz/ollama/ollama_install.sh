#!/bin/bash
set -e
cd "$(dirname "$0")"
export DEBIAN_FRONTEND=noninteractive

curl -fsSL https://ollama.com/install.sh | sh
