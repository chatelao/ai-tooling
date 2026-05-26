# Factsheet: grpcurl

## Gruppe: Schnittstellen

## Zweck

grpcurl ist ein Kommandozeilenwerkzeug, das die Interaktion mit gRPC-Servern ermöglicht, ähnlich wie curl für HTTP.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 1.9.1 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [github.com/fullstorydev/grpcurl](https://github.com/fullstorydev/grpcurl) |
| Wikipedia | [en.wikipedia.org/wiki/GRPC](https://en.wikipedia.org/wiki/GRPC) |

## Installation (Ubuntu 24.04)

```bash
curl -L https://github.com/fullstorydev/grpcurl/releases/download/v1.9.3/grpcurl_1.9.3_linux_x86_64.tar.gz -o grpcurl.tar.gz
tar -xvf grpcurl.tar.gz
sudo mv grpcurl /usr/local/bin/
rm grpcurl.tar.gz
```

## Hello World

```bash
grpcurl -plaintext localhost:50051 list
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `helloworld.proto`: Definition eines einfachen gRPC-Dienstes.
- `request.json`: Eine Beispielanfrage im JSON-Format.
- `list_services.sh`: Skript zum Auflisten von gRPC-Diensten.
- `describe_service.sh`: Skript zum Beschreiben eines Dienstes.
- `say_hello.sh`: Skript zum Aufrufen einer gRPC-Methode.
- `metadata.json`: Beispiel für gRPC-Metadaten (Header).
- `complex.proto`: Eine komplexere Proto-Definition für einen Inventardienst.

## Validierung

Version prüfen:

```bash
grpcurl --version
```

Hilfe anzeigen:

```bash
grpcurl --help
```
