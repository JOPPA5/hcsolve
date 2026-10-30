import sys
from PIL import Image, ImageOps, ImageEnhance
src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).rotate(90, expand=True)  # try orientation
im.save(out+'/rot.png')
print(im.size)
