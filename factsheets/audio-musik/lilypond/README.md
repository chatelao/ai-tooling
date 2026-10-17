# Factsheet: LilyPond

## Gruppe: Audio & Musik

## Zweck: LilyPond ist ein automatisierter Notensatz-Compiler zur Erzeugung qualitativ hochwertiger Notengravuren im PDF-, PNG- und MIDI-Format.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 2.24.3 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [lilypond.org](https://lilypond.org/) |
| Wikipedia | [de.wikipedia.org/wiki/LilyPond](https://de.wikipedia.org/wiki/LilyPond) |

## Installation (Ubuntu 24.04)

```bash
sudo apt-get update && sudo apt-get install -y lilypond
```

## Hello World

```bash
lilypond --png --pdf -o output examples/symphony_theme.ly
```

## Beispiele

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `symphony_theme.ly`: Das Haupt-LilyPond-Quellskript mit Notensequenz, Partitur-Struktur und Einbindung externer Konfigurationen.
- `chords_header.ily`: Eine LilyPond-Include-Datei zur Definition von Akkordfolgen und harmonischen Strukturen.
- `paper_layout.ily`: Eine Include-Datei zur Festlegung des Seitenlayouts, der Ränder und Notensatz-Formate.
- `rendered_score.pdf`: Das aus der Quelldatei kompilierte Partitur-Dokument im PDF-Format.
- `rendered_score.mid`: Die aus der Partitur erzeugte MIDI-Datei zur akustischen Wiedergabe und Validierung.

## Validierung

Notensatz-Kompilierung im Headless-Modus prüfen:

```bash
lilypond --version
lilypond --pdf --png -o examples/rendered_score examples/symphony_theme.ly
```
