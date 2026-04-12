#!/bin/bash
set -e
cd "$(dirname "$0")"

curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | BINDIR=$HOME/.local/bin sh
