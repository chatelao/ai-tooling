# Factsheet: Yara

## Gruppe: Firmware/analyse

## Zweck: YARA ist ein Werkzeug zur Identifizierung und Klassifizierung von Malware-Mustern basierend auf textuellen oder binären Regeln.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [virustotal.github.io/yara](https://virustotal.github.io/yara/) |
| Wikipedia | [de.wikipedia.org/wiki/YARA](https://de.wikipedia.org/wiki/YARA) |

## Installation (Ubuntu 24.04)

```bash
sudo apt install yara
```

## Hello World

```yara
rule hello { condition: true }
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `rule.yar`
- `test.bin`
- `malware.bin`
- `clean.bin`
- `sample.bin`

## Validierung

YARA-Regel anwenden:

```bash
yara factsheets/firmware-analyse/yara/examples/rule.yar factsheets/firmware-analyse/yara/examples/test.bin
```
