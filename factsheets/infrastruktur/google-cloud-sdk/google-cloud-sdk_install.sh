#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

curl https://sdk.cloud.google.com | bash
# exec -l $SHELL (skipped in automated script)
gcloud init
