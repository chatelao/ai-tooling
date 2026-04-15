# Factsheet: Gnu toolchain for arm

## Gruppe: Programmierung

## Zweck

Die GNU Toolchain for ARM (gcc-arm-none-eabi) ist eine Sammlung von Compilern,
Linkern und Utilities zum Erstellen von Software für ARM Cortex-M und Cortex-R
Mikrocontroller ("Bare-Metal"). Sie ist das Standardwerkzeug für die
Embedded-Entwicklung auf Linux-Systemen.


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
