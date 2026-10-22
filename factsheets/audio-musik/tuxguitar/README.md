# Factsheet: TuxGuitar

## Gruppe: Audio & Musik

## Zweck: TuxGuitar ist ein vielseitiger Open-Source-Editor und -Player für Gitarrentabulaturen und Partituren mit Unterstützung für verschiedene Dateiformate (GP3/GP4/GP5, PTB, TG) sowie MIDI- und PDF-Exportfunktion.

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

- `riff_master.tg`: Eine native TuxGuitar-Tabulaturdatei mit Songmetadaten, Instrumentenspuren und Notenmuster.
- `rock_classic.gp5`: Eine Tabulaturstruktur im Guitar Pro 5 Format mit Rock-Rhythmen und Akkorddiagrammen.
- `fingerpicking.ptb`: Eine Tabulaturdatei im PowerTab-Format für klassische Fingerstyle-Akkordzerlegungen.
- `tuning_presets.xml`: Eine XML-Konfigurationsdatei mit vordefinierten Gitarrenstimmungen (Standard E, Drop D, Open G).
- `tab_export.pdf`: Ein gerendertes Dokument eines Tabulatur-Exports zur Dokumentation und zum Notendruck.

## Validierung

Versionsprüfung und Headless-Funktionalität von TuxGuitar ausführen:

```bash
xvfb-run -a tuxguitar -v
```
