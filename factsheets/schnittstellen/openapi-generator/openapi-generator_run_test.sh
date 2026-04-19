#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

npx @openapitools/openapi-generator-cli help
npx @openapitools/openapi-generator-cli list
