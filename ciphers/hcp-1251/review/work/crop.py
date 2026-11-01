import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1251/work/hires/cpc_1914-04-12_HU__HU_Jasz-Arokszalas_jolanka-52_adr.jpg').convert('RGB')
# usage: name x0 y0 x1 y1 scale
a=sys.argv[1:]
for i in range(0,len(a),6):
    n,x0,y0,x1,y1,s=a[i],*map(int,a[i+1:i+6])
    im.crop((x0,y0,x1,y1)).resize(((x1-x0)*s,(y1-y0)*s),Image.LANCZOS).save(f'/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1251/review/work/c/{n}.png')
