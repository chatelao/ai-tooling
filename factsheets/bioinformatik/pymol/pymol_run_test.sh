#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

PYTHONPATH=../../../scripts xvfb-run -a /usr/bin/python3 -m pymol -c examples/protein.pdb
