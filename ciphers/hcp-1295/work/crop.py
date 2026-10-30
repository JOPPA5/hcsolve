import sys
from PIL import Image, ImageEnhance
src='ciphers/hcp-1295/work/hires/cpc_1912-06-06_HU__HU_Jasz-Arokszalas_jolanka-24_adr.jpg'
im=Image.open(src).convert('RGB')
def crop(name,x0,y0,x1,y1,s=2):
    c=im.crop((x0,y0,x1,y1)); c=c.resize((c.width*s,c.height*s),Image.LANCZOS)
    c=ImageEnhance.Contrast(c).enhance(1.4)
    c.save('ciphers/hcp-1295/work/crops/'+name+'.png')
a=sys.argv
crop(a[1],*map(int,a[2:6]),int(a[6]) if len(a)>6 else 2)
