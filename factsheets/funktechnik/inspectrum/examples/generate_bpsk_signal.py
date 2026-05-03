import numpy as np
import os

def generate_bpsk_signal(filename, fs=1e6, duration=1.0, fc=1e5, rs=1e4):
    t = np.arange(0, duration, 1/fs)
    num_symbols = int(duration * rs)
    symbols = 2 * np.random.randint(0, 2, num_symbols) - 1

    # Upsample symbols
    samples_per_symbol = int(fs / rs)
    symbols_upsampled = np.repeat(symbols, samples_per_symbol)

    # Truncate or pad to match t length
    symbols_upsampled = symbols_upsampled[:len(t)]

    carrier = np.exp(2j * np.pi * fc * t)
    signal = symbols_upsampled * carrier

    iq_data = np.empty(2 * len(signal), dtype=np.float32)
    iq_data[0::2] = signal.real
    iq_data[1::2] = signal.imag

    with open(filename, 'wb') as f:
        f.write(iq_data.tobytes())

if __name__ == "__main__":
    output_dir = os.path.dirname(__file__)
    generate_bpsk_signal(os.path.join(output_dir, "bpsk_signal.cf32"))
