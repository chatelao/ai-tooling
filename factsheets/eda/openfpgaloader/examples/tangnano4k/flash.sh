#!/bin/bash
# Program Tang Nano 4K using openFPGALoader
# Usage: ./flash.sh <bitstream_file.fs>

BITSTREAM=${1:-project.fs}

if [ ! -f "$BITSTREAM" ]; then
    echo "Error: Bitstream file $BITSTREAM not found."
    exit 1
fi

openFPGALoader -b tangnano4k "$BITSTREAM"
