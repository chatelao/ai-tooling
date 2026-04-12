#!/bin/bash
set -e
cd "$(dirname "$0")"

npx @openapitools/openapi-generator-cli help
npx @openapitools/openapi-generator-cli list
