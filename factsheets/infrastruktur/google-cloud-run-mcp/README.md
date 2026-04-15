# Google Cloud Run MCP

## Zweck

Der Google Cloud Run MCP Server ermöglicht es KI-Agenten, Anwendungen direkt aus
ihrer Umgebung auf Google Cloud Run zu deployen. Er bietet Tools zum Listen von
Services, Abrufen von Logs und zum Deployment von Code, was ihn zu einem
idealen Werkzeug für Agenten macht, die Web-Apps oder Microservices entwickeln.


## Reifegrad

Stabil




## Technische Schulden

Gering




## Erwartetes Lebensende

Kein EOL bekannt




## Installation (Ubuntu 24.04)

Voraussetzung: [Node.js](https://nodejs.org/) und `gcloud` müssen installiert
sein.

```bash
npx -y @google-cloud/cloud-run-mcp
```

## Validierung

Der Server wird normalerweise über einen MCP-Client konfiguriert. Manuell kann
die Funktionsfähigkeit (Hilfe) geprüft werden durch:

```bash
npx -y @google-cloud/cloud-run-mcp --help
```

## Nutzung für KI-Agenten

- **Deployment**: `deploy-file-contents` ermöglicht es dem Agenten, den
  generierten Code sofort in eine laufende Cloud-Umgebung zu bringen.
- **Debugging**: `get-service-log` erlaubt es dem Agenten, Fehler in deployten
  Anwendungen selbstständig zu finden.
- **Automatisierung**: Agenten können neue Projekte erstellen und diese direkt
  für das Deployment vorbereiten.
