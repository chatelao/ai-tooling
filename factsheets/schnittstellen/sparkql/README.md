# Factsheet: sparkql

## Gruppe: Schnittstellen

## Zweck

sparkql ist ein NPM-Paket zur Erstellung von SPARQL-Abfragen mit einer flüssigen API in JavaScript/TypeScript.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 2.4.0 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [npm.im/sparkql](https://npm.im/sparkql) |
| Wikipedia | [en.wikipedia.org/wiki/SPARQL](https://en.wikipedia.org/wiki/SPARQL) |

## Installation (Ubuntu 24.04)

```bash
npm install sparkql
```

## Hello World

```javascript
const { select } = require('sparkql');

const query = select('*')
  .from('<http://dbpedia.org>')
  .where('?s', '?p', '?o')
  .limit(1)
  .build();
console.log(query);
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `builder.js`: Ein JavaScript-Skript, das eine Abfrage erstellt.
- `select_complex.js`: Erstellung einer komplexeren SELECT-Abfrage mit Filtern und Sortierung.
- `construct.js`: Erstellung einer CONSTRUCT-Abfrage.
- `describe.js`: Erstellung einer DESCRIBE-Abfrage.
- `ask.js`: Erstellung einer ASK-Abfrage.

## Validierung

Skript ausführen:

```bash
node factsheets/schnittstellen/sparkql/examples/builder.js
```
