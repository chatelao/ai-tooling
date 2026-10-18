# Factsheet: SuperCollider

## Gruppe: Audio & Musik

## Zweck: SuperCollider ist eine plattformübergreifende Umgebung und domänenspezifische Programmiersprache zur Audiosynthese, elektroakustischen Musikkomposition und Echtzeit-Signalverarbeitung.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 3.13.0 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [supercollider.github.io](https://supercollider.github.io/) |
| Wikipedia | [de.wikipedia.org/wiki/SuperCollider](https://de.wikipedia.org/wiki/SuperCollider) |

## Installation (Ubuntu 24.04)

```bash
sudo apt-get update && sudo apt-get install -y --no-install-recommends supercollider-language supercollider-server
```

## Hello World

```bash
QT_QPA_PLATFORM=offscreen sclang examples/drone.scd
```

## Beispiele

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `drone.scd`: Ein Ambient-Drone-Synthesizer-Skript mit Multi-Oszillatoren und Non-Realtime (NRT) Score-Rendering.
- `synthdef.scd`: Eine `SynthDef`-Definition für einen sägezahnbasierten Synthesizer mit resonantem Tiefpassfilter.
- `pattern.scd`: Ein algorithmisches Sequenzmuster unter Verwendung der SuperCollider `Pbind`-Klasse.
- `server_config.scd`: Konfigurationseinstellungen für den SuperCollider Audio-Server (`scsynth`).
- `rendered_drone.wav`: Eine gerenderte WAV-Audiodatei, erzeugt via Headless Non-Realtime Synthesis (NRT).

## Validierung

Audiosynthese im Headless Non-Realtime (NRT) Modus prüfen:

```bash
sclang -v
QT_QPA_PLATFORM=offscreen sclang examples/drone.scd
```
