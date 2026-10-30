import sys
from PIL import Image, ImageOps, ImageEnhance
r=Image.open('review/work/rot.png')
n,x0,y0,x1,y1,s=sys.argv[1],*map(int,sys.argv[2:7])
c=r.crop((x0,y0,x1,y1))
if len(sys.argv)>7: c=ImageOps.autocontrast(c.convert('L'),cutoff=1)
c.resize((c.width*s,c.height*s),Image.LANCZOS).save('review/work/%s.png'%n)
