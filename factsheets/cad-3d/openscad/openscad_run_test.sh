#!/bin/bash
set -e
cd "$(dirname "$0")"

openscad -o examples/out.png examples/test.scad
