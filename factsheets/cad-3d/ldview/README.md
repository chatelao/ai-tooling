# Factsheet: Ldview

## Gruppe: Cad/3d

## Zweck: LDView ist ein Echtzeit-3D-Viewer für LDraw-LEGO-Modelle mit Hardware-Beschleunigung.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 4.7 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [tc3d.com/ldview](https://tc3d.com/ldview/) |
| Wikipedia | [en.wikipedia.org/wiki/LDraw](https://en.wikipedia.org/wiki/LDraw) |

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install -y libosmesa6
curl -L http://download.opensuse.org/repositories/home:/pbartfai/xUbuntu_24.04/amd64/ldview-osmesa_4.7-1_amd64.deb -o ldview.deb; sudo apt install ./ldview.deb
```

## Hello World

```bash
ldview --version
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
mkdir -p ~/.config/LDView && touch ~/.config/LDView/ldviewrc
xvfb-run -a ldview factsheets/cad-3d/ldview/examples/model.ldr
```
