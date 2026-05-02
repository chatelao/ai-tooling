# Factsheet: Blade

## Gruppe: Template-Engines

## Zweck

Blade ist die native Template-Engine des populären Laravel-Frameworks. Sie kompiliert zu reinem PHP und ist daher sehr performant.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [Link](https://laravel.com/docs/blade) |

## Installation (Ubuntu 24.04)

```bash
composer require jenssegers/blade
```

## Hello World

```blade
Hello, {{ $name }}!
```

## Validierung

```bash
ls vendor/jenssegers/blade/src/Blade.php
```
