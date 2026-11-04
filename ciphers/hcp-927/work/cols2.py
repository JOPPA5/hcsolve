import json
import numpy as np
B=json.load(open('ciphers/hcp-927/work/blobs.json'))
B=[b for b in B if b['y']>268 and 290<b['x']<1500]
B.sort(key=lambda b:b['x'])
cols=[]
for b in B:
    for c in cols:
        if abs(c['mx']-b['x'])<22:
            c['b'].append(b); c['mx']=sum(t['x'] for t in c['b'])/len(c['b']); break
    else:
        cols.append(dict(mx=b['x'],b=[b]))
seeds=[c for c in cols if len(c['b'])>=8]
small=[c for c in cols if len(c['b'])<8]
for s in seeds:
    ys=np.array([b['y'] for b in s['b']]); xs=np.array([b['x'] for b in s['b']])
    s['fit']=np.polyfit(ys,xs,1)
for c in small:
    for b in c['b']:
        best=min(seeds,key=lambda s:abs(np.polyval(s['fit'],b['y'])-b['x']))
        d=abs(np.polyval(best['fit'],b['y'])-b['x'])
        if d<25: best['b'].append(b)
        else: print('orphan',int(b['x']),int(b['y']),b['y1']-b['y0']+1,b['x1']-b['x0']+1)
seeds.sort(key=lambda s:s['mx'])
res=[]
for i,s in enumerate(seeds):
    bs=sorted(s['b'],key=lambda b:b['y'])
    out=[];prev=None;letters=[];cur=''
    for b in bs:
        h=b['y1']-b['y0']+1; w=b['x1']-b['x0']+1
        t='-' if h>=2.0*w else '.'
        gap=b['y0']-prev if prev is not None else 0
        if prev is not None and gap>=38:
            letters.append(cur); cur=''
            if gap>=130: letters.append('/')
        cur+=t; prev=b['y1']
        out.append('%s(%d,%d,%d)'%(t,int(b['y']),h,w))
    letters.append(cur)
    print('COL',i,int(s['mx']),int(np.polyval(s['fit'],300)),int(np.polyval(s['fit'],2100)))
    print('  ',' '.join(letters))
    res.append(dict(i=i,mx=s['mx'],els=[(b['y'],b['y1']-b['y0']+1,b['x1']-b['x0']+1,b['x']) for b in bs]))
json.dump(res,open('ciphers/hcp-927/work/cols.json','w'))
