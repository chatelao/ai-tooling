# Factsheet: Step ci

## Gruppe: Testing

## Zweck

Step CI ist ein modernes, deklaratives Framework für automatisierte API-Tests und Monitoring. Es unterstützt REST, GraphQL und gRPC und ermöglicht es Entwicklern, komplexe Test-Workflows in einfachen YAML- oder JSON-Dateien zu definieren.

Einsatzbereiche:
- Regressionstests in CI/CD-Pipelines (z.B. GitHub Actions).
- Kontinuierliches Monitoring der API-Verfügbarkeit und Performance.
- Lasttests und Validierung von Antwortzeiten.
- Unterstützung für Sicherheits-Checks und Datenvalidierung.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [stepci.com](https://stepci.com/) |

## Installation (Ubuntu 24.04)

```bash
npm install -g stepci
```

## Hello World

```bash
step-ci run workflow.yml
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `workflow.yml`: Definition eines REST-API Test-Workflows.
- `graphql_test.yml`: Definition eines GraphQL-API Tests.
- `test.js`: Zusätzliche Testlogik in JavaScript.
- `config.json`: Globale Konfiguration.
- `env.env`: Umgebungsvariablen für Tests.
- `output.txt`: Beispielhafte Testausgabe.

## Validierung

Step CI Test ausführen:

```bash
stepci run factsheets/testing/step-ci/examples/workflow.yml
```
