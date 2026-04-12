#!/bin/bash
set -e
cd "$(dirname "$0")"

hexdump -C examples/data.bin
