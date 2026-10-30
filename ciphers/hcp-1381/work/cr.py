import sys
from PIL import Image
# usage: name x0 y0 x1 y1 scale [d|r]
n,x0,y0,x1,y1,s=sys.argv[1],*map(int,sys.argv[2:7])
k=sys.argv[7] if len(sys.argv)>7 else 'r'
src=Image.open({'r':'crops/full_rot.png','d':'crops/full_d.png','c':'crops/full_c.png'}[k])
src.crop((x0,y0,x1,y1)).resize(((x1-x0)*s,(y1-y0)*s),Image.LANCZOS).save(f'crops/{n}.png')
