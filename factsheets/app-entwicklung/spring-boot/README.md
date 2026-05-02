# Factsheet: Spring Boot

## Gruppe: App-Entwicklung

## Zweck

Spring Boot ist ein Java-basiertes Framework zur Erstellung von produktionsreifen, eigenständigen Anwendungen, die direkt gestartet werden können. Es vereinfacht die Entwicklung von Spring-Anwendungen durch "Opinionated Configuration".

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [Link](https://spring.io/projects/spring-boot) |
| Wikipedia | [Link](https://de.wikipedia.org/wiki/Spring_Boot) |

## Installation (Ubuntu 24.04)

Die Spring Boot CLI kann manuell installiert werden:

```bash
curl -L https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-cli/3.4.2/spring-boot-cli-3.4.2-bin.tar.gz -o spring-boot-cli.tar.gz
tar -xzf spring-boot-cli.tar.gz
sudo mv spring-3.4.2 /opt/spring-boot-cli
sudo ln -sf /opt/spring-boot-cli/bin/spring /usr/local/bin/spring
rm spring-boot-cli.tar.gz
```

## Validierung

```bash
spring --version
```
