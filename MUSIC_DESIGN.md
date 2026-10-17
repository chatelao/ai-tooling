# Design-Spezifikation: Integration der Musik- und Audio-Werkzeuge (MUSIC_DESIGN.md)

Dieses Dokument überführt das High-Level-Konzept aus **[MUSIC_CONCEPT.md](MUSIC_CONCEPT.md)** in ein detailliertes technisches Design- und Architekturkonzept zur Integration aller 25 Musik- und Audio-Werkzeuge in das Repositories-System unter Ubuntu 24.04 LTS (Noble Numbat).

---

## 1. Übersicht & Architekturansatz

Das Ziel dieser Design-Spezifikation ist die systematische Einbindung aller in `MUSIC_CONCEPT.md` genannten Musikproduktions-, Synthese-, Notensatz-, Audiobearbeitungs- und Live-Coding-Werkzeuge in die automatisierten Workflows des KI-Agenten-Repositorys (gemäß [GEMINI.md](GEMINI.md), [FACTSHEET_ROADMAP.md](FACTSHEET_ROADMAP.md) und der operativen [MUSIC_ROADMAP.md](MUSIC_ROADMAP.md)).

### Core Design Principles:
1. **Neue Kategorie `Audio & Musik`:** Erstellung des Verzeichnisses `factsheets/audio-musik/`.
2. **Standardisierte Factsheet-Struktur:** Jedes Werkzeug erhält ein isoliertes Verzeichnis unter `factsheets/audio-musik/<tool-id>/`.
3. **Headless & CI-Kompatibilität:** Da viele Musik- und DAW-Tools grafische Schnittstellen oder Audiotreiber erwarten, werden headless Teststrategien mit `xvfb-run` (für GUIs) und ALSA-Dummy-Treibern bzw. PipeWire-Virtuell-Modulen (für Audio-I/O) definiert.
4. **Beispieldaten-Reichtum (Milestone 2):** Jedes Factsheet enthält mindestens 5 funktionale Beispieldateien im Ordner `examples/` (MIDI, WAV/FLAC, Csound/Pure Data/Sonic Pi Patches, LilyPond/MusicXML Scores, etc.).
5. **Zentrale Registrierung:** Automatische Synchronisation mit `TOOLS.md`, `GROUPS.md`, `VISUALIZATION.md` und `mkdocs.yml`.

---

## 2. Zentrale Systemintegration

### 2.1 Ordner- & Gruppenstruktur
- **Verzeichnis:** `factsheets/audio-musik/`
- **Kategoriename in `TOOLS.md`:** `Audio & Musik`
- **Gruppen-Hash in `GROUPS.md`:** `e3a91b2c` (oder zugewiesener Hash für die Gruppe `Audio & Musik`)

### 2.2 Dateistruktur pro Werkzeug
Für jedes Werkzeug `<tool-id>` wird folgende Dateistruktur angelegt:
```
factsheets/audio-musik/<tool-id>/
├── README.md                      # Factsheet mit Metadaten, Installation, Hello World & Validierung
├── <tool-id>_install.sh           # Ausführbares Installationsskript
├── <tool-id>_install.sh.hash.sha256 # Hash-Checksumme des Installationsskripts
├── <tool-id>_run_test.sh          # Ausführbares Testskript
├── <tool-id>_run_test.sh.hash.sha256 # Hash-Checksumme des Testskripts
└── examples/                      # Ordner mit mind. 5 repräsentativen Beispieldaten
    ├── example1...
    ├── example2...
    ├── example3...
    ├── example4...
    └── example5...
```

### 2.3 Visualisierungs-Mapping in `VISUALIZATION.md`
Die generierten visuellen und akustischen Artefakte der Musik-Tools werden wie folgt in `VISUALIZATION.md` registriert:

