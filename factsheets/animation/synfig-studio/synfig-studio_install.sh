#!/bin/bash
set -e
cd "$(dirname "$0")"

sudo apt update
DEBIAN_FRONTEND=noninteractive sudo apt install -y synfigstudio synfig
