import sys
from PIL import Image,ImageChops,ImageOps,ImageFilter
im=Image.open('hires/cpc_1912-04-_HU__HU_Jasz-Arokszalas_jolanka-104_adr.jpg').convert('RGB')
n,x0,y0,x1,y1,s,g0=sys.argv[1],*map(float,sys.argv[2:8])
b=[int(v*1.72) for v in (x0,y0,x1,y1)]
c=im.crop(b); r,g,bb=c.split()
d=ImageChops.subtract(r,g,1,0).filter(ImageFilter.MedianFilter(5)).filter(ImageFilter.GaussianBlur(1.5))
lo,hi=d.getextrema()
d=d.point(lambda v:max(0,min(255,int((v-g0)*255/(90)))))
d=ImageOps.invert(d)
d=d.resize((int(d.width*s),int(d.height*s)),Image.BICUBIC); d.save('crops/%s.png'%n)
