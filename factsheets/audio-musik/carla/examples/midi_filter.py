#!/usr/bin/env python3
"""
Carla MIDI Event Filter Example
Modifies incoming MIDI velocity and transposes note numbers.
"""

def process_midi_event(channel, event_type, note, velocity):
    # Transpose by +1 octave (12 semitones)
    if event_type == 0x90:  # Note On
        new_note = min(127, note + 12)
        new_velocity = min(127, int(velocity * 1.1))
        return channel, event_type, new_note, new_velocity
    return channel, event_type, note, velocity

if __name__ == "__main__":
    ch, evt, n, v = process_midi_event(1, 0x90, 60, 100)
    print(f"Processed MIDI Event - Channel: {ch}, Event: {evt:#x}, Note: {n}, Velocity: {v}")
