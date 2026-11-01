import sys
from PIL import Image,ImageOps
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1253/work/hires/cpc_1913-02-22_HU__HU_Jasz-Arokszalas_jolanka-33_adr.jpg').convert('L')
# args name x0 y0 x1 y1 scale [rot]
n=sys.argv[1];x0,y0,x1,y1=map(int,sys.argv[2:6]);s=float(sys.argv[6]) if len(sys.argv)>6 else 1;rot=float(sys.argv[7]) if len(sys.argv)>7 else 0
if rot: im=im.rotate(rot,resample=Image.BICUBIC,center=(0,0),fillcolor=200)
c=ImageOps.autocontrast(im.crop((x0,y0,x1,y1)),cutoff=1).resize((int((x1-x0)*s),int((y1-y0)*s)),Image.LANCZOS)
c.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1253/review/work/crops/%s.png'%n)
