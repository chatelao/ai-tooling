#!/usr/bin/env bash
set -euo pipefail

# Installation script for Carla
echo "Installing Carla and dependencies..."
sudo apt-get update && sudo apt-get install -y carla xvfb
echo "Carla installation complete."
