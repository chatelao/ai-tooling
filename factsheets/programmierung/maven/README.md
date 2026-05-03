# Factsheet: Apache Maven

## Gruppe: Programmierung

## Zweck

Apache Maven ist ein Build-Management-Tool für Java-Projekte, das auf dem Project Object Model (POM) basiert. Es automatisiert den Build-Prozess, das Abhängigkeitsmanagement und die Dokumentation.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [maven.apache.org](https://maven.apache.org/) |

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install maven
# Fix für ClassNotFoundException: org.codehaus.plexus.classworlds.launcher.Launcher
sudo rm -f /usr/share/maven/boot/plexus-classworlds-2.x.jar
```

## Hello World

```bash
mvn -version
```

## Beispiele

Im Ordner `examples/` befinden sich verschiedene Maven-Konfigurationsbeispiele:

1.  `minimal-pom.xml`: Eine grundlegende `pom.xml` für ein Java-Projekt.
2.  `compiler-config.xml`: Konfiguration der Java-Version für den Compiler.
3.  `shade-plugin-config.xml`: Beispiel für die Konfiguration des Maven Shade Plugins zur Erstellung eines "Fat JARs".
4.  `dependencies-example.xml`: Beispiel für das Hinzufügen von Abhängigkeiten (z.B. Spring Boot).
5.  `settings-example.xml`: Beispiel für eine `settings.xml` zur Konfiguration von Repositories und lokalen Pfaden.

## Validierung

```bash
mvn -version
```
