# Factsheet: Carla

## Gruppe: Audio & Musik

## Zweck: Carla ist ein modularer Audio-Plugin-Host für LV2-, VST-, VST3-, LADSPA-, DSSI- und SF2/SFZ-Plugins mit Unterstützung für flexibles Audio- und MIDI-Routing (Patchbay/Rack), Standalone-Ausführung und Canvas-Graph-Visualisierung.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 2.5.8 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [kx.studio/Applications:Carla](https://kx.studio/Applications:Carla) |
| Wikipedia | [en.wikipedia.org/wiki/KXStudio](https://en.wikipedia.org/wiki/KXStudio) |

## Installation (Ubuntu 24.04)

```bash
sudo apt-get update && sudo apt-get install -y carla carla-bridge-linux64 xvfb
```

## Hello World

```bash
PYTHONPATH=/usr/lib/python3/dist-packages xvfb-run -a carla --version
```

## Beispiele

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `patchbay_setup.carxp`: Eine XML-Projektdatei für Carla mit Konfiguration von virtuellen Audio- und MIDI-Knoten in einer modularen Patchbay-Topologie.
- `rack_layout.carxr`: Eine Carla-Rack-Preset-Datei im XML-Format zur Anordnung und Verkettung von Audio-Effekten und Plugin-Parametern.
- `plugin_blacklist.conf`: Eine Konfigurationsdatei zum Ausschließen fehlerhafter oder inkompatibler Audio-Plugins beim Start des Scanners.
- `midi_filter.py`: Ein Python-Skript für den internen Carla-MIDI-Filter-Prozessor zur Transformation von MIDI-Noten- und CC-Ereignissen.
- `canvas_export.svg`: Eine Vektorgrafik zur Visualisierung eines aus Carla exportierten Audio- und MIDI-Routing-Graphen.

## Validierung

Versionsprüfung und Headless-Funktionalität von Carla ausführen:

```bash
PYTHONPATH=/usr/lib/python3/dist-packages xvfb-run -a carla --version
```
