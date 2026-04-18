# Azure MCP Server

## Zweck

Der Azure MCP Server ermöglicht es KI-Agenten, direkt mit Azure-Diensten zu
interagieren, indem er Azure-spezifische Tools über das Model Context Protocol
bereitstellt. Er bietet eine tiefere Integration als die CLI, da er dem Modell
strukturierten Zugriff auf über 40 Azure-Dienste bietet, inklusive
Sicherheitsbewertungen und Architektur-Empfehlungen.

## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Referenzhandbuch

[Link](https://github.com/microsoft/mcp)

## Installation (Ubuntu 24.04)

Voraussetzung: [uv](https://github.com/astral-sh/uv) muss installiert sein.

```bash
uvx --from msmcp-azure azmcp server start
```

## Validierung

```bash
uvx --from msmcp-azure azmcp --help
```

## Nutzung für KI-Agenten

- **Dienste**: Zugriff auf Azure Compute, Storage, Cosmos DB, Key Vault uvm.
- **Expertise**: Der Agent kann Advisor-Empfehlungen und Well-Architected
  Framework Guidelines abrufen.
- **Integration**: Nahtlose Nutzung in VS Code (über Copilot) oder Claude
  Desktop.
