# Factsheet: Kibot

## Gruppe: Eda

## Zweck: KiBot ist ein Werkzeug zur Automatisierung von KiCad-Workflows, wie der Generierung von Fertigungsdaten.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 0.18.0 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [github.com/INTI-CMNB/KiBot](https://github.com/INTI-CMNB/KiBot) |

## Installation (Ubuntu 24.04)

```bash
pip install kibot
```

## Hello World

```bash
kibot --version
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
