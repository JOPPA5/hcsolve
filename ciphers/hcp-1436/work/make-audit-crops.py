#!/usr/bin/env python3
"""Recreate unretouched audit crops from the prior upright working crop (Pillow)."""
from pathlib import Path
from PIL import Image
p = Path(__file__).resolve().parent
im = Image.open(p / 'upright-code.jpg')
for name, box, size in [
    ('middle-audit.png', (0,100,620,220), (2480,480)),
    ('end-audit.png', (0,255,620,350), (2480,380)),
    ('rhould-audit.png', (340,190,620,227), (1680,222)),
    ('long-audit.png', (310,135,520,170), (1260,210)),
]:
    im.crop(box).resize(size).save(p / name)
