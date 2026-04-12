#!/bin/bash
set -e
cd "$(dirname "$0")"

blender --background --python-expr "import bpy; print('Blender API works')"
