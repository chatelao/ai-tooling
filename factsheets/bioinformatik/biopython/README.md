# Factsheet: Biopython

## Gruppe: Bioinformatik

## Zweck: Biopython ist eine Sammlung von frei verfügbaren Python-Werkzeugen für die biologische Datenverarbeitung (Bioinformatik), die Funktionen für Sequenzanalyse, Strukturdaten und Zugriff auf Online-Datenbanken bietet.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [Link](https://biopython.org/) |
| Wikipedia | [Link](https://en.wikipedia.org/wiki/Biopython) |

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install python3-biopython
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `example.fasta`
- `example.gbk`
- `example.pdb`
- `validate_biopython.py`
- `test1.fasta`
- `test2.fasta`
- `test3.fasta`
- `test4.fasta`
- `test5.fasta`

## Validierung

Führen Sie das Validierungsskript aus:

```bash
python3 examples/validate_biopython.py
```
