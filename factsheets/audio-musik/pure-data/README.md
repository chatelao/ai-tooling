# Factsheet: Pure Data

## Gruppe: Audio & Musik

## Zweck: Pure Data ist eine visuelle Echtzeit-Programmierumgebung zur Audiosynthese, Signalverarbeitung, MIDI-Steuerung und interaktiven Medienkunst.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 0.57-0 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [puredata.info](https://puredata.info/) |
| Wikipedia | [de.wikipedia.org/wiki/Pure_Data](https://de.wikipedia.org/wiki/Pure_Data) |

## Installation (Ubuntu 24.04)

```bash
sudo apt-get update && sudo apt-get install -y puredata
```

## Hello World

```bash
pd -nogui -noaudio -send "pd quit" -open examples/synth_engine.pd
```

## Beispiele

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `synth_engine.pd`: Der Haupt-Patch zur Demonstration der automatischen Ausführung und Initialisierung via `loadbang`.
- `oscillator_sub.pd`: Eine Sub-Patch-Abstraktion mit Oszillator und Ein-/Ausgangsanschlüssen (`inlet`/`outlet~`).
- `delay_effect.pd`: Eine Audioeffekt-Abstraktion zur Realisierung von Delay-Effekten mit `delwrite~` und `delread~`.
- `midi_in_handler.pd`: Ein Patch zur Verarbeitung eingehender MIDI-Notenwerte und Konvertierung in Frequenzen (`mtof`).
- `array_data.txt`: Eine Beispieldatei mit Zahlenwerten für Wavetable-Arrays und Funktionskurven.

## Validierung

Verarbeitung von Pure Data-Patches im Headless-Modus prüfen:

```bash
pd -version
pd -nogui -noaudio -send "pd quit" -open examples/synth_engine.pd
```
