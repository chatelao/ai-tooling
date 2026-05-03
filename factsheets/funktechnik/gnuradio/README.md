# Factsheet: GNU Radio

## Gruppe: Funktechnik

## Zweck: GNU Radio ist ein Open-Source-Toolkit für die Signalverarbeitung und Software Defined Radio

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [www.gnuradio.org/doc/doxygen](https://www.gnuradio.org/doc/doxygen/) |
| Wikipedia | [de.wikipedia.org/wiki/GNU_Radio](https://de.wikipedia.org/wiki/GNU_Radio) |

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install -y gnuradio
```

## Hello World

```bash
gnuradio-config-info --version
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `sine_wave.grc`: Flowgraph für eine einfache Sinuswelle.
- `noise_source.grc`: Flowgraph für eine Rauschquelle.
- `low_pass_filter.grc`: Beispiel für einen Tiefpassfilter.
- `throttle.grc`: Verwendung des Throttle-Blocks zur CPU-Begrenzung.
- `variable.grc`: Definition von Variablen in GNU Radio.

## Validierung

```bash
gnuradio-config-info --version
```
