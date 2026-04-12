#!/bin/bash
set -e
cd "$(dirname "$0")"

sudo add-apt-repository ppa:freecad-maintainers/freecad-stable; sudo apt update; sudo apt install freecad
