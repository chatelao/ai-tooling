# Factsheet: Binwalk

## Gruppe: Firmware/analyse

## Zweck: Binwalk ist ein Werkzeug für


## Reifegrad

Stabil




## Technische Schulden

Gering




## Erwartetes Lebensende

Kein EOL bekannt




## Installation (Ubuntu 24.04)

```bash
sudo apt install binwalk
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `firmware.bin`
- `test.bin`
- `image.bin`
- `data.bin`
- `old.bin`

## Validierung

Firmware-Image analysieren:

```bash
binwalk factsheets/firmware-analyse/binwalk/examples/firmware.bin
```
