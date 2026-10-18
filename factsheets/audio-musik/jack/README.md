# Factsheet: JACK Audio Connection Kit (JACK)

## Gruppe: Audio & Musik

## Zweck: JACK ist ein professioneller, latenzarmer Sound-Server und Connection-Manager zur flexiblen Vernetzung und synchronen Audio/MIDI-Kopplung mehrerer Anwendungen.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 1.9.22 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [jackaudio.org](https://jackaudio.org/) |
| Wikipedia | [de.wikipedia.org/wiki/JACK_Audio_Connection_Kit](https://de.wikipedia.org/wiki/JACK_Audio_Connection_Kit) |

## Installation (Ubuntu 24.04)

```bash
sudo apt-get update && sudo apt-get install -y jackd2 jack-tools
```

## Hello World

```bash
jackd --version
jackd -d dummy -r 44100 -p 1024 &
JACK_PID=$! && sleep 1 && kill $JACK_PID
```

## Beispiele

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `jackdrc`: Eine typische Konfigurationsdatei zur Definition von Startparametern für den JACK-Daemon im Headless-Modus.
- `patchbay.xml`: Eine XML-Spezifikation für automatische Audio- und MIDI-Signalverbindungen im JACK-Patchbay-Graph.
- `dummy_driver.sh`: Ein Shell-Skript zur Demonstration des Serverstarts und der Prozessverwaltung mit dem Dummy-Treiber.
- `latency_log.txt`: Ein Diagnoseprotokoll mit Performance-Metriken, Puffergrößen, Sample-Raten und Latenzberechnungen.
- `jack_lsp_output.txt`: Ein repräsentativer Log-Auszug des Befehls `jack_lsp` zur Auflistung registrierter Ports und Audio-Endpunkte.

## Validierung

Start und Versionierung des JACK-Audio-Servers im Headless-Dummy-Modus prüfen:

```bash
jackd --version
jackd -d dummy -r 44100 -p 1024 &
JACK_PID=$! && sleep 1 && kill $JACK_PID
```
