# Factsheet: Ollama

## Gruppe: Ki/inferenz

## Zweck

Ollama ist ein leichtgewichtiges Framework zum lokalen Ausführen von großen
Sprachmodellen (LLMs) wie Llama 3, Mistral oder Phi-3. Es bündelt Modellgewichte,
Konfiguration und Datensatz in einem "Modelfile" und bietet eine einfache API
sowie ein CLI-Interface, was es ideal für die Integration in KI-Agenten macht,
die lokale Inferenz benötigen.

## Reifegrad

Stabil (Aktiv gewartet, v0.20.7 Stand April 2026)

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Wikipedia

[Link](https://de.wikipedia.org/wiki/Ollama)

## Installation (Ubuntu 24.04)

```bash
sudo apt install pciutils lshw zstd
curl -fsSL https://ollama.com/install.sh | sh
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `model.mf`
- `test.py`
- `config.json`
- `prompt.txt`
- `response.json`

## Validierung

Ollama Version prüfen:

```bash
ollama --version
```
