# Factsheet: Carla

## Gruppe: Audio & Musik

## Zweck: Carla ist ein vielseitiger, modularer Audio-Plugin-Host für LADSPA, DSSI, LV2, VST2, VST3 und SoundFonts mit flexibler Patchbay, Audio-Routing und Rack-Verwaltung.

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

- `patchbay_setup.carxp`: Eine Carla-Projektdatei im XML-Format mit einer gespeicherten Modular-Patchbay-Konfiguration und virtuellen Signalverbindungen.
- `rack_layout.carxr`: Eine Carla-Rack-Preset-Datei im XML-Format zur Definition sequenzieller Plugin-Ketten und Parametergruppen.
- `plugin_blacklist.conf`: Eine Konfigurationsdatei für den Plugin-Scanner zur Verwaltung ignorierter oder inkompatibler Audio-Plugins.
- `midi_filter.py`: Ein benutzerdefiniertes Python-Skript für den internen Carla-Script-Host zur Filterung und Transformation von MIDI-Events in Echtzeit.
- `canvas_export.svg`: Eine Vektorgrafik als visuelles Diagramm des im Patchbay gerenderten Audio- und MIDI-Signalflusses.

## Validierung

Versions- und Funktionsprüfung von Carla im Headless-Modus ausführen:

```bash
PYTHONPATH=/usr/lib/python3/dist-packages xvfb-run -a carla --version
```
