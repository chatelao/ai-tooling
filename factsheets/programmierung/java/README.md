# Factsheet: Java (OpenJDK)

## Gruppe: Programmierung

## Zweck

Java ist eine objektorientierte Programmiersprache und Laufzeitumgebung, die für die Entwicklung von plattformunabhängigen Anwendungen weit verbreitet ist.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [openjdk.org](https://openjdk.org/) |

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

## Beispiele

Im Ordner `examples/` befinden sich verschiedene Java-Beispiele:

1.  `HelloWorld.java`: Ein klassisches "Hello World" Programm mit Argumentverarbeitung.
2.  `CollectionsDemo.java`: Demonstration von Java Collections (ArrayList, HashMap).
3.  `StreamApiDemo.java`: Verwendung der Stream API zum Filtern und Transformieren von Daten.
4.  `FileIODemo.java`: Lesen und Schreiben von Dateien mit Try-with-Resources.
5.  `ConcurrencyDemo.java`: Verwendung von Thread-Pools und ExecutorService für Nebenläufigkeit.
