# Inspectrum Beispiele

Dieses Verzeichnis enthält Beispiele für die Arbeit mit Inspectrum.

## Signal Generierungsskripte

Die folgenden Python-Skripte erzeugen künstliche komplexe IQ-Dateien im `.cf32` Format:

- `generate_test_signal.py`: Sinuswelle mit Rauschen.
- `generate_am_signal.py`: Amplitudenmoduliertes Signal.
- `generate_fm_signal.py`: Frequenzmoduliertes Signal.
- `generate_bpsk_signal.py`: BPSK-moduliertes Digitalsignal.
- `generate_fsk_signal.py`: FSK-moduliertes Digitalsignal.

### Voraussetzungen

- Python 3
- NumPy (`pip install numpy`)

### Ausführung

Beispiel:
```bash
python3 generate_test_signal.py
```

## Verwendung mit Inspectrum

Um eine generierte Datei zu öffnen:

```bash
inspectrum test_signal.cf32
```

In Inspectrum:
- Rechte Maustaste -> Add plot -> Spectrogram
- Frequenz und Samplerate (Standard in Skripten: 1 MHz) anpassen.
