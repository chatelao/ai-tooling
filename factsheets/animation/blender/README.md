# Factsheet: Blender

## Gruppe: Animation

## Zweck: Blender ist ein Werkzeug für

## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Wikipedia

[Link](https://de.wikipedia.org/wiki/Blender_(Software))

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install blender
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `cube.obj`
- `test.py`
- `scene.blend`
- `model1.obj`
- `model2.obj`
- `model3.obj`

## Validierung

Führen Sie Blender im Hintergrund aus:

```bash
blender --background --python-expr "import bpy; print('Blender API works')"
```
