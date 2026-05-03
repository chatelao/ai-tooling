#!/bin/bash
# Mergen von zwei OSM-Dateien
osmosis --read-pbf file="file1.osm.pbf" --read-pbf file="file2.osm.pbf" --merge --write-pbf file="merged.osm.pbf"
