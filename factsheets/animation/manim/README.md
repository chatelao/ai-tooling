# Factsheet: Manim

## Gruppe: Animation

## Zweck: Manim ist ein Werkzeug für

## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Wikipedia

[Link](https://en.wikipedia.org/wiki/Manim)

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install ffmpeg libcairo2-dev libpango1.0-dev
pip install manim
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `example.py`
- `scene1.py`
- `scene2.py`
- `scene3.py`
- `scene4.py`

## Validierung

Rendern Sie eine einfache Szene:

```bash
manim -ql factsheets/animation/manim/examples/example.py SquareToCircle
```
