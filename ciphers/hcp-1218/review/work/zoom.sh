#!/bin/sh
# Reviewer: zoom.sh <image> <out.png> <x> <y> <w> <h> [scale] [rotate-degrees]
s=${7:-8}
sips -s format png -c $6 $5 --cropOffset $4 $3 "$1" --out "$2" >/dev/null
sips -z $(($6*s)) $(($5*s)) "$2" >/dev/null
[ -n "$8" ] && sips -r $8 "$2" >/dev/null
exit 0
