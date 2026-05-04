# Factsheet: React Native

## Gruppe: App-Entwicklung

## Zweck

React Native ist ein Framework zum Erstellen nativer Apps für Android und iOS unter Verwendung von React.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [reactnative.dev](https://reactnative.dev/) |
| Wikipedia | [de.wikipedia.org/wiki/React_Native](https://de.wikipedia.org/wiki/React_Native) |

## Installation (Ubuntu 24.04)

React Native erfordert Node.js und JDK. Die CLI kann über npm ausgeführt werden.

```bash
npx react-native init MyProject
```

## Hello World

```jsx
import React from 'react';
import { Text } from 'react-native';

export default () => <Text>Hello World</Text>;
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `App.tsx` (Hauptkomponente in TypeScript)
- `package.json` (Projektkonfiguration)
- `app.json` (Expo/Native Konfiguration)
- `metro.config.js` (Bundler-Konfiguration)
- `tsconfig.json` (TypeScript-Konfiguration)

## Validierung

Version prüfen:

```bash
npx react-native --version
```
