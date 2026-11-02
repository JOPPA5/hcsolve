import sys,glob
from PIL import Image,ImageOps
im=Image.open(glob.glob('../../work/hires/*_adr.jpg')[0]).convert('RGB')
n,x0,y0,x1,y1,s=sys.argv[1],*map(float,sys.argv[2:7])
c=im.crop((int(x0),int(y0),int(x1),int(y1)))
c=ImageOps.autocontrast(c,cutoff=1)
c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c.save(n+'.png')
