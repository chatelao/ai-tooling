#!/usr/bin/env python3
"""
Carla Python MIDI Filter Example
Transforms velocity or transposed pitch of incoming MIDI events.
"""

def process_midi_event(status, data1, data2):
    # Check if Note On event (channel 1: 0x90)
    if (status & 0xF0) == 0x90 and data2 > 0:
        # Transpose note up by 12 semitones (one octave)
        data1 = min(127, data1 + 12)
    return status, data1, data2

if __name__ == "__main__":
    status, d1, d2 = process_midi_event(0x90, 60, 100)
    print(f"MIDI Transposed: Status={hex(status)}, Note={d1}, Velocity={d2}")
