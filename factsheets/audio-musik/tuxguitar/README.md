# Factsheet: TuxGuitar

## Gruppe: Audio & Musik

## Zweck: TuxGuitar ist ein plattformübergreifender Open-Source-Multitrack-Tabulatureditior und -Player zur Notationserstellung, Wiedergabe sowie zum Import und Export gängiger Formate (Guitar Pro, PowerTab, MIDI, PDF).

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

- `riff_master.tg`: Eine native TuxGuitar-Songdatei mit Mehrspur-Gitarrennotation, Taktstruktur und Instrumentenzuweisung.
- `rock_classic.gp5`: Eine Beispieldatei im Guitar-Pro-5-Format zur Demonstration der Formatkompatibilität und des Re-Imports.
- `fingerpicking.ptb`: Eine Beispieldatei im PowerTab-Format für akustische Gitarrenarrangements.
- `tuning_presets.xml`: Eine XML-Konfigurationsdatei zur Definition benutzerdefinierter Gitarren-Stimmungen (z. B. Standard E, Drop D, Open G).
- `tab_export.pdf`: Eine aus TuxGuitar gerenderte Beispiel-Exportdatei im PDF-Format zur Druck- und Notenanzeige.

## Validierung

Versionsprüfung und Headless-Funktionalität von TuxGuitar ausführen:

```bash
xvfb-run -a tuxguitar -v
```
