#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

pw-cli --version
pw-dot --version
dot -V
