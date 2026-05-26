# Factsheet: Hexdump

## Gruppe: Firmware/analyse

## Zweck: Hexdump ist ein Dienstprogramm zur Anzeige von Dateiinhalten in hexadezimaler, dezimaler, oktaler oder ASCII-Darstellung.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 2.40 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [www.kernel.org/pub/linux/utils/util-linux](https://www.kernel.org/pub/linux/utils/util-linux/) |
| Wikipedia | [de.wikipedia.org/wiki/Hexdump](https://de.wikipedia.org/wiki/Hexdump) |

## Installation (Ubuntu 24.04)

```bash
sudo apt install bsdextrautils
```

## Hello World

```bash
echo "Hello" | hexdump -C
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `data.bin`
- `test.txt`
- `random.bin`
- `header.bin`
- `footer.bin`

## Validierung

Datei im Hex-Format anzeigen:

```bash
hexdump -C factsheets/firmware-analyse/hexdump/examples/data.bin
```
