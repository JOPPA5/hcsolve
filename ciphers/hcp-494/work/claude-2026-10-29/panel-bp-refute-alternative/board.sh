#!/bin/sh
# Builds board.png: unlabelled comparison board (see README.txt for the cell order). Native crops, lanczos-scaled to 320 px height, no retouching.
cell() { ffmpeg -loglevel error -y -i "$1" -vf "scale=w=420:h=320:force_original_aspect_ratio=decrease:flags=lanczos,pad=440:360:(ow-iw)/2:(oh-ih)/2:white" "cell-$2.png"; }
cell target-native.jpg a1; cell key-pp-native.jpg a2; cell key-bb-native.jpg a3; cell key-pp-syll.jpg a4
cell ctl-proposition.jpg b1; cell ctl-praedicat.jpg b2; cell ctl-portrait.jpg b3
cell ctl-litb.jpg c1; cell ctl-brunsvicense.jpg c2; cell ctl-berlin.jpg c3; cell ctl-berlino.jpg c4
cell ctl-26.jpg d1; cell ctl-67.jpg d2; cell ctl-breviat.jpg d3
ffmpeg -loglevel error -y -i cell-a1.png -i cell-a2.png -i cell-a3.png -i cell-a4.png -filter_complex "hstack=4" row-a.png
ffmpeg -loglevel error -y -i cell-b1.png -i cell-b2.png -i cell-b3.png -filter_complex "hstack=3,pad=1760:360:0:0:white" row-b.png
ffmpeg -loglevel error -y -i cell-c1.png -i cell-c2.png -i cell-c3.png -i cell-c4.png -filter_complex "hstack=4" row-c.png
ffmpeg -loglevel error -y -i cell-d1.png -i cell-d2.png -i cell-d3.png -filter_complex "hstack=3,pad=1760:360:0:0:white" row-d.png
ffmpeg -loglevel error -y -i row-a.png -i row-b.png -i row-c.png -i row-d.png -filter_complex "vstack=4" board.png
rm -f cell-*.png row-*.png
