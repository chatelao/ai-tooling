#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"
img2pdf examples/test1.jpg -o examples/test.pdf
