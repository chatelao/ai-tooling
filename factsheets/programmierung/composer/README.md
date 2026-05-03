# Factsheet: PHP Composer

## Gruppe: Programmierung

## Zweck

Composer ist ein Abhängigkeitsmanager für PHP, der es ermöglicht, Bibliotheken und Abhängigkeiten für PHP-Projekte zu verwalten.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [getcomposer.org](https://getcomposer.org/) |

## Installation (Ubuntu 24.04)

```bash
sudo apt install composer
```

## Hello World

```bash
composer --version
```

## Beispiele

Im Ordner `examples/` befinden sich verschiedene Composer-Konfigurationsbeispiele (`.json`):

1.  `minimal-composer.json`: Eine grundlegende `composer.json` mit PHP-Version und einer Abhängigkeit.
2.  `autoload-config.json`: Konfiguration von PSR-4 Autoloading für Source- und Test-Verzeichnisse.
3.  `scripts-example.json`: Definition von benutzerdefinierten Skripten und Hooks.
4.  `custom-repository.json`: Einbinden von privaten VCS-Repositories.
5.  `config-options.json`: Verschiedene Konfigurationsoptionen zur Optimierung und Sicherheit.

## Validierung

```bash
composer --version
```
