#!/bin/bash
ffmpeg -i test.mp4 -vn -acodec libmp3lame -ab 128k output.mp3
