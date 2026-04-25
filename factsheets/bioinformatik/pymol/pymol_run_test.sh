#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

xvfb-run -a /usr/bin/python3 -m pymol -c examples/protein.pdb
