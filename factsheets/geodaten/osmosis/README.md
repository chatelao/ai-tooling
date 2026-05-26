# Factsheet: Osmosis

## Gruppe: Geodaten

## Zweck: Osmosis ist eine Java-Anwendung zur Verarbeitung von OpenStreetMap-Daten

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 0.49.2 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [wiki.openstreetmap.org/wiki/Osmosis](https://wiki.openstreetmap.org/wiki/Osmosis) |
| Wikipedia | [en.wikipedia.org/wiki/Osmosis_(software](https://en.wikipedia.org/wiki/Osmosis_(software)) |

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install -y osmosis
```

## Hello World

```bash
osmosis --help
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `simple_pipeline.xml`: Eine einfache Lese-Schreib-Pipeline.
- `tag_filter.xml`: Filtern von Objekten nach Tags (z.B. Restaurants).
- `bounding_box.xml`: Zuschneiden von Daten auf eine Bounding Box.
- `run_pipeline.sh`: Skript zum Ausführen einer XML-Pipeline.
- `merge_osm.sh`: Skript zum Zusammenführen zweier OSM-Dateien.

## Validierung

```bash
osmosis --help
```
