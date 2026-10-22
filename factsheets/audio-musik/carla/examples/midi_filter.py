#!/usr/bin/env python3
"""Carla Python MIDI Filter script.
Filters out MIDI Pitch Bend messages and transposed note-on events.
"""

def process_midi_event(status, data1, data2):
    # Filter pitch bend (0xE0)
    if (status & 0xF0) == 0xE0:
        return None
    # Transpose Note On (0x90) up 12 semitones
    if (status & 0xF0) == 0x90:
        return (status, min(127, data1 + 12), data2)
    return (status, data1, data2)

if __name__ == "__main__":
    print("Carla MIDI Filter initialized successfully.")
