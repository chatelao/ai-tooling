# Factsheet: XMLStarlet

## Gruppe: Schnittstellen

## Zweck: XMLStarlet ist ein Toolkit zur XML-Verarbeitung von der Kommandozeile (Validierung, Abfrage, Transformation, Bearbeitung)

## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Wikipedia

[Link](https://de.wikipedia.org/wiki/XMLStarlet)

## Installation (Ubuntu 24.04)

```bash
sudo apt install xmlstarlet
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `catalog.xml`: Eine einfache XML-Datei mit Buchdaten.
- `books.xml`: Eine weitere XML-Datei für Abfragen.
- `inventory.xml`: Inventardaten zur Bearbeitung.
- `config.xml`: Konfigurationsbeispiel.
- `data.xml`: Allgemeine XML-Daten.

## Validierung

XML-Datei formatieren (Pretty Print):

```bash
xmlstarlet fo factsheets/schnittstellen/xmlstarlet/examples/catalog.xml
```

Elemente mit XPath abfragen:

```bash
xmlstarlet sel -t -v "/catalog/book/title" factsheets/schnittstellen/xmlstarlet/examples/catalog.xml
```
