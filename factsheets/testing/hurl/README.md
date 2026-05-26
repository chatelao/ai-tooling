# Factsheet: Hurl

## Gruppe: Testing

## Zweck

Hurl ist ein Kommandozeilenwerkzeug zum Ausführen von HTTP-Anfragen, die in
einem einfachen Textformat definiert sind. Es kann sowohl für API-Tests als
auch für Web-Tests verwendet werden und zeichnet sich durch seine Schnelligkeit
und einfache Syntax aus. KI-Agenten nutzen Hurl, um REST- oder SOAP-Endpunkte
autonom zu validieren.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 5.0.0 |
| LTS | N/A |
| Reifegrad | Stabil (Aktiv gewartet, v7.1.0 Stand Nov 2025) |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [hurl.dev](https://hurl.dev/) |

## Installation (Ubuntu 24.04)

```bash
sudo add-apt-repository ppa:lepapareil/hurl; sudo apt update; sudo apt install hurl
```

## Hello World

```hurl
GET http://localhost:3000
HTTP 200
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `test.hurl`: Einfacher GET-Request Test.
- `ex1.hurl`: POST-Request mit JSON-Body und Feld-Validierung.
- `ex2.hurl`: Test mit Custom Headers, Bearer Token und Cookie-Prüfung.
- `ex3.hurl`: Mehrstufiger Test mit Variablen-Capture (Chaining).
- `ex4.hurl`: Test von Redirects und Basic Authentication.

## Validierung

Hurl-Anfrage ausführen:

```bash
hurl factsheets/testing/hurl/examples/test.hurl
```
