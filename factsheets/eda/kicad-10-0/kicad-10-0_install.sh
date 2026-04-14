#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

sudo add-apt-repository ppa:kicad/kicad-10.0-releases; sudo DEBIAN_FRONTEND=noninteractive apt-get -y update; sudo DEBIAN_FRONTEND=noninteractive apt-get -y install --install-recommends kicad
