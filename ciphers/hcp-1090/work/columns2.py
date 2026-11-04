# Assign blobs to columns by iterative per-column line fits (x = a + b*y); print Morse with gaps.
import json,sys,numpy as np
b=[r for r in json.load(open(sys.argv[1])) if r['y1']-r['y0']>=7 and r['x']<1600]
lines=[(75,-0.01)]+[(c,0.035) for c in (130,220,320,425,545,650,750,850,948,1052,1155,1255,1368,1490)]
for it in range(8):
    groups=[[] for _ in lines]
    for r in b:
        d=[abs(r['x']-(a+k*r['y'])) for a,k in lines]
        i=int(np.argmin(d))
        if d[i]<45: groups[i].append(r)
    new=[]
    for g,(a,k) in zip(groups,lines):
        if len(g)>5:
            ys=np.array([r['y'] for r in g]); xs=np.array([r['x'] for r in g])
            k2,a2=np.polyfit(ys,xs,1); new.append((a2,k2))
        else: new.append((a,k))
    lines=new
unassigned=[r for r in b if all(r not in g for g in groups)]
out=[]
for ci,(g,(a,k)) in enumerate(zip(groups,lines)):
    g.sort(key=lambda r:r['y'])
    s=[];prev=None
    for r in g:
        h=r['y1']-r['y0']+1
        sym='.' if h<=24 else ('-' if h<=75 else 'X')
        if prev is not None: s.append('(%d)'%(r['y0']-prev))
        s.append(sym+('' if sym!='X' else '[%d,%d]'%(r['x'],r['y'])))
        prev=r['y1']
    print(ci+1,'a=%.0f k=%.3f n=%d'%(a,k,len(g)))
    print('   ',''.join(s))
print('unassigned',[(round(r['x']),round(r['y']),r['y1']-r['y0']+1) for r in unassigned])
json.dump([[a,k] for a,k in lines],open(sys.argv[2],'w'))
