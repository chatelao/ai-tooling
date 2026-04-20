#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

sudo DEBIAN_FRONTEND=noninteractive apt-get -y install -y maven
# Fix for duplicate plexus-classworlds jar in Ubuntu 24.04
sudo rm -f /usr/share/maven/boot/plexus-classworlds-2.x.jar
