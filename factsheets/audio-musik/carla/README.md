# Factsheet: Carla

## Gruppe: Audio & Musik

## Zweck: Carla ist ein vielseitiger, modularer Audio-Plugin-Host und Patchbay-Prozessor zur Einbindung und Verschaltung von LADSPA, DSSI, LV2, VST2, VST3 und SF2/SFZ Instrumenten und Effekten.

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
sudo apt-get update && sudo apt-get install -y carla carla-bridge-linux64 xvfb
```

## Hello World

```bash
PYTHONPATH=/usr/lib/python3/dist-packages xvfb-run -a carla --version
```

## Beispiele

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `patchbay_setup.carxp`: Eine Carla-Patchbay-Projektdatei im XML-Format zur Definition virtueller Modulverbindungen und Routing-Optionen.
- `rack_layout.carxr`: Eine Carla-Rack-Preset-Datei im XML-Format zur Konfiguration von Effekt-Slots und Dry/Wet-Prozentwerten.
- `plugin_blacklist.conf`: Eine Konfigurationsdatei für den Plugin-Scanner mit Ausschlüssen fehlerhafter Pfade und Plugins.
- `midi_filter.py`: Ein benutzerdefiniertes Python-Skript für Carlas interne Python-Engine zur Modifikation und Filterung von MIDI-Ereignissen.
- `canvas_export.svg`: Eine Vektorgrafik-Diagramm-Exportdatei zur Visualisierung von Signalflüssen und Audioknoten-Topologien.

## Validierung

Funktions- und Versionsprüfung von Carla im Headless-Modus mittels Xvfb ausführen:

```bash
PYTHONPATH=/usr/lib/python3/dist-packages xvfb-run -a carla --version
```
