import sys
from PIL import Image
im=Image.open(sys.argv[1]); x0,y0,x1,y1,sc=map(int,sys.argv[3:8])
c=im.crop((x0,y0,x1,y1)); c=c.resize((c.width*sc,c.height*sc),Image.LANCZOS); c.save(sys.argv[2])