| Visualisierungstyp | Werkzeug | Gruppe |
| :--- | :--- | :--- |
| Spektrogramme & Frequenzanalyse | [Audacity](factsheets/audio-musik/audacity/README.md) | Audio & Musik |
| Partitur- & Notensatz-Rendering (PDF/PNG) | [MuseScore](factsheets/audio-musik/musescore/README.md) | Audio & Musik |
| Vektorbasiertes Notengravur-Rendering | [LilyPond](factsheets/audio-musik/lilypond/README.md) | Audio & Musik |
| Gitarren-Tabulaturen | [TuxGuitar](factsheets/audio-musik/tuxguitar/README.md) | Audio & Musik |
| Modulare Signalfluss-Graphen | [Pure Data](factsheets/audio-musik/pure-data/README.md) | Audio & Musik |
| Virtual Eurorack Modul-Graphen | [VCV Rack](factsheets/audio-musik/vcv-rack/README.md) | Audio & Musik |
| Audio-Routing-Graphen | [Carla](factsheets/audio-musik/carla/README.md) | Audio & Musik |

---

## 3. Detaillierte Spezifikationen der 25 Musik-Werkzeuge

Nachfolgend sind die konkreten Integrationsspezifikationen für alle 25 Musik-Tools aufgeführt, aufgeteilt nach den 6 Kategorien aus `MUSIC_CONCEPT.md`.

---

### Kategorie 1: Digital Audio Workstations (DAWs) & Sequencer

#### 1. Ardour (`ardour`)
- **Pfad:** `factsheets/audio-musik/ardour/`
- **Installation:** `sudo DEBIAN_FRONTEND=noninteractive apt-get install -y ardour`
- **Headless-Strategie:** `xvfb-run -a ardour5 --headless` oder Batch-Mode-Session-Export via Lua-Scripting.
- **Hello World:** `ardour-hello.lua` Skript, das eine neue Ardour-Session im Batch-Modus erstellt und eine Spur anlegt.
- **5 Beispieldaten in `examples/`:**
  1. `session_template.ardour` (Ardour XML-Session-Datei)
  2. `export_profile.xml` (Stereo Export-Profil)
  3. `lua_batch_render.lua` (Automatisations-Skript)
  4. `midi_track_config.xml` (Track-Template)
  5. `sample_loop.wav` (Test-Audio-Loop)

#### 2. LMMS (`lmms`)
- **Pfad:** `factsheets/audio-musik/lmms/`
- **Installation:** `sudo DEBIAN_FRONTEND=noninteractive apt-get install -y lmms`
- **Headless-Strategie:** `lmms render project.mmpz -o output.wav` (LMMS unterstützt CLI-Rendering nativ).
- **Hello World:** Rendering eines minimalen `.mmpz`-Beispielprojekts in eine Wave-Datei per Kommandozeile.
- **5 Beispieldaten in `examples/`:**
  1. `beat.mmpz` (LMMS Beat-Projekt)
  2. `synth_preset.xspf` (Triple-Oscillator Preset)
  3. `chord_sequence.mid` (MIDI-Akkordfolge)
  4. `drum_kit.xml` (Audio-File-Processor Config)
  5. `render_config.xml` (Export-Einstellungen)

#### 3. Qtractor (`qtractor`)
- **Pfad:** `factsheets/audio-musik/qtractor/`
- **Installation:** `sudo DEBIAN_FRONTEND=noninteractive apt-get install -y qtractor`
- **Headless-Strategie:** `xvfb-run -a qtractor -g project.qtr`
- **Hello World:** Validierung des CLI-Aufrufs und Erzeugung einer Standard-Projektdatei.
- **5 Beispieldaten in `examples/`:**
  1. `demo_session.qtr` (Qtractor Session XML)
  2. `midi_sequence.mid` (Multi-Channel MIDI)
  3. `bus_routing.xml` (JACK/PipeWire Bus-Config)
  4. `connections.qrc` (Session Connections XML)
  5. `test_click.wav` (Metronom-Sample)

