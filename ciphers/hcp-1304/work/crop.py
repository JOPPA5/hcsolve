"""crops of the hires address side. usage: crop.py name x0 y0 x1 y1 [scale] [rot]  (coords in hires pixels)"""
import sys
from PIL import Image, ImageEnhance
im=Image.open(sys.argv[1]).convert('RGB')
n,x0,y0,x1,y1=sys.argv[2],*map(int,sys.argv[3:7])
s=float(sys.argv[7]) if len(sys.argv)>7 else 2
r=int(sys.argv[8]) if len(sys.argv)>8 else 0
c=im.crop((x0,y0,x1,y1))
if r: c=c.rotate(r,expand=True)
c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c=ImageEnhance.Contrast(c).enhance(1.6)
c.save(n)
