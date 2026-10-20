# Factsheet: Frescobaldi

## Gruppe: Audio & Musik

## Zweck: Frescobaldi ist eine spezialisierte Open-Source-Editor-Umgebung für den LilyPond-Notensatz mit integrierter Partitur-Vorschau, Syntax-Hervorhebung, MIDI-Wiedergabe und automatisierten Formatierungswerkzeugen.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 3.3.0 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [frescobaldi.org](https://frescobaldi.org/) |
| Wikipedia | [de.wikipedia.org/wiki/Frescobaldi_(Software)](https://de.wikipedia.org/wiki/Frescobaldi_(Software)) |

## Installation (Ubuntu 24.04)

```bash
sudo apt-get update && sudo apt-get install -y frescobaldi xvfb
```

## Hello World

```bash
xvfb-run -a frescobaldi --version
```

## Beispiele

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `template_orchestra.ly`: Eine LilyPond-Partiturvorlage für Orchester mit mehreren Stimmgruppen, Taktarten und Layout-Optionen.
- `frescobaldi_session.xml`: Eine XML-Session-Konfigurationsdatei zur Wiederherstellung geöffneter Dokumente, Ansichten und Cursor-Positionen.
- `snippet_library.xml`: Eine Sammlung von Frescobaldi-Code-Snippets für häufig genutzte LilyPond-Notationskonstrukte und Makros.
- `midi_settings.ini`: Eine Konfigurationsdatei für MIDI-Ausgabe-Instrumente, Lautstärke, Ports und Synthesizer-Zuordnungen.
- `shortcut_scheme.xml`: Ein benutzerdefiniertes Tastaturkürzel-Schema im XML-Format zur Optimierung des Editier-Workflows.

## Validierung

Versionsprüfung und Headless-Funktionalität von Frescobaldi ausführen:

```bash
xvfb-run -a frescobaldi --version
```
