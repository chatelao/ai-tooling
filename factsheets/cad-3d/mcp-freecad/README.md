# Factsheet: Mcp freecad

## Gruppe: Cad/3d

## Zweck: MCP-FreeCAD ist ein Model Context Protocol Server zur Fernsteuerung und Automatisierung von FreeCAD.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [github.com/jango-blockchained/mcp-freecad](https://github.com/jango-blockchained/mcp-freecad) |

## Installation (Ubuntu 24.04)

```bash
git clone https://github.com/jango-blockchained/mcp-freecad.git
cd mcp-freecad && pip install -r requirements.txt
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `config.json`
- `test.py`
- `doc.md`
- `env.sh`
- `readme.txt`

## Validierung

MCP-Server starten:

```bash
cd mcp-freecad && /usr/bin/python3 mcp_server.py --help
```
