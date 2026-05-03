#!/bin/bash
# List and create compute instances
gcloud compute instances list
gcloud compute instances create my-instance --machine-type=e2-medium --zone=europe-west3-a
