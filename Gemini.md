# Strategie für KI-Agenten-Werkzeuge & Quellen

Diese Dokumentation dient als zentrale Anlaufstelle für KI-Agenten, um Werkzeuge auf einem Linux/Ubuntu-System zu identifizieren, zu dokumentieren und aktuell zu halten.

## 1. Strategie zur Verwaltung von Werkzeugen

### Sammeln (Discovery)
- **Automatisierter Scan:** Regelmäßige Überprüfung installierter Pakete über Paketmanager (`apt`), Sprach-Runtimes (`pip list`, `npm list -g`, `cargo install --list`) und Umgebungsvariablen.
- **Repository-Analyse:** Durchsuchen lokaler Projekte nach Abhängigkeiten in `package.json`, `requirements.txt`, `go.mod` und `Cargo.toml`.
- **System-Profiling:** Identifikation von Hardware-Ressourcen (CPU/GPU) zur Bestimmung der Eignung für lokale Inferenz.

### Dokumentieren (Documentation)
- **Standardisiertes Format:** Jedes Werkzeug wird mit Name, Zweck, Aufruf-Befehl und Version erfasst.
- **KI-Optimierung:** Verwendung von klaren Schlagworten und Metadaten-Blöcken für eine effiziente Kontext-Extraktion durch LLMs.
- **Abhängigkeits-Mapping:** Dokumentation von Voraussetzungen (z.B. "Benötigt Docker", "Erfordert Python >= 3.10").

### Aktualisierung (Maintenance)
- **Version-Tracking:** Abgleich lokaler Versionen mit Upstream-Releases via GitHub APIs oder Paketmanagern.
- **Health-Checks:** Regelmäßige Validierung der Erreichbarkeit und Funktionalität der Tools.

---

## 2. Vorhandene Werkzeuge (System-Analyse)

Basierend auf dem aktuellen System-Status wurden folgende Tool-Gruppen identifiziert:

### Entwicklung & Runtimes
- **Python (via pyenv):** Vielseitigste Sprache für KI-Agenten und ML.
- **Node.js (via nvm):** Essential für Web-basierte Agenten-Schnittstellen und MCP-Server.
- **Go:** Performante Tools und Agent-Infrastruktur.
- **Rust (via cargo):** Sicherheit und Geschwindigkeit für High-Performance Komponenten.
- **Flutter:** Entwicklung von Multi-Plattform UI-Frontends für Agenten.

### Infrastruktur & Deployment
- **Docker:** Containerisierung von isolierten Agent-Umgebungen und Tools.
- **Build-Tools (CMake, Clang, GCC):** Kompilierung nativer KI-Module (z.B. llama.cpp).

---

## 3. Identifizierte Lücken (Gaps)

Folgende Kategorien sind für den effektiven Einsatz von KI-Agenten essenziell, aber derzeit nicht auf dem System präsent:

### Lokale LLM-Inferenz
- **Ollama:** Einfaches Management und Ausführen von lokalen Modellen (Llama3, Mistral, etc.).
- **vLLM:** Hochperformanter Inferenz-Server für LLMs.
- **LocalAI:** Multi-Modale API-Schnittstelle (OpenAI kompatibel).

### Orchestrierung & Frameworks
- **LangChain / LangGraph:** Frameworks zur Erstellung komplexer Agent-Workflows.
- **CrewAI:** Multi-Agenten-Orchestrierung.
- **MCP (Model Context Protocol):** Standard zur Anbindung von Datenquellen an LLMs.

### Wissensdatenbanken (Vector DBs)
- **ChromaDB:** Leichtgewichtige Vektordatenbank für RAG (Retrieval Augmented Generation).
- **Qdrant:** Performante Vektordatenbank für skalierbare Agenten-Suche.

### Browsing & Automatisierung
- **Playwright / Puppeteer:** Ermöglicht Agenten die Interaktion mit Webseiten.

---

## 4. Aktionsplan zur Aktualisierung

1. **Scan-Script ausführen:** Ein Bash-Script erstellen, das monatlich die installierte Basis prüft.
2. **Gap-Closing:** Priorisierte Installation von `Ollama` und `MCP` zur Erweiterung der Agenten-Fähigkeiten.
3. **Dokumentations-Sync:** Automatischer Export von Tool-Metadaten in dieses Dokument.
