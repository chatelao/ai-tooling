# Factsheet: xsltproc

## Gruppe: Schnittstellen

## Zweck

xsltproc ist ein Kommandozeilen-Werkzeug zur Anwendung von XSLT-Stylesheets auf XML-Dokumente.

## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Referenzhandbuch

[Link](http://xmlsoft.org/XSLT/xsltproc2.html)

## Wikipedia

[Link](https://en.wikipedia.org/wiki/Libxslt)

## Installation (Ubuntu 24.04)

```bash
sudo apt install xsltproc
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `source.xml`: Die XML-Quelldatei.
- `transform.xsl`: Das XSLT-Stylesheet für die Transformation.
- `books.xml`: Eine Liste von Büchern als Datenquelle.
- `to_html.xsl`: XSLT zur Umwandlung von Buchdaten in HTML.
- `params.xsl`: Beispiel für XSLT mit Parametern.

## Validierung

XML-Transformation durchführen:

```bash
xsltproc factsheets/schnittstellen/xsltproc/examples/transform.xsl factsheets/schnittstellen/xsltproc/examples/source.xml
```

XML in HTML umwandeln:

```bash
xsltproc -o factsheets/schnittstellen/xsltproc/examples/books.html factsheets/schnittstellen/xsltproc/examples/to_html.xsl factsheets/schnittstellen/xsltproc/examples/books.xml
```
