#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

mkdir -p ~/.config/LDView && touch ~/.config/LDView/ldviewrc
xvfb-run -a ldview examples/model.ldr
