#!/bin/bash
set -e
cd "$(dirname "$0")"

xmllint --noout examples/valid.xml
xmllint --schema examples/schema.xsd examples/data_to_validate.xml --noout
