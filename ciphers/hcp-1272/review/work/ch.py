from PIL import Image, ImageOps
im=Image.open('../../work/hires/cpc_1912-04-30_HU__HU_Jasz-Arokszalas_jolanka-17_adr.jpg').convert('RGB')
b=(2620,560,3100,770)
r=im.crop(b)
R,G,B=r.split()
from PIL import ImageChops
for n,c in (('G',G),('B',B)):
    c=ImageOps.autocontrast(c,cutoff=1); c.resize((c.width*4,c.height*4),Image.LANCZOS).save('crops/s_%s.png'%n)
# (R-G) saturation-like
d=ImageChops.subtract(R,G); d=ImageOps.autocontrast(d,cutoff=1); d.resize((d.width*4,d.height*4),Image.LANCZOS).save('crops/s_RG.png')
