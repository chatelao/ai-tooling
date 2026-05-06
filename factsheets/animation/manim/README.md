# Factsheet: Manim

## Gruppe: Animation

## Zweck: Manim ist eine von Grant Sanderson (3Blue1Brown) entwickelte Python-Bibliothek zur Erstellung präziser mathematischer Animationen.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [www.manim.community](https://www.manim.community/) |
| Wikipedia | [en.wikipedia.org/wiki/Manim](https://en.wikipedia.org/wiki/Manim) |

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install ffmpeg libcairo2-dev libpango1.0-dev
pip install manim
```

## Hello World

```python
from manim import *

class HelloWorld(Scene):
    def construct(self):
        self.add(Text("Hello World"))
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `example.py`: Grundlegendes Beispiel für die Animation eines Quadrats zu einem Kreis.
- `scene1.py`: Demonstration von geometrischen Grundformen und deren Animationen.
- `scene2.py`: Erstellung und Animation von mathematischen Formeln (LaTeX).
- `scene3.py`: Darstellung und Animation von Funktionsgraphen in einem Koordinatensystem.
- `scene4.py`: Beispiel für eine 3D-Szene mit einer Purple Sphere und Kamera-Rotation.

## Validierung

Rendern Sie eine einfache Szene:

```bash
manim -ql factsheets/animation/manim/examples/example.py SquareToCircle
```
