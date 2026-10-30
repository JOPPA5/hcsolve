import sys
from PIL import Image, ImageEnhance, ImageOps
# usage: crop.py name x0 y0 x1 y1 scale [rot]
im=Image.open('ciphers/hcp-1346/work/hires/pc_hcp_27_pic.JPG').convert('L')
n,x0,y0,x1,y1,s=sys.argv[1],*map(int,sys.argv[2:7])
c=im.crop((x0,y0,x1,y1))
if len(sys.argv)>7: c=c.rotate(int(sys.argv[7]),expand=True)
c=ImageOps.autocontrast(c,cutoff=1)
c=c.resize((c.width*s,c.height*s),Image.LANCZOS)
c.save(f'ciphers/hcp-1346/review/work/{n}.png')
