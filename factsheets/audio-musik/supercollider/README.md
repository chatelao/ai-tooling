# Factsheet: SuperCollider

## Gruppe: Audio & Musik

## Zweck: SuperCollider ist eine plattformübergreifende Programmiersprache und Sound-Compiler-Engine zur Echtzeit-Audiosynthese, algorithmischen Komposition und Signalverarbeitung.

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
sudo apt-get update && sudo apt-get install -y supercollider
```

## Hello World

```bash
QT_QPA_PLATFORM=offscreen sclang examples/generative_drone.scd
```

## Beispiele

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `generative_drone.scd`: Ein SuperCollider Non-Realtime Synthesis (NRT) Skript zur automatischen Generierung und Speicherung eines Drones.
- `custom_synthdef.scd`: Eine `SynthDef`-Definition für einen subtraktiven Sägezahn-Synthesizer mit resonantem Tiefpassfilter und ADSR-Hüllkurve.
- `pattern_sequence.scd`: Ein `Pbind`-Muster-Sequenzer zur Steuerung von Notenfolgen und Parametern.
- `scsynth_config.scd`: Eine Server-Konfigurationsdatei zur Einstellung von Audiobussen, Puffergrößen und Sample-Raten.
- `rendered_buffer.wav`: Eine gerenderte WAV-Audiodatei, erzeugt durch das NRT-Generierungsskript.

## Validierung

Audiosynthese-Kompilierung im Headless-Modus prüfen:

```bash
sclang -v
QT_QPA_PLATFORM=offscreen sclang examples/generative_drone.scd
```
