#!/usr/bin/env python3
"""
Carla Python MIDI Filter Script
Transforms incoming MIDI note velocity and filters out program change messages.
"""

def process_midi_event(event_type, channel, note, velocity):
    # Ignore Program Change (0xC0)
    if event_type == 0xC0:
        return None

    # Scale Note On (0x90) velocity by 1.2, capped at 127
    if event_type == 0x90 and velocity > 0:
        scaled_velocity = min(127, int(velocity * 1.2))
        return (event_type, channel, note, scaled_velocity)

    return (event_type, channel, note, velocity)

if __name__ == "__main__":
    # Test example event
    test_event = process_midi_event(0x90, 1, 60, 80)
    print(f"Processed MIDI event: {test_event}")
