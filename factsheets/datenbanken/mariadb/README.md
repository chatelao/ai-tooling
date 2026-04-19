# Factsheet: MariaDB

## Gruppe: Datenbanken

## Zweck

MariaDB ist eines der populärsten Open-Source-Relationalen Datenbankmanagementsysteme. Es wurde von den ursprünglichen Entwicklern von MySQL als Fork erstellt und ist als Drop-in-Ersatz konzipiert.

## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Referenzhandbuch

[Link](https://mariadb.org/documentation/)

## Wikipedia

[Link](https://de.wikipedia.org/wiki/MariaDB)

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install mariadb-server
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `setup.sql`
- `dump.sql`

## Validierung

```bash
mariadb --version
```
