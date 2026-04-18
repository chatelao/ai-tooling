# Factsheet: Xvfb

## Gruppe: Infrastruktur

## Zweck

Xvfb (X Virtual Framebuffer) ist ein Display-Server, der das X11-Protokoll
implementiert, aber alle grafischen Operationen im virtuellen Speicher ausführt,
ohne eine physische Grafikhalle oder einen Monitor zu benötigen. Er ist
essenziell für KI-Agenten, die GUI-basierte Werkzeuge (wie Krita, Pencil2D oder
Bioinformatik-Viewer) in Headless-Umgebungen (CI/CD, Server) validieren müssen.

## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Referenzhandbuch

[Link](https://www.x.org/releases/X11R7.6/doc/man/man1/Xvfb.1.xhtml)

## Wikipedia

[Link](https://de.wikipedia.org/wiki/Xvfb)

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
