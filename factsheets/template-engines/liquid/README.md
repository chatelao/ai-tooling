# Factsheet: Liquid

## Gruppe: Template-Engines

## Zweck

Ursprünglich von Shopify für E-Commerce-Templates entwickelt. Heute ist es der Standard für Shopify-Themes und den weit verbreiteten Static Site Generator Jekyll.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [Link](https://shopify.github.io/liquid/) |

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
