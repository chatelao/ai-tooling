# Factsheet: Universal Radio Hacker (URH)

## Gruppe: Funktechnik

## Zweck: URH ist ein komplettes Toolkit für die Untersuchung unbekannter Funkprotokolle

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [github.com/jopohl/urh](https://github.com/jopohl/urh) |
| Wikipedia | [en.wikipedia.org/wiki/Software-defined_radio](https://en.wikipedia.org/wiki/Software-defined_radio) |

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
