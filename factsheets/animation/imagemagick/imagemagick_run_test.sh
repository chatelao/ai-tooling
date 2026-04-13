#!/bin/bash
set -e
cd "$(dirname "$0")"

convert -size 10x10 xc:white test_output.png
identify test_output.png
rm test_output.png
