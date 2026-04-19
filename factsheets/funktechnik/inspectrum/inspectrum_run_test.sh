#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

xvfb-run -a inspectrum -h 2>&1 | grep -i "Usage: inspectrum"
