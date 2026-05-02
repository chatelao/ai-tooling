# Factsheet: ERB (Embedded Ruby)

## Gruppe: Template-Engines

## Zweck

Die Standard-Engine in Ruby on Rails. Erlaubt das direkte Einbetten von Ruby-Code in Textdokumente.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [Link](https://github.com/ruby/erb) |

## Installation (Ubuntu 24.04)

```bash
sudo apt install -y ruby
```

## Hello World

```erb
<%= "Hello World" %>
```

## Validierung

```bash
erb -v
```
