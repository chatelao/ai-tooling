# Factsheet: Inspectrum

## Gruppe: Funktechnik

## Zweck: Inspectrum ist ein Werkzeug zur visuellen Analyse von erfassten Funksignalen

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [github.com/miek/inspectrum](https://github.com/miek/inspectrum) |
| Wikipedia | [en.wikipedia.org/wiki/Software-defined_radio](https://en.wikipedia.org/wiki/Software-defined_radio) |

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install -y inspectrum
```

## Hello World

```bash
inspectrum --version
```

## Validierung

```bash
xvfb-run -a inspectrum -h 2>&1 | grep -i "Usage: inspectrum"
```
