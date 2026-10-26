#!/bin/sh
# crop.sh <src> <out.png> x0 y0 x1 y1 [scale]  -- crop with sips and upscale
src=$1; out=$2; x0=$3; y0=$4; x1=$5; y1=$6; s=${7:-4}
w=$((x1-x0)); h=$((y1-y0))
sips -s format png -c $h $w --cropOffset $y0 $x0 "$src" --out "$out" >/dev/null
sips -z $((h*s)) $((w*s)) "$out" >/dev/null
echo "$out ${w}x${h} x$s"
