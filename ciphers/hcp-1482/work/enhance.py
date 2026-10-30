"""Remove the HC Portal watermark (broad, low-contrast) by background subtraction
and write a rotated (reading-orientation) enhanced image of the cipher area.
Usage (repo root): <python-with-PIL> -I ciphers/hcp-1482/work/enhance.py
"""
import os
from PIL import Image, ImageOps, ImageFilter, ImageChops
d = os.path.dirname(os.path.abspath(__file__))
im = Image.open(os.path.join(d, '..', 'source', 'address-large.jpg')).convert('L')
r = im.crop((40, 30, 620, 640)).rotate(-90, expand=True)   # lines now read left->right
for blur, gain, name in [(12, 7, 'clean-broad.png'), (4, 9, 'clean-fine.png')]:
    bg = r.filter(ImageFilter.GaussianBlur(blur))
    out = ImageOps.invert(ImageChops.subtract(bg, r).point(lambda v: min(255, v * gain)))
    out.resize((out.width * 2, out.height * 2), Image.LANCZOS).save(os.path.join(d, name))
print('written', os.path.join(d, 'clean-broad.png'), os.path.join(d, 'clean-fine.png'))
