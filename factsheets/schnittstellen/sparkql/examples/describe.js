const { describe } = require('sparkql');

const query = describe('?s')
  .where('?s', 'a', 'dbo:MusicalArtist')
  .limit(5)
  .build();

console.log(query);
