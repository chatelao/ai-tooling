#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

Xvfb :99 -screen 0 1024x768x24 &
