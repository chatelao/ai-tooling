#!/bin/bash
set -e
cd "$(dirname "$0")"

python3 examples/validate_biopython.py
