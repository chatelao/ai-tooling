#!/bin/bash
# Deploy a container to Cloud Run
SERVICE_NAME="hello-world"
IMAGE="gcr.io/cloudrun/hello"

gcloud run deploy ${SERVICE_NAME} \
  --image ${IMAGE} \
  --platform managed \
  --region europe-west3 \
  --allow-unauthenticated
