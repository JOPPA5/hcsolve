#!/bin/sh
# usage: crop.sh src out x0 y0 w h scale [rot]  -- ffmpeg only, source untouched
# rot: cw (transpose=1), ccw (transpose=2), none
src=$1; out=$2; x=$3; y=$4; w=$5; h=$6; s=$7; r=${8:-cw}
case $r in cw) t=",transpose=1";; ccw) t=",transpose=2";; *) t="";; esac
ffmpeg -loglevel error -y -i "$src" -vf "crop=$w:$h:$x:$y$t,scale=iw*$s:ih*$s:flags=lanczos" "$out"