#### 4. Zrythm (`zrythm`)
- **Pfad:** `factsheets/audio-musik/zrythm/`
- **Installation:** `sudo DEBIAN_FRONTEND=noninteractive apt-get install -y zrythm` oder Flatpak/Source Build.
- **Headless-Strategie:** `xvfb-run -a zrythm --version` und CLI-Batch Export.
- **Hello World:** Erzeugung eines Minimal-Projekts und Validierung der Zrythm-CLI.
- **5 Beispieldaten in `examples/`:**
  1. `project.zrythm` (Zrythm Projekt-Archiv)
  2. `chord_progression.mid` (Akkord-Assistent MIDI-Export)
  3. `pool_sample.wav` (Audio-Pool Sample)
  4. `plugin_chain.xml` (CLAP/LV2 Plugin-Kette)
  5. `automation_track.xml` (Automationskurven-Template)

#### 5. Helio Workstation (`helio-workstation`)
- **Pfad:** `factsheets/audio-musik/helio-workstation/`
- **Installation:** AppImage / Flatpak / PPA Build.
- **Headless-Strategie:** `xvfb-run -a helio --version`
- **Hello World:** Rendern eines Helio-JSON-Sequenzer-Projekts nach MIDI.
- **5 Beispieldaten in `examples/`:**
  1. `song.helio` (Helio JSON-Projektdatei)
  2. `melody.mid` (Exportierte Melodie-Spur)
  3. `theme.json` (UI Theme Config)
  4. `git_vcs_config.json` (Integrierte Git-Config)
  5. `keybindings.json` (Tastaturkürzel)

---

### Kategorie 2: Audio-Editing & Signalbearbeitung

#### 6. Audacity (`audacity`)
- **Pfad:** `factsheets/audio-musik/audacity/`
- **Installation:** `sudo DEBIAN_FRONTEND=noninteractive apt-get install -y audacity`
- **Headless-Strategie:** Python mod-script-pipe / Nyquist Batch Processing (`audacity --help` / `xvfb-run`).
- **Hello World:** Nyquist-Skript zur Frequenzerzeugung und Export einer `.wav`-Datei.
- **5 Beispieldaten in `examples/`:**
  1. `generate_sine.ny` (Nyquist Sinusgenerator-Skript)
  2. `noise_reduction_profile.txt` (Rauschprofil-Datei)
  3. `macro_chain.txt` (Audacity Stapelverarbeitungs-Makro)
  4. `label_track.txt` (Marker- und Textspur)
  5. `test_speech.wav` (Test-Sprachaufnahme)

#### 7. Tenacity (`tenacity`)
- **Pfad:** `factsheets/audio-musik/tenacity/`
- **Installation:** `sudo DEBIAN_FRONTEND=noninteractive apt-get install -y tenacity` (oder Flatpak/Source).
- **Headless-Strategie:** `xvfb-run -a tenacity --version`
- **Hello World:** Telemetriefreies Batch-Skript zur Konvertierung von WAV nach OGG via Nyquist.
- **5 Beispieldaten in `examples/`:**
  1. `convert_batch.ny` (Nyquist Konvertierungsskript)
  2. `equalizer_preset.xml` (EQ-Kurven-Preset)
  3. `test_tone.wav` (440Hz Testton)
  4. `labels.txt` (Export-Label-Datei)
  5. `compressor_settings.xml` (Kompressor-Preset)

#### 8. WaveSurfer (`wavesurfer`)
- **Pfad:** `factsheets/audio-musik/wavesurfer/`
- **Installation:** `sudo DEBIAN_FRONTEND=noninteractive apt-get install -y wavesurfer` (Tcl/Tk).
- **Headless-Strategie:** `xvfb-run -a wavesurfer -config spectrogram.sfr`
- **Hello World:** Automatisiertes Erzeugen eines Spektrogramm-Plots aus einem Sprachsample.
- **5 Beispieldaten in `examples/`:**
  1. `spectrogram.sfr` (WaveSurfer Spektrogramm-Konfiguration)
  2. `phonetic_transcription.lab` (Phonetische Label-Datei)
  3. `pitch_contour.f0` (Grundfrequenz-Contour-Daten)
  4. `formant_analysis.txt` (Formant-Analyse-Export)
  5. `sample_vowel.wav` (Vokal-Sprachsample)

