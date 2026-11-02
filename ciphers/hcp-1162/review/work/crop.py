import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1162/work/hires/cpc_1916-03-28_HU_Mezokovesd_HU_Szomolya_szomolya-25_adr.jpg').convert('RGB')
# usage: name x0 y0 x1 y1 scale
for spec in sys.argv[1:]:
    n,x0,y0,x1,y1,s=spec.split(',')
    x0,y0,x1,y1=map(int,(x0,y0,x1,y1)); s=float(s)
    c=im.crop((x0,y0,x1,y1)).resize((int((x1-x0)*s),int((y1-y0)*s)),Image.LANCZOS)
    c.save(f'crops/{n}.png')
