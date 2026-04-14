# Factsheet: Gnu toolchain for arm

## Gruppe: Programmierung

## Zweck: Gnu-toolchain-for-arm ist ein Werkzeug für


## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Installation (Ubuntu 24.04)

```bash
sudo apt install gcc-arm-none-eabi
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `main.c`
- `makefile`
- `startup.s`
- `linker.ld`
- `header.h`

## Validierung

Compiler prüfen:

```bash
arm-none-eabi-gcc --version
```
