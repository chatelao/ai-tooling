#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

sudo apt-get update && sudo apt-get install -y openjdk-21-jdk-headless wget unzip
wget https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_12.0.4_build/ghidra_12.0.4_PUBLIC_20260303.zip
unzip ghidra_12.0.4_PUBLIC_20260303.zip
