# Factsheet: ERB (Embedded Ruby)

## Gruppe: Template-Engines

## Zweck

Die Standard-Engine in Ruby on Rails. Erlaubt das direkte Einbetten von Ruby-Code in Textdokumente.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [github.com/ruby/erb](https://github.com/ruby/erb) |

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

## Beispiele

Im Ordner `examples/` befinden sich verschiedene ERB-Templates:

1.  `basic.erb`: Grundlegende Variablenersetzung und Ruby-Code-Ausführung.
2.  `loop.erb`: Iteration über eine Liste von Objekten.
3.  `conditional.erb`: Bedingte Logik mit `if` und `unless`.
4.  `newline_control.erb`: Steuerung von Zeilenumbrüchen mit der `-` Syntax.
5.  `partial.erb`: Konzept von Partials und sicherer HTML-Ausgabe.
