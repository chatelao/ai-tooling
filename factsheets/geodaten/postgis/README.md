# Factsheet: PostGIS

## Gruppe: Geodaten

## Zweck: PostGIS ist eine räumliche Datenbank-Erweiterung für PostgreSQL

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [postgis.net](https://postgis.net/) |
| Wikipedia | [de.wikipedia.org/wiki/PostGIS](https://de.wikipedia.org/wiki/PostGIS) |

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install -y postgis postgresql-16-postgis-3 gdal-bin
```

## Validierung

```bash
ogrinfo --version
```
