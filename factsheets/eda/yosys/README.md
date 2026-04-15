# Factsheet: Yosys

## Gruppe: EDA

## Zweck: Framework für Verilog RTL-Synthese

Yosys ist ein Open-Source-Framework für Verilog-RTL-Synthese. Es bietet eine
umfangreiche Suite von Tools zum Transformieren, Analysieren und Optimieren von
Hardware-Beschreibungen.


## Reifegrad

Stabil




## Technische Schulden

Gering




## Erwartetes Lebensende

Kein EOL bekannt




## Installation (Ubuntu 24.04)

```bash
sudo apt install yosys
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `synth.ys`: Yosys-Skript für eine grundlegende Synthese.
- `counter.v`: Ein einfaches Verilog-Zähler-Modul.
- `params.v`: Verilog-Beispiel mit Parametern zur Demonstration der
  Generierung.
- `techmap.v`: Beispiel für ein Technology Mapping Modul.
- `json_export.ys`: Skript zum Exportieren des synthetisierten Designs als
  JSON.

## Validierung

Yosys-Version prüfen:

```bash
yosys -V
```
