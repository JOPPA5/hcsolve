# Connected-component listing of ink marks in the message area (hires address side).
import sys
from PIL import Image
import numpy as np
from collections import deque
im=Image.open(sys.argv[1]).convert('L')
a=np.array(im).astype(int)
X0,Y0,X1,Y1=30,560,1820,1540
sub=a[Y0:Y1,X0:X1]
bg=np.median(sub)
mask=sub<bg-55
H,W=mask.shape
lab=np.zeros_like(mask,dtype=int);n=0;comps=[]
for y in range(H):
  for x in range(W):
    if mask[y,x] and not lab[y,x]:
      n+=1;q=deque([(y,x)]);lab[y,x]=n;pts=[]
      while q:
        cy,cx=q.popleft();pts.append((cy,cx))
        for dy in(-2,-1,0,1,2):
          for dx in(-2,-1,0,1,2):
            ny,nx=cy+dy,cx+dx
            if 0<=ny<H and 0<=nx<W and mask[ny,nx] and not lab[ny,nx]:
              lab[ny,nx]=n;q.append((ny,nx))
      if len(pts)>=12:
        ys=[p[0] for p in pts];xs=[p[1] for p in pts]
        comps.append((min(ys)+Y0,max(ys)+Y0,min(xs)+X0,max(xs)+X0,len(pts)))
comps.sort(key=lambda c:((c[0]+c[1])//2//150,c[2]))
for c in comps:
  y0,y1,x0,x1,s=c
  L=max(y1-y0,x1-x0)
  print(f'y{(y0+y1)//2:5d} x{x0:5d}-{x1:5d} w{x1-x0:4d} h{y1-y0:4d} px{s:5d} ext{L:4d}')
