#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo DEBIAN_FRONTEND=noninteractive apt-get -y install unzip
unzip awscliv2.zip
sudo ./aws/install
