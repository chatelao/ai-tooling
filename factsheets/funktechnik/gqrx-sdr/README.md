# Factsheet: Gqrx SDR

## Gruppe: Funktechnik

## Zweck: Gqrx ist ein Open-Source-SDR-Empfänger mit grafischer Benutzeroberfläche

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [gqrx.dk/doc/user-manual](https://gqrx.dk/doc/user-manual) |
| Wikipedia | [en.wikipedia.org/wiki/Gqrx](https://en.wikipedia.org/wiki/Gqrx) |

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo touch /etc/modules
sudo apt install -y gqrx-sdr
```

## Hello World

```bash
gqrx --version
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `bookmarks.csv`: Beispiel für Frequenz-Lesezeichen.
- `remote_control.py`: Python-Skript zur Fernsteuerung über TCP (rigctld-Protokoll).
- `gqrx_settings.conf`: Beispiel für eine Konfigurationsdatei.
- `udp_stream.sh`: Hinweis zum Starten mit UDP-Streaming.
- `record_wav.sh`: Hinweis zur Audio-Aufzeichnung.

## Validierung

```bash
xvfb-run -a gqrx -h 2>&1 | grep -i "Usage: gqrx"
```