---

### Kategorie 3: Software-Synthesizer, Sampler & Klangerzeugung

#### 9. Surge XT (`surge-xt`)
- **Pfad:** `factsheets/audio-musik/surge-xt/`
- **Installation:** `sudo DEBIAN_FRONTEND=noninteractive apt-get install -y surge-synthesizer` (oder Standalone / VST3 / LV2).
- **Headless-Strategie:** `surge-xt-cli` oder via LV2 Host (`lv2apply` / `carla-single`).
- **Hello World:** Rendern eines Synth-Pads aus einem Surge-Patch (`.fxp`/`.surgepreset`) in WAV.
- **5 Beispieldaten in `examples/`:**
  1. `warm_pad.surgepreset` (Surge XT Patch)
  2. `wavetable_custom.wt` (Benutzerdefinierte Wavetable)
  3. `tuning_scale.scl` (Scala Mikrotonale Skala)
  4. `keyboard_mapping.kbm` (Scala Keyboard Mapping)
  5. `mpe_test.mid` (MPE-MIDI-Datei)

#### 10. ZynAddSubFX / Yoshimi (`zynaddsubfx`)
- **Pfad:** `factsheets/audio-musik/zynaddsubfx/`
- **Installation:** `sudo DEBIAN_FRONTEND=noninteractive apt-get install -y zynaddsubfx yoshimi`
- **Headless-Strategie:** `zynaddsubfx -U -I -l patch.xmz -m test.mid -a output.wav` (Nativer CLI Headless-Modus).
- **Hello World:** Headless-Synthese einer MIDI-Sequenz mit einem ZynAddSubFX-XML-Preset.
- **5 Beispieldaten in `examples/`:**
  1. `pad_preset.xmz` (ZynAddSubFX Master Preset)
  2. `sub_synth.xiz` (Subtraktives Instrument Preset)
  3. `pad_synth.xiz` (PADsynth Harmonie-Preset)
  4. `arpeggio.mid` (Test-MIDI-Arpeggio)
  5. `effect_chain.eff` (Effektketten-Konfiguration)

#### 11. Helm (`helm`)
- **Pfad:** `factsheets/audio-musik/helm/`
- **Installation:** `sudo DEBIAN_FRONTEND=noninteractive apt-get install -y helm`
- **Headless-Strategie:** Execution via LV2 Host (`lv2apply` mit `http://tytel.org/helm`).
- **Hello World:** LV2-Patch-Rendering mit `lv2apply` und Output in Wave-Datei.
- **5 Beispieldaten in `examples/`:**
  1. `lead_synth.helm` (Helm Preset-Datei)
  2. `bass_line.mid` (MIDI-Bassline)
  3. `lfo_shape.json` (Benutzerdefinierte LFO-Form)
  4. `step_sequencer.json` (Sequenzer-Pattern)
  5. `patch_bank.helmbank` (Helm Preset-Bank)

#### 12. VCV Rack Free (`vcv-rack`)
- **Pfad:** `factsheets/audio-musik/vcv-rack/`
- **Installation:** Official VCV Rack Free binary / SDK integration.
- **Headless-Strategie:** `xvfb-run -a Rack -headful=false` oder VCV Rack Headless SDK.
- **Hello World:** Generieren eines generativen Audio-Loops aus einem `.vcv`-Patch.
- **5 Beispieldaten in `examples/`:**
  1. `generative_patch.vcv` (VCV Rack Modular Patch)
  2. `patch_selection.vcvs` (Modul-Gruppen Preset)
  3. `scope_config.json` (Oszilloskop-Modul Config)
  4. `clock_divider.vcv` (Taktteiler-Patch)
  5. `sample_shot.wav` (Generiertes Modular-Audio)

