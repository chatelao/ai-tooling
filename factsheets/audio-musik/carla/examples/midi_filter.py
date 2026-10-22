"""
Carla Python MIDI Filter Example
Transforms incoming MIDI note events by transposing octaves.
"""

def process_midi_event(event):
    # Check if event is Note On (0x90) or Note Off (0x80)
    status = event[0] & 0xF0
    if status in (0x90, 0x80):
        note = event[1]
        # Transpose note up one octave (12 semitones)
        new_note = min(127, note + 12)
        event[1] = new_note
    return event

if __name__ == "__main__":
    sample_event = [0x90, 60, 100]  # Middle C Note On
    transformed = process_midi_event(sample_event)
    print(f"Original: [0x90, 60, 100] -> Transposed: {transformed}")
