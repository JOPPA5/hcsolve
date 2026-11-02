import sys
from PIL import Image
# usage: crop.py name x0 y0 x1 y1 scale [src adr|pic]
src=sys.argv[7] if len(sys.argv)>7 else 'adr'
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1160/work/hires/cpc_1915-11-11_HU_Mezokovesd_HU_Szomolya_szomolya-05_%s.jpg'%src)
x0,y0,x1,y1=map(int,sys.argv[2:6]);s=float(sys.argv[6])
c=im.crop((x0,y0,x1,y1));c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1160/review/work/%s.png'%sys.argv[1])
