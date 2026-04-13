#!/bin/bash
set -e
cd "$(dirname "$0")"
export DEBIAN_FRONTEND=noninteractive

curl -L http://download.opensuse.org/repositories/home:/pbartfai/xUbuntu_24.04/amd64/ldview-osmesa_4.7-1_amd64.deb -o ldview.deb; sudo apt install -y ./ldview.deb
