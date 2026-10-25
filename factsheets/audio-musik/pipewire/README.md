# Factsheet: PipeWire

## Gruppe: Audio & Musik

## Zweck: PipeWire ist ein modernisiertes Multimedia-Verarbeitungssystem und Audio-Routing-Server für Linux zur latenzarmen Handhabung von Audio- und Videostreams.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 1.6.9 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [pipewire.org](https://pipewire.org/) |
| Wikipedia | [de.wikipedia.org/wiki/PipeWire](https://de.wikipedia.org/wiki/PipeWire) |

## Installation (Ubuntu 24.04)

```bash
sudo apt-get update && sudo apt-get install -y pipewire pipewire-bin pipewire-audio-client-libraries graphviz
```

## Hello World

```bash
pw-cli --version
pw-dot -j examples/pw_mon_output.txt -o output_graph.dot 2>/dev/null || pw-dot -h
```

## Beispiele

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `pipewire_custom.conf`: Eine individuelle Konfigurationsdatei für den PipeWire-Daemon mit Einstellungen für Puffergrößen, Quanten und Echtzeit-Prioritäten.
- `virtual_sink.lua`: Ein WirePlumber-Skript in Lua zur Definition und automatischen Erstellung eines virtuellen Audio-Stereo-Sinks.
- `graph_topology.dot`: Eine Graphviz DOT-Graph-Spezifikation zur Visualisierung von Audioquellen, Mixern, Adaptern und Sinks im PipeWire-Graph.
- `jack_emulation.conf`: Eine Konfigurationsdatei zur Steuerung des PipeWire-JACK-Wrapper-Subsystems für nahtlose JACK-Kompatibilität.
- `pw_mon_output.txt`: Das Ereignisprotokoll einer PipeWire-Monitor-Sitzung zur Verifikation von Server-Status, Knoten-IDs und Port-Verbindungen.

## Validierung

PipeWire-Werkzeuge und Graph-Generierung im CLI-Modus prüfen:

```bash
pw-cli --version
pw-dot --version
dot -V
```
