#!/bin/bash
set -e
cd "$(dirname "$0")"

curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
