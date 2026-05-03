import numpy as np
import os

def generate_signal(filename, fs=1e6, duration=1.0, freq=1e5):
    """
    Generiert ein einfaches komplexes Signal (Sinuswelle mit Rauschen)
    und speichert es im .cf32 Format (Complex Float 32-bit).
    """
    t = np.arange(0, duration, 1/fs)
    signal = np.exp(2j * np.pi * freq * t)

    # Rauschen hinzufügen
    noise = (np.random.randn(len(t)) + 1j * np.random.randn(len(t))) * 0.1
    signal += noise

    # Als Float32 konvertieren (IQ-Daten: I, Q, I, Q, ...)
    iq_data = np.empty(2 * len(signal), dtype=np.float32)
    iq_data[0::2] = signal.real
    iq_data[1::2] = signal.imag

    with open(filename, 'wb') as f:
        f.write(iq_data.tobytes())

    print(f"Signal gespeichert in {filename}")

if __name__ == "__main__":
    output_dir = os.path.dirname(__file__)
    generate_signal(os.path.join(output_dir, "test_signal.cf32"))
