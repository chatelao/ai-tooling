#!/usr/bin/env python3
"""
Carla Python MIDI Filter Example
Transposes incoming NoteOn/NoteOff MIDI events by +12 semitones (one octave up).
"""

def handle_midi_event(event):
    # event is a tuple or bytearray representing MIDI message: (status, note, velocity)
    if len(event) >= 3:
        status = event[0] & 0xF0
        note = event[1]
        velocity = event[2]

        # Check for NoteOn (0x90) or NoteOff (0x80)
        if status in (0x90, 0x80):
            transposed_note = min(127, max(0, note + 12))
            return bytes([event[0], transposed_note, velocity])

    return event

if __name__ == '__main__':
    # Test example
    test_note_on = bytes([0x90, 60, 100]) # Middle C
    processed = handle_midi_event(test_note_on)
    print(f"Original note: {test_note_on[1]}, Transposed note: {processed[1]}")
