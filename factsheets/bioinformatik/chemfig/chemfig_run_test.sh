#!/bin/bash
set -e
cd "$(dirname "$0")"

pdflatex examples/benzene.tex
