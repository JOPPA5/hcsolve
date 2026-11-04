import sys
from PIL import Image
src,outp,x0,y0,x1,y1,rot,n,sc=sys.argv[1],sys.argv[2],*map(int,sys.argv[3:9]),float(sys.argv[9])
im=Image.open(src).crop((x0,y0,x1,y1)).rotate(rot,expand=True)
w=im.width; step=w//n
for k in range(n):
    a=max(0,k*step-60); b=min(w,(k+1)*step+60)
    p=im.crop((a,0,b,im.height))
    p=p.resize((int(p.width*sc),int(p.height*sc)),Image.LANCZOS)
    p.save(f"{outp}{k}.png")
