#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

curl -L https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-cli/3.4.2/spring-boot-cli-3.4.2-bin.tar.gz -o spring-boot-cli.tar.gz
tar -xzf spring-boot-cli.tar.gz
sudo mv spring-3.4.2 /opt/spring-boot-cli
sudo ln -sf /opt/spring-boot-cli/bin/spring /usr/local/bin/spring
rm spring-boot-cli.tar.gz
