# Factsheet: Apache fop

## Gruppe: Dokumentation

## Zweck: Apache FOP (Formatting Objects Processor) ist ein Java-basierter Print-Formatter, der XSL-Formatting-Objects (XSL-FO) in verschiedene Ausgabeformate wie PDF, PostScript oder PCL konvertiert.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 2.9 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [xmlgraphics.apache.org/fop](https://xmlgraphics.apache.org/fop/) |
| Wikipedia | [de.wikipedia.org/wiki/Apache_FOP](https://de.wikipedia.org/wiki/Apache_FOP) |

## Installation (Ubuntu 24.04)

```bash
sudo apt install fop
```

## Hello World

```xml
<fo:block>Hello World</fo:block>
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `test.fo`: Grundlegendes XSL-FO Dokument.
- `ex1.fo`: Beispiel für eine formatierte Tabelle.
- `ex2.fo`: Beispiel für eine Aufzählungsliste.
- `ex3.fo`: Layout mit Kopf- und Fußzeile sowie Seitennummern.
- `ex4.fo`: Einbindung externer Grafiken.

## Validierung

PDF generieren:

```bash
fop factsheets/dokumentation/apache-fop/examples/test.fo factsheets/dokumentation/apache-fop/examples/test.pdf
```
