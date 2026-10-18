#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

pd -version
pd -nogui -noaudio -send "pd quit" -open examples/synth_engine.pd
