# Factsheet: Jmol

## Gruppe: Bioinformatik

## Zweck: Jmol ist ein Open-Source-Java-Viewer für chemische Strukturen in 3D mit Funktionen für Moleküle, Kristalle, Materialien und Biomoleküle.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [jmol.sourceforge.net](https://jmol.sourceforge.net/) |
| Wikipedia | [de.wikipedia.org/wiki/Jmol](https://de.wikipedia.org/wiki/Jmol) |

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install jmol
```

## Hello World

```bash
jmol -n -g 100x100 -J "load $caffeine; write image hello.png"
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `molecule.pdb`
- `test.cif`
- `test.mol`
- `sample1.pdb`
- `sample2.pdb`

## Validierung

Starten Sie Jmol mit einer Beispieldatei:

```bash
jmol factsheets/bioinformatik/jmol/examples/molecule.pdb
```
