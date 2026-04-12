#!/bin/bash
set -e
cd "$(dirname "$0")"

fop examples/test.fo examples/test.pdf
