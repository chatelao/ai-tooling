#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "Verifying SuperCollider installation..."
sclang -v

echo "Testing SuperCollider Non-Realtime Synthesis (NRT)..."
QT_QPA_PLATFORM=offscreen sclang examples/drone.scd

if [ -f "examples/rendered_drone.wav" ]; then
    echo "SuperCollider test completed successfully! Generated rendered_drone.wav"
else
    echo "Error: rendered_drone.wav was not generated."
    exit 1
fi
