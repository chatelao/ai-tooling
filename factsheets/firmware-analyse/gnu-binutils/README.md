# Factsheet: Gnu binutils

## Gruppe: Firmware/analyse

## Zweck: Gnu-binutils ist ein Werkzeug für


## Reifegrad

Stabil




## Technische Schulden

Gering




## Erwartetes Lebensende

Kein EOL bekannt




## Installation (Ubuntu 24.04)

```bash
sudo apt install binutils
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `test.o`
- `test.a`
- `test.elf`
- `test.bin`
- `symbols.txt`

## Validierung

Objektdatei-Info anzeigen:

```bash
objdump -h factsheets/firmware-analyse/gnu-binutils/examples/test.o
```
