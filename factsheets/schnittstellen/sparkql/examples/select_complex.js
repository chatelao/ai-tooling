const { select } = require('sparkql');

const query = select('?person', '?name')
  .where('?person', 'a', 'dbo:Person')
  .where('?person', 'foaf:name', '?name')
  .filter('LANG(?name) = "en"')
  .orderBy('?name')
  .limit(10)
  .build();

console.log(query);
