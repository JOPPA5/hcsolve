#!/bin/sh
# usage: crops.sh src.jpg prefix bandheight step nbands — cuts rotated message into left/right halves per band, 4x upscale
src=$1; p=$2; h=$3; st=$4; n=$5
W=$(sips -g pixelWidth $src | tail -1 | awk '{print $2}')
half=$((W/2+20))
i=0
while [ $i -lt $n ]; do
  y=$((i*st))
  sips -c $h $half --cropOffset $((y+1)) 1 $src --out ${p}${i}L.jpg >/dev/null
  sips -c $h $half --cropOffset $((y+1)) $((W-half)) $src --out ${p}${i}R.jpg >/dev/null
  sips -z $((h*4)) $((half*4)) ${p}${i}L.jpg --out ${p}${i}L.jpg >/dev/null
  sips -z $((h*4)) $((half*4)) ${p}${i}R.jpg --out ${p}${i}R.jpg >/dev/null
  i=$((i+1))
done
