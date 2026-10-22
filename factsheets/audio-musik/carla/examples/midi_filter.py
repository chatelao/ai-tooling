# Carla Custom Python MIDI Filter
def process_midi_event(event):
    # Filter out MIDI note off velocity anomalies or remap CC
    status, note, vel = event
    if status == 0x90 and vel == 0:
        # Normalize note-off event
        return (0x80, note, 64)
    return event
