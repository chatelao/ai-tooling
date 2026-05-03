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

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `generate_test_signal.py`: Sinuswelle mit Rauschen.
- `generate_am_signal.py`: Amplitudenmoduliertes Signal.
- `generate_fm_signal.py`: Frequenzmoduliertes Signal.
- `generate_bpsk_signal.py`: BPSK-moduliertes Digitalsignal.
- `generate_fsk_signal.py`: FSK-moduliertes Digitalsignal.

## Validierung

```bash
xvfb-run -a inspectrum -h 2>&1 | grep -i "Usage: inspectrum"
```
