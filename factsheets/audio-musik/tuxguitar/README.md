# Factsheet: TuxGuitar

## Gruppe: Audio & Musik

## Zweck: TuxGuitar ist ein mehrspuriger Tabulatur-Editor und -Player für Gitarre und andere Bundinstrumente mit Unterstützung für verschiedene Dateiformate wie Guitar Pro und PowerTab, MIDI-Synthese und Notendruck.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 1.5.6 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [tuxguitar.app](https://www.tuxguitar.app/) |
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

- `riff_master.tg`: Eine native TuxGuitar-Projektdatei im XML-Format mit Gitarren-Riffs, Akkordbezeichnungen und Tempoangaben.
- `rock_classic.gp5`: Eine Beispieldatei im Guitar Pro 5 Binärformat mit Rhythmus- und Solospuren für Band-Arrangements.
- `fingerpicking.ptb`: Eine PowerTab-Format-Datei für Fingerstyle-Gitarre mit detaillierten Notationssymbolen und Tabulaturdaten.
- `tuning_presets.xml`: Eine Konfigurationsdatei mit vordefinierten Gitarren-Stimmungen (E-Standard, Drop D, DADGAD, Open G).
- `tab_export.pdf`: Eine aus TuxGuitar exportierte Beispieldokumentation im PDF-Format mit Notenbild und Tabulaturzeilen.

## Validierung

Versionsprüfung und Headless-Funktionalität von TuxGuitar ausführen:

```bash
xvfb-run -a tuxguitar -v
```
