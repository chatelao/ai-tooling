# Factsheet: Vllm

## Gruppe: Ki/inferenz

## Zweck

vLLM ist eine hocheffiziente Bibliothek für die Inferenz und das Serving von
LLMs. Sie zeichnet sich durch PagedAttention aus, was den Speicherbedarf
erheblich reduziert und den Durchsatz maximiert. KI-Agenten nutzen vLLM als
Backend, um Modelle mit OpenAI-kompatibler API schnell und skalierbar
bereitzustellen.

## Reifegrad

Stabil (Aktiv gewartet, v0.19.0 Stand April 2026)

## Technische Schulden

Gering

## Erwartetes Lebensende

Kein EOL bekannt

## Installation (Ubuntu 24.04)

```bash
pip install vllm
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `test.py`
- `config.json`
- `prompt.txt`
- `output.txt`
- `env.sh`

## Validierung

vLLM Offline-Inferenz testen.
