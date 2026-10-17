#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

fluidsynth --version
fluidsynth -ni /usr/share/sounds/sf2/FluidR3_GM.sf2 examples/mozart_k545.mid -F examples/rendered_sample.wav -r 44100
