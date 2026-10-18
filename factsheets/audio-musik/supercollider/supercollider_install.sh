#!/usr/bin/env bash
set -euo pipefail

# Installation script for SuperCollider on Ubuntu 24.04 LTS
sudo apt-get update && sudo apt-get install -y --no-install-recommends supercollider-language supercollider-server
