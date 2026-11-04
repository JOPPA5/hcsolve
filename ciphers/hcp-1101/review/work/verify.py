"""Reviewer's independent red-filter check for hcp-1101.
Run from repo root with the PIL python and -I.
Thresholded R channel (ink <110 -> black, >190 -> white) of the hi-res picture side,
plus enlarged crops of every line and the open text."""
import os
from PIL import Image
D = "ciphers/hcp-1101"
im = Image.open(os.path.join(D, "work/hires/cpc_1898-02-11_CH_Basel_CH_Basel__pic.jpg")).convert("RGB")
c = im.crop((1860, 920, 3360, 1620)).split()[0]
r = c.point(lambda v: 0 if v < 110 else (255 if v > 190 else int((v - 110) * 255 / 80)))
r.save(os.path.join(D, "review/work/rf_all.png"))
r.crop((0, 30, 800, 250)).resize((2400, 660)).save(os.path.join(D, "review/work/z_l12a.png"))
r.crop((700, 30, 1400, 250)).resize((2100, 660)).save(os.path.join(D, "review/work/z_l12b.png"))
im.crop((1850, 620, 3350, 940)).save(os.path.join(D, "review/work/z_top.png"))
im.crop((1850, 1580, 3150, 1980)).save(os.path.join(D, "review/work/z_bottom.png"))
print("written")
