const { ask } = require('sparkql');

const query = ask()
  .where('?s', 'a', 'dbo:Person')
  .where('?s', 'foaf:name', '"Albert Einstein"@en')
  .build();

console.log(query);
