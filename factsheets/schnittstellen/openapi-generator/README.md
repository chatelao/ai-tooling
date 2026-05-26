# Factsheet: Openapi generator

## Gruppe: Schnittstellen

## Zweck

Der OpenAPI Generator ist ein vielseitiges Werkzeug für die automatische Codegenerierung basierend auf OpenAPI-Spezifikationen (v2 und v3). Er hilft Entwicklern, Konsistenz zwischen API-Definition und Implementierung zu gewährleisten, indem er Boilerplate-Code automatisiert erstellt.

Funktionen:
- Generierung von API-Clients für über 50 Programmiersprachen.
- Erstellung von Server-Stubs für zahlreiche Frameworks (z.B. Spring Boot, Go, Node.js).
- Automatisierte Erstellung von API-Dokumentationen (HTML, Markdown).
- Generierung von Konfigurationsdateien und Postman-Kollektionen.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 7.10.0 |
| LTS | N/A |
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
