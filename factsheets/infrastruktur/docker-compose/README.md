# Docker Compose

## Zweck

Docker Compose ist ein Werkzeug zur Definition und zum Betrieb von Multi-Container-Anwendungen. Mit einer YAML-Datei werden die Dienste, Netzwerke und Volumes der Anwendung konfiguriert. Für KI-Agenten ist es ideal, um komplexe Stacks (z.B. Datenbank + API + Frontend) mit einem einzigen Befehl lokal oder in Testumgebungen zu starten.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 2.29.7 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Wikipedia | [de.wikipedia.org/wiki/Docker_(Software](https://de.wikipedia.org/wiki/Docker_(Software)#Docker_Compose) |

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install docker-compose-plugin
```

## Hello World

```bash
docker-compose --version
```

## Validierung

```bash
docker compose version
```

## Nutzung für KI-Agenten

KI-Agenten können Docker Compose nutzen, um:

- Multi-Service-Umgebungen für Integrationstests zu provisionieren.
- Abhängigkeiten wie Vektordatenbanken (Pinecone, Milvus) oder Caches (Redis) lokal zu starten.
- Microservice-Architekturen lokal zu simulieren.
- Standardisierte Entwicklungsumgebungen für Teams bereitzustellen.

## Beispieldaten

Im Ordner `examples/` befinden sich Konfigurationsbeispiele für Docker Compose:

- `docker-compose.yml`: Basis-Konfiguration für eine Multi-Container-Anwendung.
- `docker-compose.gpu.yml`: Beispiel für die Einbindung von NVIDIA-GPUs.
- `docker-compose.test.yml`: Konfiguration für Testumgebungen.
- `monitoring.yml`: Stack für Monitoring (z.B. Prometheus/Grafana).
- `networks.yml`: Fortgeschrittene Netzwerk-Konfigurationen.
- `.env.example`: Vorlage für Umgebungsvariablen.
