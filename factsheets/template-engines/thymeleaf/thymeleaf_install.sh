#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

# Thymeleaf is typically used as a dependency in Java projects (e.g., Maven)
sudo DEBIAN_FRONTEND=noninteractive apt-get -y install -y maven
