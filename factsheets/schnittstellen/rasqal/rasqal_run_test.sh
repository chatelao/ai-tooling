#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

roqet -F turtle --data examples/data.ttl examples/example.rq
