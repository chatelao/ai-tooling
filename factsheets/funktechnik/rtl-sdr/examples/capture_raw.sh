#!/bin/bash
# Erfasse Rohdaten (I/Q Samples) für 5 Sekunden
rtl_sdr -f 100M -s 2.048M -n 10240000 capture.bin
