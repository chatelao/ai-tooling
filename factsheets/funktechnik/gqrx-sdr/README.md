# Factsheet: Gqrx SDR

## Gruppe: Funktechnik

## Zweck: Gqrx ist ein Open-Source-SDR-Empfänger mit grafischer Benutzeroberfläche

## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Referenzhandbuch

[Link](https://gqrx.dk/doc/user-manual)

## Wikipedia

[Link](https://en.wikipedia.org/wiki/Gqrx)

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install -y gqrx-sdr
```

## Validierung

```bash
xvfb-run -a gqrx -h 2>&1 | grep -i "Usage: gqrx"
```
