import sys,glob
from PIL import Image, ImageEnhance
f=glob.glob('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1172/work/hires/*adr.jpg')[0]
im=Image.open(f).convert('RGB')
out='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1172/work/crops/'
# name x0 y0 x1 y1 scale
for a in sys.argv[1:]:
    n,x0,y0,x1,y1,s=a.split(',')
    x0,y0,x1,y1=map(int,(x0,y0,x1,y1));s=float(s)
    c=im.crop((x0,y0,x1,y1)); c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
    ImageEnhance.Contrast(c).enhance(1.4).save(out+n+'.png')
