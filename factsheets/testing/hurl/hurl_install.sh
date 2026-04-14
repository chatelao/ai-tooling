#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

sudo add-apt-repository ppa:lepapareil/hurl; sudo DEBIAN_FRONTEND=noninteractive apt-get -y update; sudo DEBIAN_FRONTEND=noninteractive apt-get -y install hurl
