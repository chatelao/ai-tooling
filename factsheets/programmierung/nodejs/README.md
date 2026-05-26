# Factsheet: Node.js und npm

## Gruppe: Programmierung

## Zweck

Node.js ist eine JavaScript-Laufzeitumgebung, die auf der Chrome V8 JavaScript-Engine basiert. npm ist der Standard-Paketmanager für Node.js.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 23.2.0 |
| LTS | 22.11.0 (LTS) |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [nodejs.org](https://nodejs.org/) |

## Installation (Ubuntu 24.04)

```bash
sudo apt install nodejs npm
```

## Hello World

```javascript
console.log("Hello World");
```

## Validierung

```bash
node --version
npm --version
```

## Beispiele

Im Ordner `examples/` befinden sich verschiedene Node.js-Beispiele:

1.  `hello.js`: Grundlegende Konsolenausgabe und Prozessinformationen.
2.  `filesystem.js`: Lesen und Schreiben von Dateien mit dem `fs` Modul.
3.  `server.js`: Erstellung eines einfachen HTTP-Servers.
4.  `async_await.js`: Demonstration von asynchroner Programmierung mit Promises und async/await.
5.  `os_path.js`: Verwendung der eingebauten `os` und `path` Module für Systeminformationen und Pfadmanipulation.
