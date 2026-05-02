# Factsheet: Handlebars

## Gruppe: Template-Engines

## Zweck

Handlebars ist eine leistungsstarke Template-Engine, die auf Mustache aufbaut und diese um zusätzliche Funktionen wie Helper und Block-Helper erweitert, während sie die "logic-less" Philosophie weitgehend beibehält. Sie ermöglicht die Erstellung semantischer Templates, die sowohl auf dem Server (Node.js) als auch im Browser verwendet werden können.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [Link](https://handlebarsjs.com/) |

## Installation (Ubuntu 24.04)

```bash
npm install -g handlebars
```

## Validierung

```bash
handlebars --version
```

## Beispiele

Im Ordner `examples/` befinden sich verschiedene Handlebars-Templates und zugehörige Datendateien:

1. `greeting.hbs`: Ein einfaches Template für eine Begrüßung mit Variablenersetzung.
2. `user_list.hbs`: Demonstration von Iteration über eine Liste mit dem `{{#each}}`-Helper.
3. `conditional.hbs`: Verwendung von `{{#if}}` und `{{#unless}}` für bedingte Logik.
4. `nested_context.hbs`: Zugriff auf verschachtelte Datenstrukturen mit dem `{{#with}}`-Helper.
5. `complex_object.hbs`: Ein komplexeres Beispiel mit verschachtelten Schleifen und Fallback für leere Listen.
