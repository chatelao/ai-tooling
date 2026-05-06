# Factsheet: ChemFig

## Gruppe: Bioinformatik

## Zweck

ChemFig ist ein leistungsstarkes LaTeX-Paket, das die Erstellung chemischer Strukturformeln und Reaktionsschemata mit einer intuitiven, pfadbasierten Syntax ermöglicht. Es ist das Standardwerkzeug für chemische Dokumentation in der LaTeX-Welt.

Hauptmerkmale:
- Zeichnen von 2D-Strukturen direkt im LaTeX-Dokument (basiert auf TikZ).
- Flexible Steuerung von Bindungswinkeln, Längen und Beschriftungen.
- Unterstützung für komplexe Ringe, Verzweigungen und Elektronendarstellungen.
- Erstellung ganzer Reaktionsmechanismen und Schemata.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [mirror.init7.net/ctan/macros/generic/chemfig/chemfig-en.pdf](https://mirror.init7.net/ctan/macros/generic/chemfig/chemfig-en.pdf) |
| Wikipedia | [de.wikipedia.org/wiki/LaTeX](https://de.wikipedia.org/wiki/LaTeX) |

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install texlive-science texlive-latex-extra texlive-fonts-recommended
```

## Hello World

```latex
\chemfig{H-O-H}
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `benzene.tex`: Ein einfaches LaTeX-Dokument zum Zeichnen von Benzol.
- `caffeine.tex`: Darstellung eines komplexeren Koffein-Moleküls.
- `glucose.tex`: Zeichnen einer Glucose-Struktur (Sesselform oder Kette).
- `macros.tex`: Beispiel für die Definition eigener chemischer Makros.
- `reaction.tex`: Darstellung eines chemischen Reaktionsschemas.

## Validierung

Kompilieren Sie das Beispiel mit `pdflatex`:

```bash
pdflatex factsheets/bioinformatik/chemfig/examples/benzene.tex
```
