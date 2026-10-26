#!/bin/sh
# Independent transform (reviewer): crop message area, rotate 90 CCW (= 270 CW), mirror, upscale.
set -e
SRC=$1
sips -s format png "$SRC" --out base.png >/dev/null
# message area x 60..480, y 60..620 -> crop height 560, width 420, offset (y=60,x=60)
sips -c 560 420 --cropOffset 60 60 base.png --out msg.png >/dev/null
sips -r 270 msg.png --out msg_r.png >/dev/null
sips -f horizontal msg_r.png --out msg_rm.png >/dev/null
sips -Z 1800 msg_rm.png --out msg_rm_big.png >/dev/null
# signature strip (x 25..145)
sips -c 560 120 --cropOffset 60 25 base.png --out sig.png >/dev/null
sips -r 270 sig.png --out sig_r.png >/dev/null
sips -f horizontal sig_r.png --out sig_rm.png >/dev/null
sips -Z 1800 sig_rm.png --out sig_big.png >/dev/null
# addressee name (not mirrored)
sips -c 70 400 --cropOffset 310 520 base.png --out addr.png >/dev/null
sips -Z 1600 addr.png --out addr_big.png >/dev/null
# postmark
sips -c 120 150 --cropOffset 100 735 base.png --out pm2.png >/dev/null; sips -Z 900 pm2.png --out pm2_big.png >/dev/null
