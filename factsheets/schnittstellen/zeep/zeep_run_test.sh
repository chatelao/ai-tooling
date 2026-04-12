#!/bin/bash
set -e
cd "$(dirname "$0")"

python3 -m zeep examples/service.wsdl
python3 examples/client.py
