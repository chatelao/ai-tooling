# Factsheet: Openapi generator

## Gruppe: Schnittstellen

## Zweck: Openapi-generator ist ein Werkzeug für die automatische Codegenerierung

Das Tool ermöglicht die Generierung von API-Clients, Server-Stubs, Dokumentationen und Konfigurationsdateien aus OpenAPI-Spezifikationen (v2, v3). Es unterstützt eine Vielzahl von Programmiersprachen und Frameworks.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil (Aktiv gewartet, v7.21.0 Stand März 2026) |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [openapi-generator.tech](https://openapi-generator.tech/) |

## Installation (Ubuntu 24.04)

```bash
npm install @openapitools/openapi-generator-cli
```

## Hello World

```bash
openapi-generator-cli version
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `api.yaml`: Eine Beispiel-OpenAPI-Spezifikation.
- `petstore.yaml`: Standard Petstore-Beispiel.
- `config.json`: Konfiguration für den Generator.
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
