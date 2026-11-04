import sys
from PIL import Image
im=Image.open(sys.argv[1]).convert('L')
x0,y0,x1,y1=map(int,sys.argv[2:6]); axis=sys.argv[6]
c=im.crop((x0,y0,x1,y1)); w,h=c.size; px=c.load()
thr=int(sys.argv[7]) if len(sys.argv)>7 else 90
n = w if axis=='x' else h
prof=[]
for i in range(n):
    cnt=0
    for j in range(h if axis=='x' else w):
        v=px[i,j] if axis=='x' else px[j,i]
        if v<thr: cnt+=1
    prof.append(cnt)
runs=[];s=None
for i,v in enumerate(prof+[0]):
    if v>0 and s is None: s=i
    if v==0 and s is not None: runs.append((s,i-1)); s=None
off = x0 if axis=='x' else y0
print([(a+off,b+off) for a,b in runs])
