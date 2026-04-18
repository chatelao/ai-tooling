#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

curl -L https://github.com/fullstorydev/grpcurl/releases/download/v1.9.3/grpcurl_1.9.3_linux_x86_64.tar.gz -o grpcurl.tar.gz
tar -xvf grpcurl.tar.gz
sudo mv grpcurl /usr/local/bin/
rm grpcurl.tar.gz
