#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

sudo apt-get update
wget https://github.com/renode/renode/releases/download/v1.16.1/renode_1.16.1_amd64.deb
sudo apt-get install -y ./renode_1.16.1_amd64.deb
rm renode_1.16.1_amd64.deb
