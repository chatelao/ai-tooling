#!/bin/bash
set -e
cd "$(dirname "$0")"

binwalk examples/firmware.bin
