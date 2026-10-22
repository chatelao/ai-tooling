#!/usr/bin/env python3
"""
Custom Carla Python MIDI Filter script.
Transposes incoming MIDI note-on events by a specified interval.
"""

TRANSPOSE_SEMITONES = 12  # One octave up

def process(events):
    output_events = []
    for event in events:
        if event.type == 'note_on':
            event.note = min(127, max(0, event.note + TRANSPOSE_SEMITONES))
        output_events.append(event)
    return output_events

if __name__ == '__main__':
    print(f"Carla MIDI Transpose Filter active (Interval: +{TRANSPOSE_SEMITONES} semitones)")
