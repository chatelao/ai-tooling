#!/usr/bin/env python3
"""
Carla MIDI Filter Script
Transposes incoming MIDI note events by +12 semitones (one octave).
"""

def process_midi_event(event_type, channel, note, velocity):
    if event_type in (0x90, 0x80):  # Note On / Note Off
        transposed_note = min(127, max(0, note + 12))
        return (event_type, channel, transposed_note, velocity)
    return (event_type, channel, note, velocity)

if __name__ == '__main__':
    # Test execution
    sample_event = process_midi_event(0x90, 1, 60, 100)  # C4 -> C5
    print(f"Processed MIDI Event: {sample_event}")
