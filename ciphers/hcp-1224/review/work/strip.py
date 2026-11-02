import sys
from PIL import Image
im=Image.open('work/hires/cpc_1912-10-12_HU__HU_Jasz-Arokszalas_jolanka-32_adr.jpg').convert('RGB')
# usage: name x0 y0 x1 y1 scale
n,x0,y0,x1,y1,s=sys.argv[1],*map(int,sys.argv[2:7])
c=im.crop((x0,y0,x1,y1)); c=c.resize((c.width*s,c.height*s),Image.LANCZOS); c.save('review/work/'+n+'.png'); print(c.size)
