#!/bin/bash
# usage: zoom.sh name w h x y scale   (coords in original picture.jpg)
S=/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-905/source/picture.jpg
ffmpeg -loglevel error -y -i "$S" -vf "crop=${2}:${3}:${4}:${5},scale=iw*${6}:ih*${6}:flags=lanczos" "z-${1}.png"
