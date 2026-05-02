# Factsheet: Gnu binutils

## Gruppe: Firmware/analyse

## Zweck: Die GNU Binutils sind eine Sammlung von Werkzeugen zur Manipulation von Objektdateien (z.B. ld, as, objdump, nm).

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [Link](https://www.gnu.org/software/binutils/) |
| Wikipedia | [Link](https://de.wikipedia.org/wiki/GNU_Binutils) |

## Installation (Ubuntu 24.04)

```bash
sudo apt install binutils
```

## Hello World

```bash
objdump -h file.o
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