#### 13. FluidSynth (`fluidsynth`)
- **Pfad:** `factsheets/audio-musik/fluidsynth/`
- **Installation:** `sudo DEBIAN_FRONTEND=noninteractive apt-get install -y fluidsynth fluid-soundfont-gm`
- **Headless-Strategie:** `fluidsynth -ni /usr/share/sounds/sf2/FluidR3_GM.sf2 input.mid -F output.wav -r 44100`
- **Hello World:** Konvertierung einer MIDI-Datei mit dem General MIDI SoundFont in ein Wave-Audio.
- **5 Beispieldaten in `examples/`:**
  1. `mozart_k545.mid` (MIDI-Testdatei)
  2. `custom_font.sf2` (Minimaler SoundFont2)
  3. `fluidsynth_config.conf` (CLI Config-Datei)
  4. `shell_commands.cmd` (FluidSynth Interaktive Shell Befehle)
  5. `rendered_sample.wav` (Erzeugtes Audio)

---

### Kategorie 4: Partitur, Notensatz & Gitarren-Tabulatur

#### 14. MuseScore (`musescore`)
- **Pfad:** `factsheets/audio-musik/musescore/`
- **Installation:** `sudo DEBIAN_FRONTEND=noninteractive apt-get install -y musescore3` (oder musescore4 AppImage).
- **Headless-Strategie:** `musescore3 -o score.pdf score.mscz` / `xvfb-run -a musescore3 -o score.png score.mscx`
- **Hello World:** Rendern einer `.mscz`-Partitur in PDF und PNG-Vorschau ohne GUI.
- **5 Beispieldaten in `examples/`:**
  1. `quartet.mscz` (MuseScore Binär-Partitur)
  2. `lead_sheet.mscx` (Unkomprimierte XML-Partitur)
  3. `score_export.musicxml` (MusicXML-Austauschformat)
  4. `piano_part.pdf` (Generiertes PDF)
  5. `style_settings.mss` (MuseScore Style Sheet)

#### 15. LilyPond (`lilypond`)
- **Pfad:** `factsheets/audio-musik/lilypond/`
- **Installation:** `sudo DEBIAN_FRONTEND=noninteractive apt-get install -y lilypond`
- **Headless-Strategie:** `lilypond --png --pdf score.ly` (Nativer CLI Notensatz-Generator).
- **Hello World:** Kompilieren eines `.ly`-Textfiles zu vektorbasiertem PDF/PNG und MIDI.
- **5 Beispieldaten in `examples/`:**
  1. `symphony_theme.ly` (LilyPond Haupt-Code)
  2. `chords_header.ily` (LilyPond Include-Datei)
  3. `paper_layout.ily` (Layout- und Papier-Konfiguration)
  4. `rendered_score.pdf` (Generierte PDF-Datei)
  5. `rendered_score.mid` (Generierte MIDI-Datei)

#### 16. Frescobaldi (`frescobaldi`)
- **Pfad:** `factsheets/audio-musik/frescobaldi/`
- **Installation:** `sudo DEBIAN_FRONTEND=noninteractive apt-get install -y frescobaldi`
- **Headless-Strategie:** `xvfb-run -a frescobaldi --version`
- **Hello World:** Validierung der Frescobaldi Python-IDE Umgebung und LilyPond-Parsing.
- **5 Beispieldaten in `examples/`:**
  1. `template_orchestra.ly` (Frescobaldi Vorlage)
  2. `frescobaldi_session.xml` (Session-Konfiguration)
  3. `snippet_library.xml` (Code-Snippet-Bibliothek)
  4. `midi_settings.ini` (MIDI-Wiedergabe-Config)
  5. `shortcut_scheme.xml` (Tastatur-Hotkeys)

