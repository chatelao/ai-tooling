# Kubernetes (kubectl)

## Zweck

Kubernetes ist ein Open-Source-System zur Automatisierung der Bereitstellung, Skalierung und Verwaltung von containerisierten Anwendungen. `kubectl` ist das primäre Befehlszeilenwerkzeug zur Interaktion mit Kubernetes-Clustern. Für KI-Agenten ist es unverzichtbar, um GPU-Cluster zu steuern, Inferenz-Endpunkte zu skalieren und den Status von großflächigen Bereitstellungen zu überwachen.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Wikipedia | [de.wikipedia.org/wiki/Kubernetes](https://de.wikipedia.org/wiki/Kubernetes) |

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl gnupg
sudo mkdir -p -m 755 /etc/apt/keyrings
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.30/deb/Release.key | sudo gpg --dearmor --yes -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.30/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt update
sudo apt install -y kubectl
```

## Hello World

```bash
kubectl version
```

## Beispiele

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `deployment.yaml`: Definition eines Workloads.
- `service.yaml`: Netzwerk-Zugriff auf den Workload.
- `ingress.yaml`: Externer Zugriff über einen Ingress-Controller.
- `configmap.yaml`: Verwaltung von Konfigurationsdaten.
- `gpu-pod.yaml`: Beispiel für die Anforderung von GPU-Ressourcen.
- `secret.yaml`: Verwaltung von sensiblen Daten.

## Validierung

```bash
kubectl version --client
```

## Nutzung für KI-Agenten

KI-Agenten können Kubernetes/kubectl nutzen, um:

- Deployment-YAMLs für neue Modellversionen zu erstellen und anzuwenden.
- GPU-Ressourcen in Cloud-Umgebungen (GKE, EKS, AKS) zu verwalten.
- Logs von verteilten Trainings-Jobs zu sammeln und zu analysieren.
- Auto-Scaling-Parameter basierend auf dem aktuellen Inferenz-Verkehr anzupassen.
