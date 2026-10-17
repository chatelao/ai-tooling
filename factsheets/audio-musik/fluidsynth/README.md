# Factsheet: FluidSynth

## Gruppe: Audio & Musik

## Zweck: FluidSynth ist ein echtzeitfähiger Software-Synthesizer basierend auf den SoundFont 2- und SoundFont 3-Spezifikationen zur MIDI-Klangerzeugung.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 2.3.4 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [www.fluidsynth.org](https://www.fluidsynth.org/) |
| Wikipedia | [de.wikipedia.org/wiki/FluidSynth](https://de.wikipedia.org/wiki/FluidSynth) |

## Installation (Ubuntu 24.04)

```bash
sudo apt-get update && sudo apt-get install -y fluidsynth fluid-soundfont-gm
```

## Hello World

```bash
fluidsynth -ni /usr/share/sounds/sf2/FluidR3_GM.sf2 examples/mozart_k545.mid -F output.wav -r 44100
```

## Beispiele

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `mozart_k545.mid`: Eine Standard-MIDI-Datei zur Noten- und Wiedergabe-Validierung.
- `custom_font.sf2`: Eine minimale SoundFont2-Archivdatei zur Überprüfung der SoundFont-Laderoutine.
- `fluidsynth_config.conf`: Eine Beispiel-Konfigurationsdatei für FluidSynth-Synthesizerparameter (Sample-Rate, Gain, Polyphonie).
- `shell_commands.cmd`: Ein Stapelverarbeitungsskript mit interaktiven Shell-Befehlen für FluidSynth.
- `rendered_sample.wav`: Eine gerenderte WAV-Audiodatei, erzeugt aus der MIDI-Eingabe.

## Validierung

Audio-Rendering im Headless-Modus prüfen:

```bash
fluidsynth --version
fluidsynth -ni /usr/share/sounds/sf2/FluidR3_GM.sf2 examples/mozart_k545.mid -F examples/rendered_sample.wav -r 44100
```
