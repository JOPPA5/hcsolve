#!/bin/sh
# usage: crop.sh SRC OUT X Y W H SCALE  -- crop with sips then upscale
src=$1; out=$2; x=$3; y=$4; w=$5; h=$6; s=$7
sips -c "$h" "$w" -s format png --cropOffset "$y" "$x" "$src" --out "$out" >/dev/null
sips -z $((h*s)) $((w*s)) "$out" --out "$out" >/dev/null
echo "$out"
