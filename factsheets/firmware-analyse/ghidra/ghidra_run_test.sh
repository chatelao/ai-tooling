#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

./ghidra_12.0.4_PUBLIC/support/analyzeHeadless . temp -noanalysis -deleteProject
