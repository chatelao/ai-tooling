#!/bin/bash
set -e
cd "$(dirname "$0")"

xmlstarlet fo examples/catalog.xml
xmlstarlet sel -t -v "/catalog/book/title" examples/catalog.xml
