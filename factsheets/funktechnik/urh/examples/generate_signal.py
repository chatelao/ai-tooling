import numpy as np

def generate_ook(bits, samples_per_bit):
    signal = []
    for bit in bits:
        if bit == '1':
            signal.extend([1.0] * samples_per_bit)
        else:
            signal.extend([0.0] * samples_per_bit)
    return np.array(signal, dtype=np.complex64)

if __name__ == "__main__":
    bits = "10101100"
    signal = generate_ook(bits, 100)
    print(f"Generated signal with {len(signal)} samples.")
