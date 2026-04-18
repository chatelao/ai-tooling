# Factsheet: Zeep

## Gruppe: Schnittstellen

## Zweck: Zeep ist eine moderne SOAP-Client-Bibliothek für Python, die WSDL-Dateien parst und eine komfortable API bietet

## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Referenzhandbuch

[Link](https://docs.python-zeep.org/)

## Wikipedia

[Link](https://de.wikipedia.org/wiki/SOAP)

## Installation (Ubuntu 24.04)

```bash
sudo apt install python3-zeep
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `service.wsdl`: Eine Beispiel-WSDL-Datei.
- `client.py`: Ein Python-Skript, das Zeep zur Kommunikation nutzt.
- `request.xml`: Eine Beispiel-SOAP-Anfrage.
- `response.xml`: Eine Beispiel-SOAP-Antwort.
- `schema.xsd`: Begleitendes XML-Schema für den Service.

## Validierung

WSDL-Datei inspizieren:

```bash
python3 -m zeep factsheets/schnittstellen/zeep/examples/service.wsdl
```

Beispiel-Client ausführen (erfordert evtl. Mock-Server oder Netzwerk):

```bash
python3 factsheets/schnittstellen/zeep/examples/client.py
```
