#!/bin/bash
set -e
cd "$(dirname "$0")"

plantuml examples/test.puml
