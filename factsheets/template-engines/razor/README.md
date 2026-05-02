# Factsheet: Razor

## Gruppe: Template-Engines

## Zweck

Microsofts Standard-Engine für ASP.NET Core MVC und Blazor. Sie besticht durch einen sehr nahtlosen und flüssigen Übergang zwischen C#-Code und HTML mittels des @-Zeichens.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [Link](https://learn.microsoft.com/en-us/aspnet/core/mvc/views/razor) |

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
