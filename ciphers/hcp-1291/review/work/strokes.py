# find adjacent near-vertical stroke pairs (candidates n / d / h / p) and measure lengths (pure numpy/PIL labelling)
import numpy as np
from PIL import Image, ImageFilter
A='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1291/work/hires/cpc_1913-08-31_HU__HU_Jasz-Arokszalas_jolanka-41_adr.jpg'
im=Image.open(A).convert('L'); a=np.array(im).astype(float)
bg=np.array(im.filter(ImageFilter.GaussianBlur(40))).astype(float)
X0,X1,Y0,Y1=60,1720,90,2110
m=((bg-a)>35)[Y0:Y1,X0:X1]
seen=np.zeros(m.shape,bool); S=[]
H,W=m.shape
for y0,x0 in zip(*np.where(m)):
    if seen[y0,x0]: continue
    st=[(y0,x0)]; seen[y0,x0]=True; pts=[]
    while st:
        y,x=st.pop(); pts.append((y,x))
        for dy in (-1,0,1):
            for dx in (-1,0,1):
                v,u=y+dy,x+dx
                if 0<=v<H and 0<=u<W and m[v,u] and not seen[v,u]:
                    seen[v,u]=True; st.append((v,u))
    if len(pts)<40: continue
    p=np.array(pts,float); ys,xs=p[:,0],p[:,1]
    ev,vec=np.linalg.eigh(np.cov(np.vstack([xs,ys])))
    L=4*np.sqrt(ev[1]); Wd=4*np.sqrt(ev[0])
    ang=np.degrees(np.arctan2(abs(vec[1,1]),abs(vec[0,1])))
    S.append(dict(L=L,W=Wd,ang=ang,w=xs.max()-xs.min(),h=ys.max()-ys.min(),cx=xs.mean()+X0,cy=ys.mean()+Y0))
V=[s for s in S if s['ang']>40 and s['L']/max(s['W'],1)>1.8 and 14<s['L']<130 and s['w']<75]
V.sort(key=lambda s:s['cx'])
pairs=[]
for s in V:
    for t in V:
        dx=t['cx']-s['cx']
        if 8<dx<62 and abs(t['cy']-s['cy'])<50:
            pairs.append((round((s['cy']+t['cy'])/2),round(s['cx']),round(t['cx']),round(s['L']),round(t['L']),round(s['L']/t['L'],2)))
pairs.sort()
print('y xL xR lenL lenR ratio')
for r in pairs: print(*r)
