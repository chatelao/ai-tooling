#!/bin/bash
# Extrahiere einen Bereich basierend auf einer Bounding Box
osmium extract -b 13.0,52.0,14.0,53.0 input.osm.pbf -o output.osm.pbf
