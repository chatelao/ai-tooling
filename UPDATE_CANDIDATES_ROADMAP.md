# Upgrade Roadmap für Softwaremodule (`UPDATE_CANDIDATES_ROADMAP.md`)

Dieses Dokument definiert die operative Roadmap zur schrittweisen Aktualisierung der in **[UPDATE_CANDIDATES.md](UPDATE_CANDIDATES.md)** identifizierten Softwaremodule. Es stellt einen strukturierten, phasenbasierten Upgrade-Plan bereit, um die Systemkomponenten auf Ubuntu 24.04 LTS sicher, stabil und auf dem neuesten Stand der Upstream-Entwicklungen zu halten.

---

## 1. Übersicht & Zielsetzung

Im Rahmen der kontinuierlichen Pflege des Repositorys wurden 121 Softwaremodule analysiert und **81 Update-Kandidaten** identifiziert. Die Upgrades unterteilen sich in:
- **Critical Security & Stability Patches:** 57 Module mit bekannten CVE-Fixes, Pufferüberlauf-Korrekturen und Sicherheitsverbesserungen.
- **Major Releases & Breaking Changes:** 30 Module mit neuen Hauptversionen (z. B. React 19, FreeCAD 1.x, KiCad 10, Docker 28, Node.js 26).
- **Minor & Patch Maintenance Updates:** Laufende Funktions- und Kompatibilitätsupdates.

Die Roadmap strukturiert den Upgrade-Prozess in drei aufeinander aufbauende Phasen mit klaren Qualitätskriterien.

---

## 2. Qualitätsmeilensteine & Upgrade-Prozess

Jedes Software-Upgrade muss folgende vier Phasenprüfungen durchlaufen:

### Meilenstein 1: Kompatibilitäts- & Risikoanalyse
- Überprüfung von Breaking Changes, geänderten CLI-Flags und Konfigurationssyntax.
- Validierung der Abhängigkeiten unter Ubuntu 24.04 LTS (Python 3.12, Node.js LTS, C++ Toolchains).

### Meilenstein 2: Anpassung der Factsheets & Beispiele
- Aktualisierung der Versionsnummern in den jeweiligen `factsheets/<gruppe>/<tool>/README.md`.
- Überarbeitung und Test aller zugehörigen Beispielskripte und Konfigurationen in `examples/`.

### Meilenstein 3: Testautomatisierung & Verifizierung
- Aktualisierung der Installationsskripte (`<tool>_install.sh`) und Testskripte (`<tool>_run_test.sh`).
- Erneute Ausführung der Validierungstests und Generierung aktualisierter SHA256-Prüfsummen (`.hash.sha256`).

### Meilenstein 4: Zentrale Systemintegration
- Synchronisation der zentralen Werkzeugliste via `scripts/rebuild_tools_md.py` (`TOOLS.md`).
- Aktualisierung der Statuswerte in `UPDATE_CANDIDATES.md` und `UPDATE_CANDIDATES_ROADMAP.md`.
- Aktualisierung der MkDocs-Dokumentationsstruktur via `scripts/generate_mkdocs_config.py`.

---

## 3. Phasenbasierter Rollout-Plan

```
+-----------------------------------------------------------------------------------+
| Phase 1: Kritische Sicherheits- & Stabilitätsupdates (22 Tools)                    |
| Fokus: CVE-Patches, Container-Sicherheit, Speicherlecks & Netzwerk-Schwachstellen  |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| Phase 2: Hauptversion-Upgrades & Breaking Changes (23 Tools)                     |
| Fokus: Major Version Upgrades, API-Anpassungen & Architektur-Migrationen          |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| Phase 3: Minor- & Patch-Updates zur Systempflege (36 Tools)                      |
| Fokus: Routine-Wartung, Performance-Optimierungen & SDK-Updates                   |
+-----------------------------------------------------------------------------------+
```

---

## 4. Detaillierte Implementierungs- & Trackingmatrix

In der folgenden Tabelle sind alle 81 Update-Kandidaten geordnet nach Phase, Kategorie und Priorität aufgeführt.

### Phase 1: Prioritäre Sicherheits- & Stabilitätsupdates

