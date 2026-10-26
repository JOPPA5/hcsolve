#!/bin/sh
# Reviewer crops for hcp-1492: message area rotated 180 and upscaled.
set -e
SRC=$1
sips -s format png "$SRC" --out base.png >/dev/null
sips -c 570 460 --cropOffset 50 25 base.png --out msg.png >/dev/null
sips -r 180 msg.png --out msg_r.png >/dev/null
sips -Z 1800 msg_r.png --out msg_big.png >/dev/null
# numeric block only: original y 190..330, x 25..380
sips -c 140 355 --cropOffset 190 25 base.png --out num.png >/dev/null
sips -r 180 num.png --out num_r.png >/dev/null
sips -Z 1800 num_r.png --out num_big.png >/dev/null
# numeric block, left and right halves (rotated frame msg_r.png is 460x570)
sips -c 85 240 --cropOffset 320 0 msg_r.png --out nL.png >/dev/null; sips -Z 1600 nL.png --out nL_big.png >/dev/null
sips -c 85 240 --cropOffset 320 220 msg_r.png --out nR.png >/dev/null; sips -Z 1600 nR.png --out nR_big.png >/dev/null
# the "24 24 24" group under the printed text
sips -c 45 230 --cropOffset 425 100 msg_r.png --out x24.png >/dev/null; sips -Z 1400 x24.png --out x24_big.png >/dev/null
