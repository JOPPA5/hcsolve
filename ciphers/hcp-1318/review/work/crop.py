import sys
from PIL import Image, ImageOps, ImageEnhance
src='work/hires/cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-111_adr.jpg'
im=Image.open(src).convert('RGB')
def crop(name,box,s):
    c=im.crop(box); c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
    c=ImageEnhance.Contrast(c).enhance(1.5); c.save('review/work/crops/'+name+'.png')
if len(sys.argv)>1:
    n,x0,y0,x1,y1,s=sys.argv[1:7]; crop(n,(int(x0),int(y0),int(x1),int(y1)),float(s))
else:
    y=70;i=0
    while y<2100:
        crop(f'L{i}',(60,y,900,y+320),2.3); crop(f'R{i}',(850,y,1720,y+320),2.3); y+=290;i+=1
    print(i)
