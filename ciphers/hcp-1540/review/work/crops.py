import sys
from PIL import Image
src, outdir = sys.argv[1], sys.argv[2]
im = Image.open(src).rotate(90, expand=True)  # CCW
im.save(outdir+"/rot.png")
print(im.size)
def crop(name, box, s=4):
    c = im.crop(box); c = c.resize((c.width*s, c.height*s), Image.LANCZOS); c.save(f"{outdir}/{name}.png")
crop("full", (0,0,im.width,im.height), 1)
