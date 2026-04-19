#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

sudo DEBIAN_FRONTEND=noninteractive apt-get -y update
sudo DEBIAN_FRONTEND=noninteractive apt-get -y install -y libosmesa6
curl -L http://download.opensuse.org/repositories/home:/pbartfai/xUbuntu_24.04/amd64/ldview-osmesa_4.7-1_amd64.deb -o ldview.deb; sudo DEBIAN_FRONTEND=noninteractive apt-get -y install ./ldview.deb
