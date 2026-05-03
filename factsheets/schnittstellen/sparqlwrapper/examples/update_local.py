from SPARQLWrapper import SPARQLWrapper, POST

sparql = SPARQLWrapper("http://localhost:3030/ds/update")
sparql.setMethod(POST)
sparql.setQuery("""
    INSERT DATA {
      <http://example.org/subject> <http://example.org/predicate> "object" .
    }
""")
# results = sparql.query() # Requires a running Fuseki server
print("Update query prepared.")
