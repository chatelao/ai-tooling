#!/bin/bash
# Beschreibe einen bestimmten gRPC-Dienst (erfordert Reflection oder Proto-Dateien)
grpcurl -plaintext localhost:50051 describe helloworld.Greeter
