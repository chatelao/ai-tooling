#!/bin/bash
# Configure project and region
PROJECT_ID="my-project-id"
REGION="europe-west3"

gcloud config set project ${PROJECT_ID}
gcloud config set compute/region ${REGION}
