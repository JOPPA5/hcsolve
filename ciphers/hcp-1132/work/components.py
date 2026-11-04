# Extract ink marks (dots / dashes) from the hires address side, excluding blue print.
import json
from PIL import Image, ImageFilter
import numpy as np
img=Image.open('work/hires/cpc_--_HU_Debrecen_HU___adr.jpg').convert('RGB')
im=np.asarray(img).astype(int)
X0,Y0,X1,Y1=40,40,1500,2140
a=im[Y0:Y1,X0:X1]
R,G,B=a[...,0],a[...,1],a[...,2]
gray=(R+G+B)/3
ink=(gray<172)&((B-R)<0)
H,W=ink.shape
seen=np.zeros_like(ink,bool)
out=[]
for y0 in range(H):
    row=ink[y0]
    for x0 in np.nonzero(row & ~seen[y0])[0]:
        if seen[y0,x0]: continue
        st=[(y0,x0)]; seen[y0,x0]=True; pts=[]
        while st:
            y,x=st.pop(); pts.append((y,x))
            for dy in (-2,-1,0,1,2):
                for dx in (-2,-1,0,1,2):
                    yy,xx=y+dy,x+dx
                    if 0<=yy<H and 0<=xx<W and ink[yy,xx] and not seen[yy,xx]:
                        seen[yy,xx]=True; st.append((yy,xx))
        if len(pts)<30: continue
        p=np.array(pts)
        out.append(dict(x=round(float(p[:,1].mean())+X0,1),y=round(float(p[:,0].mean())+Y0,1),
            y0=int(p[:,0].min())+Y0,y1=int(p[:,0].max())+Y0,x0=int(p[:,1].min())+X0,x1=int(p[:,1].max())+X0,
            area=len(pts),dark=round(float(gray[p[:,0],p[:,1]].mean()),1)))
json.dump(out,open('work/comps.json','w'),indent=0)
print(len(out))
