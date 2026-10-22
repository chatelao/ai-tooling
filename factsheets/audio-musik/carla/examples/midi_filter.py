#!/usr/bin/env python3
"""
Carla MIDI Filter Script Example
Applies transpose (+12 semitones / 1 octave) to incoming MIDI note events.
"""

def process_midi_event(event_type, channel, note, velocity):
    # If event is Note On (0x90) or Note Off (0x80)
    if event_type in (0x90, 0x80):
        transposed_note = min(127, max(0, note + 12))
        return (event_type, channel, transposed_note, velocity)
    return (event_type, channel, note, velocity)

if __name__ == "__main__":
    # Test execution
    test_event = process_midi_event(0x90, 1, 60, 100)
    print(f"MIDI Transpose Test: In=(0x90, 1, 60, 100) -> Out={test_event}")
