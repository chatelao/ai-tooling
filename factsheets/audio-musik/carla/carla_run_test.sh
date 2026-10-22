#!/usr/bin/env bash
set -euo pipefail

# Test Script for Carla
PYTHONPATH=/usr/lib/python3/dist-packages xvfb-run -a carla --version
