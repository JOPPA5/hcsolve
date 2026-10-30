import sys
from collections import deque
from PIL import Image, ImageDraw
import numpy as np
im=Image.open(sys.argv[1]).convert('RGB'); g=np.asarray(im).astype(int).sum(2)/3
thr=int(sys.argv[2]); m=g<thr; H,W=m.shape
lab=np.zeros((H,W),int); comps=[]
for y in range(H):
  for x in range(W):
    if m[y,x] and not lab[y,x]:
      n=len(comps)+1; q=deque([(y,x)]); lab[y,x]=n; pts=[]
      while q:
        cy,cx=q.popleft(); pts.append((cy,cx))
        for dy in(-1,0,1):
          for dx in(-1,0,1):
            yy,xx=cy+dy,cx+dx
            if 0<=yy<H and 0<=xx<W and m[yy,xx] and not lab[yy,xx]: lab[yy,xx]=n; q.append((yy,xx))
      ys=np.array([p[0] for p in pts]); xs=np.array([p[1] for p in pts])
      comps.append((int(xs.min()),int(xs.max()),int(ys.min()),int(ys.max()),float(ys.mean()),len(pts),float(g[ys,xs].min())))
comps=[c for c in comps if c[5]>=2 and c[3]-c[2]<=12 and c[1]-c[0]<=60 and c[6]<thr-20]
import json; json.dump(comps,open('comps.json','w'))
print(len(comps))
