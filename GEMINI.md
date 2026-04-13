# Strategie für KI-Agenten-Werkzeuge & Quellen

Diese Dokumentation dient als zentrale Anlaufstelle für KI-Agenten, um Werkzeuge
auf einem Linux/Ubuntu-System zu identifizieren, zu dokumentieren und aktuell zu
halten.

## 1. Strategie zur Verwaltung von Werkzeugen

### Sammeln (Discovery)

- **Automatisierter Scan:** Regelmäßige Überprüfung installierter Pakete über
  Paketmanager (`apt`), Sprach-Runtimes (`pip list`, `npm list -g`,
  `cargo install --list`) und Umgebungsvariablen.
- **Repository-Analyse:** Durchsuchen lokaler Projekte nach Abhängigkeiten in
  `package.json`, `requirements.txt`, `go.mod` und `Cargo.toml`.
- **System-Profiling:** Identifikation von Hardware-Ressourcen (CPU/GPU) sowie
  möglicher MCP zur Bestimmung der Eignung für lokale Inferenz.

### Dokumentieren (Documentation)

#### Werkzeuge

- **Speicherort:** Führe die Werkzeuge  in [TOOLS.md](TOOLS.md)
- **Format:** Die Werkzeuge werden in Tabellenform dokumentiert.
- **Inhalte:** Jedes Werkzeug wird mit Gruppe, Name, Zweck, Installationsbefehle
  in der Tabelle geführt, Referenzhandbuch, Factsheet.
- **Installierbarkeit:** Vor der Aufnahme in die Liste wird die Software auf
  Installierbarkeit geprüft.
- **Validierung:** Nach erfolgreicher Installation wird ein Log-File
  `<script_name>.log` neben dem Installationsskript erstellt. Zur Bestätigung
  eines validen Skripts wird zudem eine Datei mit dem SHA256-Hash des Skripts im
  Format `<hash>.verified..hash` im selben Verzeichnis abgelegt.

#### Factsheets

- **Speicherort:** Jedes Werkzeug erhält ein Factsheet unter
  `factsheets/<gruppe>/<name>/README.md`.
- **Inhalte:** Name, Gruppe, Zweck, detaillierte Installationsanleitung,
  Beispieldaten, Validierungsschritte.
- **Beispiele:** Zu jedem Werkzeug werden 5-10 Beispieldaten im Ordner
  `examples/` des jeweiligen Factsheets bereitgestellt.

#### Datenquellen/-sammlungen

- **Speicherort:** Führe die Werkzeuge  in [DATASOURCES.md](DATASOURCES.md)
- **Format:** Die Datensammlungen werden ebenfalls in Tabellenform dokumentiert.
- **Inhalte:** Jedes Sammlung wird mit Gruppe, Name, Zweck, Zugriffarten zum
  Beschaffung und/oder Abfrage beschrieben, Referenzhandbuch
- **Abfragbarkeit:** Vor der Aufnahme in die Liste wird die Software auf
  Installierbarkeit geprüft.

#### Visualisierungen

- **Speicherort:** Führe die Mappings von Ergebnissen zu Werkzeugen in
  [VISUALIZATION.md](VISUALIZATION.md)
- **Format:** Die Zuordnungen werden in Tabellenform dokumentiert.
- **Inhalte:** Jeder Eintrag enthält den Visualisierungstyp, das Werkzeug und
  die Gruppe.
