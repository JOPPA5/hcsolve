from PIL import Image
import numpy as np
d='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1255/'
im=np.array(Image.open(d+'work/hires/cpc_1912-03-11_HU__HU_Jasz-Arokszalas_jolanka-08_adr.jpg').convert('RGB')).astype(int)[:1960,80:1640]
m=(im[...,0]-im[...,1]>55)
pts=set(map(tuple,np.argwhere(m).tolist()))
comps=[]
while pts:
    p=pts.pop();st_=[p];cc=[p]
    while st_:
        y,x=st_.pop()
        for dy in(-1,0,1):
            for dx in(-1,0,1):
                q=(y+dy,x+dx)
                if q in pts: pts.remove(q);st_.append(q);cc.append(q)
    comps.append(cc)
C=[]
for cc in comps:
    a=len(cc)
    if a<60: continue
    ys=[p[0] for p in cc];xs=[p[1] for p in cc]
    C.append(dict(x0=min(xs)+80,x1=max(xs)+81,y0=min(ys),y1=max(ys)+1,h=max(ys)-min(ys)+1,w=max(xs)-min(xs)+1,a=a))
print(len(C))
# bars
B=[c for c in C if c['w']>1.4*c['h'] and c['w']<130 and c['h']<30]
used=set();st=[]
B.sort(key=lambda c:c['y0'])
for i,b in enumerate(B):
    if i in used: continue
    g=[b];used.add(i)
    for j,o in enumerate(B):
        if j in used: continue
        l=g[-1]
        ov=min(l['x1'],o['x1'])-max(l['x0'],o['x0'])
        if ov>0.4*min(l['w'],o['w']) and 0<=o['y0']-l['y0']<38: g.append(o);used.add(j)
    st.append(g)
st=[(sum(c['x0'] for c in g)/len(g),sum(c['y0'] for c in g)/len(g),len(g)) for g in st]
# strokes pairs
S=[c for c in C if c['h']>1.5*c['w'] and c['h']>35 and c['w']<45]
S.sort(key=lambda c:c['x0'])
P=[]
for i,a in enumerate(S):
    for b in S[i+1:]:
        if 0<b['x0']-a['x0']<45 and abs((a['y0']+a['y1'])-(b['y0']+b['y1']))<50:
            P.append((a,b))
import json
rows={}
for x,y,c in st:
    r=round((y+0.035*(x-800)-120)/90.3)+1
    rows.setdefault(r,[]).append((int(x),c))
for r in sorted(rows): print('bars',r,[ (x,c) for x,c in sorted(rows[r])])
for a,b in sorted(P,key=lambda p:(p[0]['y0'],p[0]['x0'])):
    print('pair x',a['x0'],'y',a['y0'],'h',a['h'],b['h'],'ratio %.2f'%(b['h']/a['h']))
