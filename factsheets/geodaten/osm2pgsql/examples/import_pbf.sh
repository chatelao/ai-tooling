#!/bin/bash
# Example script to import a PBF file
DB_NAME="osm"
PBF_FILE="data.osm.pbf"

osm2pgsql --create --database $DB_NAME --slim --cache 2000 $PBF_FILE
