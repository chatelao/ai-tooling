# Factsheet: EJS (Embedded JS)

## Gruppe: Template-Engines

## Zweck

Sehr populär im Express.js-Umfeld. Verwendet eine einfache <% %> Syntax, bei der man nahezu normales JavaScript in HTML einbetten kann.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 3.1.10 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [ejs.co](https://ejs.co/) |

## Installation (Ubuntu 24.04)

```bash
sudo apt install -y node-ejs
```

## Hello World

```ejs
<%= 'Hello World' %>
```

## Validierung

```bash
npm list ejs
```

## Beispiele

Im Ordner `examples/` befinden sich verschiedene EJS-Templates:

1.  `basic_variable.ejs`: Einfache Variablen-Interpolation.
2.  `list_iteration.ejs`: Iteration über eine Liste von Objekten.
3.  `conditional_rendering.ejs`: Bedingte Anzeige von Inhalten.
4.  `escaping.ejs`: Unterschied zwischen escapter und unescapter Ausgabe.
5.  `comments.ejs`: Verwendung von Kommentaren in EJS.
