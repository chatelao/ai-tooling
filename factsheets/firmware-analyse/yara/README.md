# Factsheet: Yara

## Gruppe: Firmware/analyse

## Zweck: Yara ist ein Werkzeug für

## Installation (Ubuntu 24.04)

```bash
sudo apt install yara
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `rule.yar`
- `test.bin`
- `malware.bin`
- `clean.bin`
- `sample.bin`

## Validierung

YARA-Regel anwenden:

```bash
yara factsheets/firmware-analyse/yara/examples/rule.yar factsheets/firmware-analyse/yara/examples/test.bin
```
