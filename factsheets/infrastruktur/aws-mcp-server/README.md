# AWS MCP Server

## Zweck

Der AWS MCP Server implementiert das Model Context Protocol (MCP), um
KI-Agenten (wie Claude Desktop oder Kiro) direkten, sicheren und
dokumentationsgestützten Zugriff auf AWS-Ressourcen zu ermöglichen. Im
Gegensatz zur reinen CLI bietet der MCP Server dem Agenten Werkzeuge (Tools)
mit Metadaten an, die es dem Modell erleichtern, die richtigen Parameter zu
wählen und Best Practices einzuhalten.

## Installation (Ubuntu 24.04)

Voraussetzung: [uv](https://github.com/astral-sh/uv) muss installiert sein.

```bash
uvx awslabs.aws-api-mcp-server@latest
```

## Validierung

Der Server wird normalerweise über einen MCP-Client konfiguriert. Manuell kann
die Funktionsfähigkeit geprüft werden durch:

```bash
uvx awslabs.aws-api-mcp-server@latest --help
```

## Nutzung für KI-Agenten

- **Tools**: Der Server registriert Funktionen für S3, EC2, Lambda etc. direkt
  beim Agenten.
- **Kontext**: Der Agent erhält Zugriff auf aktuelle AWS-Dokumentationen und
  "What's New"-Posts.
- **Sicherheit**: Nutzt IAM-Rollen des Systems, ohne dass der Agent Zugriff auf
  die Secret Keys selbst benötigt.
