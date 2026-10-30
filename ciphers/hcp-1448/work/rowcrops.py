import sys
from PIL import Image, ImageOps
src, prefix = sys.argv[1], sys.argv[2]
rows = {1:(95,72),2:(140,120),3:(185,165),4:(228,205)}
im = Image.open(src).convert('RGB')
r = im.split()[0]
for k,(yl,yr) in rows.items():
    segs=[]
    for i,x in enumerate(range(50, 960, 180)):
        x1=min(x+200,970)
        yc = yl + (yr-yl)*((x+x1)/2-50)/910
        c = r.crop((x, int(yc-38), x1, int(yc+18)))
        c = ImageOps.autocontrast(c, cutoff=0.5).resize(((x1-x)*4, 56*4), Image.LANCZOS)
        c.save(f"{prefix}R{k}_{i}.png")
