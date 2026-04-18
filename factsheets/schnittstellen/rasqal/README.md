# Factsheet: Rasqal

## Gruppe: Schnittstellen

## Zweck

Rasqal ist eine C-Bibliothek, die das Parsen und Ausführen von SPARQL-Abfragen ermöglicht. Sie enthält das Kommandozeilenwerkzeug `roqet`.

## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Referenzhandbuch

[Link](https://librdf.org/rasqal/)

## Wikipedia

[Link](https://de.wikipedia.org/wiki/Rasqal)

## Installation (Ubuntu 24.04)

```bash
sudo apt install rasqal-utils
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `example.rq`: Eine einfache SPARQL-Abfrage.
- `data.ttl`: Eine Beispieldatei im Turtle-Format.

## Validierung

Abfrage lokal ausführen:

```bash
roqet -F turtle --data factsheets/schnittstellen/rasqal/examples/data.ttl factsheets/schnittstellen/rasqal/examples/example.rq
```
