import sys
from PIL import Image
# usage: crop.py side x0 y0 x1 y1 scale out
side,x0,y0,x1,y1,s,out=sys.argv[1:8]
p='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1155/work/hires/cpc_1916-02-22_HU_Mezokovesd_HU_Szomolya_szomolya-19_%s.jpg'%side
im=Image.open(p).crop((int(x0),int(y0),int(x1),int(y1)))
im=im.resize((int(im.width*float(s)),int(im.height*float(s))),Image.LANCZOS)
im.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1155/review/work/'+out)
