#!/bin/bash
# Overlay a logo (test.png) on a video (test.mp4)
# Places the logo in the top-right corner with 10px padding
ffmpeg -i test.mp4 -i test.png -filter_complex "overlay=main_w-overlay_w-10:10" -codec:a copy output_with_logo.mp4
