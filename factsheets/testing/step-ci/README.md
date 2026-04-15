# Factsheet: Step ci

## Gruppe: Testing

## Zweck: Step-ci ist ein Werkzeug für automatisierte API-Tests und Monitoring

Step CI ist ein deklaratives Framework zum Testen und Überwachen von REST-, GraphQL- und gRPC-APIs. Tests werden in YAML oder JSON definiert und können einfach in CI/CD-Pipelines integriert werden.


## Reifegrad

Stabil




## Technische Schulden

Gering




## Erwartetes Lebensende

Kein EOL bekannt




## Installation (Ubuntu 24.04)

```bash
npm install -g stepci
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `workflow.yml`: Definition des Test-Workflows.
- `test.js`: Zusätzliche Testlogik in JavaScript.
- `config.json`: Globale Konfiguration.
- `env.env`: Umgebungsvariablen für Tests.
- `output.txt`: Beispielhafte Testausgabe.

## Validierung

Step CI Test ausführen:

```bash
stepci run factsheets/testing/step-ci/examples/workflow.yml
```
