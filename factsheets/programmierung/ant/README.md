# Factsheet: Apache Ant

## Gruppe: Programmierung

## Zweck

Apache Ant ist ein Java-basiertes Build-Management-Tool, das vor allem für die Automatisierung von Kompiliervorgängen und anderen Aufgaben in der Softwareentwicklung verwendet wird.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [ant.apache.org](https://ant.apache.org/) |

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install ant
```

## Hello World

```xml
<project><target name="hello"><echo>Hello World</echo></target></project>
```

## Validierung

```bash
ant -version
```
