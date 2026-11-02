import glob,sys
from PIL import Image,ImageOps
f=glob.glob('hires/*adr.jpg')[0]
im=Image.open(f).convert('L')
# cz name y x0 x1 : two-part row image 3.2x w/ moderate contrast, height +-68
n=sys.argv[1];y=int(sys.argv[2]);x0=int(sys.argv[3]);x1=int(sys.argv[4]);h=int(sys.argv[5]) if len(sys.argv)>5 else 66
c=im.crop((x0,y-h,x1,y+h));c=ImageOps.autocontrast(c,cutoff=0.2)
c=ImageOps.colorize(c.point(lambda v:min(255,int((v/255)**0.8*255))),'black','white')
s=1500/c.width
c=c.resize((1500,int(c.height*s)),Image.LANCZOS);c.save(f'crops/{n}.png')
