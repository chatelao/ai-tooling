# Google Cloud SDK (gcloud)

## Zweck

Das Google Cloud SDK enthält das `gcloud` Kommandozeilenwerkzeug, mit dem Sie
Google Cloud-Ressourcen verwalten können. Es ist das primäre Werkzeug für
KI-Agenten, um Compute Engine Instanzen zu steuern, Cloud Run Services zu
verwalten oder BigQuery-Daten abzufragen.

## Reifegrad

Stabil (Aktiv gewartet, Stand April 2026)

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Referenzhandbuch

[Link](https://cloud.google.com/sdk)

## Wikipedia

[Link](https://de.wikipedia.org/wiki/Google_Cloud_Platform)

## Installation (Ubuntu 24.04)

```bash
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
gcloud init
```

## Validierung

```bash
gcloud version
```

## Nutzung für KI-Agenten

- **Cloud Run**: Deployment und Management von serverlosen Anwendungen.
- **Daten**: Interaktion mit Cloud Storage und BigQuery.
- **KI**: Steuerung von Vertex AI Ressourcen.
- **Status**: Überprüfung von Projektquoten und Abrechnungsinformationen.
