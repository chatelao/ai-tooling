#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

python3 examples/test.py
echo "Pillow test passed: image created."
