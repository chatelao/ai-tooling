# Factsheet: Pymol

## Gruppe: Bioinformatik

## Zweck: PyMOL ist ein leistungsstarkes molekulares Grafiksystem zur Visualisierung und Erstellung hochwertiger 3D-Bilder von kleinen Molekülen und biologischen Makromolekülen wie Proteinen.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil (gepatched für Python 3.12 Kompatibilität) |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [Link](https://pymol.org/) |
| Wikipedia | [Link](https://de.wikipedia.org/wiki/PyMOL) |

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install pymol
# Patch PyMOL for Python 3.12 compatibility (remove 'imp' dependency)
sudo sed -i 's/^from imp import find_module/import importlib.util/' /usr/lib/python3/dist-packages/pymol/__init__.py
sudo sed -i "s/find_module('pymol')\[1\]/importlib.util.find_spec('pymol').submodule_search_locations[0]/" /usr/lib/python3/dist-packages/pymol/__init__.py
```

## Hello World

```python
import pymol
pymol.finish_launching()
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `protein.pdb`
- `script.pml`
- `ex1.pdb`
- `ex2.pdb`
- `ex3.pdb`

## Validierung

Starten Sie PyMOL:

```bash
xvfb-run -a /usr/bin/python3 -m pymol -c factsheets/bioinformatik/pymol/examples/protein.pdb
```
