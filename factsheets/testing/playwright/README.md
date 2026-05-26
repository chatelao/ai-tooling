# Factsheet: Playwright

## Gruppe: Testing

## Zweck

Playwright ist ein Framework für Web-Testing und Automatisierung, das das
Testen in verschiedenen Browser-Engines (Chromium, Firefox, WebKit) ermöglicht.
KI-Agenten nutzen Playwright, um komplexe Interaktionen in Webanwendungen zu
simulieren, Screenshots zu erstellen und die korrekte Funktion von Frontends zu
verifizieren.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 1.49.0 |
| LTS | N/A |
| Reifegrad | Stabil (Aktiv gewartet, v1.59.1 Stand April 2026) |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [playwright.dev](https://playwright.dev/) |
| Wikipedia | [de.wikipedia.org/wiki/Playwright_(Software](https://de.wikipedia.org/wiki/Playwright_(Software)) |

## Installation (Ubuntu 24.04)

```bash
npm install playwright
```

## Hello World

```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('https://playwright.dev/');
  console.log(await page.title());
  await browser.close();
})();
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `test.spec.js`
- `config.js`
- `page.html`
- `script.js`
- `package.json`

## Validierung

Playwright-Test ausführen.
