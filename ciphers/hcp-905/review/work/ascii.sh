#!/bin/bash
# ascii.sh x y w h : print darkness map of picture.jpg region (gray<100 '#', <140 '+', <170 '.', else ' ')
S=/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-905/source/picture.jpg
ffmpeg -loglevel error -i "$S" -vf "crop=$3:$4:$1:$2,format=gray" -f rawvideo - | python3 -I -c "
import sys
w,h=$3,$4; b=sys.stdin.buffer.read()
for y in range(h):
    print('%3d '%y+''.join('#' if b[y*w+x]<100 else '+' if b[y*w+x]<140 else '.' if b[y*w+x]<170 else ' ' for x in range(w)))
"