| Kategorie | Werkzeug / Modul | Aktuelle Version | Zielversion | Update-Typ | Validierungsstrategie | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Animation | [ImageMagick](factsheets/animation/imagemagick/README.md) | `7.1.1` | `7.1.2-34` | Sicherheitsfix | CLI-Render-Tests & Image Decoder Check | Abgeschlossen |
| Animation | [FFmpeg](factsheets/animation/ffmpeg/README.md) | `7.1` | `9.0.2` | Hauptversion / Security | Media Encoding & Filter-Pipeline-Tests | Abgeschlossen |
| Audio-musik | [FluidSynth](factsheets/audio-musik/fluidsynth/README.md) | `2.3.4` | `2.6.1` | Security / Patch | SoundFont2/3 Parsing Test (`fluidsynth -F`) | Abgeschlossen |
| Audio-musik | [PipeWire](factsheets/audio-musik/pipewire/README.md) | `1.0.5` | `1.6.9` | Security / Patch | IPC & JACK-Emulation Test (`pw-cli`) | Abgeschlossen |
| Audio-musik | [Pure Data](factsheets/audio-musik/pure-data/README.md) | `0.54.1` | `0.57-0` | Security / Patch | Headless GUI & DSP Audio Test (`pd -nogui`) | Geplant |
| Bioinformatik | [Biopython](factsheets/bioinformatik/biopython/README.md) | `1.84` | `1.88` | Security / Patch | PDB/NCBI Parser Verification Script | Geplant |
| Bioinformatik | [RDKit](factsheets/bioinformatik/rdkit/README.md) | `2024.09.1` | `2026.9.1` | Security / Major | C++ SMILES Parser & Mol-Draw Test | Geplant |
| Datenbanken | [PostgreSQL](factsheets/datenbanken/postgresql/README.md) | `17.2` | `18.6` | Security / Major | SQL-Injektion & Ext-Security Validation | Geplant |
| Firmware-analyse | [YARA](factsheets/firmware-analyse/yara/README.md) | `4.5.1` | `4.5.8` | Security / Patch | PE/ELF Rule Match Test | Geplant |
| Funktechnik | [URH](factsheets/funktechnik/urh/README.md) | `2.9.8` | `2.10.0` | Security / Patch | SDR Driver & Signal Decoders Check | Geplant |
| Hardware-simulation | [Renode](factsheets/hardware-simulation/renode/README.md) | `1.15.3` | `1.17.0` | Security / Patch | GDB Server Module Security Test | Geplant |
| Infrastruktur | [AWS CLI](factsheets/infrastruktur/aws-cli/README.md) | `2.21.0` | `2.38.1` | Security / Patch | TLS/SSO Auth & Service API Check | Geplant |
| Infrastruktur | [Azure CLI](factsheets/infrastruktur/azure-cli/README.md) | `2.66.0` | `2.91.0` | Security / Patch | OAuth2/MSAL Auth & Bicep Validation | Geplant |
| Infrastruktur | [Docker](factsheets/infrastruktur/docker/README.md) | `27.3.1` | `28.5.2` | Security / Major | Container Isolation & Engine Upgrade Test | Geplant |
| Infrastruktur | [Docker Compose](factsheets/infrastruktur/docker-compose/README.md) | `2.29.7` | `5.6.0` | Security / Major | Compose Spec v5 Build & Secret Validation | Geplant |
| Infrastruktur | [Kubernetes (kubectl)](factsheets/infrastruktur/kubernetes/README.md) | `1.31.2` | `1.37.1` | Security / Patch | Cluster API & Security Patch Test | Geplant |
| KI-Inferenz | [Ollama](factsheets/ki-inferenz/ollama/README.md) | `0.4.1` | `0.40.6` | Security / Patch | Model Serving Concurrency & Memory Leak Test | Geplant |
| KI-Inferenz | [vLLM](factsheets/ki-inferenz/vllm/README.md) | `0.6.3` | `0.32.0` | Security / Patch | Inference Endpoint Security & Transformer Test | Geplant |
| Programmierung | [Node.js und npm](factsheets/programmierung/nodejs/README.md) | `23.2.0` | `26.12.0` | Security / Major | HTTP Smuggling, V8 & TLS Patches Test | Geplant |
| Programmierung | [PHP Composer](factsheets/programmierung/composer/README.md) | `2.8.2` | `2.10.3` | Security / Patch | Archive Extraction Security Test | Geplant |
| Programmierung | [Pillow](factsheets/programmierung/pillow/README.md) | `11.0.0` | `13.0.0` | Security / Major | Image Decoder Buffer Overflow CVE Fixes | Geplant |
| Testing | [Spectral](factsheets/testing/spectral/README.md) | `6.11.1` | `6.17.0` | Security / Patch | ReDoS JSON Schema Parser Test | Geplant |

