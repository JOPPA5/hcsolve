import sys
from PIL import Image, ImageEnhance
im=Image.open('work/hires/cpc_1916-02-29_HU_Mezokovesd_HU_Szomolya_szomolya-21_adr.jpg').convert('RGB')
n,x0,y0,x1,y1,s=sys.argv[1],*map(int,sys.argv[2:6]),float(sys.argv[6])
c=im.crop((x0,y0,x1,y1)); c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c=ImageEnhance.Contrast(c).enhance(1.4); c.save('review/work/crops/%s.png'%n)
