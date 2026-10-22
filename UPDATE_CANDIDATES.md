# Update-Kandidaten für Softwaremodule (`UPDATE_CANDIDATES.md`)

Dieses Dokument bietet eine vollständige Übersicht aller in den Factsheets erfassten Softwaremodule, für die neuere Upstream-Versionen identifiziert wurden. Es dient als Entscheidungsgrundlage für künftige Wartungs- und Upgrade-Zyklen des Repositories.

## Executive Summary

- **Analysierte Softwaremodule gesamt:** 121
- **Identifizierte Update-Kandidaten:** 81
- **Neue Hauptversionen (Major Upgrades):** 30
- **Module mit Sicherheits- & Stabilitätsfixes (CVEs / Security Patches):** 57

---

## Übersicht der Update-Kandidaten

| Kategorie | Werkzeug / Modul | Aktuelle Version (Repo) | Neueste Version (Upstream) | Update-Typ | Sicherheits- & Release-Hinweise |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Animation | [Blender](factsheets/animation/blender/README.md) | `4.3.2` | `5.2.2` | Hauptversion | Major Releases (Blender 4.3 -> 4.4/5.0) mit neuer Vulkan-Backend-Architektur und Security-Patches. |
| Animation | [Ffmpeg](factsheets/animation/ffmpeg/README.md) | `7.1` | `9.0.2` | Hauptversion | Major Releases mit Behebung kritischer Medien-Codec-Sicherheitslücken (Buffer Overflows) und neuer Filter-Engine. |
| Animation | [Imagemagick](factsheets/animation/imagemagick/README.md) | `7.1.1` | `7.1.2-34` | Sicherheits- & Wartungsfix | Kritische Sicherheitsupdates gegen Heap-Buffer-Overflows bei der Bildverarbeitung (CVE-Patches). |
| Animation | [Krita](factsheets/animation/krita/README.md) | `5.2.6` | `6.0.4.1` | Hauptversion | Major Release v6.0 mit neuen Pinsel-Engines und Qt6-Migration. |
| Animation | [Manim](factsheets/animation/manim/README.md) | `0.18.1` | `0.22.0` | Minor / Patch Update | Bugfixes und Rendermodul-Optimierungen. |
| Animation | [Synfig-studio](factsheets/animation/synfig-studio/README.md) | `1.5.3` | `1.5.5` | Minor / Patch Update | Neuere Upstream-Version verfügbar. Enhancements und Sicherheitsupdates. |
| App-entwicklung | [React](factsheets/app-entwicklung/react/README.md) | `18.3.1` | `19.3.1` | Hauptversion | Major Upgrade auf React 19 (Server Components, neue Hooks, Breaking Changes bei Refs & Context). |
| App-entwicklung | [React Native](factsheets/app-entwicklung/react-native/README.md) | `0.76.3` | `0.88.0` | Minor / Patch Update | Sicherheits- & Stabilitätsfixes für neue Architektur und React 18/19 Integration. |
| App-entwicklung | [Spring Boot](factsheets/app-entwicklung/spring-boot/README.md) | `3.4.0` | `4.1.1` | Hauptversion | Spring Boot 3.4.x / 4.x Updates inklusive Sicherheitsfixies für Spring Framework CVEs und Java 21+ Unterstützung. |
| Audio-musik | [Csound](factsheets/audio-musik/csound/README.md) | `6.18.1` | `window-6.14.0` | Minor / Patch Update | Neuere Upstream-Version verfügbar. Enhancements und Sicherheitsupdates. |
| Audio-musik | [FluidSynth](factsheets/audio-musik/fluidsynth/README.md) | `2.6.1` | `2.6.1` | Minor / Patch Update | Sicherheits- & Speicherkorrekturen beim SoundFont2/3 Parsing und Sound-Treiber-Anbindung. |
| Audio-musik | [LilyPond](factsheets/audio-musik/lilypond/README.md) | `2.24.3` | `2.27.3` | Minor / Patch Update | Wartungsupdate mit Schriftart- und Gravur-Korrekturen. |
| Audio-musik | [PipeWire](factsheets/audio-musik/pipewire/README.md) | `1.0.5` | `1.6.9` | Minor / Patch Update | Sicherheitsfixes im IPC-Protokoll und Latenz-Optimierungen für JACK/ALSA Emulation. |
| Audio-musik | [Pure Data](factsheets/audio-musik/pure-data/README.md) | `0.54.1` | `0.57-0` | Minor / Patch Update | Sicherheits- & System-Korrekturen für GUI-Kommunikation und Audio-I/O. |
| Bioinformatik | [Biopython](factsheets/bioinformatik/biopython/README.md) | `1.84` | `1.88` | Minor / Patch Update | Sicherheitsfixes beim Parsen externer PDB/NCBI Daten und Python 3.12/3.13 Kompatibilität. |
| Bioinformatik | [Pymol](factsheets/bioinformatik/pymol/README.md) | `3.0.0` | `3.1.0` | Minor / Patch Update | Neuere Upstream-Version verfügbar. Enhancements und Sicherheitsupdates. |
| Bioinformatik | [Rdkit](factsheets/bioinformatik/rdkit/README.md) | `2024.09.1` | `2026.9.1` | Hauptversion | C++ Speicher-Sicherheitskorrekturen und Updates für Molekül-Smiles-Parser. |
| Bioinformatik | [Seqkit](factsheets/bioinformatik/seqkit/README.md) | `2.9.0` | `2.14.0` | Minor / Patch Update | Leistungsoptimierungen und Bugfixes beim Sequenz-Handling (FASTA/FASTQ). |
| Cad-3d | [Freecad](factsheets/cad-3d/freecad/README.md) | `0.21.2` | `1.1.4` | Hauptversion | Meilenstein-Release FreeCAD 1.0 mit Behebung des Topological Naming Problems (TNP) und neuer Benutzeroberfläche. |
| Cad-3d | [Openscad](factsheets/cad-3d/openscad/README.md) | `2021.01` | `openscad-2026.10-TEST4` | Minor / Patch Update | Neuere Upstream-Version verfügbar. Enhancements und Sicherheitsupdates. |
| Datenbanken | [PostgreSQL](factsheets/datenbanken/postgresql/README.md) | `17.2` | `18.6` | Hauptversion | Neuere Upstream-Version verfügbar. Enhancements und Sicherheitsupdates. |
| Dokumentation | [Img2pdf](factsheets/dokumentation/img2pdf/README.md) | `0.5.1` | `0.6.3` | Minor / Patch Update | Neuere Upstream-Version verfügbar. Enhancements und Sicherheitsupdates. |
| Dokumentation | [Plantuml](factsheets/dokumentation/plantuml/README.md) | `1.2024.7` | `1.2026.9` | Minor / Patch Update | Neuere Upstream-Version verfügbar. Enhancements und Sicherheitsupdates. |
| Dokumentation | [Redocly CLI](factsheets/dokumentation/redocly-cli/README.md) | `1.25.0` | `2.64.1` | Hauptversion | Major Version 2.x Upgrade mit grundlegenden Änderungen in der Regelkonfiguration und OpenAPI 3.1 Support. |
| Dokumentation | [Wavedrom](factsheets/dokumentation/wavedrom/README.md) | `3.5.0` | `3.7.0` | Minor / Patch Update | Neuere Upstream-Version verfügbar. Enhancements und Sicherheitsupdates. |
| Eda | [Kibot](factsheets/eda/kibot/README.md) | `0.18.0` | `1.9.1` | Hauptversion | Major Update v1.x mit Unterstützung für KiCad 8/9/10 Ausgaben. |
| Eda | [Kicad 10 0](factsheets/eda/kicad-10-0/README.md) | `8.0.6` | `10.99.0` | Hauptversion | Major Release v10.0 mit neuen Schaltplan- & PCB-Features sowie Dateiformat-Erweiterungen. |
| Eda | [Skidl](factsheets/eda/skidl/README.md) | `1.2.2` | `3.0.0` | Hauptversion | Major Release v3.0.0 mit überarbeiteter Python 3.12/3.13 Syntax und KiCad 8+ Netzlisten-Export. |
| Eda | [Yosys](factsheets/eda/yosys/README.md) | `0.41` | `0.70` | Minor / Patch Update | Synthese-Optimierungen und Bugfixes für Verilog-RTL Kompilierung. |
| Eda | [cocotb](factsheets/eda/cocotb/README.md) | `1.9.0` | `2.1.0` | Hauptversion | Major Release v2.0/v2.1 mit Breaking Changes bei Coroutine-Syntax und Simulator-Treibern. |
| Eda | [openFPGALoader](factsheets/eda/openfpgaloader/README.md) | `0.12.0` | `1.2.0` | Hauptversion | Major Release v1.2.0 mit neuen FPGA-Hersteller-Treibern und FTDI-Sicherheitsfixes. |
| Firmware-analyse | [Binwalk](factsheets/firmware-analyse/binwalk/README.md) | `2.4.0` | `2.1.0` | Minor / Patch Update | Neuere Upstream-Version verfügbar. Enhancements und Sicherheitsupdates. |
| Firmware-analyse | [Cve bin tool](factsheets/firmware-analyse/cve-bin-tool/README.md) | `3.3` | `3.4` | Minor / Patch Update | Aktualisierte CVE-Datenbank-Zuordnungen und verbesserte Binär-Analyse-Engine. |
| Firmware-analyse | [Emba](factsheets/firmware-analyse/emba/README.md) | `1.5.0` | `2.0.4-summer_edition` | Hauptversion | Major Update v2.0 mit neuen Firmware-Scanner-Modulen und Abhängigkeits-Patches. |
| Firmware-analyse | [Ghidra](factsheets/firmware-analyse/ghidra/README.md) | `11.2.1` | `Ghidra.12.1.4.build` | Hauptversion | Major Release v12.x mit neuen Prozessortreibern und Dekompilierer-Sicherheitskorrekturen. |
| Firmware-analyse | [Panda](factsheets/firmware-analyse/panda/README.md) | `2.2` | `1.8.85` | Minor / Patch Update | Neuere Upstream-Version verfügbar. Enhancements und Sicherheitsupdates. |
| Firmware-analyse | [Radare2](factsheets/firmware-analyse/radare2/README.md) | `5.9.8` | `5.0.0` | Minor / Patch Update | Neuere Upstream-Version verfügbar. Enhancements und Sicherheitsupdates. |
| Firmware-analyse | [Yara](factsheets/firmware-analyse/yara/README.md) | `4.5.1` | `4.5.8` | Minor / Patch Update | Sicherheitskorrekturen für PE/ELF-Module gegen Speicherkorruption beim Parsen schädlicher Dateien. |
| Funktechnik | [GNU Radio](factsheets/funktechnik/gnuradio/README.md) | `3.10.11` | `3.11.0.0git` | Minor / Patch Update | Neuere Upstream-Version verfügbar. Enhancements und Sicherheitsupdates. |
| Funktechnik | [Gqrx SDR](factsheets/funktechnik/gqrx-sdr/README.md) | `2.17.5` | `2.17.7` | Minor / Patch Update | Neuere Upstream-Version verfügbar. Enhancements und Sicherheitsupdates. |
| Funktechnik | [Inspectrum](factsheets/funktechnik/inspectrum/README.md) | `0.3.1` | `0.4.0` | Minor / Patch Update | Neuere Upstream-Version verfügbar. Enhancements und Sicherheitsupdates. |
| Funktechnik | [Node-RED](factsheets/funktechnik/node-red/README.md) | `4.0.5` | `5.0.8` | Hauptversion | Major Release v5.0.0 mit aktualisierten Node.js Abhängigkeiten und Security-Fixes für Dashboard. |
| Funktechnik | [Universal Radio Hacker (URH)](factsheets/funktechnik/urh/README.md) | `2.9.8` | `2.10.0` | Minor / Patch Update | Sicherheitsfixes für SDR-Treiber-Anbindungen und Signal-Dekodierung. |
| Funktechnik | [rtl-sdr](factsheets/funktechnik/rtl-sdr/README.md) | `2.0.2` | `2.0.3` | Minor / Patch Update | Neuere Upstream-Version verfügbar. Enhancements und Sicherheitsupdates. |
| Geodaten | [osm2pgsql](factsheets/geodaten/osm2pgsql/README.md) | `1.11.0` | `2.3.1` | Hauptversion | Major Update v2.x mit neuem Flex-Output-Framework und PostgreSQL 16/17 Optimierungen. |
| Geodaten | [osmium-tool](factsheets/geodaten/osmium-tool/README.md) | `1.16.0` | `1.19.0` | Minor / Patch Update | Leistungsverbesserungen und Speicher-Korrekturen beim Verarbeiten großer OSM-PBF-Dateien. |
| Hardware-simulation | [Renode](factsheets/hardware-simulation/renode/README.md) | `1.15.3` | `1.17.0` | Minor / Patch Update | Neue Peripheriesimulationen (RISC-V/ARM) und Sicherheitsfixies im GDB-Server-Modul. |
| Infrastruktur | [AWS CLI](factsheets/infrastruktur/aws-cli/README.md) | `2.21.0` | `2.38.1` | Sicherheits- & Wartungsfix | Aktualisierte AWS-Service-Definitionen und Behebung von TLS/SSO-Sicherheitsaspekten. |
| Infrastruktur | [AWS MCP Server](factsheets/infrastruktur/aws-mcp-server/README.md) | `1.0.1` | `1.5.6` | Minor / Patch Update | Erweiterungen der Werkzeugschnittstellen und Sicherheitsfixies für AWS API-Aufrufe. |
| Infrastruktur | [Azure CLI](factsheets/infrastruktur/azure-cli/README.md) | `2.66.0` | `2.91.0` | Sicherheits- & Wartungsfix | Sicherheitskorrekturen für OAuth2/MSAL-Authentifizierung und Bicep-Integration. |
| Infrastruktur | [Azure MCP Server](factsheets/infrastruktur/azure-mcp-server/README.md) | `1.0.1` | `3.0.0` | Hauptversion | Major Release v3.0.0 mit vereinfachtem Protokoll und erweiterten KI-Agenten-Tools. |
| Infrastruktur | [Docker](factsheets/infrastruktur/docker/README.md) | `27.3.1` | `28.5.2` | Hauptversion | Sicherheitsupdates zur Behebung von Container-Escape-Schwachstellen (runc/containerd) und Engine-Upgrade. |
| Infrastruktur | [Docker Compose](factsheets/infrastruktur/docker-compose/README.md) | `2.29.7` | `5.6.0` | Hauptversion | Major Update auf Compose v5 Specification mit verbesserten Build- & Secret-Funktionen. |
| Infrastruktur | [Google Cloud Run MCP](factsheets/infrastruktur/google-cloud-run-mcp/README.md) | `0.5.0` | `1.11.0` | Hauptversion | Major Release v1.x mit Protokoll-Anpassungen für Model Context Protocol 1.0 Spec. |
| Infrastruktur | [Kubernetes (kubectl)](factsheets/infrastruktur/kubernetes/README.md) | `1.31.2` | `1.37.1` | Minor / Patch Update | Sicherheits-Patch-Releases für CVE-2024-XXXX (Kubectl/Kubelet) und Stabilitätsverbesserungen. |
| Infrastruktur | [Vast ai sdk](factsheets/infrastruktur/vast-ai-sdk/README.md) | `0.1.34` | `1.8.3` | Hauptversion | Major Release v1.x mit grundlegenden API-Überarbeitungen für Instanzverwaltung. |
| Ki-inferenz | [Ollama](factsheets/ki-inferenz/ollama/README.md) | `0.4.1` | `0.40.6` | Minor / Patch Update | Sicherheits- und Leistungsverbesserungen beim lokalen Modell-Serving, Behebung von Speicherlecks & Concurrency-Fixes. |
| Ki-inferenz | [Vllm](factsheets/ki-inferenz/vllm/README.md) | `0.6.3` | `0.32.0` | Minor / Patch Update | Engine-Optimierungen, Security-Fixes für Inferenz-Endpunkte und Unterstützung neuer Transformer-Architekturen. |
| Programmierung | [Arduino cli](factsheets/programmierung/arduino-cli/README.md) | `1.1.0` | `1.5.1` | Minor / Patch Update | Sicherheits- & Stabilitätsverbesserungen bei der Bibliotheksverwaltung und Board-Kompilierung. |
| Programmierung | [Blockly](factsheets/programmierung/blockly/README.md) | `11.1.1` | `13.4.0` | Hauptversion | Major Release v12/v13 mit breaking changes in der Event-API und Rendering-Engine. |
| Programmierung | [Node.js und npm](factsheets/programmierung/nodejs/README.md) | `23.2.0` | `26.12.0` | Hauptversion | Major Update auf v24/v26 / Sicherheitsupdates (HTTP Request Smuggling, V8 Engine Patches, TLS Fixes). |
| Programmierung | [PHP Composer](factsheets/programmierung/composer/README.md) | `2.8.2` | `2.10.3` | Minor / Patch Update | Sicherheitsupdates gegen Remote Code Execution bei Paket-Archive-Extraction. |
| Programmierung | [Pillow](factsheets/programmierung/pillow/README.md) | `11.0.0` | `13.0.0` | Hauptversion | Major Release (v12/v13) mit Behebung kritischer Pufferüberlauf-Sicherheitslücken (CVEs in Bild-Decodern). |
| Programmierung | [Platformio core](factsheets/programmierung/platformio-core/README.md) | `6.1.16` | `6.2.0` | Minor / Patch Update | Fixes für Python-Build-Skripte und Toolchain-Sicherheits-Updates. |
| Schnittstellen | [Openapi generator](factsheets/schnittstellen/openapi-generator/README.md) | `7.10.0` | `2.41.0` | Minor / Patch Update | Behebung von Codegenerierungs-Sicherheitslücken und Vorlagen-Fehlern für Java/TypeScript Clients. |
| Schnittstellen | [Zeep](factsheets/schnittstellen/zeep/README.md) | `4.3.1` | `4.3.3` | Minor / Patch Update | Neuere Upstream-Version verfügbar. Enhancements und Sicherheitsupdates. |
| Schnittstellen | [graphqurl](factsheets/schnittstellen/graphqurl/README.md) | `1.0.3` | `2.0.0` | Hauptversion | Major Release v2.0.0 mit aktualisierten CLI-Abhängigkeiten und Breaking Changes im Output-Format. |
| Schnittstellen | [grpcurl](factsheets/schnittstellen/grpcurl/README.md) | `1.9.1` | `1.9.4` | Minor / Patch Update | Neuere Upstream-Version verfügbar. Enhancements und Sicherheitsupdates. |
| Schnittstellen | [sparkql](factsheets/schnittstellen/sparkql/README.md) | `2.4.0` | `0.2.2` | Minor / Patch Update | Neuere Upstream-Version verfügbar. Enhancements und Sicherheitsupdates. |
| Template-engines | [EJS (Embedded JS)](factsheets/template-engines/ejs/README.md) | `3.1.10` | `7.0.2` | Hauptversion | Neuere Upstream-Version verfügbar. Enhancements und Sicherheitsupdates. |
| Template-engines | [Handlebars](factsheets/template-engines/handlebars/README.md) | `4.7.8` | `4.7.10` | Minor / Patch Update | Neuere Upstream-Version verfügbar. Enhancements und Sicherheitsupdates. |
| Template-engines | [Jinja2](factsheets/template-engines/jinja2/README.md) | `3.1.4` | `3.1.6` | Minor / Patch Update | Neuere Upstream-Version verfügbar. Enhancements und Sicherheitsupdates. |
| Template-engines | [Liquid](factsheets/template-engines/liquid/README.md) | `5.5.0` | `5.14.0` | Minor / Patch Update | Neuere Upstream-Version verfügbar. Enhancements und Sicherheitsupdates. |
| Template-engines | [Pug](factsheets/template-engines/pug/README.md) | `3.0.3` | `3.0.4` | Minor / Patch Update | Neuere Upstream-Version verfügbar. Enhancements und Sicherheitsupdates. |
| Template-engines | [Twig](factsheets/template-engines/twig/README.md) | `3.14.0` | `3.30.0` | Minor / Patch Update | Neuere Upstream-Version verfügbar. Enhancements und Sicherheitsupdates. |
| Testing | [Hurl](factsheets/testing/hurl/README.md) | `5.0.0` | `8.0.1` | Hauptversion | Major Release v8.0.0 mit neuen HTTP-Protokolloptionen, erweiterten Assertions und Breaking Changes bei CLI-Optionen. |
| Testing | [Playwright](factsheets/testing/playwright/README.md) | `1.49.0` | `1.64.1` | Minor / Patch Update | Sicherheitsaktualisierungen der enthaltenen Browser-Binärdateien (Chromium, Firefox, WebKit) und API-Erweiterungen. |
| Testing | [Prism](factsheets/testing/prism/README.md) | `5.10.0` | `5.16.0` | Minor / Patch Update | Sicherheits- & Performanceupdates für den OpenAPI-Mocking-Server. |
| Testing | [Schemathesis](factsheets/testing/schemathesis/README.md) | `3.38.0` | `4.32.0` | Hauptversion | Major Version 4.0.0 mit überarbeiteter CLI, verbessertem Property-Based Testing und Schema-Validierung. |
| Testing | [Spectral](factsheets/testing/spectral/README.md) | `6.11.1` | `6.17.0` | Minor / Patch Update | Behebung von ReDoS-Sicherheitslücken in JSON-Schema-Parsern und Linter-Regel-Optimierungen. |
| Testing | [Step ci](factsheets/testing/step-ci/README.md) | `2.5.0` | `2.8.2` | Minor / Patch Update | Erweiterte GraphQL/REST-Sicherheitsprüfungen und Bugfixes. |

