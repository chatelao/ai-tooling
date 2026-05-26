# AWS CLI

## Zweck

Das AWS Command Line Interface (AWS CLI) ist ein Open-Source-Werkzeug, mit dem
Sie über Befehle in Ihrer Befehlszeile mit AWS-Services interagieren können.
Für KI-Agenten ist es besonders wertvoll, da es eine skriptfähige Schnittstelle
bietet, um Cloud-Ressourcen zu provisionieren, Daten in S3 zu verwalten oder
Lambda-Funktionen aufzurufen.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 2.21.0 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [aws.amazon.com/cli](https://aws.amazon.com/cli/) |
| Wikipedia | [de.wikipedia.org/wiki/Amazon_Web_Services](https://de.wikipedia.org/wiki/Amazon_Web_Services) |

## Installation (Ubuntu 24.04)

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo apt install unzip
unzip awscliv2.zip
sudo ./aws/install
```

## Hello World

```bash
aws --version
```

## Validierung

```bash
aws --version
```

## Beispiele

Im Ordner `examples/` befinden sich verschiedene AWS CLI Befehlsbeispiele:

1.  `s3_ls.sh`: Auflisten von S3-Buckets.
2.  `ec2_describe.sh`: Abfragen von EC2-Instanzen mit Filterung.
3.  `iam_list_users.sh`: Auflisten von IAM-Benutzern.
4.  `lambda_list_functions.sh`: Abfragen von Lambda-Funktionen.
5.  `configure_profile.sh`: Konfiguration eines AWS-Profils.

## Nutzung für KI-Agenten

KI-Agenten können die AWS CLI nutzen, um:

- Infrastruktur-Status abzufragen (JSON-Output ist ideal für LLMs).
- Dateien für RAG-Systeme in S3-Buckets hoch- oder herunterzuladen.
- Berechtigungen über IAM-Policies zu prüfen.
- CloudWatch-Logs zur Fehleranalyse auszulesen.
