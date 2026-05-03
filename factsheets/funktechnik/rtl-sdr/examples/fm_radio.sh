#!/bin/bash
# Empfange FM Radio (Beispiel 100.0 MHz) und spiele es ab (erfordert rtl_fm und aplay)
rtl_fm -f 100.0M -M wbfm -s 200000 -r 48000 - | aplay -r 48000 -f S16_LE
