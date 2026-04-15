# Factsheet: Hurl

## Gruppe: Testing

## Zweck

Hurl ist ein Kommandozeilenwerkzeug zum Ausführen von HTTP-Anfragen, die in
einem einfachen Textformat definiert sind. Es kann sowohl für API-Tests als
auch für Web-Tests verwendet werden und zeichnet sich durch seine Schnelligkeit
und einfache Syntax aus. KI-Agenten nutzen Hurl, um REST- oder SOAP-Endpunkte
autonom zu validieren.


## Reifegrad

Stabil (Aktiv gewartet, v7.1.0 Stand Nov 2025)




## Technische Schulden

Gering




## Erwartetes Lebensende

Kein EOL bekannt




## Installation (Ubuntu 24.04)

```bash
sudo add-apt-repository ppa:lepapareil/hurl; sudo apt update; sudo apt install hurl
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `test.hurl`
- `ex1.hurl`
- `ex2.hurl`
- `ex3.hurl`
- `ex4.hurl`

## Validierung

Hurl-Anfrage ausführen:

```bash
hurl factsheets/testing/hurl/examples/test.hurl
```
