#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

xsltproc examples/transform.xsl examples/source.xml
xsltproc -o examples/books.html examples/to_html.xsl examples/books.xml
