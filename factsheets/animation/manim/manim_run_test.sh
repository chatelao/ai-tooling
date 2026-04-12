#!/bin/bash
set -e
cd "$(dirname "$0")"

manim -ql examples/example.py SquareToCircle
