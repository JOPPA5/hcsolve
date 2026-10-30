import sys
from PIL import Image, ImageOps
n,x0,y0,x1,y1,s=sys.argv[1],*map(int,sys.argv[2:7])
c=Image.open('crops/full_rot.png').convert('L').crop((x0,y0,x1,y1))
c=ImageOps.autocontrast(c,cutoff=(0.5,0.5)).resize(((x1-x0)*s,(y1-y0)*s),Image.BICUBIC)
c.save(f'crops/{n}.png')
