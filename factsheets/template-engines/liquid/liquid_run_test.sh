#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

/usr/bin/ruby -e 'require "liquid"; puts Liquid::VERSION'
