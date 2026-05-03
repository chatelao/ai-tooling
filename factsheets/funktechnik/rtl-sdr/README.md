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

## Hello World

```bash
rtl_test
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `fm_radio.sh`: Skript zum Empfangen von UKW-Radio.
- `scan_frequencies.sh`: Beispiel für einen Frequenzscan mit `rtl_power`.
- `capture_raw.sh`: Erfassen von I/Q-Rohdaten.
- `device_info.sh`: Abrufen von Geräteinformationen.
- `ppm_test.sh`: Testen des Frequenzfehlers (PPM).

## Validierung

```bash
rtl_test -h 2>&1 | head -n 1
```
