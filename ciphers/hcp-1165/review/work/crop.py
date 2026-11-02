import sys,glob
from PIL import Image, ImageEnhance
im=Image.open(glob.glob('../../work/hires/*adr.jpg')[0]).convert('RGB')
def c(n,x0,y0,x1,y1,s=3):
    r=im.crop((x0,y0,x1,y1)); r=r.resize((r.width*s,r.height*s),Image.LANCZOS)
    ImageEnhance.Contrast(r).enhance(1.5).save(n+'.png')
a=sys.argv[1:]
c(a[0],*map(int,a[1:5]),int(a[5]) if len(a)>5 else 3)
