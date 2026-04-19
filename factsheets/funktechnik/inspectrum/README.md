# Factsheet: Inspectrum

## Gruppe: Funktechnik

## Zweck: Inspectrum ist ein Werkzeug zur visuellen Analyse von erfassten Funksignalen

## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Referenzhandbuch

[Link](https://github.com/miek/inspectrum)

## Wikipedia

[Link](https://en.wikipedia.org/wiki/Software-defined_radio)

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install -y inspectrum
```

## Validierung

```bash
xvfb-run -a inspectrum -h 2>&1 | grep -i "Usage: inspectrum"
```
