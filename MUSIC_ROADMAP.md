# Integration Roadmap: Musik- und Audio-Werkzeuge (MUSIC_ROADMAP.md)

Dieses Dokument definiert den operativen Zeitplan, die Phasenstruktur und die Qualitätsmeilensteine für das Onboarding und die Integration der 25 Musik- und Audio-Werkzeuge aus **[MUSIC_DESIGN.md](MUSIC_DESIGN.md)** und **[MUSIC_CONCEPT.md](MUSIC_CONCEPT.md)** in das Repositories-System (`factsheets/audio-musik/`).

---

## 1. Übersicht & Zielsetzung

Die Integration erweitert das Repository um die neue Hauptkategorie **Audio & Musik** (Gruppe `e3a91b2c` in `GROUPS.md`). Um eine durchgehend hohe Qualität, CI/CD-Tauglichkeit und Testbarkeit auf Ubuntu 24.04 LTS sicherzustellen, erfolgt der Rollout in drei sequenziellen Phasen und orientiert sich an vier zentralen Qualitätsmeilensteinen.

---

## 2. Qualitätsmeilensteine für jedes Werkzeug

Jedes der 25 Musik-Werkzeuge muss im Zuge der Integration folgende Qualitätskriterien erfüllen:

### Meilenstein 1: Factsheet-Erstellung & Zweckbeschreibung (Content Completion)
- Erstellung des Verzeichnisses `factsheets/audio-musik/<tool-id>/`.
- Erstellung einer `README.md` mit präziser technische Zweckbeschreibung (ohne Platzhalter), Installation, CLI-Nutzung, Hello World und Validierungsanweisungen.

### Meilenstein 2: Beispieldatensatz-Erweiterung (Example Richness)
- Bereitstellung von mindestens 5 funktionalen, Nicht-Dummy-Beispieldateien im Ordner `examples/` (z. B. MIDI, WAV, Patch-Dateien, Score-Dateien, Skripte).
- Vollständige Dokumentation aller Beispieldateien im Abschnitt `## Beispiele` der `README.md`.

### Meilenstein 3: Scripting & Verifizierungssicherheit (Deployment Confidence)
- Erstellung ausführbarer Installations- (`<tool-id>_install.sh`) und Testskripte (`<tool-id>_run_test.sh`).
- Erzeugung und Validierung von SHA256-Checksummen (`.hash.sha256`) für alle Skripte.
- Headless-Konfiguration via `xvfb-run`, ALSA-Dummy-Treiber oder Native CLI-Render-Modi.

### Meilenstein 4: Zentrale Systemintegration & Registrierung
- Registrierung in `TOOLS.md` unter der Kategorie `Audio & Musik`.
- Mapping visueller und akustischer Artefakte in `VISUALIZATION.md`.
- Generierung der Dokumentationsnavigation via `scripts/generate_mkdocs_config.py`.

---

## 3. Phasenbasierter Rollout-Plan

Der Rollout ist nach technischer Komplexität und Abhängigkeiten strukturiert:

```
+-----------------------------------------------------------------------------------+
| Phase 1: Headless CLI Tools & Core Subsystems (7 Tools)                           |
| Fokus: Signalverarbeitung, Sound-Compiler, Notensatz-Engines & Audio-Server      |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| Phase 2: Audio-Editoren, Notensatz & Hybrid-Synthesizer (9 Tools)                 |
| Fokus: GUI-Standard-Tools mit CLI-Export, Software-Synths & Tabulatur-Editoren    |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| Phase 3: DAWs & Komplexe GUI-Workstations (9 Tools)                               |
| Fokus: Multitrack-Workstations, Modular-Synthesizer & Live-Coding-Umgebungen     |
+-----------------------------------------------------------------------------------+
```

---

## 4. Detaillierte Implementierungs- & Trackingmatrix

In der folgenden Tabelle sind alle 25 Musik-Tools mit ihren Zielpfaden, Beispieldaten, Validierungsstrategien und dem aktuellen Integrationsstatus aufgeführt.

