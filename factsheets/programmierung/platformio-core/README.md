# Factsheet: Platformio core

## Gruppe: Programmierung

## Zweck

PlatformIO Core ist das Herzstück des PlatformIO-Ökosystems, ein
plattformübergreifendes Build-System und Bibliotheksmanager für die
Embedded-Entwicklung. KI-Agenten nutzen PIO Core, um Hardware-Projekte für
Hunderte von Boards (Arduino, ESP32, STM32 etc.) automatisiert zu konfigurieren
und zu kompilieren.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil (Aktiv gewartet, v6.1.19 Stand April 2026) |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [platformio.org](https://platformio.org/) |
| Wikipedia | [de.wikipedia.org/wiki/PlatformIO](https://de.wikipedia.org/wiki/PlatformIO) |

## Installation (Ubuntu 24.04)

```bash
pip install platformio
```

## Hello World

```bash
pio --version
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `platformio.ini`
- `src.cpp`
- `lib.cpp`
- `include.h`
- `test.cpp`

## Validierung

Version prüfen:

```bash
pio --version
```
