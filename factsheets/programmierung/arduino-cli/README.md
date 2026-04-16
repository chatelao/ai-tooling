# Factsheet: Arduino cli

## Gruppe: Programmierung

## Zweck

Die Arduino CLI ist ein All-in-One-Kommandozeilenwerkzeug, das alle Funktionen
der Arduino IDE (Kompilieren, Hochladen, Bibliotheksverwaltung) bietet. Sie
ermöglicht es KI-Agenten, Firmware für Mikrocontroller autonom zu entwickeln,
zu bauen und auf Hardware zu flashen, ohne auf eine grafische Oberfläche
angewiesen zu sein.

## Reifegrad

Stabil (Aktiv gewartet, v1.4.1 Stand Jan 2026)

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Wikipedia

[Link](https://de.wikipedia.org/wiki/Arduino_(Plattform))

## Installation (Ubuntu 24.04)

```bash
curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | BINDIR=$HOME/.local/bin sh
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `sketch.ino`
- `config.yaml`
- `lib.zip`
- `board.json`
- `output.hex`

## Validierung

Version prüfen:

```bash
arduino-cli version
```
