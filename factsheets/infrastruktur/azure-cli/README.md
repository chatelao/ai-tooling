# Azure CLI

## Zweck

Die Azure CLI ist ein plattformübergreifendes Befehlszeilenprogramm zur
Verbindung mit Azure und zur Ausführung von Verwaltungsbefehlen für
Azure-Ressourcen. KI-Agenten nutzen die Azure CLI, um Abfragen über die
Infrastruktur zu tätigen, Ressourcen zu skalieren oder DevOps-Pipelines zu
steuern.


## Reifegrad

Stabil (Aktiv gewartet, v2.85.0 Stand April 2026)




## Technische Schulden

Gering




## Erwartetes Lebensende

Kein EOL bekannt




## Installation (Ubuntu 24.04)

```bash
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

## Validierung

```bash
az --version
```

## Nutzung für KI-Agenten

- **Ressourcen-Management**: Erstellen und Verwalten von Resource Groups, VMs
  und Web-Apps.
- **Automatisierung**: Skripting von komplexen Cloud-Infrastrukturen (IaC).
- **Abfrage**: Filtern von Azure-Ressourcen mittels JMESPath-Abfragen, was
  ideal für die Datenextraktion durch LLMs ist.
