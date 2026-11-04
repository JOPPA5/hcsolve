# Detect ink blobs (Morse elements) in the message area of the hi-res address side.
import sys, json
from PIL import Image
import numpy as np
from collections import deque
HI='ciphers/hcp-927/work/hires/cpc_1910-06-19_DE_Graudenz-(Grudziadz)_DE_Rendsburg__adr.jpg'
X0,Y0,X1,Y1=40,40,1560,2150
im=np.array(Image.open(HI).convert('RGB')).astype(int)[Y0:Y1,X0:X1]
gray=im.mean(2)
mask=gray<165
H,W=mask.shape
lab=np.zeros((H,W),int)
blobs=[]
n=0
for y in range(H):
    row=mask[y]
    for x in np.nonzero(row)[0]:
        if lab[y,x]: continue
        n+=1; q=deque([(y,x)]); lab[y,x]=n; pts=[]
        while q:
            cy,cx=q.popleft(); pts.append((cy,cx))
            for dy in (-1,0,1):
                for dx in (-1,0,1):
                    ny,nx=cy+dy,cx+dx
                    if 0<=ny<H and 0<=nx<W and mask[ny,nx] and not lab[ny,nx]:
                        lab[ny,nx]=n; q.append((ny,nx))
        if len(pts)<25: continue
        ys=[p[0] for p in pts]; xs=[p[1] for p in pts]
        blobs.append(dict(x=float(X0+sum(xs)/len(xs)),y=float(Y0+sum(ys)/len(ys)),x0=int(X0+min(xs)),x1=int(X0+max(xs)),y0=int(Y0+min(ys)),y1=int(Y0+max(ys)),a=len(pts),dark=float(gray[ys,xs].mean())))
json.dump(blobs,open('ciphers/hcp-927/work/blobs.json','w'),indent=0)
print(len(blobs))
