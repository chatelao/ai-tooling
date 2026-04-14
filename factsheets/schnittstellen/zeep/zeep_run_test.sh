#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

/usr/bin/python3 -m zeep examples/service.wsdl
/usr/bin/python3 examples/client.py
