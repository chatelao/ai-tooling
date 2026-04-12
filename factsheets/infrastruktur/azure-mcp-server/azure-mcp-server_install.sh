#!/bin/bash
set -e
cd "$(dirname "$0")"

uvx --from msmcp-azure azmcp server start
