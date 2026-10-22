# Factsheet: TuxGuitar

## Gruppe: Audio & Musik

## Zweck: TuxGuitar ist ein vielseitiger Open-Source-Gitarren-Tabulatur-Editor und -Player zur Notation, Transkription und Wiedergabe von Multitrack-Partituren für Gitarre, Bass und Ensembles.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 1.5.6 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [tuxguitar.app](https://tuxguitar.app/) |
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

- `riff_master.tg`: NATIVE TuxGuitar-Partiturdatei mit mehrspuriger Gitarren- und Bassnotierung.
- `rock_classic.gp5`: Eine Beispieldatei im Guitar Pro 5 (.gp5) Format für maximale Kompatibilität mit etablierten Tabulatur-Standards.
- `fingerpicking.ptb`: Eine PowerTab (.ptb) Transkriptionsdatei für Fingerstyle-Gitarrenarrangements.
- `tuning_presets.xml`: Eine XML-Konfigurationsdatei mit benutzerdefinierten Gitarren-Stimmungen (Drop D, DADGAD, Open G, Standard).
- `tab_export.pdf`: Eine aus TuxGuitar gerenderte PDF-Partitur zur visuellen Darstellung der Notations- und Tabulaturausgabe.

## Validierung

Versionsprüfung und Headless-Funktionalität von TuxGuitar ausführen:

```bash
xvfb-run -a tuxguitar -v
```
