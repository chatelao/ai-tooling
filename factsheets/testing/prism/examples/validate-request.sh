#!/bin/bash
# Validate a specific request against the API definition
curl -X POST http://127.0.0.1:4010/docs -H "Content-Type: application/json" -d '{"invalid": "data"}'
