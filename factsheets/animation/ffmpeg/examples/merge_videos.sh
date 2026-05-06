#!/bin/bash
# Merge multiple videos using the concat demuxer
# Create a list of files to merge
echo "file 'test.mp4'" > inputs.txt
echo "file 'test.mp4'" >> inputs.txt

ffmpeg -f concat -safe 0 -i inputs.txt -c copy merged.mp4
rm inputs.txt