#### 17. TuxGuitar (`tuxguitar`)
- **Pfad:** `factsheets/audio-musik/tuxguitar/`
- **Installation:** `sudo DEBIAN_FRONTEND=noninteractive apt-get install -y tuxguitar`
- **Headless-Strategie:** `xvfb-run -a tuxguitar -p song.gp5` (Konvertierung nach MIDI/PDF via Java CLI).
- **Hello World:** Exportieren einer Guitar-Pro (.gp5) Tabulatur in PDF und MIDI.
- **5 Beispieldaten in `examples/`:**
  1. `riff_master.tg` (TuxGuitar Nativ-Format)
  2. `rock_classic.gp5` (Guitar Pro 5 Format)
  3. `fingerpicking.ptb` (PowerTab Format)
  4. `tuning_presets.xml` (Gitarren-Stimmungen)
  5. `tab_export.pdf` (Rendertab-PDF)

---

### Kategorie 5: Algorithmische Komposition & Live Coding

#### 18. Sonic Pi (`sonic-pi`)
- **Pfad:** `factsheets/audio-musik/sonic-pi/`
- **Installation:** `sudo DEBIAN_FRONTEND=noninteractive apt-get install -y sonic-pi`
- **Headless-Strategie:** `sonic-pi-tool eval "play 60"` / `ruby sonic_pi_cli.rb script.rb`
- **Hello World:** Ausführen eines Ruby-Live-Coding-Skripts zur Erzeugung eines Ambient-Pads.
- **5 Beispieldaten in `examples/`:**
  1. `ambient_generative.rb` (Sonic Pi Live-Code Skript)
  2. `drum_beat_loop.rb` (Algorithnischer Beat)
  3. `synth_melody.rb` (Synth-Akkord-Muster)
  4. `osc_controller.rb` (OSC Empfänger Skript)
  5. `recorded_output.wav` (Audio-Mitschnitt)

#### 19. Pure Data (`pure-data`)
- **Pfad:** `factsheets/audio-musik/pure-data/`
- **Installation:** `sudo DEBIAN_FRONTEND=noninteractive apt-get install -y puredata`
- **Headless-Strategie:** `pd -nogui -send "pd dac 1" -open patch.pd -batch`
- **Hello World:** Ausführen eines headless DSP-Patches zur Synthese eines Sinustons in eine WAV-Datei.
- **5 Beispieldaten in `examples/`:**
  1. `synth_engine.pd` (Pure Data Haupt-Patch)
  2. `oscillator_sub.pd` (Sub-Patch Abstraktion)
  3. `delay_effect.pd` (Audio-Effekt Abstraktion)
  4. `midi_in_handler.pd` (MIDI-Eingabe Patch)
  5. `array_data.txt` (Wavetable Array Daten)

#### 20. SuperCollider (`supercollider`)
- **Pfad:** `factsheets/audio-musik/supercollider/`
- **Installation:** `sudo DEBIAN_FRONTEND=noninteractive apt-get install -y supercollider sclang scsynth`
- **Headless-Strategie:** `sclang -D script.scd` (sclang steuert den headless scsynth Server).
- **Hello World:** Erstellen einer SynthDef im Headless-Modus und Render-NTP-Audio-Export.
- **5 Beispieldaten in `examples/`:**
  1. `generative_drone.scd` (SuperCollider Code-Skript)
  2. `custom_synthdef.scd` (SynthDef Definition)
  3. `pattern_sequence.scd` (Pbind Sequenzierer)
  4. `scsynth_config.scd` (Server Options Setup)
  5. `rendered_buffer.wav` (Gerendertes Audio)

