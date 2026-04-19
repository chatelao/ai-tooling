# Factsheet: MSSQL Express

## Gruppe: Datenbanken

## Zweck

Microsoft SQL Server Express ist eine kostenlos nutzbare Edition des relationalen Datenbankmanagementsystems von Microsoft. Sie ist ideal für das Erlernen, Entwickeln und den Betrieb kleinerer Serveranwendungen.

## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Referenzhandbuch

[Link](https://learn.microsoft.com/de-de/sql/sql-server/)

## Wikipedia

[Link](https://de.wikipedia.org/wiki/Microsoft_SQL_Server)

## Installation (Ubuntu 24.04)

```bash
curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | sudo gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg
curl -fsSL https://packages.microsoft.com/config/ubuntu/24.04/mssql-server-2025.list | sudo tee /etc/apt/sources.list.d/mssql-server-2025.list
sudo apt update
sudo apt install mssql-server
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `init.sql`

## Validierung

```bash
/opt/mssql/bin/mssql-conf --version
```
