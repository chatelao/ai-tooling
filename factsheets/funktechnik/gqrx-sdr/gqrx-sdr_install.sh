#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

sudo DEBIAN_FRONTEND=noninteractive apt-get -y update
sudo touch /etc/modules
sudo DEBIAN_FRONTEND=noninteractive apt-get -y install -y gqrx-sdr
