#!/bin/bash
set -e
cd "$(dirname "$0")"

objdump -h examples/test.o
