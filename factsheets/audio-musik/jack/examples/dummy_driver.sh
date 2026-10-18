#!/bin/bash
# Script demonstrating headless JACK audio server startup using the dummy driver
set -e

echo "Starting JACK daemon in dummy driver mode..."
jackd -d dummy -r 48000 -p 512 &
JACK_PID=$!

sleep 2

if kill -0 $JACK_PID 2>/dev/null; then
    echo "JACK daemon running successfully (PID: $JACK_PID)."
    kill $JACK_PID
    wait $JACK_PID 2>/dev/null || true
    echo "JACK daemon stopped."
else
    echo "Failed to start JACK daemon."
    exit 1
fi
