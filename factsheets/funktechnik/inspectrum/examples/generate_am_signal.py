import numpy as np
import os

def generate_am_signal(filename, fs=1e6, duration=1.0, fc=1e5, fm=1e3, m=0.5):
    t = np.arange(0, duration, 1/fs)
    message = np.cos(2 * np.pi * fm * t)
    carrier = np.exp(2j * np.pi * fc * t)
    signal = (1 + m * message) * carrier

    iq_data = np.empty(2 * len(signal), dtype=np.float32)
    iq_data[0::2] = signal.real
    iq_data[1::2] = signal.imag

    with open(filename, 'wb') as f:
        f.write(iq_data.tobytes())

if __name__ == "__main__":
    output_dir = os.path.dirname(__file__)
    generate_am_signal(os.path.join(output_dir, "am_signal.cf32"))
