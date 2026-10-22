# Factsheet: Carla

## Gruppe: Audio & Musik

## Zweck: Carla ist ein modularer Open-Source-Audio-Plugin-Host zur flexiblen Verschaltung und Steuerung von LADSPA-, DSSI-, LV2-, VST- und SF2/SFZ-Audio-Plugins sowie MIDI-Routings.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 2.5.8 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [kx.studio/Applications:Carla](https://kx.studio/Applications:Carla) |
| Wikipedia | [en.wikipedia.org/wiki/Carla_(software)](https://en.wikipedia.org/wiki/Carla_(software)) |

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

- `patchbay_setup.carxp`: Eine Carla-Projektkonfigurationsdatei im XML-Format zur Definition virtueller Signal- und MIDI-Patchbay-Routings.
- `rack_layout.carxr`: Eine Carla-Rack-Layoutkonfigurationsdatei zur Platzierung und Einstellung von Audio-Effekten und Instrumenten.
- `plugin_blacklist.conf`: Eine Ausschlusskonfiguration für die automatische Plugin-Erkennung zur Verhinderung von Ladefehlern.
- `midi_filter.py`: Ein Python-Skript zur Filterung und Transformation von MIDI-Events innerhalb der Carla-Umgebung.
- `canvas_export.svg`: Eine Vektorgrafik-Visualisierung des modularen Signalflusses der Carla-Patchbay.

## Validierung

Start und Systemaufruf von Carla im Headless-Modus prüfen:

```bash
PYTHONPATH=/usr/lib/python3/dist-packages xvfb-run -a carla --version
```
