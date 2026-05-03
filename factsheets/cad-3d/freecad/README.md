# Factsheet: Freecad

## Gruppe: Cad/3d

## Zweck: FreeCAD ist ein quelloffener, parametrischer 3D-CAD-Modellierer zur Konstruktion realer Objekte.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [www.freecad.org](https://www.freecad.org/) |
| Wikipedia | [de.wikipedia.org/wiki/FreeCAD](https://de.wikipedia.org/wiki/FreeCAD) |

## Installation (Ubuntu 24.04)

```bash
sudo add-apt-repository ppa:freecad-maintainers/freecad-stable; sudo apt update; sudo apt install freecad
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `test.fcstd`
- `part1.step`
- `part2.step`
- `model.obj`
- `script.py`

## Validierung

Version prüfen:

```bash
xvfb-run -a freecad --version 2>&1 | grep -v "libEGL warning"
```
