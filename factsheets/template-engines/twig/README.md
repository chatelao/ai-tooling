# Factsheet: Twig

## Gruppe: Template-Engines

## Zweck

Twig ist die Standard-Engine des Symfony-Frameworks. Sie wurde stark von Jinja2 inspiriert, ist sehr sicher (automatisches Escaping) und modern.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 3.14.0 |
| LTS | N/A |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [twig.symfony.com](https://twig.symfony.com/) |

## Installation (Ubuntu 24.04)

```bash
sudo apt install -y php-twig
```

## Hello World

```twig
{{ "Hello World" }}
```

## Validierung

```bash
php -r 'if (file_exists("/usr/share/php/Twig/Environment.php")) echo "Twig installed\n";'
```

## Beispiele

Im Ordner `examples/` befinden sich verschiedene Twig-Templates:

1.  `hello.twig`: Einfache Variablen-Interpolation.
2.  `for_loop.twig`: Iteration über eine Liste.
3.  `if_statement.twig`: Bedingte Logik.
4.  `filters.twig`: Anwendung von Twig-Filtern (upper, date, etc.).
5.  `inheritance_base.twig`: Basis-Template für Template-Vererbung.
