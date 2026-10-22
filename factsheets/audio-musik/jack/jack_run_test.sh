#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

jackd --version
jackd -d dummy -r 44100 -p 1024 &
JACK_PID=$! && sleep 1 && kill $JACK_PID
