# Factsheet: Blender

## Gruppe: Animation

## Zweck: Blender ist eine freie, quelloffene 3D-Grafiksuite, die für die Modellierung, Animation, Simulation, Rendering und Videobearbeitung verwendet wird.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [www.blender.org](https://www.blender.org/) |
| Wikipedia | [de.wikipedia.org/wiki/Blender_(Software](https://de.wikipedia.org/wiki/Blender_(Software)) |

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install blender
```

## Hello World

```python
import bpy
bpy.ops.mesh.primitive_cube_add()
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
