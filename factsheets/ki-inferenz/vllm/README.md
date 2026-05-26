# Factsheet: Vllm

## Gruppe: Ki/inferenz

## Zweck

vLLM ist eine hocheffiziente Bibliothek für die Inferenz und das Serving von
LLMs. Sie zeichnet sich durch PagedAttention aus, was den Speicherbedarf
erheblich reduziert und den Durchsatz maximiert. KI-Agenten nutzen vLLM als
Backend, um Modelle mit OpenAI-kompatibler API schnell und skalierbar
bereitzustellen.

| Eigenschaft | Wert |
| :--- | :--- |
| Latest | 0.6.3 |
| LTS | N/A |
| Reifegrad | Stabil (Aktiv gewartet, v0.19.0 Stand April 2026) |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [github.com/vllm-project/vllm](https://github.com/vllm-project/vllm) |

## Installation (Ubuntu 24.04)

```bash
pip install vllm
```

## Hello World

```bash
python3 -m vllm.entrypoints.openai.api_server
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `test.py`
- `config.json`
- `prompt.txt`
- `output.txt`
- `run_server.sh`
- `openai_client.py`: Python-Client für die OpenAI-kompatible API.
- `offline_inference.py`: Beispiel für die direkte Nutzung der vLLM-Engine ohne Server.
- `distributed_inference.py`: Hinweise zur verteilten Inferenz auf mehreren GPUs.

## Validierung

vLLM Offline-Inferenz testen.
