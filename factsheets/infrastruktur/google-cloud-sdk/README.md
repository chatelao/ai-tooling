# Google Cloud SDK (gcloud)

## Zweck

Das Google Cloud SDK enthält das `gcloud` Kommandozeilenwerkzeug, mit dem Sie
Google Cloud-Ressourcen verwalten können. Es ist das primäre Werkzeug für
KI-Agenten, um Compute Engine Instanzen zu steuern, Cloud Run Services zu
verwalten oder BigQuery-Daten abzufragen.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 499.0.0 |
| LTS | N/A |
| Reifegrad | Stabil (Aktiv gewartet, Stand April 2026) |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [cloud.google.com/sdk](https://cloud.google.com/sdk) |
| Wikipedia | [de.wikipedia.org/wiki/Google_Cloud_Platform](https://de.wikipedia.org/wiki/Google_Cloud_Platform) |

## Installation (Ubuntu 24.04)

```bash
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
gcloud init
```

## Hello World

```bash
gcloud --version
```

## Validierung

```bash
gcloud version
```

## Beispiele

Im Ordner `examples/` befinden sich verschiedene Google Cloud SDK (gcloud) Beispiele:

1.  `auth.sh`: Authentifizierung am Google Cloud Account.
2.  `project_config.sh`: Konfiguration von Projekt-ID und Region.
3.  `compute_instances.sh`: Auflisten und Erstellen von Compute Engine Instanzen.
4.  `storage_buckets.sh`: Verwaltung von Cloud Storage Buckets und Dateien.
5.  `cloud_run_deploy.sh`: Deployment eines Containers auf Cloud Run.

## Nutzung für KI-Agenten

- **Cloud Run**: Deployment und Management von serverlosen Anwendungen.
- **Daten**: Interaktion mit Cloud Storage und BigQuery.
- **KI**: Steuerung von Vertex AI Ressourcen.
- **Status**: Überprüfung von Projektquoten und Abrechnungsinformationen.
