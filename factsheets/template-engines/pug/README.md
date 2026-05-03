# Factsheet: Pug

## Gruppe: Template-Engines

## Zweck

Setzt auf eine stark abstrahierte, einrückungsbasierte Syntax komplett ohne schließende HTML-Tags. Der Code wird dadurch sehr kompakt. Ehemals bekannt als Jade.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [pugjs.org](https://pugjs.org/) |

## Installation (Ubuntu 24.04)

```bash
npm install -g pug-cli
```

## Hello World

```pug
p Hello World
```

## Validierung

```bash
pug --version
```

## Beispiele

Im Ordner `examples/` befinden sich verschiedene Pug-Templates:

1.  `basic.pug`: Grundlegende Syntax mit Einrückung, Attributen und Variablen.
2.  `loop.pug`: Iteration über Arrays mit `each`.
3.  `conditional.pug`: Bedingte Logik mit `if` und `else`.
4.  `mixin.pug`: Wiederverwendbare Code-Blöcke (Mixins) mit Parametern.
5.  `inheritance.pug`: Layout-Konzept mit `extends`, `block` und `include`.
