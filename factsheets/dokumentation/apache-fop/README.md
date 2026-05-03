# Factsheet: Apache fop

## Gruppe: Dokumentation

## Zweck: Apache FOP (Formatting Objects Processor) ist ein Java-basierter Print-Formatter, der XSL-Formatting-Objects (XSL-FO) in verschiedene Ausgabeformate wie PDF, PostScript oder PCL konvertiert.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [xmlgraphics.apache.org/fop](https://xmlgraphics.apache.org/fop/) |
| Wikipedia | [de.wikipedia.org/wiki/Apache_FOP](https://de.wikipedia.org/wiki/Apache_FOP) |

## Installation (Ubuntu 24.04)

```bash
sudo apt install fop
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
