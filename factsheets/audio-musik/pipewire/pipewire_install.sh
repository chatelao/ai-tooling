#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

sudo apt-get update && sudo apt-get install -y pipewire pipewire-bin pipewire-audio-client-libraries graphviz
