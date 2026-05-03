# Factsheet: Renode

## Gruppe: Hardware/simulation

## Zweck: Renode ist ein Werkzeug für die Simulation von eingebetteten Systemen.

| Eigenschaft | Wert |
| :--- | :--- |
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
