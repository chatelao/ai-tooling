#!/usr/bin/env bash
set -e

PYTHONPATH=/usr/lib/python3/dist-packages xvfb-run -a carla --version
