# Factsheet: Kicad 10 0

## Gruppe: Eda

## Zweck: KiCad 10.0 ist eine Suite für das Design von elektronischen Schaltungen und Leiterplatten (EDA).

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [Link](https://www.kicad.org/) |
| Wikipedia | [Link](https://de.wikipedia.org/wiki/KiCad) |

## Installation (Ubuntu 24.04)

```bash
sudo add-apt-repository ppa:kicad/kicad-10.0-releases; sudo apt update; sudo apt install --install-recommends kicad
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `project.kicad_pro`
- `pcb.kicad_pcb`
- `sch.kicad_sch`
- `lib.kicad_sym`
- `fp.kicad_mod`

## Validierung

KiCad-Version prüfen:

```bash
kicad-cli --version
```
