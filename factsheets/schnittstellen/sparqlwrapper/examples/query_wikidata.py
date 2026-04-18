from SPARQLWrapper import SPARQLWrapper, JSON

def main():
    sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
    sparql.setQuery("""
        SELECT ?label WHERE {
          wd:Q42 rdfs:label ?label .
          FILTER (lang(?label) = "en")
        }
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        print(result["label"]["value"])

if __name__ == "__main__":
    main()
