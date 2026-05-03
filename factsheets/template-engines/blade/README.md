# Factsheet: Blade

## Gruppe: Template-Engines

## Zweck

Blade ist die native Template-Engine des populären Laravel-Frameworks. Sie kompiliert zu reinem PHP und ist daher sehr performant.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [laravel.com/docs/blade](https://laravel.com/docs/blade) |

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

## Beispiele

Im Ordner `examples/` befinden sich verschiedene Blade-Templates:

1.  `basic.blade.php`: Grundlegende Variablenersetzung und unescaped HTML.
2.  `loop.blade.php`: Verwendung von `@foreach` und `@forelse` Schleifen.
3.  `conditional.blade.php`: Bedingte Anweisungen mit `@if`, `@auth` und `@guest`.
4.  `layout.blade.php`: Definition eines Master-Layouts mit `@yield` und `@section`.
5.  `child.blade.php`: Erweitern eines Layouts mit `@extends` und Überschreiben von Sektionen.
