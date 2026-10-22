#!/usr/bin/env bash
set -euo pipefail

# Installation script for Carla
sudo apt-get update && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y carla xvfb
