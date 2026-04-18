#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"
export PYTHONPATH=$PYTHONPATH:/usr/lib/python3/dist-packages/
# Just print version and exit successfully
kibot --version
