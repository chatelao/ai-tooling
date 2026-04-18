#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"
pdflatex -interaction=nonstopmode -output-directory=examples examples/test.tex
