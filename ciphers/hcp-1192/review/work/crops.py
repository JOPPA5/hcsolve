import sys
from PIL import Image
src, out = sys.argv[1], sys.argv[2]
im = Image.open(src)
s = 3468/1024
def c(name, box, rot=0, scale=1.0):
    b = tuple(int(v*s) for v in box)
    x = im.crop(b)
    if rot: x = x.rotate(rot, expand=True)
    if scale != 1: x = x.resize((int(x.width*scale), int(x.height*scale)), Image.LANCZOS)
    x.save(f"{out}/{name}.png")
# right panel, split in two halves vertically (card coords); rotate -90 => clockwise, tops (left) go up
c("right_lower", (790, 330, 950, 625), rot=-90, scale=0.9)
c("right_upper", (790, 80, 950, 340), rot=-90, scale=0.9)
# top strip: writer upside-down, rotate 180
c("top_r", (500, 62, 770, 90), rot=180, scale=1.2)
c("top_l", (270, 62, 520, 90), rot=180, scale=1.2)
# left strip: tops toward right (picture) -> rotate +90 (ccw) makes right go up
c("left_t", (42, 90, 75, 300), rot=90, scale=1.2)
c("left_b", (42, 290, 75, 545), rot=90, scale=1.2)
c("bottom", (240, 595, 520, 625), scale=1.2)
