# Factsheet: JOSM

## Gruppe: Geodaten

## Zweck: JOSM ist ein Editor für die Erstellung und Bearbeitung von OpenStreetMap-Daten

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [josm.openstreetmap.de](https://josm.openstreetmap.de/) |
| Wikipedia | [de.wikipedia.org/wiki/JOSM](https://de.wikipedia.org/wiki/JOSM) |

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install -y josm
```

## Hello World

```bash
josm --version
```

## Beispieldaten

Die folgenden `.osm` Beispieldaten befinden sich im Ordner `examples/`:

- `small_area.osm`: Ein einfacher Knoten für Berlin.
- `nodes_with_tags.osm`: Beispiele für Knoten mit Attributen (Bank, Mülleimer).
- `way_with_tags.osm`: Beispiel für einen Weg (Straße) mit Attributen.
- `relation_example.osm`: Beispiel für ein Multipolygon (Wiese).
- `changeset_dummy.osm`: Beispiel für eine `osmChange` Datei.

## Validierung

```bash
xvfb-run -a josm --help
```
