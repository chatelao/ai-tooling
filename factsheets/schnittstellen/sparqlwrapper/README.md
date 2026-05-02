# Factsheet: SPARQLWrapper

## Gruppe: Schnittstellen

## Zweck

SPARQLWrapper ist eine Python-Bibliothek, die als Wrapper um einen SPARQL-Endpunkt dient. Sie vereinfacht die Erstellung von Abfragen und das Parsen der Ergebnisse.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [Link](https://sparqlwrapper.readthedocs.io/) |
| Wikipedia | [Link](https://en.wikipedia.org/wiki/SPARQL) |

## Installation (Ubuntu 24.04)

```bash
sudo apt install python3-sparqlwrapper
```

## Hello World

```python
from SPARQLWrapper import SPARQLWrapper

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("SELECT * WHERE { ?s ?p ?o } LIMIT 1")
results = sparql.query().convert()
print(results)
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `query_wikidata.py`: Ein Python-Skript, das eine Abfrage an Wikidata sendet.

## Validierung

Skript ausführen:

```bash
/usr/bin/python3 factsheets/schnittstellen/sparqlwrapper/examples/query_wikidata.py
```
