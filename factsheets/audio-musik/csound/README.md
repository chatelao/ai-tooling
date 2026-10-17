# Factsheet: Csound

## Gruppe: Audio & Musik

## Zweck: Csound ist eine domänenspezifische Programmiersprache und Sound-Compiler-Engine zur Audiosynthese, Signalverarbeitung und elektroakustischen Musikkomposition.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 6.18.1 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [csound.com](https://csound.com/) |
| Wikipedia | [de.wikipedia.org/wiki/Csound](https://de.wikipedia.org/wiki/Csound) |

## Installation (Ubuntu 24.04)

```bash
sudo apt-get update && sudo apt-get install -y csound
```

## Hello World

```bash
csound -o output.wav examples/simple_sine.csd
```

## Beispiele

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `simple_sine.csd`: Eine vereinheitlichte Csound-Quelldatei (Orchester und Partitur) zur Erzeugung von Sinustönen mit Amplitude-Envelopes.
- `reverb_patch.orc`: Eine Csound-Orchesterdatei (.orc) mit Instrumentendefinitionen und Hall-Effektbaustein (`freeverb`).
- `melody.sco`: Eine Csound-Partiturdatei (.sco) mit zeitlich gestaffelten Notenereignissen und Frequenzangaben.
- `synth_config.csd`: Ein Csound-Synthesizer-Skript zur Demonstration subtraktiver Synthese mit Sägezahn-Oszillator und Moog-Filter.
- `rendered_sample.wav`: Eine kompilierte WAV-Audiodatei, erzeugt aus der Synthesizer-Definition.

## Validierung

Audiosynthese-Kompilierung im Headless-Modus prüfen:

```bash
csound --version
csound -o examples/rendered_sample.wav examples/simple_sine.csd
```
