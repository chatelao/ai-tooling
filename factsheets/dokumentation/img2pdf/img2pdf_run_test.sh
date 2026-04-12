#!/bin/bash
set -e
cd "$(dirname "$0")"

img2pdf examples/*.jpg -o output.pdf
