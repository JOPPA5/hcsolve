import sys
from PIL import Image, ImageOps, ImageEnhance
src, out, x0,y0,x1,y1, rot, sc = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:7]), float(sys.argv[7]), float(sys.argv[8])
im = Image.open(src).convert('L').crop((x0,y0,x1,y1))
im = ImageOps.autocontrast(im, cutoff=1)
im = ImageEnhance.Contrast(im).enhance(2.0)
im = im.rotate(rot, expand=True, fillcolor=255, resample=Image.BICUBIC)
im = im.resize((int(im.width*sc), int(im.height*sc)), Image.LANCZOS)
im.save(out)
