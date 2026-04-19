#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

docker pull container-registry.oracle.com/database/free:latest
