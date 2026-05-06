#!/bin/bash
set -e

# Healthcheck for a web service
if curl -f http://localhost:8080/health; then
  exit 0
else
  exit 1
fi
