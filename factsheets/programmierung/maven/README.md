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

## Validierung

```bash
mvn -version
```
