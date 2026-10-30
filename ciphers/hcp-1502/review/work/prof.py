import sys
from PIL import Image
im=Image.open(sys.argv[1]).convert('L')
y0,y1,x0,x1,th=map(int,sys.argv[2:7])
runs=[];cur=None
for x in range(x0,x1):
    col=[im.getpixel((x,y)) for y in range(y0,y1)]
    m=min(col); dark=m<th
    n=sum(1 for v in col if v<th)
    if dark and cur is None: cur=[x,x,n]
    elif dark: cur[1]=x; cur[2]=max(cur[2],n)
    elif cur: runs.append(cur);cur=None
if cur: runs.append(cur)
for a,b,h in runs: print(f'{a}-{b} len={b-a+1} h={h}')
