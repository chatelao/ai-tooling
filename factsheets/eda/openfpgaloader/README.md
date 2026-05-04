# Factsheet: openFPGALoader

## Gruppe: EDA

## Zweck: Universelles Werkzeug zum Programmieren von FPGAs

openFPGALoader ist ein universelles Hilfsprogramm zum Programmieren von FPGAs.
Es unterstützt viele verschiedene FPGA-Hersteller (wie Xilinx, Altera, Lattice,
Gowin, Efinix, Anlogic) und verschiedene Programmierkabel (JTAG, USB).

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [github.com/trabucayre/openFPGALoader](https://github.com/trabucayre/openFPGALoader) |

## Installation (Ubuntu 24.04)

```bash
sudo apt install openfpgaloader
```

## Hello World

```bash
openFPGALoader --version
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `tangnano4k/led_blink.v`: Verilog-Code für ein LED-Blink-Beispiel auf dem
- `ulx3s.bit` (ULX3S Board)
- `flea_fpga.bit` (FleaFPGA Board)
- `arty_a7.bit` (Arty A7 Board)
  Tang Nano 4K.
- `tangnano4k/pins.cst`: Constraints-Datei (Physical Constraints) für den
- `ulx3s.bit` (ULX3S Board)
- `flea_fpga.bit` (FleaFPGA Board)
- `arty_a7.bit` (Arty A7 Board)
  Tang Nano 4K.
- `tangnano4k/Makefile`: Makefile zum Bauen (mit externen Tools) und Flashen.
- `ulx3s.bit` (ULX3S Board)
- `flea_fpga.bit` (FleaFPGA Board)
- `arty_a7.bit` (Arty A7 Board)
- `tangnano4k/flash.sh`: Shell-Skript zum direkten Programmieren des
- `ulx3s.bit` (ULX3S Board)
- `flea_fpga.bit` (FleaFPGA Board)
- `arty_a7.bit` (Arty A7 Board)
  Tang Nano 4K mit openFPGALoader.
- `generic_ice40.bin`: Beispiel-Bitstream für iCE40 FPGAs.
- `generic_ecp5.bit`: Beispiel-Bitstream für ECP5 FPGAs.

## Validierung

openFPGALoader-Version prüfen:

```bash
openFPGALoader -V
```
