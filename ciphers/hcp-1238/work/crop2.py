import sys
from PIL import Image, ImageOps, ImageFilter
im=Image.open('hires/cpc_1914--_HU__HU_Jasz-Arokszalas_jolanka-118_adr.jpg').convert('RGB')
a=sys.argv
x=im.crop(tuple(map(int,a[2:6]))).split()[1]
bg=x.filter(ImageFilter.GaussianBlur(25))
from PIL import ImageChops
d=ImageChops.subtract(bg,x.filter(ImageFilter.GaussianBlur(0.8)))
d=ImageOps.invert(ImageOps.autocontrast(d,cutoff=(0,0.5)))
s=int(a[6]);d.resize((d.width*s,d.height*s),Image.BICUBIC).save('crops/%s.png'%a[1])
