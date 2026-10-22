#!/usr/bin/env bash
set -euo pipefail

# Test script for Carla
echo "Testing Carla installation..."
PYTHONPATH=/usr/lib/python3/dist-packages xvfb-run -a carla --version
echo "Carla test passed successfully."
