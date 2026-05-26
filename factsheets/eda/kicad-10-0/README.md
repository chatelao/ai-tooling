# Factsheet: Kicad 10 0

## Gruppe: Eda

## Zweck: KiCad 10.0 ist eine Suite für das Design von elektronischen Schaltungen und Leiterplatten (EDA).

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 8.0.6 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [www.kicad.org](https://www.kicad.org/) |
| Wikipedia | [de.wikipedia.org/wiki/KiCad](https://de.wikipedia.org/wiki/KiCad) |

## Installation (Ubuntu 24.04)

```bash
sudo add-apt-repository ppa:kicad/kicad-10.0-releases; sudo apt update; sudo apt install --install-recommends kicad
```

## Hello World

```bash
kicad --version
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
