#!/bin/sh
# usage: crop.sh src x y w h scale out [rotate]
src=$1; x=$2; y=$3; w=$4; h=$5; s=$6; out=$7; rot=${8:-}
vf="crop=$w:$h:$x:$y,scale=iw*$s:ih*$s:flags=lanczos"
[ -n "$rot" ] && vf="$vf,$rot"
ffmpeg -loglevel error -y -i "$src" -vf "$vf" "$out"
