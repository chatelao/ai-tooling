#!/bin/bash
set -e
cd "$(dirname "$0")"
export DEBIAN_FRONTEND=noninteractive

sudo add-apt-repository ppa:kicad/kicad-10.0-releases; sudo apt update; sudo apt install -y --install-recommends kicad
