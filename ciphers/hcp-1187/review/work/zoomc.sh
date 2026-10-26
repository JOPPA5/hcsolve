#!/bin/sh
# usage: zoomc.sh SRC OUT X Y W H SCALE -- crop, upscale (nearest), grayscale + contrast via ffmpeg
ffmpeg -loglevel error -y -i "$1" -vf "crop=$5:$6:$3:$4,scale=iw*$7:ih*$7:flags=neighbor,format=gray,eq=contrast=1.6:brightness=0.02" "$2" && echo "$2"
