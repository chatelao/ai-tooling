#!/bin/bash
set -e
cd "$(dirname "$0")"

sudo apt update
sudo apt install ffmpeg libcairo2-dev libpango1.0-dev
pip install manim
