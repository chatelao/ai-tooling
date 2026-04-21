#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

/usr/bin/python3 -c "import jinja2; print(jinja2.__version__)"
