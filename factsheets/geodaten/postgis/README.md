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

## Hello World

```sql
SELECT PostGIS_Full_Version();
```

## Validierung

```bash
ogrinfo --version
```

## Beispiele

Im Ordner `examples/` befinden sich verschiedene PostGIS-Beispiele:

1.  `setup_postgis.sql`: Aktivierung der Erweiterung.
2.  `spatial_table.sql`: Erstellung einer Tabelle mit Geometriespalte und Index.
3.  `insert_geometries.sql`: Einfügen von Punkt-Daten (WGS84).
4.  `distance_calc.sql`: Berechnung der Entfernung zwischen Städten in Kilometern.
5.  `spatial_query.sql`: Umkreissuche mit `ST_DWithin`.
