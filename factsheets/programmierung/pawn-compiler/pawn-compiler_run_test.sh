#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

# Pawn-Compiler ausführen.
pawncc examples/test.pwn -oexamples/test.amx
pawncc --version
