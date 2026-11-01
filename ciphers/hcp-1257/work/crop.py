import sys
from PIL import Image
im=Image.open('hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-69_adr.jpg').convert('RGB')
# left block overlapping 3 columns, 6 row bands
n=0
ys=[(40,420),(370,750),(700,1080),(1030,1410),(1360,1740),(1690,2180)]
xs=[(50,620),(560,1130),(1070,1640)]
for r,(y0,y1) in enumerate(ys):
    for c,(x0,x1) in enumerate(xs):
        im.crop((x0,y0,x1,y1)).resize(((x1-x0)*5//2,(y1-y0)*5//2),Image.LANCZOS).save(f'crops/r{r}c{c}.jpg',quality=90)
