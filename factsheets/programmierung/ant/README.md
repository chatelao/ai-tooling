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

## Beispiele

Im Ordner `examples/` befinden sich verschiedene Ant-Build-Dateien (`.xml`):

1.  `build-minimal.xml`: Ein minimales Ant-Projekt mit einem "Hello World" Target.
2.  `build-java.xml`: Ein strukturierter Build-Prozess für Java (Clean, Compile, Jar).
3.  `build-properties.xml`: Verwendung von Properties und Laden von Property-Dateien.
4.  `build-conditions.xml`: Einsatz von Bedingungen zur Steuerung des Build-Flusses.
5.  `build-files.xml`: Dateioperationen wie Kopieren, Filtern und Archivieren.
