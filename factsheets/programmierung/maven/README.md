# Factsheet: Maven

## Gruppe: Programmierung

## Zweck

Apache Maven ist ein Werkzeug für das Build-Management und die Automatisierung von Java-Projekten, basierend auf dem Konzept eines Project Object Models (POM).

## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Referenzhandbuch

[Link](https://maven.apache.org/)

## Installation (Ubuntu 24.04)

```bash
sudo apt install -y maven
# Fix for duplicate plexus-classworlds jar in Ubuntu 24.04
sudo rm -f /usr/share/maven/boot/plexus-classworlds-2.x.jar
```

## Validierung

```bash
mvn -version
```
