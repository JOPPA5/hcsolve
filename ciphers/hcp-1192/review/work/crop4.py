import sys
from PIL import Image
im = Image.open(sys.argv[1]); s=3468/1024
def c(name, box, rot=0, scale=1.0):
    b = tuple(int(v*s) for v in box); x = im.crop(b)
    if rot: x = x.rotate(rot, expand=True)
    if scale!=1: x = x.resize((int(x.width*scale), int(x.height*scale)), Image.LANCZOS)
    x.save(f"{sys.argv[2]}/{name}.png")
c("ladders_top", (280, 60, 680, 92), rot=180, scale=1.0)
c("ladders_r", (790, 150, 950, 330), rot=-90, scale=1.0)