| # | Werkzeug ID | Kategorie | Factsheet-Pfad | Phase | Geplante Beispieldaten (`examples/`) | Headless / CI Validierungsstrategie | Status |
| :-: | :--- | :--- | :--- | :-: | :--- | :--- | :-: |
| 1 | `fluidsynth` | Synthesizer | `factsheets/audio-musik/fluidsynth/` | Phase 1 | `.mid`, `.sf2`, `.conf`, `.cmd`, `.wav` | Native CLI Audio-Rendering (`fluidsynth -F`) | Abgeschlossen |
| 2 | `lilypond` | Notensatz | `factsheets/audio-musik/lilypond/` | Phase 1 | `.ly`, `.ily` (Include), Layout-Config, `.pdf`, `.mid` | Native CLI Compilation (`lilypond --png --pdf`) | Abgeschlossen |
| 3 | `csound` | Live Coding / DSP | `factsheets/audio-musik/csound/` | Phase 1 | `.csd`, `.orc`, `.sco`, Reverb Patch, `.wav` | Native CLI Compilation (`csound -o output.wav`) | Abgeschlossen |
| 4 | `supercollider` | Live Coding / DSP | `factsheets/audio-musik/supercollider/` | Phase 1 | `.scd` (Drone), `.scd` (SynthDef), Pattern, Server-Config, `.wav` | Headless `sclang` Non-Realtime Synthesis (NRT) | Abgeschlossen |
| 5 | `pure-data` | Visuelle Prog. | `factsheets/audio-musik/pure-data/` | Phase 1 | Main `.pd`, Sub-Patch `.pd`, Effect `.pd`, MIDI `.pd`, Wavetable Array | Headless DSP Processing (`pd -nogui -batch`) | Abgeschlossen |
| 6 | `pipewire` | Infrastruktur | `factsheets/audio-musik/pipewire/` | Phase 1 | `.conf`, WirePlumber Lua, `.dot` Graph, JACK Config, Mon-Log | CLI Graph & Node Management (`pw-cli`, `pw-dot`) | Abgeschlossen |
| 7 | `jack` | Infrastruktur | `factsheets/audio-musik/jack/` | Phase 1 | `jackdrc`, Patchbay XML, Dummy Driver Script, Latency Log, LSP Log | `jackd` mit Dummy-Treiber (`jackd -d dummy`) | Abgeschlossen |
| 8 | `audacity` | Audio-Editor | `factsheets/audio-musik/audacity/` | Phase 2 | Nyquist `.ny`, Noise Profile, Macro Chain, Label Track, Sample `.wav` | Nyquist Script Batch Mode & `xvfb-run` | Geplant |
| 9 | `tenacity` | Audio-Editor | `factsheets/audio-musik/tenacity/` | Phase 2 | Nyquist Convert `.ny`, EQ Preset XML, Test Tone `.wav`, Labels, Compressor XML | Batch Mode via Nyquist & `xvfb-run` | Geplant |
| 10 | `surge-xt` | Synthesizer | `factsheets/audio-musik/surge-xt/` | Phase 2 | `.surgepreset`, Custom `.wt`, Scala `.scl`, Mapping `.kbm`, MPE `.mid` | Surge XT CLI / LV2 Host Rendering (`lv2apply`) | Geplant |
| 11 | `zynaddsubfx` | Synthesizer | `factsheets/audio-musik/zynaddsubfx/` | Phase 2 | Master `.xmz`, SUB Preset `.xiz`, PAD Preset `.xiz`, Arpeggio `.mid`, Effekte | Native CLI Headless Output (`zynaddsubfx -U -I -a`) | Geplant |
| 12 | `helm` | Synthesizer | `factsheets/audio-musik/helm/` | Phase 2 | `.helm` Preset, Bass `.mid`, LFO JSON, Sequencer JSON, `.helmbank` | LV2 Host Rendering via `lv2apply` | Geplant |
| 13 | `musescore` | Notensatz | `factsheets/audio-musik/musescore/` | Phase 2 | `.mscz`, Uncompressed `.mscx`, `MusicXML`, Export `.pdf`, Style `.mss` | Headless Converter CLI (`musescore3 -o`) | Geplant |
| 14 | `frescobaldi` | Notensatz | `factsheets/audio-musik/frescobaldi/` | Phase 2 | Template `.ly`, Session XML, Snippets XML, MIDI Config, Hotkeys XML | `xvfb-run -a frescobaldi --version` & Linting | Geplant |
| 15 | `tuxguitar` | Notensatz | `factsheets/audio-musik/tuxguitar/` | Phase 2 | Native `.tg`, Guitar Pro `.gp5`, PowerTab `.ptb`, Tunings XML, Export `.pdf` | Headless Export via Java CLI & `xvfb-run` | Geplant |
| 16 | `carla` | Plugin-Host | `factsheets/audio-musik/carla/` | Phase 2 | Project `.carxp`, Rack `.carxr`, Blacklist Conf, Python MIDI Filter, Canvas `.svg` | Headless Plugin-Host CLI (`carla-single`) | Geplant |
| 17 | `ardour` | DAW | `factsheets/audio-musik/ardour/` | Phase 3 | Session XML, Export Profile XML, Lua Render Script, Track Template, Loop `.wav` | Lua Batch Render Mode & `xvfb-run` | Geplant |
| 18 | `lmms` | DAW | `factsheets/audio-musik/lmms/` | Phase 3 | Beat `.mmpz`, Synth Preset `.xspf`, Chord `.mid`, Drum Kit XML, Render Conf | Native CLI Renderer (`lmms render`) | Geplant |
| 19 | `qtractor` | DAW | `factsheets/audio-musik/qtractor/` | Phase 3 | Session `.qtr`, Multi-Channel `.mid`, Bus Routing XML, Connections XML, Metronome | Session Verification via `xvfb-run` | Geplant |
| 20 | `zrythm` | DAW | `factsheets/audio-musik/zrythm/` | Phase 3 | Archive `.zrythm`, Chord `.mid`, Pool Sample `.wav`, Plugin Chain XML, Automation | CLI Batch Export & `xvfb-run` | Geplant |
| 21 | `helio-workstation` | DAW | `factsheets/audio-musik/helio-workstation/` | Phase 3 | Project `.helio`, Melody `.mid`, Theme JSON, Git VCS JSON, Keybindings | Headless JSON-to-MIDI Render via `xvfb-run` | Geplant |
| 22 | `wavesurfer` | Audio-Editor | `factsheets/audio-musik/wavesurfer/` | Phase 3 | Spectrogram `.sfr`, Labels `.lab`, Pitch `.f0`, Formant Text, Vowel `.wav` | Spectrogram Export via `xvfb-run` | Geplant |
| 23 | `vcv-rack` | Modul-Synth | `factsheets/audio-musik/vcv-rack/` | Phase 3 | Modular `.vcv`, Module Selection `.vcvs`, Scope JSON, Clock Divider, Render `.wav` | VCV Headless SDK / Non-GUI Execution | Geplant |
| 24 | `sonic-pi` | Live Coding | `factsheets/audio-musik/sonic-pi/` | Phase 3 | Ambient `.rb`, Drum Beat `.rb`, Synth Pattern `.rb`, OSC Script `.rb`, Recorded `.wav` | CLI Evaluation via `sonic-pi-tool` / Ruby CLI | Geplant |
| 25 | `orca` | Live Coding | `factsheets/audio-musik/orca/` | Phase 3 | Polyrhythm `.orca`, Euclidean `.orca`, MIDI CC `.orca`, Config JSON, Event Log | Terminal Headless Execution (`orca-c`) | Geplant |

---

## 5. Automated Audit & Quality Gate

Nach Abschluss jeder Phase werden die automatisierte Qualitätsprüfung und Dokumentationsgenerierung durchgeführt:

1. **Factsheet-Analyse & Roadmap-Aktualisierung:**
   ```bash
   python3 scripts/analyze_factsheets.py
   ```
2. **Neugenerierung der zentralen Werkzeugliste (`TOOLS.md`):**
   ```bash
   python3 scripts/rebuild_tools_md.py
   ```
3. **Aktualisierung der MkDocs-Dokumentationskonfiguration (`mkdocs.yml`):**
   ```bash
   python3 scripts/generate_mkdocs_config.py
   ```

---

## 6. Zusammenfassung

Mit der vorliegenden Roadmap `MUSIC_ROADMAP.md` ist der Fahrplan zur Erweiterung des KI-Agenten-Repositorys von 114 auf 139 Factsheets präzise terminiert und nachvollziehbar dokumentiert. Jedes Werkzeug wird systematisch von der Dokumentation über funktionale Beispiele bis hin zum Headless-Integrationstest geführt.
