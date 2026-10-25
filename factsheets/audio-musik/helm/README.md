# Factsheet: Helm

## Gruppe: Audio & Musik

## Zweck: Helm ist ein vielseitiger, polyphoner Open-Source-Softwaresynthesizer mit flexibler Modulationsmatrix, integriertem Arpeggiator, Step-Sequenzer und Unterstützung für VST-, LV2- sowie Standalone-Ausführung.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 0.9.0 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [tytel.org/helm](https://tytel.org/helm/) |
| Wikipedia | [en.wikipedia.org/wiki/Helm_(synthesizer)](https://en.wikipedia.org/wiki/Helm_(synthesizer)) |

## Installation (Ubuntu 24.04)

```bash
curl -sL -o /tmp/helm.deb https://tytel.org/static/dist/helm_0.9.0_amd64_r.deb && sudo DEBIAN_FRONTEND=noninteractive apt-get update && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y /tmp/helm.deb && rm -f /tmp/helm.deb
```

## Hello World

```bash
xvfb-run -a helm --version
```

## Beispiele

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `lead_synth.helm`: Ein Helm Synthesizer-Patch-Preset im JSON-Format mit Oszillator-, Filter-, Hüllkurven- und Effekteinstellungen.
- `bass_line.mid`: Eine Standard-MIDI-Datei (Typ 0) mit einer repräsentativen Bassline-Notensequenz.
- `lfo_shape.json`: Eine Konfigurationsdatei im JSON-Format zur Definition benutzerdefinierter LFO-Wellenformen und Modulationsfrequenzen.
- `step_sequencer.json`: Eine Step-Sequenzer-Pattern-Konfigurationsdatei mit 16 Werteschritten für rhythmische Parameter-Modulationen.
- `patch_bank.helmbank`: Eine Helm Patch-Bank als komprimiertes Archiv zur gebündelten Bereitstellung mehrerer Synthesizer-Presets.

## Validierung

Versionsaufruf und Funktionsprüfung von Helm in einer Headless-X11-Umgebung:

```bash
xvfb-run -a helm --version
```
