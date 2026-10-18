# Factsheet: Audacity

## Gruppe: Audio & Musik

## Zweck: Audacity ist ein gängiger plattformübergreifender Open-Source-Audioeditor und Rekorder zur Mehrspur-Bearbeitung, Spektrogramm-Analyse und digitalen Signalverarbeitung via Nyquist-Skripten.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 3.4.2 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [www.audacityteam.org](https://www.audacityteam.org/) |
| Wikipedia | [de.wikipedia.org/wiki/Audacity](https://de.wikipedia.org/wiki/Audacity) |

## Installation (Ubuntu 24.04)

```bash
sudo apt-get update && sudo apt-get install -y audacity xvfb
```

## Hello World

```bash
xvfb-run -a audacity --version
```

## Beispiele

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `generate_sine.ny`: Ein Nyquist-LISP-Skript zur automatisierten Erzeugung von 440 Hz Sinustönen.
- `noise_reduction_profile.txt`: Eine Beispieldatei mit Frequenzanalyse-Abtastwerten zur Rauschunterdrückung.
- `macro_chain.txt`: Eine Makro-Spezifikation für die automatisierte Stapelverarbeitung und Effektausführung.
- `label_track.txt`: Eine zeitstempelbasierte Audacity-Labelspur mit Text-Markerpositionen.
- `test_speech.wav`: Eine Beispiels-Audiodatei im WAV-Format für Signalanalysen und Effektanwendungen.

## Validierung

Start und Systemaufruf von Audacity im Headless-Modus prüfen:

```bash
xvfb-run -a audacity --version
```
