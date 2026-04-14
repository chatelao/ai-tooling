# Factsheet: Spectral

## Gruppe: Testing

## Zweck: Spectral ist ein flexibler Linter für JSON/YAML, spezialisiert auf OpenAPI

Spectral ermöglicht das Linting von API-Beschreibungen (OpenAPI v2/v3, AsyncAPI),
um die Einhaltung von Best Practices und Design-Richtlinien sicherzustellen. Es
ist hochgradig erweiterbar durch eigene Regelsätze.


## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Installation (Ubuntu 24.04)

```bash
npm install @stoplight/spectral-cli
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `api.yaml`: Eine einfache, valide OpenAPI-Spezifikation.
- `invalid.yaml`: Eine OpenAPI-Spezifikation mit absichtlichen Design-Fehlern.
- `.spectral.yaml`: Standard-Konfigurationsdatei für Spectral.
- `custom-ruleset.yaml`: Ein Beispiel für benutzerdefinierte Regeln.
- `lint.sh`: Shell-Skript zur Ausführung des Linting-Prozesses.

## Validierung

OpenAPI-Schema linten:

```bash
npx spectral lint factsheets/testing/spectral/examples/api.yaml --ruleset factsheets/testing/spectral/examples/.spectral.yaml
```
