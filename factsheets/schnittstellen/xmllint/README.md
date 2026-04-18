# Factsheet: xmllint

## Gruppe: Schnittstellen

## Zweck: xmllint ist ein Werkzeug aus dem libxml2-Paket zur Validierung, Formatierung und Analyse von XML-Dateien

## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Referenzhandbuch

[Link](http://xmlsoft.org/xmllint.html)

## Wikipedia

[Link](https://de.wikipedia.org/wiki/Libxml2)

## Installation (Ubuntu 24.04)

```bash
sudo apt install libxml2-utils
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `valid.xml`: Eine valide XML-Datei.
- `invalid.xml`: Eine XML-Datei mit Syntaxfehlern.
- `schema.xsd`: Ein XML-Schema zur Validierung.
- `data_to_validate.xml`: XML-Daten, die gegen das Schema geprüft werden können.
- `formatted.xml`: Beispiel für eine formatierte XML-Ausgabe.

## Validierung

XML-Datei auf Wohlgeformtheit prüfen:

```bash
xmllint --noout factsheets/schnittstellen/xmllint/examples/valid.xml
```

XML gegen XSD-Schema validieren:

```bash
xmllint --schema factsheets/schnittstellen/xmllint/examples/schema.xsd factsheets/schnittstellen/xmllint/examples/data_to_validate.xml --noout
```