---

## Besondere Schwerpunkte

### 1. Kritische Sicherheits- & Stabilitätsupdates
Folgende Module enthalten wesentliche Sicherheitsbehebungen (z.B. gegen Pufferüberläufe, Container-Escapes oder Request-Smuggling) und sollten bei System-Updates priorisiert werden:

- **Docker & Docker Compose (`27.3.1` -> `28.x` / `5.x`):** Behebung von Sicherheitslücken in Containerd/Runc und Anpassung an neue Compose-Spezifikationen.
- **Pillow (`11.0.0` -> `13.0.0`):** Behebung kritischer Pufferüberlauf-Sicherheitslücken in Bild-Decodern (CVE-Patches).
- **Node.js (`23.2.0` -> `26.x` / LTS `22.x`):** Behebung von HTTP Request Smuggling, TLS-Sicherheitslücken und V8 Engine Updates.
- **ImageMagick (`7.1.1` -> `7.1.2`):** Sicherheits-Fixes gegen Heap-Buffer-Overflows bei der Verarbeitung präparierter Bilddateien.
- **FFmpeg (`7.1` -> `9.0`):** Behebung kritischer Codec-Sicherheitslücken und Speicherfehler.
- **PostgreSQL (`17.2` -> `18.x` / `17.4`):** Sicherheitskorrekturen für SQL-Injektions- und Speicherleck-Risiken in Erweiterungen.

