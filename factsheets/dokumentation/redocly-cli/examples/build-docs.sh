#!/bin/bash
# Generate static HTML documentation
npx @redocly/cli build-docs api.yaml --output index.html
