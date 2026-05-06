# Factsheet: Wavedrom

## Gruppe: Dokumentation

## Zweck: WaveDrom ist eine JavaScript-Engine zur Darstellung digitaler Zeitverlaufsdiagramme (Waveforms) aus einer JSON-basierten Textbeschreibung.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [wavedrom.com](https://wavedrom.com/) |

## Installation (Ubuntu 24.04)

```bash
npm install wavedrom
```

## Hello World

```json
{ "signal": [ { "name": "clk", "wave": "p....." } ] }
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `test.json`: Einfaches Taktsignal.
- `ex1.json`: SPI-Bus Transaktion mit MISO/MOSI und Select.
- `ex2.json`: I2C Schreibzyklus (vereinfacht).
- `ex3.json`: Taktsignal mit asynchronem Reset und Datenbus.
- `ex4.json`: Zustandsübergänge einer State Machine.

## Validierung

CLI-Version verwenden (falls installiert) oder Editor öffnen.
