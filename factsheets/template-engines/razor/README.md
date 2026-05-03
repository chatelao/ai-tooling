# Factsheet: Razor

## Gruppe: Template-Engines

## Zweck

Microsofts Standard-Engine für ASP.NET Core MVC und Blazor. Sie besticht durch einen sehr nahtlosen und flüssigen Übergang zwischen C#-Code und HTML mittels des @-Zeichens.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [learn.microsoft.com/en-us/aspnet/core/mvc/views/razor](https://learn.microsoft.com/en-us/aspnet/core/mvc/views/razor) |

## Installation (Ubuntu 24.04)

```bash
sudo apt install -y dotnet-sdk-8.0
```

## Hello World

```razor
@("Hello World")
```

## Validierung

```bash
dotnet --version
```

## Beispiele

Im Ordner `examples/` befinden sich verschiedene Razor-Templates (`.cshtml`):

1.  `basic.cshtml`: Grundlegende Syntax mit Modellen, Datumsausgabe und Null-Coalescing.
2.  `loop.cshtml`: Verwendung von `@foreach` und `@for` Schleifen zur Iteration.
3.  `conditional.cshtml`: Bedingte Logik mit `@if`/`@else` und `@switch`.
4.  `layout.cshtml`: Definition eines Layouts mit `@RenderBody()` und `@RenderSection()`.
5.  `partial.cshtml`: Erstellung eines wiederverwendbaren Partials.
