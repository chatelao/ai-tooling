# Factsheet: JOSM

## Gruppe: Geodaten

## Zweck: JOSM ist ein Editor für die Erstellung und Bearbeitung von OpenStreetMap-Daten

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [Link](https://josm.openstreetmap.de/) |
| Wikipedia | [Link](https://de.wikipedia.org/wiki/JOSM) |

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install -y josm
```

## Hello World

```bash
josm --version
```

## Validierung

```bash
xvfb-run -a josm --help
```
