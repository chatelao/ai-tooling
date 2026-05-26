# Factsheet: Spring Boot

## Gruppe: App-Entwicklung

## Zweck

Spring Boot ist ein Java-basiertes Framework zur Erstellung von produktionsreifen, eigenständigen Anwendungen, die direkt gestartet werden können. Es vereinfacht die Entwicklung von Spring-Anwendungen durch "Opinionated Configuration".

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 3.4.0 |
| LTS | 3.3.x |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [spring.io/projects/spring-boot](https://spring.io/projects/spring-boot) |
| Wikipedia | [de.wikipedia.org/wiki/Spring_Boot](https://de.wikipedia.org/wiki/Spring_Boot) |

## Installation (Ubuntu 24.04)

Die Spring Boot CLI kann manuell installiert werden:

```bash
curl -L https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-cli/3.4.2/spring-boot-cli-3.4.2-bin.tar.gz -o spring-boot-cli.tar.gz
tar -xzf spring-boot-cli.tar.gz
sudo mv spring-3.4.2 /opt/spring-boot-cli
sudo ln -sf /opt/spring-boot-cli/bin/spring /usr/local/bin/spring
rm spring-boot-cli.tar.gz
```

## Hello World

```java
@RestController
class Hello {
    @GetMapping("/")
    String hi() { return "Hello World"; }
}
```

## Validierung

```bash
spring --version
```

## Beispiele

Im Ordner `examples/` befinden sich verschiedene Spring Boot Konfigurations- und Codebeispiele:

1.  `HelloController.java`: Ein einfacher REST-Controller.
2.  `application.properties`: Standard-Konfigurationsdatei.
3.  `pom.xml`: Maven-Projektkonfiguration mit Spring Boot Parent.
4.  `User.java`: Eine mit JPA-Annotationen versehene Entity-Klasse (Hibernate).
5.  `UserRepository.java`: Ein Spring Data JPA Repository Interface.
6.  `SecurityConfig.java`: Beispiel für eine Sicherheitskonfiguration mit Spring Security.
