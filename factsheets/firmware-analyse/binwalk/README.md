# Factsheet: Binwalk

## Gruppe: Firmware/analyse

## Zweck: Binwalk ist ein Werkzeug zur Analyse, Reverse Engineering und Extraktion von Firmware-Images.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [github.com/ReFirmLabs/binwalk](https://github.com/ReFirmLabs/binwalk) |
| Wikipedia | [en.wikipedia.org/wiki/Binwalk](https://en.wikipedia.org/wiki/Binwalk) |

## Installation (Ubuntu 24.04)

```bash
sudo apt install binwalk
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `firmware.bin`: Eine Beispieldatei mit GZIP-Signatur.
- `test.bin`: Ein ZIP-Archiv mit einer Textdatei.
- `image.bin`: Eine Beispieldatei mit PNG-Signatur.
- `data.bin`: Eine Beispieldatei mit ELF-Signatur (64-bit LSB executable).
- `old.bin`: Eine Beispieldatei mit JPEG-Signatur.

## Validierung

Firmware-Image analysieren:

```bash
binwalk factsheets/firmware-analyse/binwalk/examples/firmware.bin
```
