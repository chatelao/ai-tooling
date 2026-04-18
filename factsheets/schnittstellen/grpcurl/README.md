# Factsheet: grpcurl

## Gruppe: Schnittstellen

## Zweck

grpcurl ist ein Kommandozeilenwerkzeug, das die Interaktion mit gRPC-Servern ermöglicht, ähnlich wie curl für HTTP.

## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Referenzhandbuch

[Link](https://github.com/fullstorydev/grpcurl)

## Wikipedia

[Link](https://en.wikipedia.org/wiki/GRPC)

## Installation (Ubuntu 24.04)

```bash
curl -L https://github.com/fullstorydev/grpcurl/releases/download/v1.9.3/grpcurl_1.9.3_linux_x86_64.tar.gz -o grpcurl.tar.gz
tar -xvf grpcurl.tar.gz
sudo mv grpcurl /usr/local/bin/
rm grpcurl.tar.gz
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `helloworld.proto`: Definition eines einfachen gRPC-Dienstes.
- `request.json`: Eine Beispielanfrage im JSON-Format.

## Validierung

Version prüfen:

```bash
grpcurl --version
```

Hilfe anzeigen:

```bash
grpcurl --help
```
