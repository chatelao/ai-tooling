# Factsheet: Surge XT

## Gruppe: Audio & Musik

## Zweck: Surge XT ist ein leistungsstarker, hybrid-synthetischer Open-Source-Softwaresynthesizer mit vielfältigen Oszillator-Algorithmen, MPE-Unterstützung, umfangreicher Modulations-Matrix und Headless-CLI-Schnittstelle.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 1.3.4 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [surge-synthesizer.github.io](https://surge-synthesizer.github.io/) |
| Wikipedia | [en.wikipedia.org/wiki/Surge_(synthesizer)](https://en.wikipedia.org/wiki/Surge_(synthesizer)) |

## Installation (Ubuntu 24.04)

```bash
DEB_URL=$(curl -s https://api.github.com/repos/surge-synthesizer/surge/releases/tags/Nightly | grep -o 'https://[^"]*surge-xt-linux-x64-[^"]*\.deb' | head -n 1) && curl -sL -o /tmp/surge-xt.deb "$DEB_URL" && sudo DEBIAN_FRONTEND=noninteractive apt-get update && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y /tmp/surge-xt.deb && rm -f /tmp/surge-xt.deb
```

## Hello World

```bash
surge-xt-cli --version
```

## Beispiele

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `warm_pad.surgepreset`: Ein Surge XT Patch-Preset im XML-Format mit warmem Polysynth-Klang und Envelope-Filtereinstellungen.
- `wavetable_custom.wt`: Eine benutzerdefinierte Wavetable-Audiodatei im WAV/RIFF-Format für Oszillator-Wavetable-Synthesis.
- `tuning_scale.scl`: Eine Scala-Stimmungsdatei im SCL-Format zur Definition gleichstufiger und mikrotonaler Frequenzintervalle.
- `keyboard_mapping.kbm`: Eine Scala-Keyboard-Mapping-Datei im KBM-Format zur Zuweisung von Tastatur-Noten zu Frequenzskalen.
- `mpe_test.mid`: Eine Standard-MIDI-Datei (Typ 1) mit MPE-Expressionsdaten (Polyphonic Pitch Bend und Channel Pressure).

## Validierung

Versionsaufruf und Funktionsprüfung von Surge XT über die Befehlszeile:

```bash
surge-xt-cli --version
```
