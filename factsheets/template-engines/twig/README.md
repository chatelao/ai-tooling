# Factsheet: Twig

## Gruppe: Template-Engines

## Zweck

Twig ist die Standard-Engine des Symfony-Frameworks. Sie wurde stark von Jinja2 inspiriert, ist sehr sicher (automatisches Escaping) und modern.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [Link](https://twig.symfony.com/) |

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
