# Google Cloud Run MCP

## Zweck

Der Google Cloud Run MCP Server ermöglicht es KI-Agenten, Anwendungen direkt aus
ihrer Umgebung auf Google Cloud Run zu deployen. Er bietet Tools zum Listen von
Services, Abrufen von Logs und zum Deployment von Code, was ihn zu einem
idealen Werkzeug für Agenten macht, die Web-Apps oder Microservices entwickeln.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [github.com/GoogleCloudPlatform/cloud-run-mcp](https://github.com/GoogleCloudPlatform/cloud-run-mcp) |

## Installation (Ubuntu 24.04)

Voraussetzung: [nodejs.org](https://nodejs.org/) und `gcloud` müssen installiert
sein.

```bash
npx -y @google-cloud/cloud-run-mcp
```

## Hello World

```bash
npx @google-cloud/cloud-run-mcp
```

## Validierung

Der Server wird normalerweise über einen MCP-Client konfiguriert. Manuell kann
die Funktionsfähigkeit (Hilfe) geprüft werden durch:

```bash
npx -y @google-cloud/cloud-run-mcp --help
```

## Beispiele

Im Ordner `examples/` befinden sich verschiedene Beispiele für Google Cloud Run MCP:

1.  `config_claude_desktop.json`: Konfiguration für Claude Desktop.
2.  `deploy.sh`: Beispielskript für ein manuelles Deployment.
3.  `prompt_deploy.txt`: Beispiel-Prompt für ein Deployment über den Agenten.
4.  `prompt_list.txt`: Beispiel-Prompt zum Auflisten der Services.
5.  `prompt_logs.txt`: Beispiel-Prompt zur Abfrage von Service-Logs.

## Nutzung für KI-Agenten

- **Deployment**: `deploy-file-contents` ermöglicht es dem Agenten, den
  generierten Code sofort in eine laufende Cloud-Umgebung zu bringen.
- **Debugging**: `get-service-log` erlaubt es dem Agenten, Fehler in deployten
  Anwendungen selbstständig zu finden.
- **Automatisierung**: Agenten können neue Projekte erstellen und diese direkt
  für das Deployment vorbereiten.