#### 21. Orca (`orca`)
- **Pfad:** `factsheets/audio-musik/orca/`
- **Installation:** Node.js package / C build (`orca-c`).
- **Headless-Strategie:** `orca-c -t 120 patch.orca` (Terminal-basierter ASCII-Sequenzer).
- **Hello World:** Ausführen eines 2D-ASCII-Rasters zur Generierung von MIDI-Events.
- **5 Beispieldaten in `examples/`:**
  1. `polyrhythm.orca` (Orca ASCII Grid Patch)
  2. `euclidean_beat.orca` (Euklidischer Rhythmus Grid)
  3. `midi_cc_control.orca` (MIDI Modulation Patch)
  4. `orca_config.json` (CLI Einstellungen)
  5. `output_events.log` (Geloggter MIDI-Stream)

#### 22. Csound (`csound`)
- **Pfad:** `factsheets/audio-musik/csound/`
- **Installation:** `sudo DEBIAN_FRONTEND=noninteractive apt-get install -y csound`
- **Headless-Strategie:** `csound -o output.wav piece.csd` (Nativer High-Performance Compiler).
- **Hello World:** Rendern einer `.csd`-Datei (Orchestra + Score) in eine hochauflösende WAV-Datei.
- **5 Beispieldaten in `examples/`:**
  1. `fm_synthesis.csd` (Vereinigte Csound Datei)
  2. `additive_orch.orc` (Orchestra-Datei)
  3. `score_events.sco` (Score-Datei)
  4. `reverb_effect.csd` (DSP Effekt-Prozessor)
  5. `csound_output.wav` (Audio-Export)

---

### Kategorie 6: Audio-Infrastruktur, Routing & Plugin-Hosts

#### 23. PipeWire (`pipewire`)
- **Pfad:** `factsheets/audio-musik/pipewire/`
- **Installation:** `sudo DEBIAN_FRONTEND=noninteractive apt-get install -y pipewire pipewire-audio-client-libraries pw-cli`
- **Headless-Strategie:** `pw-cli info` / `pw-dot -o graph.dot` (Headless Multimedia Graph Management).
- **Hello World:** Erzeugen eines PipeWire Virtuell-Sink-Knotens und Exportieren des Graph-Diagramms.
- **5 Beispieldaten in `examples/`:**
  1. `pipewire_custom.conf` (PipeWire Daemon Config)
  2. `virtual_sink.lua` (WirePlumber Lua-Skript)
  3. `graph_topology.dot` (Graphviz Subsystem-Topology)
  4. `jack_emulation.conf` (JACK Emulations-Profil)
  5. `pw_mon_output.txt` (PW-Mon Ereignislog)

#### 24. JACK Audio Connection Kit (`jack`)
- **Pfad:** `factsheets/audio-musik/jack/`
- **Installation:** `sudo DEBIAN_FRONTEND=noninteractive apt-get install -y jackd2 libjack-jackd2-dev`
- **Headless-Strategie:** `jackd -r -d dummy -r 44100 -p 1024 &` (Nativer Dummy-Treiber für Headless/CI).
- **Hello World:** Starten des `jackd` Dummy-Servers und Abfragen von `jack_lsp`.
- **5 Beispieldaten in `examples/`:**
  1. `jackdrc.conf` (JACK Server Parameter)
  2. `patchbay_matrix.xml` (JACK-Patchbay Verbindungen)
  3. `dummy_driver_setup.sh` (Dummy-Treiber Startskript)
  4. `latency_test.txt` (Latenz-Messdaten)
  5. `jack_lsp_output.txt` (Port-Liste Log)

