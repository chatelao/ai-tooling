#!/bin/bash
set -e
cd "$(dirname "$0")"

npm install react react-dom
npx create-react-app my-app
