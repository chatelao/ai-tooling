# Factsheet: Schemathesis

## Gruppe: Testing

## Zweck

Schemathesis ist ein leistungsstarkes Werkzeug für das eigenschaftsbasierte Testen (Property-based Testing) von APIs. Es nutzt die OpenAPI- oder GraphQL-Spezifikation einer API, um automatisch eine Vielzahl von Testfällen zu generieren, die die API auf Konformität, Robustheit und Sicherheit prüfen.

Vorteile:
- Automatisches Finden von Abstürzen und unerwarteten Fehlern (5xx).
- Verifizierung der Spezifikationstreue (Validierung von Response-Schemas).
- Integration in Python-Test-Suites (Pytest) oder als Standalone-CLI.
- Unterstützung für zustandshafte Tests und komplexe Workflows.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [schemathesis.io](https://schemathesis.io/) |

## Installation (Ubuntu 24.04)

```bash
pip install schemathesis
```

## Hello World

```bash
schemathesis run http://localhost:8080/openapi.json
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `api.yaml`: OpenAPI-Schema als Testgrundlage.
- `test.py`: Python-Skript für fortgeschrittene Schemathesis-Tests.
- `config.json`: Testkonfiguration.
- `report.txt`: Beispiel für einen Testbericht.
- `hooks.py`: Benutzerdefinierte Hooks für den Testprozess.
- `docker-compose.yml`: Docker Compose Konfiguration für API-Tests.

## Validierung

OpenAPI-Schema testen:

```bash
/usr/bin/python3 -m http.server 8080 > /dev/null 2>&1 & sleep 2; schemathesis run factsheets/testing/schemathesis/examples/api.yaml --url http://localhost:8080 || true; kill $! 2>/dev/null || true
```
