#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

psql --version
# Starten des Services (falls erforderlich)
sudo service postgresql start || sudo /etc/init.d/postgresql start
# Test-Abfrage als postgres-Benutzer
sudo -u postgres psql -c "SELECT 1;"
