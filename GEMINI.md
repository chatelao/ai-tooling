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

| Name | Zweck | Referenzhandbuch | Installationsbefehle |
| :--- | :--- | :--- | :--- |
| vLLM | LLM Inferenz-Engine | [Link](https://github.com/vllm-project/vllm) | `pip install vllm` |
| Vast.ai SDK | Management von GPU-Instanzen | [Link](https://github.com/Vast-ai/vast-python) | `pip install vastai` |
| Pawn Compiler | Skriptsprache für Embedded Systems | [Link](https://github.com/compuphase/pawn) | - |
| Blockly | Visuelle Programmierung | [Link](https://developers.google.com/blockly) | `npm install blockly` |
| Renode | Emulator für Hardware-Systeme | [Link](https://renode.io/) | [Download](https://renode.io/#download) |
| Playwright | E2E Testing für Webanwendungen | [Link](https://playwright.dev/) | `npm install playwright` |
| MCP-FreeCAD | Model Context Protocol für FreeCAD | [Link](https://github.com/jango-blockchained/mcp-freecad) | - |
| MeshLab | Bearbeitung von 3D-Meshes | [Link](https://www.meshlab.net/) | `sudo apt install meshlab` |
| KiBot | Automatisierung für KiCAD | [Link](https://github.com/INTI-CMNB/KiBot) | `pip install kibot` |
| SKiDL | Schaltungsentwurf in Python | [Link](https://devbisme.github.io/skidl/) | `pip install skidl` |
| Apache FOP | Print Formatter für XSL-FO | [Link](https://xmlgraphics.apache.org/fop/) | `sudo apt install fop` |
| Ollama | Lokaler Betrieb von LLMs | [Link](https://ollama.com/) | `curl -fsSL https://ollama.com/install.sh \| sh` |
| WaveDrom | Zeitdiagramm-Renderer | [Link](https://wavedrom.com/) | `npm install wavedrom` |

#### Datenquellen/-sammlungen
- **Format:** Die Datensammlungen werden ebenfalls in Tabellenform dokumentiert.
- **Inhalte:** Jedes Sammlung wird mit Name, Zweck, Referenzhandbuch sowie Zugriffarten zum Beschaffung und/oder Abfrage beschrieben
- **Abfragbarkeit:** Vor der Aufnahme in die Liste wird die Software auf Installierbarkeit geprüft.

| Name | Zweck | Referenzhandbuch | Zugriff / Abfrage |
| :--- | :--- | :--- | :--- |
| GitHub API | Repository- und Issue-Daten | [Link](https://docs.github.com/en/rest) | REST / GraphQL API |
| Google Jules | Interner Task-Status | - | API-Integration |
| Hugging Face | Modell-Repository | [Link](https://huggingface.co/) | `huggingface-cli download` |
| IHP Open PDK | Open Source PDK (130nm) | [Link](https://github.com/IHP-GmbH/IHP-Open-PDK) | git clone |
| ISO 20022 camt.053 | Bankkontoauszüge | - | XML Import |
| eCH-0196 | Schweizer Steuerauszug | - | XML Import |
| CircuiTikZ | TeX/LaTeX-Paket zum Zeichnen von elektrischen Schaltungen | [Handbuch](https://mirror.init7.net/ctan/graphics/pgf/contrib/circuitikz/doc/circuitikzmanual.pdf) | `sudo apt-get install texlive-pictures` |

