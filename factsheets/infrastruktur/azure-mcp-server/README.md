# Azure MCP Server

## Zweck

Der Azure MCP Server ermöglicht es KI-Agenten, direkt mit Azure-Diensten zu
interagieren, indem er Azure-spezifische Tools über das Model Context Protocol
bereitstellt. Er bietet eine tiefere Integration als die CLI, da er dem Modell
strukturierten Zugriff auf über 40 Azure-Dienste bietet, inklusive
Sicherheitsbewertungen und Architektur-Empfehlungen.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [github.com/microsoft/mcp](https://github.com/microsoft/mcp) |

## Installation (Ubuntu 24.04)

Voraussetzung: [github.com/astral-sh/uv](https://github.com/astral-sh/uv) muss installiert sein.

```bash
uvx --from msmcp-azure azmcp server start
```

## Hello World

```bash
npx @microsoft/azmcp
```

## Validierung

```bash
uvx --from msmcp-azure azmcp --help
```

## Beispiele

Im Ordner `examples/` befinden sich verschiedene Beispiele für den Azure MCP Server:

1.  `config_claude_desktop.json`: Konfiguration für Claude Desktop.
2.  `credentials.json`: Beispiel für die Struktur der Anmeldedaten.
3.  `prompt_advisor.txt`: Beispiel-Prompt zur Abfrage von Azure Advisor Empfehlungen.
4.  `prompt_aks.txt`: Beispiel-Prompt zur Interaktion mit Azure Kubernetes Service.
5.  `prompt_keyvault.txt`: Beispiel-Prompt zur Verwaltung von Geheimnissen im Key Vault.

## Nutzung für KI-Agenten

- **Dienste**: Zugriff auf Azure Compute, Storage, Cosmos DB, Key Vault uvm.
- **Expertise**: Der Agent kann Advisor-Empfehlungen und Well-Architected
  Framework Guidelines abrufen.
- **Integration**: Nahtlose Nutzung in VS Code (über Copilot) oder Claude
  Desktop.
