# Factsheet: Carla

## Gruppe: Audio & Musik

## Zweck: Carla ist ein modularer Open-Source-Audio-Plugin-Host, der verschiedene Formate wie Ladspa, DSSI, LV2, VST2, VST3 und SF2/SFZ unterstützt und flexibles Audio- und MIDI-Routing sowie Rack- und Patchbay-Ansichten bietet.

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

- `patchbay_setup.carxp`: Eine Carla-Patchbay-Sitzungsdatei im XML-Format mit definierten Audio- und MIDI-Verbindungen zwischen Plugins.
- `rack_layout.carxr`: Eine Carla-Rack-Sitzungskonfiguration mit geladenen Effekten und Instrumenten-Plugins.
- `plugin_blacklist.conf`: Eine Konfigurationsdatei zum Ausschließen fehlerhafter oder inkompatibler Audio-Plugins beim Scan.
- `midi_filter.py`: Ein Python-Skript für den integrierten Carla-Python-MIDI-Filter zur Echtzeit-Transformation von MIDI-Events.
- `canvas_export.svg`: Eine Vektorgrafik-Exportdatei des visuellen Routing-Graphen der Patchbay-Topologie.

## Validierung

Versionsprüfung und Headless-Funktionalität von Carla ausführen:

```bash
PYTHONPATH=/usr/lib/python3/dist-packages xvfb-run -a carla --version
```
