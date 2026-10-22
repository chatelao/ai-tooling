# Factsheet: Carla

## Gruppe: Audio & Musik

## Zweck: Carla ist ein modularer Audio-Plugin-Host und Patchbay zur flexiblen Verschaltung von LV2-, VST2/3-, LADSPA-, DSSI- und SF2/SFZ-Audio-Plugins, JACK/PipeWire-Routing sowie internen Python-MIDI-Filtern.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 2.5.8 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [kx.studio/Applications:Carla](https://kx.studio/Applications:Carla) |
| Wikipedia | [de.wikipedia.org/wiki/Carla_(Software)](https://de.wikipedia.org/wiki/Carla_(Software)) |

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

- `patchbay_setup.carxp`: Eine Carla-Projektdatei im XML-Format zur Definition virtueller Audio- und MIDI-Patchbay-Knotenverbindungen.
- `rack_layout.carxr`: Eine Rack-Preset-Konfigurationsdatei mit geladenen Signaleffekten und Plugin-Parametern.
- `plugin_blacklist.conf`: Eine Konfigurationsdatei für den Carla Plugin-Scanner zum Ausschluss inkompatibler Audio-Plugins.
- `midi_filter.py`: Ein benutzerdefiniertes Python-Skript zur Inline-Transformation und Filterung von MIDI-Events.
- `canvas_export.svg`: Ein exportiertes Vektordiagramm der visuellen Routing-Topologie der Patchbay.

## Validierung

Start und Systemaufruf von Carla im Headless-Modus prüfen:

```bash
PYTHONPATH=/usr/lib/python3/dist-packages xvfb-run -a carla --version
```
