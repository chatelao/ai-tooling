# Factsheet: osmium-tool

## Gruppe: Geodaten

## Zweck: Osmium-tool ist ein vielseitiges Werkzeug zur Verarbeitung von OpenStreetMap-Dateien

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 1.16.0 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [osmcode.org/osmium-tool](https://osmcode.org/osmium-tool/) |
| Wikipedia | [en.wikipedia.org/wiki/Osmium_(software](https://en.wikipedia.org/wiki/Osmium_(software)) |

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install -y osmium-tool
```

## Hello World

```bash
osmium --version
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `extract_area.sh`: Extraktion eines Bereichs mittels Bounding Box.
- `filter_amenities.sh`: Filtern von Objekten nach Tags.
- `inspect_file.sh`: Anzeigen von Dateiinformationen.
- `convert_format.sh`: Konvertierung zwischen OSM-Formaten.
- `show_history.sh`: Anzeigen der Objekthistorie.

## Validierung

```bash
osmium --version
```
