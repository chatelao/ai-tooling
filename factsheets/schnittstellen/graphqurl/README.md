# Factsheet: graphqurl

## Gruppe: Schnittstellen

## Zweck

graphqurl (gq) ist ein Kommandozeilenwerkzeug und eine JavaScript-Bibliothek für die Interaktion mit GraphQL-Endpunkten, ähnlich wie curl für HTTP.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 1.0.3 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [github.com/hasura/graphqurl](https://github.com/hasura/graphqurl) |
| Wikipedia | [en.wikipedia.org/wiki/GraphQL](https://en.wikipedia.org/wiki/GraphQL) |

## Installation (Ubuntu 24.04)

```bash
sudo npm install -g graphqurl
```

## Hello World

```bash
gq https://countries.trevorblades.com/ --query "{ countries { name } }"
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `query.graphql`: Eine Beispiel-GraphQL-Abfrage.
- `variables.json`: Variablen für die GraphQL-Abfrage.
- `introspection_query.graphql`: Eine Abfrage zur Schemadurchsuchung.
- `mutation_example.graphql`: Beispiel für eine GraphQL-Mutation.
- `subscription_example.graphql`: Beispiel für eine GraphQL-Subscription.

## Validierung

Version prüfen:

```bash
gq --version
```

Hilfe anzeigen:

```bash
gq --help
```
