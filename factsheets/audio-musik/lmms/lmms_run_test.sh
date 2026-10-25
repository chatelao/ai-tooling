#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

lmms render examples/beat.mmpz -o output.wav -f wav
