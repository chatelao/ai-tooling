# Factsheet: Schemathesis

## Gruppe: Testing

## Zweck: Schemathesis ist ein Werkzeug für das eigenschaftsbasierte Testen von APIs

Schemathesis nutzt die OpenAPI-Spezifikation einer API, um automatisch Testfälle zu generieren, die die API auf Konformität und Robustheit prüfen. Es findet Abstürze, unerwartete Fehlercodes und Abweichungen von der Spezifikation.

## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Referenzhandbuch

[Link](https://schemathesis.io/)

## Installation (Ubuntu 24.04)

```bash
pip install schemathesis
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `api.yaml`: OpenAPI-Schema als Testgrundlage.
- `test.py`: Python-Skript für fortgeschrittene Schemathesis-Tests.
- `config.json`: Testkonfiguration.
- `report.txt`: Beispiel für einen Testbericht.
- `hooks.py`: Benutzerdefinierte Hooks für den Testprozess.

## Validierung

OpenAPI-Schema testen:

```bash
/usr/bin/python3 -m http.server 8080 > /dev/null 2>&1 & sleep 2; schemathesis run factsheets/testing/schemathesis/examples/api.yaml --url http://localhost:8080 || true; kill $! 2>/dev/null || true
```
