#!/bin/bash
set -e
cd "$(dirname "$0")"
export DEBIAN_FRONTEND=noninteractive

sudo apt update
sudo apt install -y ffmpeg libcairo2-dev libpango1.0-dev
pip install manim