### Phase 2: Hauptversion-Upgrades & Breaking Changes

| Kategorie | Werkzeug / Modul | Aktuelle Version | Zielversion | Update-Typ | Validierungsstrategie | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Animation | [Blender](factsheets/animation/blender/README.md) | `4.3.2` | `5.2.2` | Hauptversion | Headless Vulkan Render Test (`blender -b`) | Geplant |
| Animation | [Krita](factsheets/animation/krita/README.md) | `5.2.6` | `6.0.4.1` | Hauptversion | Qt6 Engine & Brush Preset Test | Geplant |
| App-entwicklung | [React](factsheets/app-entwicklung/react/README.md) | `18.3.1` | `19.3.1` | Hauptversion | Server Components & Ref/Context Test | Geplant |
| App-entwicklung | [Spring Boot](factsheets/app-entwicklung/spring-boot/README.md) | `3.4.0` | `4.1.1` | Hauptversion | Java 21+ & Spring Framework CVE Test | Geplant |
| CAD-3D | [FreeCAD](factsheets/cad-3d/freecad/README.md) | `0.21.2` | `1.1.4` | Hauptversion | TNP Fix Geometry Export Test | Geplant |
| EDA | [KiBot](factsheets/eda/kibot/README.md) | `0.18.0` | `1.9.1` | Hauptversion | KiCad 8/9/10 Export Validation | Geplant |
| EDA | [KiCad](factsheets/eda/kicad-10-0/README.md) | `8.0.6` | `10.99.0` | Hauptversion | Schematic & PCB Format Conversion Test | Geplant |
| EDA | [SKiDL](factsheets/eda/skidl/README.md) | `1.2.2` | `3.0.0` | Hauptversion | Python 3.12 Syntax & Netlist Export | Geplant |
| EDA | [cocotb](factsheets/eda/cocotb/README.md) | `1.9.0` | `2.1.0` | Hauptversion | Coroutine Syntax & Simulator Driver Test | Geplant |
| EDA | [openFPGALoader](factsheets/eda/openfpgaloader/README.md) | `0.12.0` | `1.2.0` | Hauptversion | FTDI Driver & FPGA Flash Verification | Geplant |
| Firmware-analyse | [EMBA](factsheets/firmware-analyse/emba/README.md) | `1.5.0` | `2.0.4-summer_edition` | Hauptversion | Firmware Scanning Engine v2 Test | Geplant |
| Firmware-analyse | [Ghidra](factsheets/firmware-analyse/ghidra/README.md) | `11.2.1` | `Ghidra.12.1.4.build` | Hauptversion | Headless Decompiler & CPU Driver Test | Geplant |
| Funktechnik | [Node-RED](factsheets/funktechnik/node-red/README.md) | `4.0.5` | `5.0.8` | Hauptversion | Flow Engine & Dashboard Security Check | Geplant |
| Geodaten | [osm2pgsql](factsheets/geodaten/osm2pgsql/README.md) | `1.11.0` | `2.3.1` | Hauptversion | Flex Output & PostgreSQL 16/17 Test | Geplant |
| Infrastruktur | [Azure MCP Server](factsheets/infrastruktur/azure-mcp-server/README.md) | `1.0.1` | `3.0.0` | Hauptversion | Protocol v3.0 & Agent Tools Validation | Geplant |
| Infrastruktur | [Google Cloud Run MCP](factsheets/infrastruktur/google-cloud-run-mcp/README.md) | `0.5.0` | `1.11.0` | Hauptversion | MCP 1.0 Spec Compatibility Test | Geplant |
| Infrastruktur | [Vast AI SDK](factsheets/infrastruktur/vast-ai-sdk/README.md) | `0.1.34` | `1.8.3` | Hauptversion | API Instance Management Test | Geplant |
| Programmierung | [Blockly](factsheets/programmierung/blockly/README.md) | `11.1.1` | `13.4.0` | Hauptversion | Event API & Renderer Compatibility Check | Geplant |
| Dokumentation | [Redocly CLI](factsheets/dokumentation/redocly-cli/README.md) | `1.25.0` | `2.64.1` | Hauptversion | OpenAPI 3.1 & Rule Config v2 Test | Geplant |
| Schnittstellen | [graphqurl](factsheets/schnittstellen/graphqurl/README.md) | `1.0.3` | `2.0.0` | Hauptversion | CLI Output & Dependency Test | Geplant |
| Template-engines | [EJS](factsheets/template-engines/ejs/README.md) | `3.1.10` | `7.0.2` | Hauptversion | Template Compilation Test | Geplant |
| Testing | [Hurl](factsheets/testing/hurl/README.md) | `5.0.0` | `8.0.1` | Hauptversion | HTTP Assertions & CLI Flags Test | Geplant |
| Testing | [Schemathesis](factsheets/testing/schemathesis/README.md) | `3.38.0` | `4.32.0` | Hauptversion | CLI v4.0 & Property-based Testing Check | Geplant |

