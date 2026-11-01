import sys
from PIL import Image, ImageEnhance
im=Image.open('hires/cpc_1914-06-10_HU__HU_Jasz-Arokszalas_jolanka-54_adr.jpg').convert('RGB')
k=3445/1500
for spec in sys.argv[1:]:
    n,x0,y0,x1,y1=spec.split(',')
    r=im.crop(tuple(int(float(v)*k) for v in (x0,y0,x1,y1)))
    z=min(4.0,1500/r.width)
    r=r.resize((int(r.width*z),int(r.height*z)),Image.BICUBIC)
    ImageEnhance.Contrast(ImageEnhance.Color(r).enhance(2)).enhance(1.3).save('crops/%s.png'%n)
