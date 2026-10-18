#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

csound --version
csound -o examples/rendered_sample.wav examples/simple_sine.csd
