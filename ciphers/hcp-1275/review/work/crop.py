import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1275/work/hires/cpc_1913-08-13_HU__HU_Jasz-Arokszalas_jolanka-40_adr.jpg').convert('RGB')
# usage: crop.py name x0 y0 x1 y1 scale [rot]
n,x0,y0,x1,y1,s=sys.argv[1],*map(int,sys.argv[2:7])
r=im.crop((x0,y0,x1,y1)); r=r.resize((r.width*s,r.height*s),Image.LANCZOS)
if len(sys.argv)>7: r=r.rotate(int(sys.argv[7]),expand=True)
r.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1275/review/work/crops/'+n+'.png')
