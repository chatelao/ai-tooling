#!/bin/bash
set -e
cd "$(dirname "$0")"

seqkit stats examples/data.fasta
