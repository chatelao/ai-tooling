#!/bin/bash
# Filtere alle 'amenity' tags aus einer OSM-Datei
osmium tags-filter input.osm.pbf n/amenity -o amenities.osm.pbf
