# Factsheet: ZynAddSubFX

## Gruppe: Audio & Musik

## Zweck: ZynAddSubFX ist ein quelloffener, echtzeitfähiger Softwaresynthesizer für additiver, subtraktiver und PADsynth-Klangerzeugung mit vielseitigen Filtern, Effekten und Headless-Audio-Rendering.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 3.0.6 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [zynaddsubfx.sourceforge.io](https://zynaddsubfx.sourceforge.io/) |
| Wikipedia | [en.wikipedia.org/wiki/ZynAddSubFX](https://en.wikipedia.org/wiki/ZynAddSubFX) |

## Installation (Ubuntu 24.04)

```bash
sudo apt-get update && sudo apt-get install -y zynaddsubfx zynaddsubfx-data
```

## Hello World

```bash
zynaddsubfx --help
```

## Beispiele

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `master_patch.xmz`: Ein ZynAddSubFX-Master-Preset im XML-Format inklusive globaler Synthesizer- und Instrumenteneinstellungen.
- `sub_synth.xiz`: Ein ZynAddSubFX-Instrumenten-Preset im XML-Format für subtraktive Synthesizer-Bässe.
- `pad_synth.xiz`: Ein ZynAddSubFX-Instrumenten-Preset für harmonische Pad-Klänge basierend auf der PADsynth-Algorithmen-Synthese.
- `arpeggio.mid`: Eine Standard-MIDI-Datei (Typ 0) mit einer repräsentativen Arpeggio-Notensequenz.
- `effect_chain.eff`: Eine ZynAddSubFX-Effektkonfigurationsdatei mit Parametern für die integrierte Effekteinheit.

## Validierung

Versions- und Funktionsprüfung von ZynAddSubFX im CLI-Modus ausführen:

```bash
zynaddsubfx --version
```
