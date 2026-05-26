# Factsheet: Pawn compiler

## Gruppe: Programmierung

## Zweck

Pawn ist eine einfache, typenlose 32-Bit-Skriptsprache mit einer C-ähnlichen
Syntax. Der Pawn-Compiler übersetzt Quellcode in ein kompaktes P-Code-Format
(AMX), das auf einer abstrakten Maschine ausgeführt wird. KI-Agenten nutzen
Pawn oft für eingebettete Systeme oder zur Erweiterung von Anwendungen durch
Skripting.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 3.10.10 |
| LTS | N/A |
| Reifegrad | Stabil (Eingeschränkte Wartung) |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [github.com/compuphase/pawn](https://github.com/compuphase/pawn) |
| Wikipedia | [de.wikipedia.org/wiki/Pawn_(Programmiersprache](https://de.wikipedia.org/wiki/Pawn_(Programmiersprache)) |

## Installation (Ubuntu 24.04)

Vom GitHub-Repository laden.

## Hello World

```pawn
main() {
    print("Hello World");
}
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `test.pwn`
- `include.inc`
- `amx.amx`
- `config.cfg`
- `log.txt`

## Validierung

Pawn-Compiler ausführen.