#### 25. Carla (`carla`)
- **Pfad:** `factsheets/audio-musik/carla/`
- **Installation:** `sudo DEBIAN_FRONTEND=noninteractive apt-get install -y carla carla-bridge-linux32 carla-bridge-linux64`
- **Headless-Strategie:** `carla-single vst3 /path/to/plugin.so` / `xvfb-run -a carla project.carxp`
- **Hello World:** Headless-Laden einer Carla-Patchbay-Session (`.carxp`) mit einem LV2-Plugin.
- **5 Beispieldaten in `examples/`:**
  1. `patchbay_setup.carxp` (Carla XML Projekt-Datei)
  2. `rack_layout.carxr` (Carla Rack Preset)
  3. `plugin_blacklist.conf` (Plugin-Scanner Config)
  4. `midi_filter.py` (Integrierter Carla Python-MIDI-Filter)
  5. `canvas_export.svg` (Visualisiertes Routing Diagramm)

---

## 4. Automatisierung & Integrations-Pipeline

Der Prozess zur automatisierten Aufnahme eines neuen Musik-Werkzeugs folgt folgender Pipeline:

```
+-------------------------------------------------------------------------+
| Step 1: Factsheet-Ordner & README.md in factsheets/audio-musik/ anlegen |
+-------------------------------------------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
| Step 2: 5+ funktionale Beispieldateien in examples/ bereitstellen       |
+-------------------------------------------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
| Step 3: Skript-Generierung via `generate_tool_scripts.py`               |
| (Erzeugt <tool>_install.sh und <tool>_run_test.sh)                      |
+-------------------------------------------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
| Step 4: Testausführung & SHA256-Hash-Generierung                         |
| (Erzeugt .log und .hash.sha256 Verifizierungsdateien)                  |
+-------------------------------------------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
| Step 5: Zentrale Registrierung in TOOLS.md, GROUPS.md, VISUALIZATION.md |
| `scripts/rebuild_tools_md.py` & `scripts/generate_mkdocs_config.py`    |
+-------------------------------------------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
| Step 6: Validierung & Audit via `scripts/analyze_factsheets.py`        |
+-------------------------------------------------------------------------+
```

### Befehle zur Skript-Generierung & Rebuild:
```bash
# 1. Skripte aus README.md extrahieren
python3 generate_tool_scripts.py

# 2. Skript-Hashes erzeugen
sha256sum factsheet_install.sh > factsheet_install.sh.hash.sha256
sha256sum factsheet_run_test.sh > factsheet_run_test.sh.hash.sha256

# 3. TOOLS.md neu aufbauen
python3 scripts/rebuild_tools_md.py

# 4. MkDocs-Konfiguration regenerieren
python3 scripts/generate_mkdocs_config.py

# 5. Quality Audit durchführen
python3 scripts/analyze_factsheets.py
```

---

## 5. Meilensteine & Zeitplan für das Rollout

Die Onboarding-Phase der Musik-Tools ist in 3 Meilensteine gegliedert (detailliert in **[MUSIC_ROADMAP.md](MUSIC_ROADMAP.md)**):

| Meilenstein | Zielstellung | Fokus-Werkzeuge |
| :--- | :--- | :--- |
| **Phase 1** | Headless CLI Tools & Core Synthesizer | FluidSynth, LilyPond, Csound, SuperCollider, Pure Data, PipeWire, JACK |
| **Phase 2** | Audio-Editoren, Notensatz & Hybrid-Synths | Audacity, Tenacity, Surge XT, ZynAddSubFX, MuseScore, TuxGuitar, Carla |
| **Phase 3** | DAWs & Komplexe GUI-Workstations | Ardour, LMMS, Qtractor, Zrythm, VCV Rack, Helio, Sonic Pi, Orca, WaveSurfer |

---

## 6. Zusammenfassung & Nächste Schritte

Mit dieser Design-Spezifikation ist ein reproduzierbarer, automatisierbarer und voll integrierter Leitfaden vorhanden, um das Repository von 114 Factsheets auf 139 Factsheets zu erweitern.

Die Einbindung von `MUSIC_DESIGN.md` und `MUSIC_ROADMAP.md` in die Hauptnavigation von `mkdocs.yml` stellt sicher, dass Entwickler und KI-Agenten jederzeit Zugriff auf diese Spezifikation und den operativen Rollout-Plan haben.
