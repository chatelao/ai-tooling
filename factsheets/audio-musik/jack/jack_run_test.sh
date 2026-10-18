#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

jackd --version
jackd -d dummy -r 44100 -p 1024 &
JACK_PID=$!
sleep 1
if kill -0 $JACK_PID 2>/dev/null; then
    kill $JACK_PID
    wait $JACK_PID 2>/dev/null || true
    echo "JACK test successful."
else
    echo "JACK test failed."
    exit 1
fi
