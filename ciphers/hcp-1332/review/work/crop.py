import sys
from PIL import Image
src,x0,y0,x1,y1,sc,out,rot=sys.argv[1],*map(int,sys.argv[2:7]),sys.argv[7],(int(sys.argv[8]) if len(sys.argv)>8 else 0)
im=Image.open(src).convert('RGB').crop((x0,y0,x1,y1))
if rot: im=im.rotate(rot,expand=True)
im=im.resize((im.width*sc,im.height*sc),Image.LANCZOS); im.save(out)
