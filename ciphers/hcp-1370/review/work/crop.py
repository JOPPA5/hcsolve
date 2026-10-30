import sys
from PIL import Image, ImageOps
src=sys.argv[1]
im=Image.open(src).convert('RGB').rotate(90,expand=True)
print(im.size)
im.save('review/work/rot.png')
