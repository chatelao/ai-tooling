# Factsheet: Freecad

## Gruppe: Cad/3d

## Zweck: FreeCAD ist ein quelloffener, parametrischer 3D-CAD-Modellierer zur Konstruktion realer Objekte.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 0.21.2 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [www.freecad.org](https://www.freecad.org/) |
| Wikipedia | [de.wikipedia.org/wiki/FreeCAD](https://de.wikipedia.org/wiki/FreeCAD) |

## Installation (Ubuntu 24.04)

```bash
sudo add-apt-repository ppa:freecad-maintainers/freecad-stable; sudo apt update; sudo apt install freecad
```

## Hello World

```python
import FreeCAD
FreeCAD.Console.PrintMessage("Hello World\n")
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `test.fcstd`: Beispiel für eine native FreeCAD-Projektdatei.
- `part1.step`: Exportiertes 3D-Modell im standardisierten STEP-Format.
- `part2.step`: Ein weiteres Beispielmodell im STEP-Format.
- `model.obj`: 3D-Geometriedaten im Wavefront OBJ-Format.
- `script.py`: Python-Skript zur automatisierten Erstellung von 3D-Objekten (Box und Zylinder) über die FreeCAD API.

## Validierung

Version prüfen:

```bash
xvfb-run -a freecad --version 2>&1 | grep -v "libEGL warning"
```
