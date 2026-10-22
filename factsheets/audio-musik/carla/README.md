# Factsheet: Carla

## Gruppe: Audio & Musik

## Zweck: Carla ist ein modularer Audio-Plugin-Host, Patchbay und Plugin-Manager mit Unterstützung für LADSPA, DSSI, LV2, VST2/3, CLAP und SF2/SFZ Instrumente sowie flexiblem Audio- und MIDI-Routing.

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
sudo apt-get update && sudo apt-get install -y carla xvfb
```

## Hello World

```bash
PYTHONPATH=/usr/lib/python3/dist-packages xvfb-run -a carla --version
```

## Beispiele

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `patchbay_setup.carxp`: Eine Carla-Projektdatei im XML-Format mit definierten Audio- und MIDI-Knotenverbindungen für das Patchbay-Routing.
- `rack_layout.carxr`: Eine Carla-Rack-Presetdatei mit vordefinierten Effektketten-Slots (Chorus, Delay).
- `plugin_blacklist.conf`: Eine Konfigurationsdatei für den Carla Plugin-Scanner zur Verwaltung von Whitelists, Blacklists und Host-Engine-Optionen.
- `midi_filter.py`: Ein Python-Skript für den integrierten Carla MIDI-Prozessor zur Transponierung und Geschwindigkeitsfilterung von MIDI-Ereignissen.
- `canvas_export.svg`: Eine Vektorgrafik-Exportdatei des grafischen Audio- und MIDI-Verbindungs-Graphen.

## Validierung

Versionsprüfung und Headless-Funktionalität von Carla ausführen:

```bash
PYTHONPATH=/usr/lib/python3/dist-packages xvfb-run -a carla --version
```
