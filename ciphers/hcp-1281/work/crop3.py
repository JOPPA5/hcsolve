import sys
from PIL import Image, ImageEnhance
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1281/work/hires/cpc_1914-06-10_HU__HU_Jasz-Arokszalas_jolanka-54_adr.jpg').convert('RGB')
s=1.7225
for spec in sys.argv[1:]:
    n,x0,y0,x1,y1,z=spec.split(',')
    r=im.crop(tuple(int(float(v)*s) for v in (x0,y0,x1,y1)))
    z=float(z); r=r.resize((int(r.width*z),int(r.height*z)),Image.BICUBIC)
    ImageEnhance.Contrast(ImageEnhance.Color(r).enhance(2.2)).enhance(1.4).save('crops/%s.png'%n)
