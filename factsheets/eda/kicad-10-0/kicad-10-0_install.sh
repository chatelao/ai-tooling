#!/bin/bash
set -e
cd "$(dirname "$0")"

sudo add-apt-repository ppa:kicad/kicad-10.0-releases; sudo apt update; sudo apt install --install-recommends kicad
