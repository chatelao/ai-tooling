#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

DEB_URL=$(curl -s https://api.github.com/repos/surge-synthesizer/surge/releases/tags/Nightly | grep -o 'https://[^"]*surge-xt-linux-x64-[^"]*\.deb' | head -n 1) && curl -sL -o /tmp/surge-xt.deb "$DEB_URL" && sudo DEBIAN_FRONTEND=noninteractive apt-get update && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y /tmp/surge-xt.deb && rm -f /tmp/surge-xt.deb
