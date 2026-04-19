#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

xvfb-run -a freecad --version 2>&1 | grep -v "libEGL warning"
