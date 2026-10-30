import sys
from PIL import Image
# crop.py side x0 y0 x1 y1 scale out
s,x0,y0,x1,y1,k,o=sys.argv[1:8]
i=Image.open(f'/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1787/work/hires/pc_hcp_468_{s}.JPG').convert('RGB')
x0,y0,x1,y1=map(int,(x0,y0,x1,y1));k=float(k)
c=i.crop((x0,y0,x1,y1));c=c.resize((int(c.width*k),int(c.height*k)),Image.LANCZOS)
c.save(o,quality=92)
