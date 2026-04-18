# Factsheet: Ldview

## Gruppe: Cad/3d

## Zweck: Ldview ist ein Werkzeug für

## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Referenzhandbuch

[Link](https://tc3d.com/ldview/)

## Wikipedia

[Link](https://en.wikipedia.org/wiki/LDraw)

## Installation (Ubuntu 24.04)

```bash
curl -L http://download.opensuse.org/repositories/home:/pbartfai/xUbuntu_24.04/amd64/ldview-osmesa_4.7-1_amd64.deb -o ldview.deb; sudo apt install ./ldview.deb
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `model.ldr`
- `car.ldr`
- `house.ldr`
- `tree.ldr`
- `brick.dat`

## Validierung

LDView ausführen:

```bash
ldview factsheets/cad-3d/ldview/examples/model.ldr
```
