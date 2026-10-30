import sys
from PIL import Image
im=Image.open(sys.argv[1]).convert('RGB')
x0,y0,x1,y1,s=map(int,sys.argv[3:8])
c=im.crop((x0,y0,x1,y1)); c=c.resize(((x1-x0)*s,(y1-y0)*s),Image.LANCZOS); c.save(sys.argv[2])
