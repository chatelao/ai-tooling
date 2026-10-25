# Factsheet: Ardour

## Gruppe: Audio & Musik

## Zweck: Ardour ist eine hochprofessionelle, open-source Digital Audio Workstation (DAW) für Mehrspur-Audioaufnahme, MIDI-Arrangement, Nicht-lineares Mischen und komplexes Signal-Routing mit Lua-Automatisierungsschnittstelle.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 8.4.0 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [manual.ardour.org](https://manual.ardour.org/) |
| Wikipedia | [de.wikipedia.org/wiki/Ardour](https://de.wikipedia.org/wiki/Ardour) |

## Installation (Ubuntu 24.04)

```bash
sudo apt-get update && sudo apt-get install -y ardour xvfb
```

## Hello World

```bash
xvfb-run -a ardour --version
```

## Beispiele

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `session_template.ardour`: Eine XML-basierte Ardour-Session-Vorlage (`.ardour`) mit Vorkonfiguration für Bus-Routing, Master-Outputs und Sample-Rate.
- `export_profile.xml`: Eine XML-Exportprofil-Spezifikation für hochwertiges Stereo-WAV-Rendering (24-Bit, 44.1 kHz).
- `lua_batch_render.lua`: Ein Lua-Automatisierungsskript zur Ausführung über die integrierte Ardour-Lua-Engine im Batch-Modus.
- `midi_track_config.xml`: Eine XML-Konfigurationsvorlage zur Definition von MIDI-Spuren und Instrumenten-Routings.
- `sample_loop.wav`: Eine monophone WAVE-Audio-Testdatei (44.1 kHz Sine-Wave) für den Import und Test-Renderings in Ardour-Spuren.

## Validierung

Versions- und Funktionsprüfung von Ardour im Headless-CLI-Modus ausführen:

```bash
xvfb-run -a ardour --version
```
