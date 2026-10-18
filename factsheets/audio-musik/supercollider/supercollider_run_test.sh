#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

sclang -v
QT_QPA_PLATFORM=offscreen sclang examples/generative_drone.scd
test -s examples/rendered_buffer.wav
