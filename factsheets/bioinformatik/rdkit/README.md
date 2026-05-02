# Factsheet: Rdkit

## Gruppe: Bioinformatik

## Zweck: RDKit ist eine Open-Source-Sammlung von Software für die Chemoinformatik und das maschinelle Lernen, die Funktionen für die Manipulation chemischer Strukturen und die Deskriptorberechnung bietet.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [Link](https://www.rdkit.org/) |
| Wikipedia | [Link](https://en.wikipedia.org/wiki/RDKit) |

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install python3-rdkit
```

## Hello World

```python
from rdkit import Chem
print(Chem.MolToSmiles(Chem.MolFromSmiles('C')))
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `molecules.smi`
- `validate_rdkit.py`
- `mol1.mol`
- `mol2.mol`
- `mol3.mol`
- `mol4.mol`
- `mol5.mol`

## Validierung

Führen Sie das Validierungsskript aus:

```bash
python3 examples/validate_rdkit.py
```
