import sys
from PIL import Image
im=Image.open(sys.argv[1]); y0,y1=int(sys.argv[2]),int(sys.argv[3]); x0,x1=int(sys.argv[4]),int(sys.argv[5])
c=im.crop((x0,y0,x1,y1)); s=min(4,1800/c.width); c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS).save(sys.argv[6])
