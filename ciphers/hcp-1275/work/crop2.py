import sys
from PIL import Image, ImageEnhance
im=Image.open('hires/cpc_1913-08-13_HU__HU_Jasz-Arokszalas_jolanka-40_adr.jpg').convert('RGB')
n,x0,y0,x1,y1,s=sys.argv[1],*map(int,sys.argv[2:7])
r=im.crop((x0,y0,x1,y1)); r=r.resize((r.width*s,r.height*s),Image.LANCZOS)
r=ImageEnhance.Contrast(r).enhance(1.5); r.save('crops/'+n+'.png')
