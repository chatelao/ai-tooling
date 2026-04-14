#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

git clone https://github.com/e-m-b-a/emba.git
