import sys
from PIL import Image
im = Image.open(sys.argv[1]); s=3468/1024
def c(name, box, rot=0, scale=1.0):
    b = tuple(int(v*s) for v in box); x = im.crop(b)
    if rot: x = x.rotate(rot, expand=True)
    if scale!=1: x = x.resize((int(x.width*scale), int(x.height*scale)), Image.LANCZOS)
    x.save(f"{sys.argv[2]}/{name}.png")
c("date3", (885, 420, 960, 545), rot=-90, scale=2.0)
c("date3_180", (885, 420, 960, 545), rot=90, scale=2.0)
