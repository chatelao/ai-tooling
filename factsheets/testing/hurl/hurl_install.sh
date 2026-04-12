#!/bin/bash
set -e
cd "$(dirname "$0")"

sudo add-apt-repository ppa:lepapareil/hurl; sudo apt update; sudo apt install hurl
