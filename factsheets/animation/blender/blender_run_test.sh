#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

blender --background --python-expr "import bpy; print('Blender API works')"
