#!/usr/bin/env bash
set -euo pipefail

# Run test script for Carla
echo "Testing Carla CLI..."
PYTHONPATH=/usr/lib/python3/dist-packages xvfb-run -a carla --version
