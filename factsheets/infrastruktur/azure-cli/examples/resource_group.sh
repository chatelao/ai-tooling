#!/bin/bash
# Create a resource group
RG_NAME="myResourceGroup"
LOCATION="westeurope"

az group create --name ${RG_NAME} --location ${LOCATION}