### Phase 3: Minor- & Patch-Updates zur Systempflege

| Kategorie | Werkzeug / Modul | Aktuelle Version | Zielversion | Update-Typ | Validierungsstrategie | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Animation | [Manim](factsheets/animation/manim/README.md) | `0.18.1` | `0.22.0` | Minor / Patch | Render Module Scene Execution Test | Geplant |
| Animation | [Synfig Studio](factsheets/animation/synfig-studio/README.md) | `1.5.3` | `1.5.5` | Minor / Patch | CLI Rendering & CLI Flags Test | Geplant |
| App-entwicklung | [React Native](factsheets/app-entwicklung/react-native/README.md) | `0.76.3` | `0.88.0` | Minor / Patch | Build Architecture Integration Check | Geplant |
| Audio-musik | [Csound](factsheets/audio-musik/csound/README.md) | `6.18.1` | `window-6.14.0` | Minor / Patch | CSD Audio Render Verification | Geplant |
| Audio-musik | [LilyPond](factsheets/audio-musik/lilypond/README.md) | `2.24.3` | `2.27.3` | Minor / Patch | Engraving & PDF Render Test | Geplant |
| Bioinformatik | [PyMOL](factsheets/bioinformatik/pymol/README.md) | `3.0.0` | `3.1.0` | Minor / Patch | Headless PyMOL Script Execution Test | Geplant |
| Bioinformatik | [SeqKit](factsheets/bioinformatik/seqkit/README.md) | `2.9.0` | `2.14.0` | Minor / Patch | FASTA/FASTQ Sequence Processing Check | Geplant |
| CAD-3D | [OpenSCAD](factsheets/cad-3d/openscad/README.md) | `2021.01` | `openscad-2026.10-TEST4` | Minor / Patch | CSG Render & STL Export Test | Geplant |
| Dokumentation | [Img2pdf](factsheets/dokumentation/img2pdf/README.md) | `0.5.1` | `0.6.3` | Minor / Patch | PDF Conversion Test Script | Geplant |
| Dokumentation | [PlantUML](factsheets/dokumentation/plantuml/README.md) | `1.2024.7` | `1.2026.9` | Minor / Patch | Diagram Rendering Verification | Geplant |
| Dokumentation | [WaveDrom](factsheets/dokumentation/wavedrom/README.md) | `3.5.0` | `3.7.0` | Minor / Patch | Timing Diagram SVG Render Test | Geplant |
| EDA | [Yosys](factsheets/eda/yosys/README.md) | `0.41` | `0.70` | Minor / Patch | Verilog Synthesis Script Test | Geplant |
| Firmware-analyse | [Binwalk](factsheets/firmware-analyse/binwalk/README.md) | `2.4.0` | `2.1.0` | Minor / Patch | Extraction Module Verification | Geplant |
| Firmware-analyse | [CVE Bin Tool](factsheets/firmware-analyse/cve-bin-tool/README.md) | `3.3` | `3.4` | Minor / Patch | CVE Database Mapping Test | Geplant |
| Firmware-analyse | [PANDA](factsheets/firmware-analyse/panda/README.md) | `2.2` | `1.8.85` | Minor / Patch | Dynamic Analysis Verification | Geplant |
| Firmware-analyse | [Radare2](factsheets/firmware-analyse/radare2/README.md) | `5.9.8` | `5.0.0` | Minor / Patch | Disassembly & Analysis Test | Geplant |
| Funktechnik | [GNU Radio](factsheets/funktechnik/gnuradio/README.md) | `3.10.11` | `3.11.0.0git` | Minor / Patch | Flowgraph Execution Test | Geplant |
| Funktechnik | [Gqrx SDR](factsheets/funktechnik/gqrx-sdr/README.md) | `2.17.5` | `2.17.7` | Minor / Patch | Receiver Simulation Verification | Geplant |
| Funktechnik | [Inspectrum](factsheets/funktechnik/inspectrum/README.md) | `0.3.1` | `0.4.0` | Minor / Patch | Signal Analysis Verification | Geplant |
| Funktechnik | [rtl-sdr](factsheets/funktechnik/rtl-sdr/README.md) | `2.0.2` | `2.0.3` | Minor / Patch | Driver & Sample Acquisition Check | Geplant |
| Geodaten | [osmium-tool](factsheets/geodaten/osmium-tool/README.md) | `1.16.0` | `1.19.0` | Minor / Patch | OSM PBF Processing Test | Geplant |
| Infrastruktur | [AWS MCP Server](factsheets/infrastruktur/aws-mcp-server/README.md) | `1.0.1` | `1.5.6` | Minor / Patch | MCP Tool Schnittstellen Check | Geplant |
| Programmierung | [Arduino CLI](factsheets/programmierung/arduino-cli/README.md) | `1.1.0` | `1.5.1` | Minor / Patch | Library Manager & Sketch Compile Test | Geplant |
| Programmierung | [PlatformIO Core](factsheets/programmierung/platformio-core/README.md) | `6.1.16` | `6.2.0` | Minor / Patch | Toolchain & Python Build Script Test | Geplant |
| Schnittstellen | [OpenAPI Generator](factsheets/schnittstellen/openapi-generator/README.md) | `7.10.0` | `2.41.0` | Minor / Patch | Client Code Generation Test | Geplant |
| Schnittstellen | [Zeep](factsheets/schnittstellen/zeep/README.md) | `4.3.1` | `4.3.3` | Minor / Patch | WSDL SOAP Client Request Check | Geplant |
| Schnittstellen | [grpcurl](factsheets/schnittstellen/grpcurl/README.md) | `1.9.1` | `1.9.4` | Minor / Patch | gRPC Reflection Request Test | Geplant |
| Schnittstellen | [Sparkql](factsheets/schnittstellen/sparkql/README.md) | `2.4.0` | `0.2.2` | Minor / Patch | SPARQL Query Execution Test | Geplant |
| Template-engines | [Handlebars](factsheets/template-engines/handlebars/README.md) | `4.7.8` | `4.7.10` | Minor / Patch | Template Rendering Test | Geplant |
| Template-engines | [Jinja2](factsheets/template-engines/jinja2/README.md) | `3.1.4` | `3.1.6` | Minor / Patch | Python Template Evaluation Check | Geplant |
| Template-engines | [Liquid](factsheets/template-engines/liquid/README.md) | `5.5.0` | `5.14.0` | Minor / Patch | Ruby Liquid Filter Test | Geplant |
| Template-engines | [Pug](factsheets/template-engines/pug/README.md) | `3.0.3` | `3.0.4` | Minor / Patch | HTML Compile Verification | Geplant |
| Template-engines | [Twig](factsheets/template-engines/twig/README.md) | `3.14.0` | `3.30.0` | Minor / Patch | PHP Template Render Test | Geplant |
| Testing | [Playwright](factsheets/testing/playwright/README.md) | `1.49.0` | `1.64.1` | Minor / Patch | Browser Binary Execution Check | Geplant |
| Testing | [Prism](factsheets/testing/prism/README.md) | `5.10.0` | `5.16.0` | Minor / Patch | Mocking Server Response Test | Geplant |
| Testing | [Step CI](factsheets/testing/step-ci/README.md) | `2.5.0` | `2.8.2` | Minor / Patch | REST/GraphQL Workflow Execution Test | Geplant |

---

## 5. Durchführungs- & Prüfroutine (Workflow)

Nach der Abarbeitung von Upgrades in den jeweiligen Phasen wird folgender automatisierten Kontrollzyklus ausgeführt:

1. **Skriptverifizierung & SHA256-Checksummen-Generierung:**
   ```bash
   bash scripts/verify_tools.sh
   ```
2. **Neugenerierung der zentralen Dokumentations-Tabelle (`TOOLS.md`):**
   ```bash
   python3 scripts/rebuild_tools_md.py
   ```
3. **Aktualisierung der MkDocs-Navigationsstruktur (`mkdocs.yml`):**
   ```bash
   python3 scripts/generate_mkdocs_config.py
   ```

---

## 6. Zusammenfassung

Mit der Implementierung von `UPDATE_CANDIDATES_ROADMAP.md` verfügt das Repository über einen strukturierten, nach Priorität und Risiko gestaffelten Fahrplan. Sämtliche 81 identifizierten Software-Upgrades sind transparent erfasst, mit Validierungsstrategien hinterlegt und bereit für die systematische Bearbeitung.
