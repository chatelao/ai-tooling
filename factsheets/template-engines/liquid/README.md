# Factsheet: Liquid

## Gruppe: Template-Engines

## Zweck

Ursprünglich von Shopify für E-Commerce-Templates entwickelt. Heute ist es der Standard für Shopify-Themes und den weit verbreiteten Static Site Generator Jekyll.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [shopify.github.io/liquid](https://shopify.github.io/liquid/) |

## Installation (Ubuntu 24.04)

```bash
sudo apt install -y ruby-liquid
```

## Hello World

```liquid
{{ "Hello World" | upcase }}
```

## Validierung

```bash
/usr/bin/ruby -e 'require "liquid"; puts Liquid::VERSION'
```

## Beispiele

Im Ordner `examples/` befinden sich verschiedene Liquid-Templates:

1.  `basic.liquid`: Grundlegende Variablenersetzung und Filter.
2.  `loop.liquid`: Iteration über Kollektionen mit `for`.
3.  `conditional.liquid`: Bedingte Logik mit `if`, `elsif` und `unless`.
4.  `filters.liquid`: Anwendung verschiedener eingebauter Filter (Datum, String-Manipulation, Mathe).
5.  `assign_capture.liquid`: Variablenzuweisung, Text-Capturing und Einbinden von Partials.
