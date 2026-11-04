import sys
from PIL import Image
im = Image.open(sys.argv[1]); s=3468/1024
def c(name, box, rot=0, scale=1.0):
    b = tuple(int(v*s) for v in box); x = im.crop(b)
    if rot: x = x.rotate(rot, expand=True)
    if scale!=1: x = x.resize((int(x.width*scale), int(x.height*scale)), Image.LANCZOS)
    x.save(f"{sys.argv[2]}/{name}.png")
c("z_sis", (900, 160, 950, 260), rot=-90, scale=3.0)
c("z_warren", (850, 270, 900, 340), rot=-90, scale=3.0)
c("z_is_ger", (540, 60, 680, 92), rot=180, scale=3.0)
c("z_are", (795, 240, 860, 370), rot=-90, scale=2.5)
c("z_warren2", (788, 265, 845, 350), rot=-90, scale=3.0)
c("z_gert", (300, 60, 440, 92), rot=180, scale=3.0)
c("z_corner_tl", (40, 55, 120, 140), rot=0, scale=2.5)
c("z_corner_bl", (40, 520, 130, 630), rot=0, scale=2.0)
c("z_bottom", (230, 595, 520, 625), rot=0, scale=1.6)
