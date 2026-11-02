import sys
from PIL import Image, ImageOps
f='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1227/work/hires/cpc_-09-26_HU__HU_Jasz-Arokszalas_jolanka-95_%s.jpg'
# usage: crop.py out adr x0 y0 x1 y1 scale
out,s,x0,y0,x1,y1,sc=sys.argv[1:8]
x0,y0,x1,y1=map(int,(x0,y0,x1,y1));sc=float(sc)
im=Image.open(f%s).convert('RGB').crop((x0,y0,x1,y1))
if len(sys.argv)>8 and sys.argv[8]=='g':
    r,g,b=im.split()
    im=ImageOps.autocontrast(r)
im=im.resize((int(im.width*sc),int(im.height*sc)),Image.LANCZOS)
im.save('review/work/'+out)
