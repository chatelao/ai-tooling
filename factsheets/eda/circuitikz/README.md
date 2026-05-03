# Factsheet: Circuitikz

## Gruppe: Eda

## Zweck: CircuiTikZ ist ein LaTeX-Paket zur Erstellung von elektronischen Schaltkreisen mit TikZ.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [mirror.init7.net/ctan/graphics/pgf/contrib/circuitikz/doc/circuitikzmanual.pdf](https://mirror.init7.net/ctan/graphics/pgf/contrib/circuitikz/doc/circuitikzmanual.pdf) |
| Wikipedia | [de.wikipedia.org/wiki/PGF/TikZ](https://de.wikipedia.org/wiki/PGF/TikZ) |

## Installation (Ubuntu 24.04)

```bash
sudo apt install texlive-pictures
```

## Hello World

```latex
\begin{circuitikz}
\draw (0,0) to[R=1<\ohm>] (2,0);
\end{circuitikz}
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `test.tex`
- `ex1.tex`
- `ex2.tex`
- `ex3.tex`
- `ex4.tex`

## Validierung

LaTeX-Dokument kompilieren.
