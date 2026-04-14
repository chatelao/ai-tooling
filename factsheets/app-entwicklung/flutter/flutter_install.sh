#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

export PATH="$PATH:/opt/flutter/bin"
flutter doctor
