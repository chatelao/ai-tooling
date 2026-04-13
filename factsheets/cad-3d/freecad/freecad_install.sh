#!/bin/bash
set -e
cd "$(dirname "$0")"
export DEBIAN_FRONTEND=noninteractive

sudo add-apt-repository ppa:freecad-maintainers/freecad-stable; sudo apt update; sudo apt install -y freecad
