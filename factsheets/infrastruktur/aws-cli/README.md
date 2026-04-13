# AWS CLI

## Zweck

Das AWS Command Line Interface (AWS CLI) ist ein Open-Source-Werkzeug, mit dem
Sie über Befehle in Ihrer Befehlszeile mit AWS-Services interagieren können.
Für KI-Agenten ist es besonders wertvoll, da es eine skriptfähige Schnittstelle
bietet, um Cloud-Ressourcen zu provisionieren, Daten in S3 zu verwalten oder
Lambda-Funktionen aufzurufen.


## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Installation (Ubuntu 24.04)

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo apt install unzip
unzip awscliv2.zip
sudo ./aws/install
```

## Validierung

```bash
aws --version
```

## Nutzung für KI-Agenten

KI-Agenten können die AWS CLI nutzen, um:

- Infrastruktur-Status abzufragen (JSON-Output ist ideal für LLMs).
- Dateien für RAG-Systeme in S3-Buckets hoch- oder herunterzuladen.
- Berechtigungen über IAM-Policies zu prüfen.
- CloudWatch-Logs zur Fehleranalyse auszulesen.
