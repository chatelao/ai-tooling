#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

PYTHONPATH=/usr/lib/python3/dist-packages xvfb-run -a carla --version
