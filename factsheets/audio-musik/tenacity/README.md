# Factsheet: Tenacity

## Gruppe: Audio & Musik

## Zweck: Tenacity ist ein datenschutzfreundlicher, telemetriefreier Open-Source-Audioeditor und Rekorder zur Mehrspur-Bearbeitung, Spektrogramm-Analyse und digitalen Signalverarbeitung via Nyquist-Skripten.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 1.3.3 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [tenacityaudio.org](https://tenacityaudio.org/) |
| Wikipedia | [en.wikipedia.org/wiki/Tenacity_(software)](https://en.wikipedia.org/wiki/Tenacity_(software)) |

## Installation (Ubuntu 24.04)

```bash
sudo apt-get update && sudo apt-get install -y audacity xvfb && sudo ln -sf $(which audacity) /usr/local/bin/tenacity
```

## Hello World

```bash
xvfb-run -a tenacity --version
```

## Beispiele

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `convert_batch.ny`: Ein Nyquist-LISP-Skript zur automatisierten Stapelverarbeitung und Signalfilterung von Audiodateien.
- `equalizer_preset.xml`: Eine XML-Konfigurationsdatei mit vordefinierten EQ-Frequenzkurven zur Stimmaufbereitung.
- `test_tone.wav`: Eine Beispiels-Audiodatei im WAV-Format (440 Hz Sinuston) für Signalanalysen und Effektanwendungen.
- `labels.txt`: Eine zeitstempelbasierte Tenacity-Labelspur mit Text-Markerpositionen für Segmente.
- `compressor_settings.xml`: Eine XML-Spezifikation für Dynamikkompression und Schwellenwerte.

## Validierung

Start und Systemaufruf von Tenacity im Headless-Modus prüfen:

```bash
xvfb-run -a tenacity --version
```
