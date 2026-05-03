from SPARQLWrapper import SPARQLWrapper, XML

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
    SELECT ?s ?p ?o
    WHERE { ?s ?p ?o }
    LIMIT 5
""")
sparql.setReturnFormat(XML)
results = sparql.query().convert()
print(results.toxml())
