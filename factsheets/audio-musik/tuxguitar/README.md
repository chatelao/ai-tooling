# Factsheet: TuxGuitar

## Gruppe: Audio & Musik

## Zweck: TuxGuitar ist ein mehrspuriger Open-Source-Editor und Player für Gitarren-Tabulaturen und Notensatz mit Unterstützung verschiedener Dateiformate (GP3/GP4/GP5, PTB, TG) sowie MIDI-Synthese und PDF-Export.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 1.5.6 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [tuxguitar.app](http://www.tuxguitar.app/) |
| Wikipedia | [de.wikipedia.org/wiki/TuxGuitar](https://de.wikipedia.org/wiki/TuxGuitar) |

## Installation (Ubuntu 24.04)

```bash
sudo apt-get update && sudo apt-get install -y tuxguitar xvfb
```

## Hello World

```bash
xvfb-run -a tuxguitar -v
```

## Beispiele

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `riff_master.tg`: Eine native TuxGuitar-Tabulaturdatei im XML-Format mit Gitarrennoten, Spuren und Taktstrukturen.
- `rock_classic.gp5`: Eine Guitar Pro 5 kompatible Tabulaturdatei mit Bänden, Akkorden und Notationsattributen.
- `fingerpicking.ptb`: Eine PowerTab kompatible Datei mit Akustikgitarren-Fingerpicking-Notationen.
- `tuning_presets.xml`: Eine XML-Konfigurationsdatei mit vordefinierten Gitarren-Stimmungen (Standard E, Drop D, Open G, DADGAD).
- `tab_export.pdf`: Eine aus TuxGuitar exportierte Tabulatur- und Notenblattdarstellung im PDF-Format.

## Validierung

Versionsprüfung und Headless-Aufruf von TuxGuitar ausführen:

```bash
xvfb-run -a tuxguitar -v
```
