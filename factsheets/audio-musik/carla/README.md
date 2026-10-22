# Factsheet: Carla

## Gruppe: Audio & Musik

## Zweck: Carla ist ein vielseitiger, modularer Audio-Plugin-Host und Signal-Router zur Einbindung und Verschaltung von LADSPA-, DSSI-, LV2-, VST2-, VST3- und SF2/SFZ-Plugins unter Linux.

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

- `patchbay_setup.carxp`: Eine Carla-Patchbay-Projektdatei im XML-Format zur Definition virtueller Audio- und MIDI-Verbindungen zwischen Plugins.
- `rack_layout.carxr`: Eine Carla-Rack-Konfigurationsdatei im XML-Format zur seriellen Verschaltung von Effekt-Plugins in einer Rack-Ansicht.
- `plugin_blacklist.conf`: Eine Konfigurationsdatei zur Steuerung des Plugin-Scanners und zum Ausschluss inkompatibler Audio-Plugins.
- `midi_filter.py`: Ein Python-Skript für den integrierten Carla-MIDI-Filter zur Echtzeit-Transformation und -Kanalzuordnung von MIDI-Events.
- `canvas_export.svg`: Ein als Vektorgrafik exportiertes Routing-Diagramm zur Darstellung der Modulverbindungen innerhalb der Carla-Patchbay.

## Validierung

Versions- und Funktionsprüfung von Carla im Headless-Modus ausführen:

```bash
PYTHONPATH=/usr/lib/python3/dist-packages xvfb-run -a carla --version
```
