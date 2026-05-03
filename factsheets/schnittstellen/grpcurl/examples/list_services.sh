#!/bin/bash
# Liste alle verfügbaren gRPC-Dienste auf einem Server auf
grpcurl -plaintext localhost:50051 list
