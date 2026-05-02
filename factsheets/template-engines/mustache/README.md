# Factsheet: Mustache

## Gruppe: Template-Engines

## Zweck

Mustache ist eine "logikfreie" Template-Engine, die eine strikte Trennung zwischen Daten und Präsentation erzwingt. Da sie fast keine Programmierlogik (wie if-else oder Schleifen im herkömmlichen Sinne) direkt in den Templates zulässt, ist sie besonders wartungsfreundlich und sprachübergreifend einsetzbar (Implementierungen existieren für Ruby, JavaScript, Python, PHP, Java und viele mehr).

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [Link](https://mustache.github.io/) |

## Installation (Ubuntu 24.04)

```bash
sudo apt install -y node-mustache
```

## Validierung

```bash
mustache.js --version
```

## Hello World

```mustache
{{name}}
```

## Beispiele

Im Ordner `examples/` befinden sich verschiedene Mustache-Templates und zugehörige Datendateien:

1.  `simple_greeting.mustache`: Ein einfaches Template für eine Begrüßung.
2.  `user_list.mustache`: Demonstration von Iteration über eine Liste von Benutzern.
3.  `conditional_section.mustache`: Verwendung von Sektionen für bedingte Anzeige (basierend auf der Existenz von Daten).
4.  `nested_data.mustache`: Zugriff auf verschachtelte Objektstrukturen.
5.  `inverted_section.mustache`: Verwendung von invertierten Sektionen für den Fall, dass Daten fehlen oder eine Liste leer ist.
