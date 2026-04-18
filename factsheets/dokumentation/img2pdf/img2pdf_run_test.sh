#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

img2pdf examples/*.jpg -o output.pdf
