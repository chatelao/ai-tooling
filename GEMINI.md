# Strategie für KI-Agenten-Werkzeuge & Quellen

Diese Dokumentation dient als zentrale Anlaufstelle für KI-Agenten, um Werkzeuge auf einem Linux/Ubuntu-System zu identifizieren, zu dokumentieren und aktuell zu halten.

## 1. Strategie zur Verwaltung von Werkzeugen

### Sammeln (Discovery)
- **Automatisierter Scan:** Regelmäßige Überprüfung installierter Pakete über Paketmanager (`apt`), Sprach-Runtimes (`pip list`, `npm list -g`, `cargo install --list`) und Umgebungsvariablen.
- **Repository-Analyse:** Durchsuchen lokaler Projekte nach Abhängigkeiten in `package.json`, `requirements.txt`, `go.mod` und `Cargo.toml`.
- **System-Profiling:** Identifikation von Hardware-Ressourcen (CPU/GPU) zur Bestimmung der Eignung für lokale Inferenz.

### Dokumentieren (Documentation)
#### Werkzeuge
- **Format:** Die Werkzeuge werden in Tabellenform dokumentiert.
- **Inhalte:** Jedes Werkzeug wird mit Name, Zweck, Referenzhandbuch, Installationsbefehle in der Tabelle geführt
- **Installierbarkeit:** Vor der Aufnahme in die Liste wird die Software auf Installierbarkeit geprüft.

#### Datenqullen/-sammlungen
- **Format:** Die Datensammlungen werden ebenfalls in Tabellenform dokumentiert.
- **Inhalte:** Jedes Sammlung wird mit Name, Zweck, Referenzhandbuch sowie Zugriffarten zum Beschaffung und/oder Abfrage beschrieben
- **Abfragbarkeit:** Vor der Aufnahme in die Liste wird die Software auf Installierbarkeit geprüft.
