# Factsheet: React

## Gruppe: App-Entwicklung

## Zweck

React ist eine JavaScript-Bibliothek zum Erstellen von Benutzeroberflächen, die auf Komponenten basiert und von Meta entwickelt wurde.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [react.dev](https://react.dev/) |
| Wikipedia | [de.wikipedia.org/wiki/React](https://de.wikipedia.org/wiki/React) |

## Installation (Ubuntu 24.04)

React wird üblicherweise über `npm` oder `yarn` in ein Projekt eingebunden.

```bash
npm install react react-dom
```

Oder ein neues Projekt erstellen:

```bash
npx create-react-app my-app
```

## Hello World

```jsx
import React from 'react';
import ReactDOM from 'react-dom';

ReactDOM.render(<h1>Hello, world!</h1>, document.getElementById('root'));
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `App.js` (Hauptkomponente)
- `index.js` (Einstiegspunkt)
- `package.json` (Abhängigkeiten)
- `App.css` (Styles)

## Validierung

In einem React-Projekt die Version in `package.json` prüfen oder:

```bash
npm list react
```
