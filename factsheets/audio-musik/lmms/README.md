# Factsheet: LMMS

## Gruppe: Audio & Musik

## Zweck: LMMS (Linux MultiMedia Studio) ist eine plattformübergreifende Digital Audio Workstation (DAW) zur Erstellung, Arrangement und Synthese von Musik mit integrierten Klangerzeugern, Effekt-Plugins und nativem Headless-CLI-Audio-Rendering.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 1.2.2 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [lmms.io/documentation](https://lmms.io/documentation) |
| Wikipedia | [de.wikipedia.org/wiki/LMMS](https://de.wikipedia.org/wiki/LMMS) |

## Installation (Ubuntu 24.04)

```bash
sudo apt-get update && sudo apt-get install -y lmms xvfb
```

## Hello World

```bash
lmms --version
```

## Beispiele

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `beat.mmpz`: Eine komprimierte LMMS-Projektdatei (`.mmpz`) mit vollständigen Synth-Spuren, Patterns und Automationen.
- `synth_preset.xspf`: Eine XML-basierte Instrumenten-Preset-Datei (`.xpf`/`.xspf`) zur Konfiguration virtueller Synthesizer.
- `chord_sequence.mid`: Eine Standard-MIDI-Datei mit Akkordfolgen und Melodie-Patterns für den Import in LMMS-Tracks.
- `drum_kit.xml`: Eine XML-Konfigurationsdatei zur Definition von Sample-Zuweisungen im Audio File Processor (Drum Kit).
- `render_config.xml`: Eine XML-Einstellungsdatei zur Konfiguration von Audio-Export-Parametern (Abtastrate, Format, Interpolation).

## Validierung

Versionsprüfung und Headless-Audio-Rendering von LMMS ausführen:

```bash
lmms render examples/beat.mmpz -o output.wav -f wav
```
