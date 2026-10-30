#!/usr/bin/env python3
"""HCP 1375: make the two report figures from the original address-side scan (rotation 90 degrees CCW)."""
from pathlib import Path
from PIL import Image, ImageOps
D = Path(__file__).resolve().parents[1]
i = Image.open(D / 'work/hires/pc_hcp_56_adr.JPG').convert('L')
r = ImageOps.autocontrast(i.crop((90, 50, 840, 1110)).rotate(90, expand=True), cutoff=1)
r.save(D / 'work/message-rotated.png')
print(r.size)
# Enlargement of the first sign of the closing group (N with a stub on its second foot).
r.crop((460, 510, 560, 590)).resize((500, 400), Image.BICUBIC).save(D / 'work/closing-N-stub.png')
