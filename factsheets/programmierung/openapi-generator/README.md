# Factsheet: Openapi generator

## Gruppe: Programmierung

## Zweck: Openapi-generator ist ein Werkzeug für die automatische Codegenerierung

Das Tool ermöglicht die Generierung von API-Clients, Server-Stubs, Dokumentationen und Konfigurationsdateien aus OpenAPI-Spezifikationen (v2, v3). Es unterstützt eine Vielzahl von Programmiersprachen und Frameworks.


## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Installation (Ubuntu 24.04)

```bash
npm install @openapitools/openapi-generator-cli
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `api.yaml`: Eine Beispiel-OpenAPI-Spezifikation.
- `config.json`: Konfiguration für den Generator.
- `out.sh`: Skript zur Ausführung der Codegenerierung.
- `test.json`: Beispieldaten für Tests.
- `doc.md`: Generierte Dokumentationsvorschau.

## Validierung

Hilfe anzeigen:

```bash
npx @openapitools/openapi-generator-cli help
```

Verfügbare Generatoren auflisten:

```bash
npx @openapitools/openapi-generator-cli list
```
