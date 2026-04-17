# Factsheet: ChemFig

## Gruppe: Bioinformatik

## Zweck: ChemFig ist ein Werkzeug für

- das Zeichnen chemischer 2D-Strukturen direkt in LaTeX.
- die Erstellung von komplexen Molekülen, Mechanismen und Schemata.
- die Anpassung von Bindungswinkeln, Längen und Beschriftungen.

## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Wikipedia

[Link](https://de.wikipedia.org/wiki/LaTeX)

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install texlive-science
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `benzene.tex` - Ein einfaches LaTeX-Dokument zum Zeichnen von Benzol mit `chemfig`.

## Validierung

Kompilieren Sie das Beispiel mit `pdflatex`:

```bash
pdflatex factsheets/bioinformatik/chemfig/examples/benzene.tex
```
