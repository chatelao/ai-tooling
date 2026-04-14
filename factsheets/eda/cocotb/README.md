# Factsheet: cocotb

## Gruppe: EDA

## Zweck: Python-basiertes Verifikations-Framework für VHDL/Verilog RTL

cocotb ist ein Koroutinen-basiertes Co-Simulations-Verifikations-Framework für
das Testen von VHDL- und Verilog-Hardware-Designs mit Python.


## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Installation (Ubuntu 24.04)

```bash
pip install cocotb
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `adder.v`: Ein einfaches Verilog-Addierer-Modul.
- `test_adder.py`: cocotb-Testskript in Python für den Addierer.
- `Makefile`: Konfiguration für das Ausführen des Tests mit einem Simulator
  (z.B. Icarus Verilog).
- `coco_config.xml`: Beispiel für eine XML-Konfigurationsdatei.
- `runner.py`: Ein Python-Skript, das `cocotb.runner` verwendet, um Tests ohne
  externes Makefile zu starten.

## Validierung

cocotb-Installation prüfen:

```bash
pip show cocotb
```
