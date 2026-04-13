# Factsheet: Prism

## Gruppe: Testing

## Zweck: Prism ist ein Mock-Server für OpenAPI-Spezifikationen

Prism ermöglicht es, basierend auf einer OpenAPI-Spezifikation (v2/v3),
automatisch Mock-Server zu erstellen. Diese Server können API-Anfragen
validieren und basierend auf dem Schema realistische Beispiel-Antworten
generieren.


## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Installation (Ubuntu 24.04)

```bash
npm install @stoplight/prism-cli
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `api.yaml`: Eine OpenAPI-Spezifikation für die Generierung des Mock-Servers.
- `prism-config.json`: Beispiel für eine Prism-Konfigurationsdatei.
- `run-mock.sh`: Skript zum Starten des Mock-Servers.
- `proxy.sh`: Skript zur Nutzung von Prism als Validierungsproxy.
- `validate-request.sh`: Beispiel für eine Anfrage-Validierung.

## Validierung

Mock-Server starten:

```bash
npx prism mock factsheets/testing/prism/examples/api.yaml
```
