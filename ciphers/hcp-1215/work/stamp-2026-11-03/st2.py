import sys
from PIL import Image, ImageOps
f,out=sys.argv[1],sys.argv[2]
im=Image.open(f).convert('RGB')
def c(n,b,s,mode='col'):
    r=im.crop(b).resize((int((b[2]-b[0])*s),int((b[3]-b[1])*s)),Image.LANCZOS)
    if mode=='col': r=ImageOps.autocontrast(r,cutoff=0.5)
    else: r=ImageOps.autocontrast(r.split()['rgb'.index(mode)],cutoff=1)
    r.save(out+'/'+n+'.png')
# overview offset x+2500
c('rows12',(2780,270,3120,420),4,'r')
c('rows34',(2780,380,3160,540),4,'r')
c('rows56',(2800,490,3160,680),4,'r')
