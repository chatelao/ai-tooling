#!/bin/bash
# Manage Cloud Storage buckets
BUCKET_NAME="my-unique-bucket-name"
gsutil mb gs://${BUCKET_NAME}
gsutil cp test.txt gs://${BUCKET_NAME}/
gsutil ls gs://${BUCKET_NAME}
