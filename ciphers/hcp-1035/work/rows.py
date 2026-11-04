import sys
from PIL import Image
im=Image.open(sys.argv[1]).convert('L')
w,h=im.size
x0,x1=int(sys.argv[2]),int(sys.argv[3])
px=im.load()
prof=[]
for y in range(1380,h):
    s=sum(1 for x in range(x0,x1,2) if px[x,y]<140)
    prof.append((y,s))
for y,s in prof:
    if y%6==0: print(y,'#'*(s//8))
