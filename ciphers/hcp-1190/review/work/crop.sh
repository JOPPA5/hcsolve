#!/bin/sh
# usage: crop.sh SRC OUT X Y W H SCALE  (sips: crop then upscale)
SRC=$1; OUT=$2; X=$3; Y=$4; W=$5; H=$6; S=$7
sips -c $H $W --cropOffset $Y $X "$SRC" --out "$OUT.tmp.png" -s format png >/dev/null
sips -z $((H*S)) $((W*S)) "$OUT.tmp.png" --out "$OUT" >/dev/null
rm -f "$OUT.tmp.png"
