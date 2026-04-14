# Factsheet: Xvfb

## Gruppe: Infrastruktur

## Zweck: Xvfb ist ein Werkzeug für


## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Installation (Ubuntu 24.04)

```bash
sudo apt install xvfb
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `start.sh`
- `stop.sh`
- `config.conf`
- `log.txt`
- `test.py`

## Validierung

Virtuellen Framebuffer starten:

```bash
Xvfb :99 -screen 0 1024x768x24 &
```
