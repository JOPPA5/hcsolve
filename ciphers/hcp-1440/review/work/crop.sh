#!/bin/bash
# usage: crop.sh SRC OUTPNG X Y W H SCALE
ffmpeg -loglevel error -y -i "$1" -vf "crop=${5}:${6}:${3}:${4},scale=iw*${7}:ih*${7}:flags=lanczos" "$2"
