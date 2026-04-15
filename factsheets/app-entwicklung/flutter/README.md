# Factsheet: Flutter

## Gruppe: App-Entwicklung

## Zweck

Flutter ist ein UI-Toolkit von Google für die Entwicklung nativ kompilierter
Anwendungen für Mobile, Web und Desktop aus einer einzigen Codebasis.


## Reifegrad

Stabil




## Technische Schulden

Gering




## Erwartetes Lebensende

Kein EOL bekannt




## Installation (Ubuntu 24.04)

Flutter ist im System unter `/opt/flutter/bin/flutter` vorinstalliert.

```bash
export PATH="$PATH:/opt/flutter/bin"
flutter doctor
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `main.dart` (Einfache App-Struktur)
- `pubspec.yaml` (Projektkonfiguration)
- `widget_test.dart` (Beispiel-Test)
- `analysis_options.yaml` (Linter-Konfiguration)

## Validierung

Version prüfen:

```bash
flutter --version
```
