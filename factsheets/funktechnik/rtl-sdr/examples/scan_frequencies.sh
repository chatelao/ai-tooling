#!/bin/bash
# Scanne Frequenzen von 88MHz bis 108MHz
rtl_power -f 88M:108M:125k -i 1s scan_results.csv
