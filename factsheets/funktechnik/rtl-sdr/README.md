# Factsheet: rtl-sdr

## Gruppe: Funktechnik

## Zweck: rtl-sdr ist ein Werkzeug für den Zugriff auf RTL2832U-basierte SDR-Empfänger

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [osmocom.org/projects/rtl-sdr/wiki/Rtl-sdr](https://osmocom.org/projects/rtl-sdr/wiki/Rtl-sdr) |
| Wikipedia | [de.wikipedia.org/wiki/RTL-SDR](https://de.wikipedia.org/wiki/RTL-SDR) |

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install -y rtl-sdr
```

## Validierung

```bash
rtl_test -h 2>&1 | head -n 1
```
