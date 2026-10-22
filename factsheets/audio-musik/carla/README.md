# Factsheet: Carla

## Gruppe: Audio & Musik

## Zweck: Carla ist ein modularer Audio-Plugin-Host und Patchbay-Manager zur Einbindung, Verschaltung und Steuerung von LADSPA-, DSSI-, LV2-, VST2-, VST3- und SF2/SFZ-Audio-Plugins und Soundfonts.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 2.5.8 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [kx.studio/Applications:Carla](https://kx.studio/Applications:Carla) |
| Wikipedia | [en.wikipedia.org/wiki/Carla_(audio_host)](https://en.wikipedia.org/wiki/Carla_(audio_host)) |

## Installation (Ubuntu 24.04)

```bash
sudo apt-get update && sudo apt-get install -y carla xvfb
```

## Hello World

```bash
PYTHONPATH=/usr/lib/python3/dist-packages xvfb-run -a carla --version
```

## Beispiele

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `patchbay_setup.carxp`: Eine Carla-XML-Projektdatei mit einer Patchbay-Konfiguration für Gain- und Pan-Signale.
- `rack_layout.carxr`: Eine Carla-Rack-Projektdatei im XML-Format zur Definition von Rack-Effekt-Slots.
- `plugin_blacklist.conf`: Eine Konfigurationsdatei mit Ausschlussregeln für problematische oder inkompatible Plugins.
- `midi_filter.py`: Ein benutzerdefiniertes Python-Skript zur Skalierung und Oktav-Transponierung von MIDI-Ereignissen.
- `canvas_export.svg`: Ein exportiertes SVG-Diagramm zur Visualisierung der Modul- und Routing-Topologie.

## Validierung

Versionsprüfung und Headless-Funktionalität von Carla ausführen:

```bash
PYTHONPATH=/usr/lib/python3/dist-packages xvfb-run -a carla --version
```
