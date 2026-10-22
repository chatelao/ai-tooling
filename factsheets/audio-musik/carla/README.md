# Factsheet: Carla

## Gruppe: Audio & Musik

## Zweck: Carla ist ein modularer Open-Source-Plugin-Host und eine virtuelle Patchbay zur Verwaltung, Verkettung und Steuerung von Audio-Plugins (LV2, VST2/3, LADSPA, DSSI, SF2/SFZ) sowie MIDI-Routing.

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

- `project_patchbay.carxp`: Eine Carla-Projektdatei im XML-Format zur Definition von Audio- und MIDI-Routing-Patchbays sowie Plugin-Verbindungen.
- `rack_layout.carxr`: Eine Carla-Rack-Layoutdatei im XML-Format mit vorkonfigurierten Effektketten, Modulparametern und Master-Gains.
- `plugin_blacklist.conf`: Eine Konfigurationsdatei zum Ausschließen fehlerhafter Plugins und zur Verwaltung von Plugin-Suchpfaden.
- `midi_filter.py`: Ein benutzerdefiniertes Python-Skript zur Inline-Transformation und Filterung von MIDI-Events innerhalb der Carla-Engine.
- `canvas_export.svg`: Eine Vektorgrafik im SVG-Format zur visuellen Darstellung des virtuellen Patchbay-Routing-Graphen.

## Validierung

Versionsprüfung und Headless-Funktionalität von Carla ausführen:

```bash
PYTHONPATH=/usr/lib/python3/dist-packages xvfb-run -a carla --version
```
