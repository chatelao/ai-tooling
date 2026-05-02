# Factsheet: EJS (Embedded JS)

## Gruppe: Template-Engines

## Zweck

Sehr populär im Express.js-Umfeld. Verwendet eine einfache <% %> Syntax, bei der man nahezu normales JavaScript in HTML einbetten kann.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [Link](https://ejs.co/) |

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
