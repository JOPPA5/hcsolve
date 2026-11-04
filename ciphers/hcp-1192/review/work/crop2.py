import sys
from PIL import Image
im = Image.open(sys.argv[1]); s=3468/1024
def c(name, box, rot=0, scale=1.0):
    b = tuple(int(v*s) for v in box); x = im.crop(b)
    if rot: x = x.rotate(rot, expand=True)
    if scale!=1: x = x.resize((int(x.width*scale), int(x.height*scale)), Image.LANCZOS)
    x.save(f"{sys.argv[2]}/{name}.png")
c("date", (900, 470, 950, 625), rot=-90, scale=2.0)
c("sis", (900, 150, 950, 260), rot=-90, scale=2.0)
c("left_end", (42, 440, 75, 545), rot=90, scale=2.5)
c("left_start", (42, 90, 75, 200), rot=90, scale=2.5)
