#!/bin/bash
set -e
cd "$(dirname "$0")"

export PATH="$PATH:/opt/flutter/bin"
flutter doctor
