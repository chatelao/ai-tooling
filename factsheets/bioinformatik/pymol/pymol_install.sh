#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

sudo DEBIAN_FRONTEND=noninteractive apt-get -y update
sudo DEBIAN_FRONTEND=noninteractive apt-get -y install pymol

# Patch PyMOL for Python 3.12 compatibility (remove 'imp' dependency)
sudo sed -i 's/^from imp import find_module/import importlib.util/' /usr/lib/python3/dist-packages/pymol/__init__.py
sudo sed -i "s/find_module('pymol')\[1\]/importlib.util.find_spec('pymol').submodule_search_locations[0]/" /usr/lib/python3/dist-packages/pymol/__init__.py
