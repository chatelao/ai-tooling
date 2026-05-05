# AWS MCP Server

## Zweck

Der AWS MCP Server implementiert das Model Context Protocol (MCP), um
KI-Agenten (wie Claude Desktop oder Kiro) direkten, sicheren und
dokumentationsgestützten Zugriff auf AWS-Ressourcen zu ermöglichen. Im
Gegensatz zur reinen CLI bietet der MCP Server dem Agenten Werkzeuge (Tools)
mit Metadaten an, die es dem Modell erleichtern, die richtigen Parameter zu
wählen und Best Practices einzuhalten.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [github.com/awslabs/mcp](https://github.com/awslabs/mcp) |

## Installation (Ubuntu 24.04)

Voraussetzung: [github.com/astral-sh/uv](https://github.com/astral-sh/uv) muss installiert sein.

```bash
uvx awslabs.aws-api-mcp-server@latest
```

## Hello World

```bash
npx @awslabs/aws-api-mcp-server
```

## Validierung

Der Server wird normalerweise über einen MCP-Client konfiguriert. Manuell kann
die Funktionsfähigkeit geprüft werden durch:

```bash
uvx awslabs.aws-api-mcp-server@latest --help
```

## Beispiele

Im Ordner `examples/` befinden sich verschiedene Beispiele für den AWS MCP Server:

1.  `config.json`: Allgemeine Konfigurationsdatei.
2.  `config_claude_desktop.json`: Konfiguration für Claude Desktop.
3.  `prompt_lambda.txt`: Beispiel-Prompt zur Interaktion mit Lambda.
4.  `prompt_logs.txt`: Beispiel-Prompt zur Abfrage von CloudWatch-Logs.
5.  `prompt_s3.txt`: Beispiel-Prompt zur Verwaltung von S3-Buckets.

## Nutzung für KI-Agenten

- **Tools**: Der Server registriert Funktionen für S3, EC2, Lambda etc. direkt
  beim Agenten.
- **Kontext**: Der Agent erhält Zugriff auf aktuelle AWS-Dokumentationen und
  "What's New"-Posts.
- **Sicherheit**: Nutzt IAM-Rollen des Systems, ohne dass der Agent Zugriff auf
  die Secret Keys selbst benötigt.
