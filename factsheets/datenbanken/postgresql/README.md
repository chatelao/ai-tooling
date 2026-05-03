# Factsheet: PostgreSQL

## Gruppe: Datenbanken

## Zweck

PostgreSQL ist ein fortschrittliches, objekt-relationales Open-Source-Datenbankmanagementsystem (ORDBMS). Es zeichnet sich durch seine Zuverlässigkeit, Feature-Reichtum und die Einhaltung von SQL-Standards aus.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [www.postgresql.org/docs](https://www.postgresql.org/docs/) |
| Wikipedia | [de.wikipedia.org/wiki/PostgreSQL](https://de.wikipedia.org/wiki/PostgreSQL) |

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install postgresql
```

## Hello World

```sql
SELECT 'Hello World';
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `schema.sql`
- `data.sql`

## Validierung

```bash
psql --version
# Starten des Services (falls erforderlich)
sudo service postgresql start || sudo /etc/init.d/postgresql start
# Test-Abfrage als postgres-Benutzer
sudo -u postgres psql -c "SELECT 1;"
```
