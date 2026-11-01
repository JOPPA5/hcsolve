import sys
from PIL import Image
im=Image.open('work/hires/cpc_1912-03-13_HU__HU_Jasz-Arokszalas_jolanka-09_adr.jpg').convert('RGB')
# name x0 y0 x1 y1 scale
for a in sys.argv[1:]:
    n,x0,y0,x1,y1,s=a.split(',')
    x0,y0,x1,y1,s=int(x0),int(y0),int(x1),int(y1),float(s)
    c=im.crop((x0,y0,x1,y1)); c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
    c.save(f'review/work/crops/{n}.png')
