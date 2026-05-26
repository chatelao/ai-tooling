# Factsheet: osm2pgsql

## Gruppe: Geodaten

## Zweck: osm2pgsql ist ein Werkzeug zum Importieren von OpenStreetMap-Daten in eine PostgreSQL-Datenbank

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 1.11.0 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [osm2pgsql.org](https://osm2pgsql.org/) |
| Wikipedia | [en.wikipedia.org/wiki/Osm2pgsql](https://en.wikipedia.org/wiki/Osm2pgsql) |

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install -y osm2pgsql
```

## Hello World

```bash
osm2pgsql --version
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `default.style`: Standard-Style-Datei für die klassische Ausgabe.
- `flex-config.lua`: Lua-Konfiguration für den flexiblen Output-Modus.
- `import_pbf.sh`: Beispiel-Shell-Skript für einen Import-Vorgang.
- `minimal.lua`: Eine minimale Lua-Konfigurationsdatei.
- `custom.style`: Benutzerdefinierte Style-Datei für Gebäude und Straßen.

## Validierung

```bash
osm2pgsql --version
```
