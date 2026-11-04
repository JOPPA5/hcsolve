import sys
from PIL import Image
src,out,x0,y0,x1,y1,sc,rot,thr=sys.argv[1],sys.argv[2],*map(int,sys.argv[3:5]),*map(int,sys.argv[5:7]),float(sys.argv[7]),int(sys.argv[8]),int(sys.argv[9])
im=Image.open(src).convert('L').crop((x0,y0,x1,y1))
im=im.point(lambda v: 0 if v<thr else 255)
if rot: im=im.rotate(rot,expand=True)
im=im.resize((int(im.width*sc),int(im.height*sc)),Image.NEAREST)
im.save(out)
