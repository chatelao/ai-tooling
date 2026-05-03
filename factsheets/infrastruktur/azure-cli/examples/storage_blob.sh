#!/bin/bash
# Manage storage accounts and blobs
STORAGE_ACCOUNT="mystorageaccount"
CONTAINER_NAME="mycontainer"

az storage account create --name ${STORAGE_ACCOUNT} --resource-group myResourceGroup --location westeurope --sku Standard_LRS
az storage container create --name ${CONTAINER_NAME} --account-name ${STORAGE_ACCOUNT}
az storage blob upload --account-name ${STORAGE_ACCOUNT} --container-name ${CONTAINER_NAME} --name myfile.txt --file test.txt
