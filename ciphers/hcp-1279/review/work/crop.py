import sys
from PIL import Image, ImageOps
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1279/work/hires/cpc_1914-04-12_HU__HU_Jasz-Arokszalas_jolanka-53_adr.jpg').convert('RGB')
n,x0,y0,x1,y1,s=sys.argv[1],*map(int,sys.argv[2:7])
r=im.crop((x0,y0,x1,y1)); r=r.resize((r.width*s,r.height*s),Image.LANCZOS); r=ImageOps.autocontrast(r,cutoff=1); r.save('crops/'+n+'.png')
