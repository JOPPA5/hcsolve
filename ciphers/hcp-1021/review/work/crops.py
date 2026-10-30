import sys
from PIL import Image, ImageOps
src=sys.argv[1]; out=sys.argv[2]
im=Image.open(src).convert('L')
print(im.size)
strip=im.crop((60,5,870,60)).rotate(180)
strip=ImageOps.autocontrast(strip,cutoff=1)
# segments in rotated coordinates
W=strip.size[0]
for i,(a,b) in enumerate([(0,280),(260,540),(520,810)]):
    s=strip.crop((a,0,b,55)).resize(((b-a)*4,55*4),Image.LANCZOS)
    s.save(f"{out}/top_rot_{i}.png")
strip.resize((W*2,110),Image.LANCZOS).save(f"{out}/top_rot_full.png")
