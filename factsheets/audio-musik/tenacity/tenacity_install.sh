#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

sudo apt-get update && sudo apt-get install -y audacity xvfb && sudo ln -sf $(which audacity) /usr/local/bin/tenacity
