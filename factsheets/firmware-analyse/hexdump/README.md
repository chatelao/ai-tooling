# Factsheet: Hexdump

## Gruppe: Firmware/analyse

## Zweck: Hexdump ist ein Werkzeug für


## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Installation (Ubuntu 24.04)

```bash
sudo apt install bsdextrautils
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `data.bin`
- `test.txt`
- `random.bin`
- `header.bin`
- `footer.bin`

## Validierung

Datei im Hex-Format anzeigen:

```bash
hexdump -C factsheets/firmware-analyse/hexdump/examples/data.bin
```
