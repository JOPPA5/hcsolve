import sys
from PIL import Image
src, out = sys.argv[1], sys.argv[2]
im = Image.open(src)
for name,(x0,y0,x1,y1),s in [('greet',(225,105,360,140),6),('body1',(195,445,370,500),6),('body2',(360,445,540,500),6),('sig',(85,560,215,610),6)]:
    c = im.crop((x0,y0,x1,y1)); c = c.resize((c.width*s, c.height*s), Image.LANCZOS); c.save(f'{out}/{name}.png')
