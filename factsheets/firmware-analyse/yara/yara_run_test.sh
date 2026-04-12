#!/bin/bash
set -e
cd "$(dirname "$0")"

yara examples/rule.yar examples/test.bin
