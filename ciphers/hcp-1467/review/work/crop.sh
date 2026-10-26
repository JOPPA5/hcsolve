#!/bin/sh
# usage: crop.sh SRC OUT X Y W H SCALE  -- crop (W x H at X,Y) and upscale by SCALE using sips
src="$1"; out="$2"; x="$3"; y="$4"; w="$5"; h="$6"; s="$7"
cp "$src" "$out.tmp.jpg"
sips -s format png --cropOffset "$y" "$x" -c "$h" "$w" "$out.tmp.jpg" --out "$out" >/dev/null
sips --resampleWidth $((w*s)) "$out" >/dev/null
rm -f "$out.tmp.jpg"
