import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1269/work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-71_adr.jpg').convert('RGB')
x0,y0,x1,y1=map(int,sys.argv[1:5]); s=float(sys.argv[5]); out=sys.argv[6]
rot=int(sys.argv[7]) if len(sys.argv)>7 else 0
c=im.crop((x0,y0,x1,y1)).resize((int((x1-x0)*s),int((y1-y0)*s)),Image.LANCZOS)
if rot: c=c.rotate(rot,expand=True)
c.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1269/work/crops/'+out)
