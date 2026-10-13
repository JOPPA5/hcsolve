#!/bin/sh
# Reviewer: upscaled strips of a scan for an independent reading (macOS sips).
# usage: crops.sh <image> <outdir> <x0> <width> [step] [height]
src=$1; out=$2; x0=$3; w=$4; step=${5:-100}; h=${6:-125}
y=10; i=0
while [ $y -lt 625 ]; do
  hh=$h; [ $((y+hh)) -gt 657 ] && hh=$((657-y))
  f=$(printf '%s/strip-%02d-y%d.png' "$out" $i $y)
  sips -s format png -c $hh $w --cropOffset $y $x0 "$src" --out "$f" >/dev/null
  sips -z $((hh*4)) $((w*4)) "$f" >/dev/null
  y=$((y+step)); i=$((i+1))
done
