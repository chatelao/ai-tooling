# Factsheet: Jinja2

## Gruppe: Template-Engines

## Zweck

Jinja2 ist eine sehr mächtige und ausdrucksstarke Template-Engine für Python. Sie ist der Standard im Web-Framework Flask und wird zudem intensiv in Automatisierungstools wie Ansible verwendet.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [jinja.palletsprojects.com](https://jinja.palletsprojects.com/) |

## Installation (Ubuntu 24.04)

```bash
pip install Jinja2
```

## Validierung

```bash
python3 -c "import jinja2; print(jinja2.__version__)"
```

## Hello World

```jinja2
Hello {{ name }}!
```

## Beispiele

Im Ordner `examples/` befinden sich verschiedene Jinja2-Templates:

1.  `hello.html.j2`: Ein einfaches HTML-Template mit Variablenersetzung.
2.  `inventory.ini.j2`: Ein komplexeres Beispiel für die Generierung einer Ansible-ähnlichen Inventory-Datei unter Verwendung von Schleifen.
3.  `report.txt.j2`: Ein Textbericht-Template mit Datumsangaben, Schleifen und Filtern.
4.  `user_profile.html.j2`: Ein HTML-Snippet für ein Benutzerprofil, das bedingte Logik und Filter nutzt.
5.  `web_config.yaml.j2`: Ein Konfigurations-Template im YAML-Format mit Standardwerten.
