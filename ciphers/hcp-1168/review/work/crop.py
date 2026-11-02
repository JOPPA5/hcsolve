import sys
from PIL import Image
src,x0,y0,x1,y1,s,out=sys.argv[1:8]
im=Image.open(src).convert('RGB').crop((int(x0),int(y0),int(x1),int(y1)))
im=im.resize((im.width*int(s),im.height*int(s)),Image.LANCZOS); im.save(out)
