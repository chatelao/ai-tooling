#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

sudo DEBIAN_FRONTEND=noninteractive apt-get -y install fop libxalan2-java libxerces2-java libserializer-java
