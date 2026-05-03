#!/bin/bash
# Rufe eine gRPC-Methode mit Daten aus einer JSON-Datei auf
grpcurl -plaintext -d @request.json -proto helloworld.proto localhost:50051 helloworld.Greeter/SayHello