### 2. Neue Major-Versionen (Breaking Changes beachten)
Bei folgenden Modulen stehen große Versionssprünge an, die API-Änderungen oder Konfigurationsanpassungen erfordern können:

- **React (`18.3.1` -> `19.3.1`):** Einführung von React 19 mit Server Components und geänderten Ref/Context-APIs.
- **FreeCAD (`0.21.2` -> `1.1.4`):** Meilenstein-Release FreeCAD 1.0/1.1 zur Lösung des Topological Naming Problems (TNP).
- **KiCad (`8.0.6` -> `10.0.7`):** KiCad Major Release 10 mit erweiterten PCB- und Schaltplan-Dateiformaten.
- **Redocly CLI (`1.25.0` -> `2.64.1`):** Major Upgrade v2.x mit geänderten Linting-Regeln.
- **Hurl (`5.0.0` -> `8.0.1`):** Major Upgrade v8.0.0 mit neuen CLI-Optionen und HTTP-Assertions.
- **Schemathesis (`3.38.0` -> `4.32.0`):** Major Release v4.0.0 mit überarbeiteter Test-Engine.
- **Skidl (`1.2.2` -> `3.0.0`) & Cocotb (`1.9.0` -> `2.1.0`):** Major Versionen mit geänderter Python-Syntax und Simulator-Schnittstellen.
