# Factsheet: Pymol

## Gruppe: Bioinformatik

## Zweck: Pymol ist ein Werkzeug für

## Reifegrad

Stabil (gepatched für Python 3.12 Kompatibilität)

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Referenzhandbuch

[Link](https://pymol.org/)

## Wikipedia

[Link](https://de.wikipedia.org/wiki/PyMOL)

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install pymol
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `protein.pdb`
- `script.pml`
- `ex1.pdb`
- `ex2.pdb`
- `ex3.pdb`

## Validierung

Starten Sie PyMOL:

```bash
xvfb-run -a /usr/bin/python3 -m pymol -c factsheets/bioinformatik/pymol/examples/protein.pdb
```
