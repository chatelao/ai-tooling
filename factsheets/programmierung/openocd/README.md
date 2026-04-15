# Factsheet: OpenOCD

## Gruppe: Programmierung

## Zweck: JTAG/SWD Debug-Lösung für Embedded-Geräte

Open On-Chip Debugger (OpenOCD) bietet Debugging-, systemnahe Programmierung und
Boundary-Scan-Tests für eingebettete Zielgeräte. Es unterstützt eine Vielzahl
von Hardware-Adaptern und Zielarchitekturen.


## Reifegrad

Stabil




## Technische Schulden

Gering




## Erwartetes Lebensende

Kein EOL bekannt




## Installation (Ubuntu 24.04)

```bash
sudo apt install openocd
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `openocd.cfg`: Beispiel für eine allgemeine Konfigurationsdatei.
- `gowin_tangnano4k.cfg`: Konfiguration für das Sipeed Tang Nano 4K Board.
- `stm32g4_swd.cfg`: Konfiguration für STM32G4-Mikrocontroller über SWD.
- `ft232r.cfg`: Interface-Konfiguration für FT232R-basierte
  USB-JTAG-Adapter.
- `jlink_swd.cfg`: Interface-Konfiguration für Segger J-Link Adapter im
  SWD-Modus.

## Validierung

OpenOCD-Version prüfen:

```bash
openocd --version
```
