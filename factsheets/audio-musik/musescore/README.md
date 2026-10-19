# Factsheet: MuseScore

## Gruppe: Audio & Musik

## Zweck: MuseScore ist ein plattformübergreifendes Open-Source-Notensatzprogramm zur graphischen Noteneingabe, Wiedergabe und zum Multi-Format-Export (PDF, PNG, MIDI, MusicXML) inkl. Headless-CLI-Batch-Konvertierung.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 3.2.3 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [musescore.org/de/handbuch](https://musescore.org/de/handbuch) |
| Wikipedia | [de.wikipedia.org/wiki/MuseScore](https://de.wikipedia.org/wiki/MuseScore) |

## Installation (Ubuntu 24.04)

```bash
sudo apt-get update && sudo apt-get install -y musescore3 xvfb
```

## Hello World

```bash
xvfb-run -a musescore3 --version
```

## Beispiele

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `lead_sheet.mscx`: Eine unkomprimierte MuseScore-Partitur-Datei im XML-Format mit Notenstrukturen, Stimmführung und Instrumenten-Layout.
- `quartet.mscz`: Eine komprimierte MuseScore-Partitur-Datei im Container-Format für vollständige Musikstücke.
- `score_export.musicxml`: Eine im MusicXML-Standard formatierte Partitur-Datei zum plattformübergreifenden Austausch.
- `piano_part.pdf`: Eine aus MuseScore gerenderte Partitur-Exportdatei im PDF-Format für Druck und Notensatzdarstellung.
- `style_settings.mss`: Eine MuseScore-Stildatei im XML-Format zur Anpassung von Schriftarten, Spatien und Notengravur-Parametern.

## Validierung

Start und Systemaufruf von MuseScore im Headless-Modus prüfen:

```bash
xvfb-run -a musescore3 --version
```
