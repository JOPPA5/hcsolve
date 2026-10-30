import sys
from PIL import Image, ImageOps
src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("L")
# text strip, rotate so caption reads left-to-right
strip = im.crop((840, 25, 925, 610)).rotate(-90, expand=True)  # now width 585, height 85
strip = ImageOps.autocontrast(strip, cutoff=1)
W = strip.width
n = 6
for i in range(n):
    x0 = max(0, i*W//n - 10); x1 = min(W, (i+1)*W//n + 10)
    c = strip.crop((x0, 0, x1, strip.height)).resize(((x1-x0)*5, strip.height*5), Image.LANCZOS)
    c.save(f"{out}/r{i}.png")
strip.resize((W*2, strip.height*2), Image.LANCZOS).save(f"{out}/strip.png")
