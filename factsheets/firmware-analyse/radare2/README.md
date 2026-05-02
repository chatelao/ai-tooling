# Factsheet: Radare2

## Gruppe: Firmware/analyse

## Zweck: Radare2 ist ein quelloffenes Framework für Reverse Engineering und die Analyse von Binärdateien.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [www.radare.org](https://www.radare.org/) |
| Wikipedia | [en.wikipedia.org/wiki/Radare2](https://en.wikipedia.org/wiki/Radare2) |

## Installation (Ubuntu 24.04)

```bash
sudo apt install radare2
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `test.bin`
- `script.r2`
- `data.txt`
- `lib.so`
- `main.exe`

## Validierung

Binärdatei öffnen:

```bash
r2 factsheets/firmware-analyse/radare2/examples/test.bin
```
