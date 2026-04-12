#!/bin/bash
set -e
cd "$(dirname "$0")"

stepci run examples/workflow.yml
