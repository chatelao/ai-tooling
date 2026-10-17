#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

lilypond --version
lilypond --pdf --png -o examples/rendered_score examples/symphony_theme.ly
