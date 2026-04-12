#!/bin/bash
set -e
cd "$(dirname "$0")"

sudo apt update
sudo apt install python3-biopython
