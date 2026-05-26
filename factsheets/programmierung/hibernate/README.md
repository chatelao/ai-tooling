# Factsheet: Hibernate ORM

## Gruppe: Programmierung

## Zweck

Hibernate ORM ist ein Framework für Java-Anwendungen zur Abbildung von objektorientierten Datenmodellen auf relationale Datenbanken (Object-Relational Mapping, ORM). Es implementiert die Jakarta Persistence API (JPA) und bietet leistungsstarke Funktionen für Datenabfrage, Caching und Transaktionsmanagement.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 6.6.1 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [hibernate.org](https://hibernate.org/) |
| Wikipedia | [de.wikipedia.org/wiki/Hibernate_(Framework)](https://de.wikipedia.org/wiki/Hibernate_(Framework)) |

## Installation (Ubuntu 24.04)

Hibernate wird üblicherweise als Abhängigkeit in Java-Build-Tools wie Maven oder Gradle eingebunden.

```bash
# Erfordert Maven
sudo apt update
sudo apt install maven
```

## Hello World

```java
@Entity
@Table(name = "users")
public class User {
    @Id @GeneratedValue
    private Long id;
    private String name;
    // Getters/Setters...
}
```

## Validierung

```bash
mvn --version
```

## Beispiele

Im Ordner `examples/` befinden sich verschiedene Hibernate-Beispiele:

1.  `User.java`: Eine mit JPA-Annotationen versehene Entity-Klasse.
2.  `hibernate.cfg.xml`: Konfigurationsdatei für die Hibernate SessionFactory (JDBC-URL, Dialekt).
3.  `HibernateUtil.java`: Eine Utility-Klasse zur Bereitstellung der Hibernate-Session.
4.  `Main.java`: Ein Beispielprogramm, das ein Objekt speichert und wieder ausliest.
5.  `pom.xml`: Maven-Konfiguration mit Hibernate-Core und H2-Datenbank.
