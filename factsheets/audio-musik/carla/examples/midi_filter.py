#!/usr/bin/env python3
"""
Carla MIDI Filter Script
Modifies MIDI velocity and filters out specific MIDI CC messages.
"""

def process_midi_event(status, note, velocity):
    # Pass Note-On events with scaled velocity
    if 0x90 <= status <= 0x9F and velocity > 0:
        scaled_velocity = min(127, int(velocity * 1.1))
        return status, note, scaled_velocity
    # Pass all other events unchanged
    return status, note, velocity

if __name__ == "__main__":
    event = process_midi_event(0x90, 60, 100)
    print(f"Processed MIDI Event: Status={hex(event[0])}, Note={event[1]}, Velocity={event[2]}")
