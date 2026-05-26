# Factsheet: Redocly CLI

## Gruppe: Dokumentation

## Zweck: Redocly CLI ist ein CLI für OpenAPI-Dokumentation, Linting und Bündelung

Redocly CLI bietet Werkzeuge zum Validieren (Linting), Bündeln (Bundling) und
Rendern von OpenAPI-Spezifikationen. Es kann statische HTML-Dokumentationen
generieren und APIs in der Vorschau anzeigen.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 1.25.0 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [redocly.com/docs/cli](https://redocly.com/docs/cli/) |
| Wikipedia | [en.wikipedia.org/wiki/OpenAPI_Specification](https://en.wikipedia.org/wiki/OpenAPI_Specification) |

## Installation (Ubuntu 24.04)

```bash
npm install @redocly/cli
```

## Hello World

```bash
redocly lint openapi.yaml
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `api.yaml`: Eine OpenAPI-Spezifikation für die Dokumentationserstellung.
- `redocly.yaml`: Konfigurationsdatei für Redocly.
- `bundle.sh`: Skript zum Bündeln mehrteiliger API-Definitionen.
- `build-docs.sh`: Skript zum Generieren statischer HTML-Dokumentation.
- `preview.sh`: Skript zur Vorschau der API-Dokumentation.
- `rules.yaml`: Beispiel für benutzerdefinierte Linting-Regeln.

## Validierung

OpenAPI-Schema validieren:

```bash
npx @redocly/cli lint factsheets/dokumentation/redocly-cli/examples/api.yaml
```
