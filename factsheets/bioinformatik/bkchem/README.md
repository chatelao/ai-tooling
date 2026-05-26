# Factsheet: BKChem

## Gruppe: Bioinformatik

## Zweck

BKChem ist ein freier Editor für chemische Strukturen, der in Python geschrieben ist. Es ermöglicht das Zeichnen von 2D-Molekülen und deren Export in verschiedene Formate wie SVG, EPS, PDF und PNG.

Hauptmerkmale:
- Intuitives Zeichnen chemischer Strukturen in 2D.
- Export in vektor- und rasterbasierte Grafikformate.
- Native Unterstützung für CDML (Chemical Design Markup Language).
- Unterstützung für Plugins zur Erweiterung der Funktionalität.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 0.14.0-pre4 |
| LTS | N/A |
| Reifegrad | Veraltet (Inkompatibel mit Python 3.12) |
| Technische Schulden | Hoch |
| Erwartetes Lebensende | Projekt eingestellt |
| Referenzhandbuch | [bkchem.zirael.org](https://bkchem.zirael.org/) |
| Wikipedia | [de.wikipedia.org/wiki/BKChem](https://de.wikipedia.org/wiki/BKChem) |

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install bkchem
```

## Hello World

```bash
bkchem --version
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `benzene.mol`: Eine Model-Datei für Benzol.
- `water.cdml`: Eine BKChem-native XML-Datei für Wasser.
- `molecule.cdml`: Beispiel für eine komplexere Molekülstruktur in CDML.
- `aspirin.svg`: Exportiertes Vektorbild der Aspirin-Struktur.
- `plugin.py`: Beispiel für ein Python-Plugin zur Funktionserweiterung.

## Validierung

Starten Sie BKChem über die Kommandozeile oder das Anwendungsmenü:

```bash
PYTHONPATH=../../../scripts xvfb-run -a /usr/bin/python3 /usr/share/bkchem/bkchem/bkchem.py --help
```
