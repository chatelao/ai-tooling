# Factsheet: Carla

## Gruppe: Audio & Musik

## Zweck: Carla ist ein modularer Audio-Plugin-Host für LV2, VST2, VST3, SoundFont2 und SFZ mit flexibler Patchbay-Routing-Architektur, Rack-Modularisierung und Python-Skripting.

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

- `patchbay_setup.carxp`: Eine Carla-Projektdatei im XML-Format mit Knoten-Layout, Audio/MIDI-Verbindungen und Parameterkonfigurationen der Patchbay.
- `rack_layout.carxr`: Eine Carla-Rack-Layoutkonfigurationsdatei im XML-Format zur Speicherung sequenzieller Plugin-Instanzen.
- `plugin_blacklist.conf`: Eine Ausschluss-Konfigurationsdatei für fehlerhafte oder inkompatible Audio-Plugins im Host-System.
- `midi_filter.py`: Ein Python-Skript zur Konvertierung und Transformation von MIDI-Ereignissen über Carlas Python-API.
- `canvas_export.svg`: Eine Vektorgrafik-Diagrammdatei zur Darstellung des virtuellen Signalflusses und der Modulverschaltung.

## Validierung

Versions- und Headless-Funktionsprüfung von Carla ausführen:

```bash
PYTHONPATH=/usr/lib/python3/dist-packages xvfb-run -a carla --version
```
