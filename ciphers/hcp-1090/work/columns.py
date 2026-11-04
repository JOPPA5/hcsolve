# Chain blobs into vertical columns and print sequence with gaps.
import json,sys
b=json.load(open(sys.argv[1]))
b=[x for x in b if x['y1']-x['y0']>=7]
b.sort(key=lambda r:r['y'])
cols=[]
for r in b:
    best=None;bd=1e9
    for c in cols:
        l=c[-1]; d=abs(l['x']-r['x'])
        if d<38 and r['y0']-l['y1']<400 and d<bd: best=c;bd=d
    if best is None: cols.append([r])
    else: best.append(r)
cols.sort(key=lambda c:c[0]['x'])
for i,c in enumerate(cols):
    s=[];prev=None
    for r in c:
        h=r['y1']-r['y0']+1
        sym='.' if h<=24 else ('-' if h<=75 else 'X')
        if prev is not None: s.append('(%d)'%(r['y0']-prev))
        s.append(sym)
        prev=r['y1']
    print(i,'x=%d..%d y=%d..%d n=%d'%(c[0]['x'],c[-1]['x'],c[0]['y0'],c[-1]['y1'],len(c)))
    print('   ',''.join(s))
