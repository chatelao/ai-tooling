# Factsheet: Oracle Database Free

## Gruppe: Datenbanken

## Zweck

Oracle Database Free (ehemals Express Edition/XE) ist eine kostenlos nutzbare Edition der Oracle-Datenbank. Sie bietet den vollen Funktionsumfang der Oracle-Datenbank in einem kompakten Paket für Entwickler und kleine Unternehmen.

## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Referenzhandbuch

[Link](https://www.oracle.com/database/technologies/oracle-database-free-downloads.html)

## Wikipedia

[Link](https://de.wikipedia.org/wiki/Oracle_(Datenbank))

## Installation (Ubuntu 24.04)

Für Ubuntu 24.04 wird die Verwendung des offiziellen Docker-Images empfohlen, da keine nativen Debian-Pakete für diese Version bereitgestellt werden.

```bash
docker pull container-registry.oracle.com/database/free:latest
```

Alternativ finden Sie die Downloads für andere Linux-Distributionen hier:
[Download Link](https://www.oracle.com/database/technologies/oracle-database-free-downloads.html)

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `create_user.sql`

## Validierung

Prüfen des Docker-Images:

```bash
docker images container-registry.oracle.com/database/free
```
