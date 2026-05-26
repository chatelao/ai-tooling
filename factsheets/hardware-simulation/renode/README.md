# Factsheet: Renode

## Gruppe: Hardware/simulation

## Zweck

Renode ist ein Open-Source-Simulations-Framework für komplexe eingebettete Systeme (Embedded Systems). Es ermöglicht die Simulation von Hardware-Plattformen inklusive CPUs (ARM, RISC-V, etc.), Peripheriegeräten, Sensoren und sogar ganzen Netzwerken von Geräten.

Vorteile für die Entwicklung:
- Software-Tests ohne physische Hardware.
- Simulation von Multi-Node-Systemen und deren Kommunikation.
- Deterministische Ausführung für einfaches Debugging.
- Integration in CI/CD-Pipelines für automatisiertes Testen von Firmware.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 1.15.3 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [renode.io](https://renode.io/) |

## Installation (Ubuntu 24.04)

```bash
sudo apt-get update
wget https://github.com/renode/renode/releases/download/v1.16.1/renode_1.16.1_amd64.deb
sudo apt-get install -y ./renode_1.16.1_amd64.deb
rm renode_1.16.1_amd64.deb
```

## Hello World

```bash
renode -e "echo 'Hello World'; quit"
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `test.resc`
- `machine.repl`
- `firmware.bin`
- `log.txt`
- `config.json`

## Validierung

```bash
renode factsheets/hardware-simulation/renode/examples/test.resc
renode --version
```
