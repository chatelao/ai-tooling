# Azure CLI

## Zweck

Die Azure CLI ist ein plattformübergreifendes Befehlszeilenprogramm zur
Verbindung mit Azure und zur Ausführung von Verwaltungsbefehlen für
Azure-Ressourcen. KI-Agenten nutzen die Azure CLI, um Abfragen über die
Infrastruktur zu tätigen, Ressourcen zu skalieren oder DevOps-Pipelines zu
steuern.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil (Aktiv gewartet, v2.85.0 Stand April 2026) |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [docs.microsoft.com/en-us/cli/azure](https://docs.microsoft.com/en-us/cli/azure/) |
| Wikipedia | [de.wikipedia.org/wiki/Microsoft_Azure](https://de.wikipedia.org/wiki/Microsoft_Azure) |

## Installation (Ubuntu 24.04)

```bash
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

## Hello World

```bash
az --version
```

## Validierung

```bash
az --version
```

## Beispiele

Im Ordner `examples/` befinden sich verschiedene Azure CLI Beispiele:

1.  `login.sh`: Anmeldung am Azure-Konto.
2.  `resource_group.sh`: Erstellen einer Ressourcengruppe.
3.  `vm_operations.sh`: Erstellen und Auflisten von virtuellen Maschinen.
4.  `storage_blob.sh`: Verwaltung von Storage Accounts und Blobs.
5.  `network_vnet.sh`: Erstellen eines virtuellen Netzwerks und Subnetzes.

## Nutzung für KI-Agenten

- **Ressourcen-Management**: Erstellen und Verwalten von Resource Groups, VMs
  und Web-Apps.
- **Automatisierung**: Skripting von komplexen Cloud-Infrastrukturen (IaC).
- **Abfrage**: Filtern von Azure-Ressourcen mittels JMESPath-Abfragen, was
  ideal für die Datenextraktion durch LLMs ist.
