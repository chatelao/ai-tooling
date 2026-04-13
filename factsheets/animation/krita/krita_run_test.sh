#!/bin/bash
set -e
cd "$(dirname "$0")"

xvfb-run -a krita --version
