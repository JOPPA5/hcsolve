#!/bin/sh
# Reviewer crops for hcp-1496: numeric message in three horizontal bands, upscaled.
set -e
SRC=$1
sips -s format png "$SRC" --out base.png >/dev/null
sips -c 140 520 --cropOffset 225 50 base.png --out b1.png >/dev/null; sips -Z 1800 b1.png --out b1_big.png >/dev/null
sips -c 140 520 --cropOffset 355 50 base.png --out b2.png >/dev/null; sips -Z 1800 b2.png --out b2_big.png >/dev/null
sips -c 140 520 --cropOffset 495 50 base.png --out b3.png >/dev/null; sips -Z 1800 b3.png --out b3_big.png >/dev/null
# detail crops (original coordinates)
sips -c 40 200 --cropOffset 405 230 base.png --out d5.png >/dev/null; sips -Z 1400 d5.png --out d5_big.png >/dev/null
sips -c 45 230 --cropOffset 445 280 base.png --out d6.png >/dev/null; sips -Z 1400 d6.png --out d6_big.png >/dev/null
sips -c 45 260 --cropOffset 500 250 base.png --out d7.png >/dev/null; sips -Z 1400 d7.png --out d7_big.png >/dev/null
sips -c 45 230 --cropOffset 545 320 base.png --out d8.png >/dev/null; sips -Z 1400 d8.png --out d8_big.png >/dev/null
# single-number details
sips -c 34 50 --cropOffset 450 455 base.png --out n6end.png >/dev/null; sips -Z 900 n6end.png --out n6end_big.png >/dev/null
sips -c 36 110 --cropOffset 545 420 base.png --out n8end.png >/dev/null; sips -Z 1400 n8end.png --out n8end_big.png >/dev/null
sips -c 40 70 --cropOffset 540 490 base.png --out n8last.png >/dev/null; sips -Z 900 n8last.png --out n8last_big.png >/dev/null
# postmark
sips -c 130 130 --cropOffset 115 690 base.png --out pm.png >/dev/null; sips -Z 800 pm.png --out pm_big.png >/dev/null
# addressee
sips -c 70 440 --cropOffset 320 530 base.png --out addr.png >/dev/null; sips -Z 1400 addr.png --out addr_big.png >/dev/null
