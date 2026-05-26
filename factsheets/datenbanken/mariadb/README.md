# Factsheet: MariaDB

## Gruppe: Datenbanken

## Zweck

MariaDB ist eines der populärsten Open-Source-Relationalen Datenbankmanagementsysteme. Es wurde von den ursprünglichen Entwicklern von MySQL als Fork erstellt und ist als Drop-in-Ersatz konzipiert.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 11.5 |
| LTS | 11.4 (LTS) |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [mariadb.org/documentation](https://mariadb.org/documentation/) |
| Wikipedia | [de.wikipedia.org/wiki/MariaDB](https://de.wikipedia.org/wiki/MariaDB) |

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install mariadb-server
```

## Hello World

```sql
SELECT 'Hello World';
```

## Beispiele

Im Ordner `examples/` befinden sich verschiedene MariaDB-Beispiele:

1.  `setup.sql`: Grundlegende Tabellenerstellung.
2.  `dump.sql`: Beispiel für einen Datenbank-Dump.
3.  `insert_data.sql`: Einfügen von Testdaten.
4.  `complex_query.sql`: Eine JOIN-Abfrage mit Aggregation.
5.  `backup.sh`: Ein einfaches Backup-Skript mit `mysqldump`.

## Validierung

```bash
mariadb --version
```
