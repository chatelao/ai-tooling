# Factsheet: Thymeleaf

## Gruppe: Template-Engines

## Zweck

Der De-facto-Standard für moderne Spring-Boot-Anwendungen. Die Besonderheit: Thymeleaf-Templates sind valides HTML und können auch ohne Server direkt im Browser als Mockup angezeigt werden.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 3.1.2 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [www.thymeleaf.org](https://www.thymeleaf.org/) |

## Installation (Ubuntu 24.04)

```bash
# Thymeleaf is typically used as a dependency in Java projects (e.g., Maven)
sudo apt install -y maven
```

## Hello World

```html
<p th:text="'Hello World'"></p>
```

## Validierung

```bash
mvn --version
```

## Beispiele

Im Ordner `examples/` befinden sich verschiedene Thymeleaf-Templates (`.html`):

1.  `basic.html`: Grundlegende Textausgabe, Attribut-Handling und URL-Generierung.
2.  `loop.html`: Iteration über Listen mit `th:each`.
3.  `conditional.html`: Bedingte Anzeige mit `th:if`, `th:unless` und `th:switch`.
4.  `fragment.html`: Definition und Verwendung von wiederverwendbaren Fragmenten (`th:fragment`).
5.  `expression_objects.html`: Verwendung von eingebauten Objekten wie `#calendars`, `#strings` und `#lists`.
