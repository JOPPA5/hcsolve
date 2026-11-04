# Detect ink marks (dots/dashes) on the message side (hi-res scan); output JSON list of blobs.
import sys, json
from PIL import Image
import numpy as np
from collections import deque
im=Image.open(sys.argv[1]).convert('L')
a=np.array(im)[:2230,:1640]
mask=a<int(sys.argv[3]) if len(sys.argv)>3 else a<120
seen=np.zeros_like(mask)
H,W=mask.shape
res=[]
ys,xs=np.nonzero(mask)
for y,x in zip(ys,xs):
    if seen[y,x]: continue
    q=deque([(y,x)]); seen[y,x]=1; pts=[]
    while q:
        cy,cx=q.popleft(); pts.append((cy,cx))
        for dy in (-2,-1,0,1,2):
            for dx in (-2,-1,0,1,2):
                ny,nx=cy+dy,cx+dx
                if 0<=ny<H and 0<=nx<W and mask[ny,nx] and not seen[ny,nx]:
                    seen[ny,nx]=1; q.append((ny,nx))
    if len(pts)<60: continue
    p=np.array(pts)
    res.append(dict(y=float(p[:,0].mean()),x=float(p[:,1].mean()),y0=int(p[:,0].min()),y1=int(p[:,0].max()),x0=int(p[:,1].min()),x1=int(p[:,1].max()),area=len(pts)))
json.dump(res,open(sys.argv[2],'w'))
print(len(res))
