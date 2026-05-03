# Factsheet: Node-RED

## Gruppe: Funktechnik

## Zweck: Node-RED ist ein flussbasiertes Programmierwerkzeug für die Ereignissteuerung und IoT

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [nodered.org/docs](https://nodered.org/docs/) |
| Wikipedia | [de.wikipedia.org/wiki/Node-RED](https://de.wikipedia.org/wiki/Node-RED) |

## Installation (Ubuntu 24.04)

```bash
sudo npm install -g --unsafe-perm node-red
```

## Hello World

```bash
node-red --version
```

## Beispieldaten

Die folgenden Beispiel-Flows befinden sich im Ordner `examples/`:

- `hello_world.json`: Ein einfacher Inject- und Debug-Flow.
- `http_endpoint.json`: Erzeugt einen HTTP-Endpunkt unter `/hello`.
- `mqtt_bridge.json`: Beispiel für die Verarbeitung von MQTT-Nachrichten.
- `dashboard_minimal.json`: Ein einfaches Dashboard mit Slider und Gauge.
- `function_node.json`: Verwendung von JavaScript in einer Function-Node.

## Validierung

```bash
node-red --help
```
