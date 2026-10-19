#!/usr/bin/env bash
set -euo pipefail

# Installation script for ZynAddSubFX
sudo apt-get update && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y zynaddsubfx zynaddsubfx-data
