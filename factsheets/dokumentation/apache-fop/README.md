# Factsheet: Apache fop

## Gruppe: Dokumentation

## Zweck: Apache-fop ist ein Werkzeug für

## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Wikipedia

[Link](https://de.wikipedia.org/wiki/Apache_FOP)

## Installation (Ubuntu 24.04)

```bash
sudo apt install fop libxalan2-java libxerces2-java libserializer-java
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `test.fo`
- `ex1.fo`
- `ex2.fo`
- `ex3.fo`
- `ex4.fo`

## Validierung

PDF generieren:

```bash
fop factsheets/dokumentation/apache-fop/examples/test.fo factsheets/dokumentation/apache-fop/examples/test.pdf
```
