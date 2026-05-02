# Factsheet: Java (OpenJDK)

## Gruppe: Programmierung

## Zweck

Java ist eine objektorientierte Programmiersprache und Laufzeitumgebung, die für die Entwicklung von plattformunabhängigen Anwendungen weit verbreitet ist.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [Link](https://openjdk.org/) |

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install openjdk-21-jdk
```

## Hello World

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```

## Validierung

```bash
java -version
javac -version
```
