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
