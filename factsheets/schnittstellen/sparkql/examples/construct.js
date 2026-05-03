const { construct } = require('sparkql');

const query = construct('?s <http://example.org/alias> ?o')
  .where('?s', '<http://www.w3.org/2000/01/rdf-schema#label>', '?o')
  .build();

console.log(query);
