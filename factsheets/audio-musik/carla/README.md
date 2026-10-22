# Factsheet: Carla

## Gruppe: Audio & Musik

## Zweck: Carla ist ein vielseitiger, modularer Open-Source-Audio-Plugin-Host für LADSPA, DSSI, LV2, VST2, VST3 und SF2/SFZ mit grafischem Patchbay-Routing, Rack-Visualisierung und Headless-CLI-Ausführung.

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

- `patchbay_setup.carxp`: Eine Carla-Projektkonfiguration im XML-Format mit Routing-Informationen und Node-Verbindungen.
- `rack_layout.carxr`: Eine Carla-Rack-Layoutdefinition im XML-Format zur Speicherung von Host- und Plugin-Rackansichten.
- `plugin_blacklist.conf`: Eine Konfigurationsdatei mit Ausschlussregeln für den automatisierten Plugin-Suchlauf.
- `midi_filter.py`: Ein Python-Skript zur benutzerdefinierten Transformation und Filterung von MIDI-Events in Carla.
- `canvas_export.svg`: Eine Vektorgrafik-Exportdatei der grafischen Patchbay-Kopplung von Signalströmen.

## Validierung

Versions- und Funktionsprüfung von Carla via Virtual Framebuffer und Python-API ausführen:

```bash
PYTHONPATH=/usr/lib/python3/dist-packages xvfb-run -a carla --version
```
