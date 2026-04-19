# Factsheet: Ghidra

## Gruppe: Firmware/analyse

## Zweck: Ghidra ist ein Werkzeug für

## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Referenzhandbuch

[Link](https://ghidra-re.org/)

## Wikipedia

[Link](https://de.wikipedia.org/wiki/Ghidra)

## Installation (Ubuntu 24.04)

```bash
sudo apt-get update && sudo apt-get install -y openjdk-21-jdk-headless wget unzip
wget https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_12.0.4_build/ghidra_12.0.4_PUBLIC_20260303.zip
unzip ghidra_12.0.4_PUBLIC_20260303.zip
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `project.gpr`
- `test.exe`
- `lib.so`
- `binary.bin`
- `code.c`

## Validierung

Ghidra headless Modus verifizieren:

```bash
./ghidra_12.0.4_PUBLIC/support/analyzeHeadless . temp -noanalysis -deleteProject
```
