# Factsheet: openFPGALoader

## Gruppe: EDA

## Zweck: Universelles Werkzeug zum Programmieren von FPGAs

openFPGALoader ist ein universelles Hilfsprogramm zum Programmieren von FPGAs.
Es unterstützt viele verschiedene FPGA-Hersteller (wie Xilinx, Altera, Lattice,
Gowin, Efinix, Anlogic) und verschiedene Programmierkabel (JTAG, USB).


## Reifegrad

Stabil




## Technische Schulden

Gering




## Erwartetes Lebensende

Kein EOL bekannt




## Installation (Ubuntu 24.04)

```bash
sudo apt install openfpgaloader
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `tangnano4k/led_blink.v`: Verilog-Code für ein LED-Blink-Beispiel auf dem
  Tang Nano 4K.
- `tangnano4k/pins.cst`: Constraints-Datei (Physical Constraints) für den
  Tang Nano 4K.
- `tangnano4k/Makefile`: Makefile zum Bauen (mit externen Tools) und Flashen.
- `tangnano4k/flash.sh`: Shell-Skript zum direkten Programmieren des
  Tang Nano 4K mit openFPGALoader.
- `generic_ice40.bin`: Beispiel-Bitstream für iCE40 FPGAs.
- `generic_ecp5.bit`: Beispiel-Bitstream für ECP5 FPGAs.

## Validierung

openFPGALoader-Version prüfen:

```bash
openfpgaloader --version
```
