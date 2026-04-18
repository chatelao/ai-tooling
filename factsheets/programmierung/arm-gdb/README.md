# Factsheet: ARM GDB

## Gruppe: Programmierung

## Zweck: Debugger für ARM Cortex-M/R Prozessoren

Der GNU Debugger (GDB) in der Multiarch-Variante ermöglicht das Debuggen von
Anwendungen für verschiedene Architekturen, insbesondere ARM Cortex-M und
Cortex-R Mikrocontroller.

## Reifegrad

Stabil

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Referenzhandbuch

[Link](https://www.gnu.org/software/gdb/)

## Wikipedia

[Link](https://de.wikipedia.org/wiki/GNU_Debugger)

## Installation (Ubuntu 24.04)

```bash
sudo apt install gdb-multiarch
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `.gdbinit`: Standard-Initialisierungsskript für GDB.
- `attach_openocd.gdb`: Skript zum Verbinden mit einer OpenOCD-Sitzung.
- `dump_memory.gdb`: Skript zum Sichern eines Speicherbereichs in eine Datei.
- `break_and_log.gdb`: Skript zum Setzen von Breakpoints mit automatischem
  Logging.
- `display_registers.gdb`: Skript zur formatierten Anzeige von CPU-Registern.

## Validierung

GDB-Version prüfen:

```bash
gdb-multiarch --version
```
