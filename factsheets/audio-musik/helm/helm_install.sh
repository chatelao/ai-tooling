#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

curl -sL -o /tmp/helm.deb https://tytel.org/static/dist/helm_0.9.0_amd64_r.deb && sudo DEBIAN_FRONTEND=noninteractive apt-get update && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y /tmp/helm.deb && rm -f /tmp/helm.deb
