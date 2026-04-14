#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
