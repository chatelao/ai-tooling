# Factsheet: Kibot

## Gruppe: Eda

## Zweck: KiBot ist ein Werkzeug zur Automatisierung von KiCad-Workflows, wie der Generierung von Fertigungsdaten.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [Link](https://github.com/INTI-CMNB/KiBot) |

## Installation (Ubuntu 24.04)

```bash
pip install kibot
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `config.kibot.yaml`
- `test.kicad_pcb`
- `test.kicad_sch`
- `out.yaml`
- `in.yaml`

## Validierung

KiBot ausführen:

```bash
kibot -v
```
