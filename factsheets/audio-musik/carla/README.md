# Factsheet: Carla

## Gruppe: Audio & Musik

## Zweck: Carla ist ein flexibler Open-Source-Plugin-Host für Audio-Effekte und Instrumente, der Schnittstellen wie LADSPA, DSSI, LV2, VST2, VST3 und SF2/SFZ unterstützt sowie komplexes Signal-Routing ermöglicht.

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

- `project.carxp`: Eine Carla-Projektdatei im XML-Format zur Speicherung von Host-Einstellungen, geladenen Plugins und Modul-Verbindungen.
- `rack.carxr`: Eine Carla-Rack-Preset-Datei im XML-Format zur Speicherung von Effektketten und Parameterzuständen.
- `blacklist.conf`: Eine Konfigurationsdatei zum Ausschließen fehlerhafter oder inkompatibler Audio-Plugins beim Systemscan.
- `midi_filter.py`: Ein Python-Skript für den integrierten Carla-MIDI-Filter-Knoten zur Echtzeit-Transformation von MIDI-Events.
- `canvas.svg`: Eine Vektorgrafik zur Visualisierung der virtuellen Modul-Vorschau und des Routing-Graphen.

## Validierung

Versionsprüfung und Headless-Funktionalität von Carla ausführen:

```bash
PYTHONPATH=/usr/lib/python3/dist-packages xvfb-run -a carla --version
```
