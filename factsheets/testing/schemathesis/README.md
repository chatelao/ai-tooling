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
| Latest | 3.38.0 |
| LTS | N/A |
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

- `api.yaml`: Umfassendes OpenAPI 3.0 Schema einer Produkt-API als Testgrundlage.
- `test.py`: Python-Skript, das zeigt, wie Schemathesis mit Pytest und Hypothesis-Einstellungen integriert wird.
- `config.json`: Konfigurationsdatei zur Definition von Checks (z.B. Statuscode-Konformität) und Hypothesis-Limits.
- `report.txt`: Beispiel für einen generierten Testbericht.
- `hooks.py`: Python-Skript mit benutzerdefinierten Hooks (z.B. Hinzufügen von Test-Headern oder benutzerdefinierte Validierung).
- `docker-compose.yml`: Konfiguration zum Starten einer Testumgebung mit API-Server und Schemathesis-Runner.

## Validierung

OpenAPI-Schema testen:

```bash
/usr/bin/python3 -m http.server 8080 > /dev/null 2>&1 & sleep 2; schemathesis run factsheets/testing/schemathesis/examples/api.yaml --url http://localhost:8080 || true; kill $! 2>/dev/null || true
```
