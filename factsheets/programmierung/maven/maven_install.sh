#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

sudo DEBIAN_FRONTEND=noninteractive apt-get -y update
sudo DEBIAN_FRONTEND=noninteractive apt-get -y install maven
# Fix für ClassNotFoundException: org.codehaus.plexus.classworlds.launcher.Launcher
sudo rm -f /usr/share/maven/boot/plexus-classworlds-2.x.jar
