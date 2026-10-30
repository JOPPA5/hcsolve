import sys
from PIL import Image, ImageOps, ImageEnhance
SRC='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1314/work/hires/cpc_1913-03-20_HU__HU_Jasz-Arokszalas_jolanka-35_adr.jpg'
im=Image.open(SRC).convert('L')
def crop(box,name,scale=2,rot=0):
    c=im.crop(box)
    if rot: c=c.rotate(rot,expand=True)
    c=ImageOps.autocontrast(c,cutoff=(1,1))
    c=c.resize((int(c.width*scale),int(c.height*scale)),Image.LANCZOS)
    c.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1314/work/crops/'+name)
a=sys.argv[1:]
if a:
    x0,y0,x1,y1=map(int,a[:4]);crop((x0,y0,x1,y1),a[4],float(a[5]) if len(a)>5 else 2,int(a[6]) if len(a)>6 else 0)
else:
    n=0
    for y in range(40,2100,260):
        crop((50,y,800,y+300),f'L{n}.png'); crop((750,y,1500,y+300),f'R{n}.png'); n+=1
    print(n)
