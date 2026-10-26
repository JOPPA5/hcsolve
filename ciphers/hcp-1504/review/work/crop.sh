#!/bin/sh
# usage: crop.sh src out x0 y0 x1 y1 scale   (sips only, source untouched)
src=$1; out=$2; x0=$3; y0=$4; x1=$5; y1=$6; s=$7
w=$((x1-x0)); h=$((y1-y0))
sips -s format png --cropOffset $y0 $x0 -c $h $w "$src" --out "$out" >/dev/null
sips -z $((h*s)) $((w*s)) "$out" >/dev/null
