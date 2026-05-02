# Factsheet: Universal Radio Hacker (URH)

## Gruppe: Funktechnik

## Zweck: URH ist ein komplettes Toolkit für die Untersuchung unbekannter Funkprotokolle

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [Link](https://github.com/jopohl/urh) |
| Wikipedia | [Link](https://en.wikipedia.org/wiki/Software-defined_radio) |

## Installation (Ubuntu 24.04)

```bash
pip install urh
```

## Hello World

```bash
urh --version
```

## Validierung

```bash
xvfb-run -a urh --version
```
