#!/usr/bin/env python3
"""
Carla Python MIDI Filter Example Script
Filtering out MIDI velocity values below threshold and transposing notes.
"""

def process_midi_event(status, note, velocity, channel=1, transpose=0):
    # MIDI Note On event (0x90 = 144)
    if (status & 0xF0) == 0x90 and velocity > 0:
        if velocity < 10:
            # Filter out ghost notes
            return None
        transposed_note = max(0, min(127, note + transpose))
        return (status, transposed_note, velocity)
    return (status, note, velocity)

if __name__ == "__main__":
    event = process_midi_event(144, 60, 80, transpose=12)
    print(f"Processed MIDI Event: status={event[0]}, note={event[1]}, velocity={event[2]}")
