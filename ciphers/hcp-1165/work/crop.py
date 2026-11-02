import sys,glob
from PIL import Image, ImageEnhance
im=Image.open(glob.glob('work/hires/*adr.jpg')[0] if 0 else glob.glob('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1165/work/hires/*adr.jpg')[0]).convert('RGB')
def c(name,x0,y0,x1,y1,s=2):
    r=im.crop((x0,y0,x1,y1)); r=r.resize((r.width*s,r.height*s),Image.LANCZOS)
    r=ImageEnhance.Contrast(r).enhance(1.4)
    r.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1165/work/crops/%s.png'%name)
if len(sys.argv)>1:
    a=sys.argv[1:]; c(a[0],*map(int,a[1:6]))
else:
    for i,(y0,y1) in enumerate([(30,250),(160,350),(240,430),(320,510),(400,590),(470,660)]):
        c('L%da'%i,40,y0,1400,y1); c('L%db'%i,1300,y0,2720,y1)
