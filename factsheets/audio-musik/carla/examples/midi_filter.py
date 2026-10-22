#!/usr/bin/env python3
"""
Carla Custom MIDI Event Processing Filter Script
"""

def process_midi_event(event_type, channel, note, velocity):
    """
    Filters MIDI Note On events, modifying velocity or transposing pitch.
    """
    if event_type == 0x90:  # Note On
        # Transpose one octave up (12 semitones)
        transposed_note = min(127, note + 12)
        # Normalize velocity
        scaled_velocity = min(127, int(velocity * 1.1))
        return event_type, channel, transposed_note, scaled_velocity
    return event_type, channel, note, velocity

if __name__ == "__main__":
    evt = process_midi_event(0x90, 1, 60, 100)  # C4 Note On
    print(f"Processed MIDI Event: type=0x{evt[0]:X}, ch={evt[1]}, note={evt[2]}, vel={evt[3]}")
